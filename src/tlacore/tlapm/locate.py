"""Locate the tlapm binary and its standard-library directory.

Single source of truth, replacing the duplicated lookups previously in
``check_proof.py`` and ``runner.py``.
"""

from __future__ import annotations

import os
import shutil
from typing import Optional

_BIN_CANDIDATES = [
    "/opt/tlapm/bin/tlapm",
    os.path.expanduser("~/.tlapm/bin/tlapm"),
    "/tmp/tlapm/bin/tlapm",
]

_LIB_SUBDIRS = ["lib/tlapm/stdlib", "lib/tlaps", "lib/tlapm", "lib"]


def find_tlapm() -> Optional[str]:
    """Return the path to the tlapm binary, or None."""
    for cand in _BIN_CANDIDATES + [shutil.which("tlapm")]:
        if cand and os.path.isfile(cand):
            return cand
    return None


def find_tlapm_lib(tlapm_path: str) -> Optional[str]:
    """Derive the stdlib directory from the tlapm binary path.

    tlapm 1.6 keeps the stdlib at lib/tlapm/stdlib; 1.5 used lib/tlaps. The
    1.6 subdir is checked first because lib/tlapm exists in 1.6 too but does
    not directly hold the .tla files.
    """
    base = os.path.dirname(os.path.dirname(tlapm_path))
    for sub in _LIB_SUBDIRS:
        path = os.path.join(base, sub)
        if os.path.isdir(path):
            return path
    return None


def resolve(tlapm: Optional[str] = None,
            tlapm_lib: Optional[str] = None) -> tuple[str, str]:
    """Resolve (tlapm_binary, tlapm_lib), raising if either cannot be found."""
    tlapm = tlapm or find_tlapm()
    if not tlapm:
        raise FileNotFoundError("tlapm binary not found (looked in /opt, ~/.tlapm, /tmp, PATH)")
    tlapm_lib = tlapm_lib or find_tlapm_lib(tlapm)
    if not tlapm_lib:
        raise FileNotFoundError(f"tlapm stdlib not found relative to {tlapm}")
    return tlapm, tlapm_lib
