"""The validation ladder. See PHASE-2.md task 2.2.

Never edit the incumbent in place — each candidate is materialised into a
fresh directory. Reject everything free before spending a sandbox launch:
a sandbox costs seconds, a scored evaluation costs more.
"""

from __future__ import annotations

import ast

MAX_GROWTH = 3.0


def _has_frozen_signature(tree: ast.AST, frozen_name: str) -> bool:
    """The frozen entrypoint must not be redefined inside the mutation
    surface. A candidate block is the *body* of an existing function, so
    finding a top-level `def <frozen_name>` anywhere in the materialised
    file's parsed tree means the block tried to redefine the frozen
    wrapper rather than just filling in its body."""
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == frozen_name:
            # exactly one definition (the frozen scaffolding's own) is
            # expected; a second one means the candidate redefined it.
            count = sum(
                1
                for n in ast.walk(tree)
                if isinstance(n, ast.FunctionDef) and n.name == frozen_name
            )
            return count == 1
    return False


def _reaches_evaluator(tree: ast.AST) -> bool:
    """The candidate must never import the evaluator, fitness, or the task
    set. Reaching any of them turns the search into reward hacking."""
    forbidden = {"harness.scorer", "harness.fitness", "scorer", "fitness", "tasks"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = {alias.name for alias in node.names}
        elif isinstance(node, ast.ImportFrom):
            names = {node.module} if node.module else set()
        else:
            continue
        if names & forbidden:
            return True
    return False


def admissible(
    new_block: str,
    parent_block: str,
    materialise,
    frozen_entrypoint: str = "solve",
    max_growth: float | None = None,
) -> tuple[bool, str]:
    """`materialise` is the adapter's own materialise(block) -> Path;
    admissibility is checked against the *full* file it produces, since
    that's what actually has to parse and run.

    Hardcoded `candidate.py` here crashed outright for any executes_code=
    False solution (capability_case: materialise() writes instructions.txt,
    not candidate.py) — found by the session-review workflow, 2026-09-22.
    Fixed generically, the same way as harness/incumbent.py: read whichever
    single file materialise() actually produced, and only run the
    Python-specific checks below (frozen signature, forbidden imports) when
    that file is actually Python. Neither concept has a text-artifact
    equivalent: there is no function signature a prose instructions block
    could redefine, and no import statement to forbid. The unchanged/growth
    checks above are the only ones that generalise to any artifact shape.

    max_growth defaults to MAX_GROWTH (3.0), sized for code — a 3x rewrite
    of a function body usually is bloat. capability_case's first real
    hill-climb run (2026-09-22) found this cap rejected every single
    proposal across 12 iterations, 100% inadmissible, all for "grew Nx"
    (3.2x-5.7x): its incumbent is a genuinely short (676-char) prose
    paragraph, and a correct rewrite covering four evidence dimensions
    plus three anti-pattern checks legitimately needs to be several times
    longer — that's the fix doing its job, not runaway bloat. Callers pass
    getattr(adapter, "max_growth", None); an adapter can override this
    default the same way as eval_timeout_s and rubric.
    """
    growth_cap = max_growth if max_growth is not None else MAX_GROWTH
    if new_block.strip() == parent_block.strip():
        return False, "unchanged"
    if len(new_block) > growth_cap * len(parent_block):
        return False, f"grew {len(new_block) / len(parent_block):.1f}x"

    cand_dir = materialise(new_block)
    files = [f for f in cand_dir.iterdir() if f.is_file()]
    if len(files) != 1:
        return False, f"expected exactly one file in {cand_dir}, found {[f.name for f in files]}"
    cand_file = files[0]

    if cand_file.suffix != ".py":
        return True, "ok"

    full_source = cand_file.read_text()
    try:
        tree = ast.parse(full_source)
    except SyntaxError as e:
        return False, f"syntax: {e}"

    if not _has_frozen_signature(tree, frozen_entrypoint):
        return False, "signature changed"
    if _reaches_evaluator(tree):
        return False, "imports the evaluator"
    return True, "ok"
