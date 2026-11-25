"""capability_case_author: candidate instructions make the worker write a
capability case from raw evidence notes. See SOLUTION.md and checks/rubric.py.

Mirrors capability_case's adapter where the reasons carry over: the worker
runs on the proposer role (decision 56: the 4B judge model cannot follow a
conditional rule), the harness appends the output contract after the
candidate's instructions (decision 66), and the judge sees only the
extracted case, never the raw response.
"""

from __future__ import annotations

import json
import re
import tempfile
import time
from pathlib import Path
from typing import Any

from harness.judge import judge_client
from harness.types import Run, Task
from solutions.capability_case_author.checks.rubric import (
    DIMENSIONS,
    JUDGE_RUBRIC,
    OUTPUT_SKELETON,
    REASON_TERMS,
    evidence_blocks,
    fabricated_numbers,
    recommendation,
    sections,
    shape_ok,
    stated_strength,
)

SYSTEM_SUFFIX = "\n\nOUTPUT FORMAT (overrides any format described above).\n" + OUTPUT_SKELETON


class CapabilityCaseAuthorAdapter:
    solution_id = "capability_case_author"
    executes_code = False
    rubric = JUDGE_RUBRIC
    eval_timeout_s = 900.0  # AGENTS.md: client timeouts must exceed 15 minutes
    max_growth = 15.0  # a short seed legitimately grows several-fold, as in capability_case
    # Off 2026-10-19 (TODO.md decision 82): rubric v1 gave BAND 3 to all 24
    # calibration items, so its 30% was a constant, and the operator chose to
    # search on the mechanical checks rather than wait for calibration labels.
    # Turning it back on is a fitness change (CHANGE-PROCEDURES section 2).
    use_judge = False

    def materialise(self, block: str) -> Path:
        d = Path(tempfile.mkdtemp(prefix="capauthor-cand-"))
        (d / "instructions.txt").write_text(block.strip("\n") + "\n")
        return d

    def invoke(self, cand: Path, task_input: str, timeout: float) -> Run:
        instructions = (cand / "instructions.txt").read_text()
        notes = json.loads(task_input)["notes"]
        t0 = time.perf_counter()
        try:
            r = judge_client().chat.completions.create(
                model="proposer",  # the worker role; grading stays on the judge role
                temperature=0.0,
                messages=[
                    {"role": "system", "content": instructions + SYSTEM_SUFFIX},
                    {"role": "user", "content": notes},
                ],
                timeout=timeout,
            )
        except Exception as e:
            return Run(output=None, tokens=0, tool_calls=0, wall_time_s=time.perf_counter() - t0,
                       raw={"stderr": repr(e)[:2000]})
        text = (r.choices[0].message.content or "").strip()
        return Run(
            output=text,
            tokens=r.usage.total_tokens if r.usage else 0,
            tool_calls=0,
            wall_time_s=time.perf_counter() - t0,
            raw={"completion_tokens": r.usage.completion_tokens if r.usage else 0},
        )

    def shape_ok(self, output: Any) -> bool:
        return isinstance(output, str) and shape_ok(output)

    def judge_view(self, output: str) -> str:
        """Only the case's own sections, rebuilt from the parsed structure, so
        text outside them never reaches the grading call."""
        s = sections(output)
        return "\n\n".join(f"## {k}\n{s[k].strip()}" for k in ("Request", "Evidence", "Disqualifiers", "Recommendation") if k in s)

    def programmatic_checks(self, output: Any, task: Task) -> dict[str, tuple[float, str]]:
        notes = json.loads(task.input)["notes"]
        exp = task.expected
        s = sections(output)

        invented = fabricated_numbers(output, notes)
        checks = {"no_fabrication": (0.0 if invented else 1.0,
                                     f"numbers not in the notes: {invented}" if invented else "every number traces to the notes")}

        blocks = evidence_blocks(s.get("Evidence", ""))
        right, wrong = 0, []
        for key, name in DIMENSIONS.items():
            got = stated_strength(blocks.get(name, ""))
            if got == exp["evidence"][key]:
                right += 1
            else:
                wrong.append(f"{name}: stated {got!r}, notes show {exp['evidence'][key]!r}")
        checks["strength_honest"] = (right / len(DIMENSIONS), "; ".join(wrong) or "all four strengths stated correctly")

        rec = recommendation(output)
        if exp["must_reject"]:
            ok = rec == "Do not proceed"
            why = f"a disqualifier is present ({'; '.join(exp['reasons'])}); recommended {rec!r}"
        else:
            ok = rec in ("Proceed", "Gather more evidence")
            why = f"no disqualifier; recommended {rec!r} ('Do not proceed' would be wrong here)"
        checks["floor_correct"] = (1.0 if ok else 0.0, why)

        if not exp["must_reject"]:
            # Added 2026-10-20 (TODO.md decision 84). Without it the floor
            # accepted Proceed and Gather more evidence alike on every
            # floor-pass task, and the first search's winner recommended
            # Proceed on all of them, including cases with all four dimensions
            # thin, while the seed had calibrated every one correctly.
            # The rule is capability_case's operator-calibrated rubric: all
            # four thorough means Proceed, even one thin means Gather more
            # evidence. Its two close calls (over-caution on a clean case,
            # leniency with exactly one thin dimension) earn half, as BAND 1
            # does there.
            thin = sum(v == "thin" for v in exp["evidence"].values())
            want = "Proceed" if thin == 0 else "Gather more evidence"
            close = (thin == 0 and rec == "Gather more evidence") or (thin == 1 and rec == "Proceed")
            score = 1.0 if rec == want else 0.5 if close else 0.0
            checks["recommendation_calibrated"] = (score, f"{thin} thin dimension(s): wanted {want!r}, got {rec!r}")

        disq = s.get("Disqualifiers", "").lower()
        if exp["must_reject"]:
            named = [k for k in exp["reason_keys"] if any(t in disq for t in REASON_TERMS[k])]
            missing = sorted(set(exp["reason_keys"]) - set(named))
            checks["disqualifiers_named"] = (len(named) / len(exp["reason_keys"]),
                                             f"not named: {missing}" if missing else "every disqualifier named")
        else:
            none = bool(re.match(r"\W*none\b", disq.strip()))
            checks["disqualifiers_named"] = (1.0 if none else 0.0,
                                             "correctly states none" if none else "names a disqualifier the notes do not contain")
        return checks

    def task_class(self, task: Task) -> str:
        """Balanced over the floor, as in capability_case: a constant
        'Do not proceed' policy must not score the must-reject share."""
        return "must_reject" if task.expected["must_reject"] else "floor_pass"

    def needs_judgement(self, task: Task) -> bool:
        # Argument quality is what varies once the floor passes; a
        # must-reject case is decided by the mechanical checks.
        return self.use_judge and not task.expected["must_reject"]

    def descriptors(self, run: Run) -> tuple[int, int]:
        """Archive coordinates: case length bin (400-char steps) and latency
        bin (15 s steps, sized to LLM calls as in capability_case)."""
        length_bin = min(len(run.output or "") // 400, 5)
        latency_bin = min(int(run.wall_time_s // 15), 5)
        return (length_bin, latency_bin)
