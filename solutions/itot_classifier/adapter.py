"""SolutionAdapter for itot_classifier. See PHASE-1.md task 1.1.

Reuses the same sandboxed-subprocess execution shape as the fixture
(harness.sandbox.run_in_sandbox) — the only thing genuinely different
from solutions/fixture/adapter.py is programmatic_checks(): this
solution's output is a structured, multi-field classification (gateway,
approval, a set of anti-pattern flags), not a single scalar, so partial
credit is graded per-field rather than all-or-nothing per task.
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


class ItotClassifierAdapter:
    solution_id = "itot_classifier"
    executes_code = True

    def materialise(self, block: str) -> Path:
        d = Path(tempfile.mkdtemp(prefix="itot-cand-"))
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
            d = json.loads(output)
        except (ValueError, TypeError):
            return False
        return isinstance(d, dict) and "gateway" in d

    def programmatic_checks(self, output: Any, task: Task) -> dict[str, tuple[float, str]]:
        try:
            got = json.loads(output)
        except (ValueError, TypeError):
            return {"parses": (0.0, f"output was not valid JSON: {output!r}")}

        expected = task.expected
        checks: dict[str, tuple[float, str]] = {}

        gw_ok = got.get("gateway") == expected.get("gateway")
        checks["gateway"] = (1.0 if gw_ok else 0.0, f"got={got.get('gateway')!r} expected={expected.get('gateway')!r}")

        approved_ok = got.get("approved") == expected.get("approved")
        checks["approved"] = (
            1.0 if approved_ok else 0.0,
            f"got={got.get('approved')!r} expected={expected.get('approved')!r}",
        )

        got_ap = set(got.get("anti_patterns_detected") or [])
        exp_ap = set(expected.get("anti_patterns_detected") or [])
        if not exp_ap and not got_ap:
            ap_score = 1.0
        else:
            union = got_ap | exp_ap
            ap_score = len(got_ap & exp_ap) / len(union) if union else 1.0
        checks["anti_patterns"] = (
            ap_score,
            f"got={sorted(got_ap)} expected={sorted(exp_ap)}",
        )

        return checks

    def needs_judgement(self, task: Task) -> bool:
        return False  # deterministic scoring end to end, like the fixture

    def descriptors(self, run: Run) -> tuple[int, int]:
        """Archive coordinates: output length bin, runtime bin. Not optimised."""
        length_bin = max(0, min(int(math.log2(max(len(run.output or ""), 1))), 5))
        runtime_bin = max(0, min(int(run.wall_time_s * 100), 5))
        return (length_bin, runtime_bin)
