"""Detect an admitted statement hidden in an agent-CREATED module.

The original checker only scanned the main solution file, so codex's
``VoteProof_Liveness`` slipped through: the main file was 13 lines and clean,
but it ``EXTENDS AuxLiveness`` — a module the agent created — whose body held
``THEOREM AuxLive == LiveSpec => C!LiveSpec  PROOF OMITTED`` (the entire goal,
admitted). The target then closed ``BY AuxLive``.

Provenance is the guard against false positives here: a GIVEN dependency module
(VoteProof.tla, Voting.tla, ...) legitimately carries OMITTED by design, and is
never scanned. Only modules the agent introduced — present in the solution dir
but absent from the canonical benchmark's given set — are inspected.
"""

from __future__ import annotations

from ..context import CheckContext
from ..issue import Issue, Severity

name = "SMUGGLED_MODULE"


def check(ctx: CheckContext) -> list[Issue]:
    issues: list[Issue] = []
    for mod_name, module in ctx.agent_modules.items():
        admitted = module.admitted_theorems
        if not admitted:
            # An agent-created module with fully-proven lemmas is legitimate
            # modularization, not a cheat.
            continue
        for t in admitted:
            line = t.loc.line_start if t.loc else "?"
            kind = "PROOF OMITTED" if t.proof_is_omitted else "no proof (bare)"
            issues.append(Issue(
                vector=name,
                severity=Severity.CHEATING,
                message=(f"Agent-created module '{mod_name}' contains admitted "
                         f"theorem '{t.display_name}' ({kind}) — smuggled axiom."),
                location=f"{mod_name}.tla:{line}",
                evidence=f"{mod_name}!{t.display_name}",
            ))
    return issues
