"""Run SANY over a .tla file and return its semantic model.

Thin wrapper around ``DumpSemantics`` (the tla2sany-based dumper). Reuses the
existing ``run.sh`` plumbing, which compiles the Java if needed and sets up the
TLA-Library search path (TLAPS stdlib + the input file's own directory so that
sibling-module EXTENDS/INSTANCE resolve).

This is the single entry point both the benchmark generator and the checker use
to get a parsed view of a module — no regex parsing of TLA+ source anywhere.
"""

from __future__ import annotations

import glob
import json
import os
import re
import shutil
import subprocess
import tempfile
from typing import Optional

from ..model import Module

_HERE = os.path.dirname(os.path.abspath(__file__))
# run.sh currently lives under the existing sany-dump location; we shell out to
# it rather than duplicating the build/launch logic. (A later cleanup may move
# the Java + scripts under this package and drop this indirection.)
_REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_RUN_SH = os.path.join(_REPO_ROOT, "src", "dataset", "sany-dump", "run.sh")

_MARKER = "--- BEGIN SANY-DUMP JSON ---"


class SanyError(RuntimeError):
    """SANY failed to parse the module (parse/semantic error, or no output)."""


def dump_raw(tla_path: str, timeout: int = 180) -> dict:
    """Run SANY on ``tla_path`` and return the raw JSON dict."""
    res = subprocess.run(
        [_RUN_SH, tla_path],
        capture_output=True, text=True, timeout=timeout,
    )
    out = res.stdout
    idx = out.find(_MARKER)
    if idx < 0:
        err = (res.stderr or "").strip()
        raise SanyError(
            f"SANY produced no dump for {tla_path} (exit {res.returncode}). "
            f"stderr: {err[:400]}"
        )
    try:
        return json.loads(out[idx + len(_MARKER):])
    except json.JSONDecodeError as e:
        raise SanyError(f"Could not parse SANY dump for {tla_path}: {e}")


def dump(tla_path: str, timeout: int = 180) -> Module:
    """Run SANY on ``tla_path`` and return a typed :class:`Module`."""
    return Module.parse(dump_raw(tla_path, timeout=timeout))


def try_dump(tla_path: str, timeout: int = 180) -> Optional[Module]:
    """Like :func:`dump` but returns ``None`` on any SANY failure.

    Useful when scanning a set of files where some may legitimately fail to
    parse in isolation (e.g. a dependency missing its own deps).
    """
    try:
        return dump(tla_path, timeout=timeout)
    except (SanyError, subprocess.TimeoutExpired, OSError):
        return None


_MODULE_DECL = re.compile(r"^-+\s*MODULE\s+(\w+)", re.MULTILINE)


def module_name_of(tla_path: str) -> Optional[str]:
    """Read the declared module name from a .tla file's header."""
    try:
        with open(tla_path, encoding="utf-8", errors="ignore") as f:
            m = _MODULE_DECL.search(f.read())
        return m.group(1) if m else None
    except OSError:
        return None


def dump_normalized(tla_path: str, dep_dir: Optional[str] = None,
                    timeout: int = 180) -> Module:
    """Parse ``tla_path`` robustly, even when its filename != module name.

    TLA+/SANY requires the file name to match the declared module name. Some
    submissions are stored as ``solution.tla`` while declaring a different
    module. We copy the file (and the sibling .tla dependencies from
    ``dep_dir``, default = the file's own directory) into a temp dir, renaming
    the target to ``<module>.tla`` so SANY accepts it and resolves deps.
    """
    mod = module_name_of(tla_path)
    src_dir = dep_dir or os.path.dirname(os.path.abspath(tla_path))
    base = os.path.basename(tla_path)
    # Fast path: filename already matches module name -> no copy needed.
    if mod is None or base == f"{mod}.tla":
        return dump(tla_path, timeout=timeout)

    tmp = tempfile.mkdtemp(prefix="tlacore_sany_")
    try:
        for dep in glob.glob(os.path.join(src_dir, "*.tla")):
            shutil.copy2(dep, os.path.join(tmp, os.path.basename(dep)))
        target = os.path.join(tmp, f"{mod}.tla")
        shutil.copy2(tla_path, target)
        return dump(target, timeout=timeout)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def try_dump_normalized(tla_path: str, dep_dir: Optional[str] = None,
                        timeout: int = 180) -> Optional[Module]:
    try:
        return dump_normalized(tla_path, dep_dir=dep_dir, timeout=timeout)
    except (SanyError, subprocess.TimeoutExpired, OSError):
        return None
