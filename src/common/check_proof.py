#!/usr/bin/env python3
"""
Check a single TLAPS benchmark proof for correctness and cheating.

Designed for AI agents to get quick feedback during proof writing.

Usage:
    python3 check_proof.py benchmark/Euclid/GCD_GCD3.tla \\
        [--level {1,2}] [--tlapm PATH] [--tlapm-lib PATH] [--timeout SECS]

Levels:
    1 (default) — proof completion. The preamble (above PROOF OBVIOUS) must be
                  byte-identical to the baseline.
    2          — proof from scratch. The agent may add new LEMMAs above the
                  target theorem; preamble integrity is not enforced. Other
                  cheating checks (PROOF OMITTED, axiom injection, bare QED,
                  dependency tampering) still apply.

Output:
    - Raw tlapm output (preserved verbatim)
    - Cheating check (compares against main branch where applicable)
    - Summary verdict: PASS / FAIL / CHEATING

Exit codes:
    0 = PASS
    1 = FAIL (proof doesn't verify)
    2 = CHEATING (tampering detected)
    3 = ERROR (could not run check)
"""

import os
import sys
import re
import shutil
import signal
import subprocess
import tempfile
import argparse
import glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cheating_detection import (
    detect_proof_omitted, detect_extra_axioms,
    detect_preamble_modification, detect_empty_proof,
    detect_zero_total_obligations, detect_dependency_modification,
    detect_missing_proof, detect_missing_proofs_summary, strip_comments,
)


def run_killgroup(cmd, timeout, cwd):
    """Run `cmd` with a wall-clock `timeout`, killing the ENTIRE process group
    on timeout. Returns (stdout, stderr, returncode); re-raises
    subprocess.TimeoutExpired after cleanup.

    tlapm spawns its backend solvers (z3, cvc4, zenon, ...) as separate
    processes. subprocess.run's timeout kills only the direct child (tlapm),
    orphaning the solvers — they keep running, steal CPU, and accumulate
    across runs, which in turn slows every later verification into spurious
    timeouts. start_new_session=True puts tlapm in its own process group; on
    timeout we SIGKILL the whole group so no solver survives.
    """
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        cwd=cwd, start_new_session=True,
    )
    try:
        out, err = proc.communicate(timeout=timeout)
        return out, err, proc.returncode
    except subprocess.TimeoutExpired:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
        try:
            proc.communicate(timeout=10)
        except Exception:
            pass
        raise


def find_tlapm():
    """Find tlapm binary."""
    candidates = [
        '/opt/tlapm/bin/tlapm',
        os.path.expanduser('~/.tlapm/bin/tlapm'),
        '/tmp/tlapm/bin/tlapm',
        shutil.which('tlapm'),
    ]
    for candidate in candidates:
        if candidate and os.path.isfile(candidate):
            return candidate
    return None


def find_tlapm_lib(tlapm_path):
    """Derive lib path from tlapm binary path.

    tlapm 1.6 puts stdlib at lib/tlapm/stdlib; tlapm 1.5 used lib/tlaps.
    The 1.6 sub is checked first because lib/tlapm exists in 1.6 too but
    does NOT directly contain the .tla files.
    """
    base = os.path.dirname(os.path.dirname(tlapm_path))
    for sub in ['lib/tlapm/stdlib', 'lib/tlaps', 'lib/tlapm', 'lib']:
        path = os.path.join(base, sub)
        if os.path.isdir(path):
            return path
    return None


def get_main_version(filepath):
    """Get the file content from the main/master branch."""
    repo_root = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'],
        capture_output=True, text=True, cwd=os.path.dirname(filepath) or '.'
    ).stdout.strip()

    if not repo_root:
        return None

    rel_path = os.path.relpath(filepath, repo_root)

    for branch in ['main', 'master']:
        result = subprocess.run(
            ['git', 'show', f'{branch}:{rel_path}'],
            capture_output=True, text=True, cwd=repo_root
        )
        if result.returncode == 0:
            return result.stdout

    return None


def find_proof_obvious_line(lines):
    """Find the line number (0-indexed) of 'PROOF OBVIOUS' in the file."""
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == 'PROOF OBVIOUS':
            return i
    return None


def check_cheating(filepath, level: int = 1):
    """Check for cheating by comparing against main branch.

    Args:
        level: 1 = strict preamble + proof-section checks;
               2 = preamble may grow (the agent can add lemmas), so the
                   preamble-integrity check is skipped and PROOF OMITTED is
                   scanned across the whole current file.

    Returns list of (line_number_1indexed, description) issues.
    """
    issues = []

    # Get main branch version
    main_content = get_main_version(filepath)
    if main_content is None:
        issues.append((0, "WARNING: Could not retrieve main branch version for comparison"))
        return issues

    main_lines = main_content.split('\n')
    with open(filepath, 'r') as f:
        current_content = f.read()
    current_lines = current_content.split('\n')

    # Find PROOF OBVIOUS in main version - this is the boundary
    po_line = find_proof_obvious_line(main_lines)
    if po_line is None:
        issues.append((0, "WARNING: No PROOF OBVIOUS found in main branch version"))
        return issues

    if level == 1 and len(current_lines) < po_line:
        issues.append((len(current_lines), f"File truncated: preamble had {po_line} lines, file has {len(current_lines)}"))
        return issues

    # 1. Preamble modification — L1 only.
    # L2 permits new declarations above the target theorem, so a byte-for-byte
    # preamble check would reject legitimate proofs.
    if level == 1:
        for ci in detect_preamble_modification(main_lines, current_lines, po_line):
            issues.append((ci.line or 0, ci.description))

    # 2. PROOF OMITTED / bare OMITTED.
    # L1: only the proof section can plausibly contain it (and must not).
    # L2: scan the whole current file — the agent may add proofs anywhere.
    if level == 1:
        proof_section = '\n'.join(current_lines[po_line:])
        for ci in detect_proof_omitted(proof_section):
            issues.append((po_line + (ci.line or 0), ci.description))
    else:
        for ci in detect_proof_omitted(current_content):
            issues.append((ci.line or 0, ci.description))

    # 3. Extra AXIOM/ASSUME (shared module)
    for ci in detect_extra_axioms(main_content, current_content):
        issues.append((0, ci.description))

    # 4. Dependency file modification (shared module)
    bench_dir = os.path.dirname(filepath)
    repo_root = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'],
        capture_output=True, text=True, cwd=bench_dir or '.'
    ).stdout.strip()

    if repo_root:
        dep_files = {}
        for dep_file in glob.glob(os.path.join(bench_dir, '*.tla')):
            if os.path.abspath(dep_file) == os.path.abspath(filepath):
                continue
            dep_basename = os.path.basename(dep_file)
            dep_rel = os.path.relpath(dep_file, repo_root)
            dep_main = None
            for branch in ['main', 'master']:
                r = subprocess.run(
                    ['git', 'show', f'{branch}:{dep_rel}'],
                    capture_output=True, text=True, cwd=repo_root
                )
                if r.returncode == 0:
                    dep_main = r.stdout
                    break
            if dep_main is None:
                continue
            with open(dep_file, 'r') as f:
                dep_current = f.read()
            dep_files[dep_basename] = (dep_main, dep_current)

        for ci in detect_dependency_modification(dep_files):
            issues.append((0, ci.description))

    return issues


def main():
    parser = argparse.ArgumentParser(description='Check a single TLAPS benchmark proof')
    parser.add_argument('file', help='Path to the benchmark .tla file')
    parser.add_argument('--level', type=int, default=1, choices=[1, 2],
                        help='Benchmark level — controls cheating rules (default: 1)')
    parser.add_argument('--tlapm', default=None, help='Path to tlapm binary')
    parser.add_argument('--tlapm-lib', default=None, help='Path to tlapm lib directory')
    parser.add_argument('--timeout', type=int, default=600, help='Timeout in seconds')
    parser.add_argument('--output', '-o', default=None, help='Write results to this file (default: <input>.result)')
    args = parser.parse_args()

    filepath = os.path.abspath(args.file)
    if not os.path.isfile(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(3)

    # Set up output: write to file and stdout
    output_path = args.output
    if output_path is None:
        output_path = os.path.splitext(filepath)[0] + '.result'

    # Collect all output lines, print at end and write to file
    output_lines = []

    def emit(line=""):
        output_lines.append(line)
        print(line)

    # Find tlapm
    tlapm_path = args.tlapm or find_tlapm()
    if not tlapm_path:
        emit("ERROR: tlapm not found. Use --tlapm to specify path.")
        with open(output_path, 'w') as f:
            f.write('\n'.join(output_lines) + '\n')
        sys.exit(3)

    tlapm_lib = args.tlapm_lib or find_tlapm_lib(tlapm_path)
    if not tlapm_lib:
        emit("ERROR: tlapm lib not found. Use --tlapm-lib to specify path.")
        with open(output_path, 'w') as f:
            f.write('\n'.join(output_lines) + '\n')
        sys.exit(3)

    emit(f"Checking: {os.path.relpath(filepath)}")
    emit(f"tlapm: {tlapm_path}")
    emit()

    # --- Step 1: Run tlapm ---
    emit("=" * 60)
    emit("TLAPM OUTPUT")
    emit("=" * 60)

    tmp_dir = tempfile.mkdtemp(prefix='tlaps_check_')
    try:
        basename = os.path.basename(filepath)
        tmp_file = os.path.join(tmp_dir, basename)
        shutil.copy2(filepath, tmp_file)

        # Copy dependency files from the same directory
        bench_dir = os.path.dirname(filepath)
        for dep_file in glob.glob(os.path.join(bench_dir, '*.tla')):
            dep_basename = os.path.basename(dep_file)
            if dep_basename != basename:
                shutil.copy2(dep_file, os.path.join(tmp_dir, dep_basename))

        cmd = [tlapm_path, '-I', tlapm_lib, tmp_file]
        try:
            out, err, rc = run_killgroup(cmd, args.timeout, tmp_dir)
            tlapm_output = out + err
            tlapm_exit = rc
        except subprocess.TimeoutExpired:
            tlapm_output = f"TIMEOUT after {args.timeout}s"
            tlapm_exit = -1
        except Exception as e:
            tlapm_output = f"ERROR: {e}"
            tlapm_exit = -2

        for line in tlapm_output.split('\n'):
            emit(line)
        tlapm_passed = (tlapm_exit == 0)

        # Run --summary to detect missing proofs (e.g. bare QED)
        summary_output = ""
        if tlapm_passed:
            try:
                out, err, _ = run_killgroup(
                    [tlapm_path, '-I', tlapm_lib, '--summary', tmp_file],
                    30, tmp_dir,
                )
                summary_output = out + err
            except Exception:
                pass
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    # --- Step 2: Cheating check ---
    emit()
    emit("=" * 60)
    emit("CHEATING CHECK")
    emit("=" * 60)

    cheating_issues = check_cheating(filepath, level=args.level)
    real_issues = [i for i in cheating_issues if not i[1].startswith("WARNING:")]
    warnings = [i for i in cheating_issues if i[1].startswith("WARNING:")]

    # Check for empty PROOF blocks and 0-obligation (independent of git comparison)
    if tlapm_passed:
        with open(filepath, 'r') as f:
            cur_lines = f.read().split('\n')

        if args.level == 1:
            # L1: PROOF OBVIOUS in main is the boundary; slice current at the
            # same index because the preamble is required to be unchanged.
            main_content = get_main_version(filepath)
            if main_content:
                main_lines = main_content.split('\n')
                po_line = find_proof_obvious_line(main_lines)
                if po_line is not None:
                    proof_section = '\n'.join(cur_lines[po_line:])
                    clean = strip_comments(proof_section)
                    for ci in detect_empty_proof(clean):
                        real_issues.append((po_line + (ci.line or 0), ci.description))
                    for ci in detect_zero_total_obligations(tlapm_output):
                        real_issues.append((0, ci.description))
                    for ci in detect_missing_proof(main_lines, cur_lines, po_line):
                        real_issues.append((ci.line or 0, ci.description))
        else:
            # L2: the agent may grow the preamble (new lemmas above target),
            # so there's no stable boundary. Scan the whole file; the bare-QED
            # check via --summary below catches what detect_missing_proof did.
            clean = strip_comments('\n'.join(cur_lines))
            for ci in detect_empty_proof(clean):
                real_issues.append((ci.line or 0, ci.description))
            for ci in detect_zero_total_obligations(tlapm_output):
                real_issues.append((0, ci.description))

        # --summary missing-proofs check is shared (target theorem is still
        # the last THEOREM/LEMMA in the file for both levels).
        if summary_output:
            target_line = None
            for li, l in enumerate(cur_lines):
                if re.match(r'^(THEOREM|LEMMA|COROLLARY|PROPOSITION)\b', l.strip()):
                    target_line = li + 1  # 1-indexed
            for ci in detect_missing_proofs_summary(summary_output, target_line):
                real_issues.append((0, ci.description))

    for line_num, desc in warnings:
        emit(f"  WARNING: {desc}")

    if real_issues:
        for line_num, desc in real_issues:
            emit(f"  Line {line_num}: {desc}")
    else:
        emit("  No cheating detected.")

    # --- Step 3: Verdict ---
    emit()
    emit("=" * 60)
    emit("VERDICT")
    emit("=" * 60)

    if real_issues:
        verdict = "CHEATING"
        exit_code = 2
        emit(f"  ⚠️  CHEATING — {len(real_issues)} issue(s) found")
    elif tlapm_passed:
        verdict = "PASS"
        exit_code = 0
        emit(f"  ✅ PASS — all obligations proved")
    else:
        verdict = "FAIL"
        exit_code = 1
        # Extract obligation summary
        m = re.search(r'(\d+)/(\d+) obligation', tlapm_output)
        if m:
            emit(f"  ❌ FAIL — {m.group(1)}/{m.group(2)} obligations failed")
        elif "TIMEOUT" in tlapm_output:
            emit(f"  ❌ FAIL — timeout after {args.timeout}s")
        else:
            emit(f"  ❌ FAIL — tlapm exit code {tlapm_exit}")

    # Write result file
    with open(output_path, 'w') as f:
        f.write('\n'.join(output_lines) + '\n')
    emit(f"\nResult written to: {output_path}")

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
