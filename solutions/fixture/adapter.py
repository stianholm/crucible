"""SolutionAdapter for the fixture. See PHASE-1.md task 1.1 and PHASE-2.md
task 2.3.

Execution runs through harness.sandbox — a single docker sandbox slot
(rootless, no network, read-only root, capped memory/pids, all
capabilities dropped). Phase 1 built an interim subprocess-based version
of this file; this is the real one, swapped in without changing the
adapter interface, as planned.
"""

from __future__ import annotations

import json
import math
import tempfile
import textwrap
from pathlib import Path
from typing import Any

from harness.sandbox import run_in_sandbox
from harness.types import Run, Task

SOL_DIR = Path(__file__).resolve().parent
FROZEN_HEADER = (SOL_DIR / "candidate" / "candidate.py").read_text().split("# EVOLVE-BLOCK-START")[0]
FROZEN_FOOTER = (SOL_DIR / "candidate" / "candidate.py").read_text().split("# EVOLVE-BLOCK-END")[1]


class FixtureAdapter:
    solution_id = "fixture"
    executes_code = True

    def materialise(self, block: str) -> Path:
        """Frozen scaffolding plus the proposed EVOLVE-BLOCK, in a fresh dir.

        `block` is normalised to exactly 4-space indentation regardless of
        what indentation it arrives with (none, already 4-space, etc.) via
        dedent-then-indent — a block written as plain top-level Python and
        one copy-pasted from the on-disk candidate.py (already indented)
        must both produce a valid file. Getting this wrong doesn't raise
        here; it silently produces a candidate that crashes with an
        IndentationError, which scores identically to "ran fine but wrong
        answer" (quality 0) — a bug in test/proposer code would be
        invisible without checking Fitness.detail.
        """
        d = Path(tempfile.mkdtemp(prefix="fixture-cand-"))
        indented = textwrap.indent(textwrap.dedent(block).strip("\n"), "    ")
        full = FROZEN_HEADER + "# EVOLVE-BLOCK-START\n" + indented + "\n    # EVOLVE-BLOCK-END" + FROZEN_FOOTER
        (d / "candidate.py").write_text(full)
        return d

    def invoke(self, cand: Path, task_input: str, timeout: float) -> Run:
        return run_in_sandbox(cand, task_input, timeout)

    def shape_ok(self, output: Any) -> bool:
        if not isinstance(output, str):
            return False
        try:
            json.loads(output)
        except (ValueError, TypeError):
            return False
        return True

    def programmatic_checks(self, output: Any, task: Task) -> dict[str, tuple[float, str]]:
        try:
            got = json.loads(output)
        except (ValueError, TypeError):
            return {"parses": (0.0, f"output was not valid JSON: {output!r}")}

        expected = task.expected
        if isinstance(expected, float) or isinstance(got, float):
            ok = isinstance(got, (int, float)) and math.isclose(got, expected, rel_tol=1e-6, abs_tol=1e-9)
        else:
            ok = got == expected
        return {
            "matches_expected": (
                1.0 if ok else 0.0,
                f"got={got!r} expected={expected!r}",
            )
        }

    def needs_judgement(self, task: Task) -> bool:
        return False  # fixture is deterministic scoring end to end, no judge

    def descriptors(self, run: Run) -> tuple[int, int]:
        """Archive coordinates: output length bin, runtime bin. Not optimised."""
        length_bin = max(0, min(int(math.log2(max(len(run.output or ""), 1))), 5))
        runtime_bin = max(0, min(int(run.wall_time_s * 100), 5))
        return (length_bin, runtime_bin)
