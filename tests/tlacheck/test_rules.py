"""Unit tests for the SANY-based cheat rules, on minimal synthetic modules.

Run: PYTHONPATH=src python3 -m pytest tests/tlacheck/test_rules.py
(or just: PYTHONPATH=src python3 tests/tlacheck/test_rules.py)
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from tlacore.sany.dump import dump
from tlacore.provenance import Provenance
from tlacheck.context import CheckContext
from tlacheck.rules import admitted_statement
from tlacheck.issue import Severity

FIX = os.path.join(os.path.dirname(__file__), "fixtures")


def _ctx(name, baseline=None):
    m = dump(os.path.join(FIX, name + ".tla"))
    return CheckContext(target_name=name, solution_dir=FIX, solution=m,
                        baseline=baseline, provenance=Provenance(target=name))


def test_clean_proof_not_flagged():
    issues = admitted_statement.check(_ctx("CleanProof"))
    assert issues == [], f"clean proof wrongly flagged: {issues}"


def test_bare_theorem_flagged():
    issues = admitted_statement.check(_ctx("BareTheorem"))
    vectors = {i.vector for i in issues}
    assert "ADMITTED_STATEMENT" in vectors
    assert all(i.severity is Severity.CHEATING for i in issues)
    # Should flag both the bare 'Hard' and the circular 'Goal BY Hard'.
    msgs = " ".join(i.message for i in issues)
    assert "Hard" in msgs and "circular" in msgs


if __name__ == "__main__":
    test_clean_proof_not_flagged()
    test_bare_theorem_flagged()
    print("ok: all tlacheck rule tests passed")
