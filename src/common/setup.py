"""Shared setup utilities for ensuring host dependencies exist."""

import os
import subprocess
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def ensure_build_deps(is_docker: bool = False) -> None:
    """Ensure dependencies exist on the host.

    Downloads lib/tla2tools.jar, lib/community/, and ~/.tlapm via install_deps.sh.
    check_proof_bin and SANY DumpSemantics are compiled inside Docker (multi-stage build).
    """
    install_deps = os.path.join(REPO_ROOT, "scripts", "install_deps.sh")
    if os.path.isfile(install_deps):
        cmd = ["bash", install_deps]
        if is_docker:
            cmd.append("--docker-only")
        r = subprocess.run(cmd, cwd=REPO_ROOT)
        if r.returncode != 0:
            print("ERROR: Failed to install deps. Run `bash scripts/install_deps.sh` manually.")
            sys.exit(1)
