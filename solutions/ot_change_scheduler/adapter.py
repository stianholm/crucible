"""SolutionAdapter for ot_change_scheduler. Same sandboxed execution as
itot_classifier; the difference is the score. A plan that breaks any rule
scores 0, and a valid plan scores its value over the instance's exact
optimum (checks/generate_tasks.py), so quality measures distance from the
best possible schedule rather than agreement with a reference heuristic.
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
from solutions.ot_change_scheduler.checks.model import verify

SOL_DIR = Path(__file__).resolve().parent
_SRC = (SOL_DIR / "candidate" / "candidate.py").read_text()
FROZEN_HEADER = _SRC.split("# EVOLVE-BLOCK-START")[0]
FROZEN_FOOTER = _SRC.split("# EVOLVE-BLOCK-END")[1]


class OtChangeSchedulerAdapter:
    solution_id = "ot_change_scheduler"
    executes_code = True
    eval_timeout_s = 10.0   # the standard's hard kill
    # A short greedy seed legitimately grows several-fold into a search: the
    # first segments rejected 17 of 96 proposals at 3.1x to 5.4x under the
    # default 3.0. Code, so lower than the text solutions' 15; the 10 s kill
    # and the latency term already bound what a long block can cost.
    max_growth = 8.0

    def materialise(self, block: str) -> Path:
        d = Path(tempfile.mkdtemp(prefix="otcs-cand-"))
        indented = textwrap.indent(textwrap.dedent(block).strip("\n"), "    ")
        (d / "candidate.py").write_text(
            FROZEN_HEADER + "# EVOLVE-BLOCK-START\n" + indented + "\n    # EVOLVE-BLOCK-END" + FROZEN_FOOTER)
        return d

    def invoke(self, cand: Path, task_input: str, timeout: float) -> Run:
        return run_in_sandbox(cand, task_input, timeout)

    def shape_ok(self, output: Any) -> bool:
        try:
            d = json.loads(output)
        except (ValueError, TypeError):
            return False
        return isinstance(d, dict) and isinstance(d.get("plan"), dict)

    def programmatic_checks(self, output: Any, task: Task) -> dict[str, tuple[float, str]]:
        try:
            plan = json.loads(output)["plan"]
        except (ValueError, TypeError, KeyError):
            return {"parses": (0.0, f"output is not JSON with a plan: {str(output)[:200]!r}")}
        inst = json.loads(task.input)
        violations, value = verify(inst, plan)
        if violations:
            more = f" (+{len(violations) - 3} more)" if len(violations) > 3 else ""
            return {"valid_plan": (0.0, "; ".join(violations[:3]) + more)}
        opt = task.expected["optimum"]
        n = len(inst["changes"])
        return {"value": (min(1.0, value / opt) if opt else 1.0,
                          f"value {value} of optimum {opt}; {len(plan)} of {n} changes scheduled")}

    def needs_judgement(self, task: Task) -> bool:
        return False

    def descriptors(self, run: Run) -> tuple[int, int]:
        """Archive coordinates, never optimised: the share of changes the plan
        schedules (selective against packed), and runtime (a quick greedy
        against a search that spends its time budget)."""
        try:
            d = json.loads(run.output)
            share = len(d["plan"]) / max(1, d["n_changes"])
        except (ValueError, TypeError, KeyError):
            share = 0.0
        share_bin = max(0, min(int(share * 6), 5))
        runtime_bin = max(0, min(int(math.log2(max(run.wall_time_s, 0.125) / 0.125)), 5))
        return (share_bin, runtime_bin)
