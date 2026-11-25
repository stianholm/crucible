"""Loads a solution's incumbent EVOLVE-BLOCK content off disk.

Was duplicated identically in harness/run.py, harness/run_population.py and
bench/noise.py, each hardcoding `candidate/candidate.py` and the
`# EVOLVE-BLOCK-START`/`# EVOLVE-BLOCK-END` comment-marker convention —
true for fixture and itot_classifier (Python files), but not for
capability_case, whose frozen artifact is `candidate/candidate.txt` with
bare, non-commented markers (it's prose, not Python; see
solutions/capability_case/SOLUTION.md's mutation-surface answer). Calling
any of the three duplicates against capability_case raised FileNotFoundError
then IndexError — found by the session-review workflow, 2026-09-22.

Fixed here, once, generically: the candidate file is whatever single file
lives in candidate/ (not a hardcoded name), and the marker split is on the
bare marker text without a `#` prefix requirement — which still matches
correctly when a `#` prefix *is* present, since it's a substring, so this
is strictly more general and doesn't change behaviour for fixture or
itot_classifier.
"""

from __future__ import annotations

from pathlib import Path


def load_incumbent_block(sol_dir: Path) -> str:
    cand_dir = sol_dir / "candidate"
    files = [f for f in cand_dir.iterdir() if f.is_file()]
    if len(files) != 1:
        raise RuntimeError(f"expected exactly one file in {cand_dir}, found {[f.name for f in files]}")
    text = files[0].read_text()
    return text.split("EVOLVE-BLOCK-START")[1].split("EVOLVE-BLOCK-END")[0].strip("\n")
