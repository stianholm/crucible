"""RUN.md generation. See PHASE-2.md task 2.7.

Generated automatically when a run ends — this is how you discover the
loop has been doing something silly for forty iterations, before you
waste the next forty finding out by hand.
"""

from __future__ import annotations

from pathlib import Path

from harness.loop import AggregateScore


def _pct(n: int, total: int) -> str:
    return f"{100 * n / total:.1f}%" if total else "n/a"


def _health_line(label: str, value: str, healthy: bool) -> str:
    mark = "OK" if healthy else "CHECK"
    return f"| {label} | {value} | {mark} |"


def generate_run_report(
    rows: list[dict],
    solution_id: str,
    run_id: str,
    budget_summary: dict,
    baseline_scalar: float,
    out_path: Path,
    held_out: AggregateScore | None = None,
) -> str:
    total = len(rows)
    scored = [r for r in rows if r["status"] == "scored"]
    parse_failed = [r for r in rows if r["status"] == "parse_failed"]
    inadmissible = [r for r in rows if r["status"] == "inadmissible"]
    accepted = [r for r in rows if r["accepted"]]

    accept_rate = len(accepted) / total if total else 0.0
    parse_fail_rate = len(parse_failed) / total if total else 0.0
    inadmissible_rate = len(inadmissible) / total if total else 0.0

    prompt_tokens = [r["prompt_tokens"] for r in rows if r.get("prompt_tokens")]
    tokens_trend = "flat" if len(prompt_tokens) < 2 else (
        "rising" if prompt_tokens[-1] > 1.3 * (sum(prompt_tokens[: max(1, len(prompt_tokens) // 3)]) / max(1, len(prompt_tokens) // 3))
        else "flat"
    )

    trajectory = []
    running_best = baseline_scalar
    for r in rows:
        if r["status"] == "scored" and r["scalar"] is not None:
            running_best = max(running_best, r["scalar"]) if r["accepted"] else running_best
            trajectory.append(f"n={r['n']:>3}  scalar={r['scalar']:.4f}  accepted={r['accepted']}  incumbent_best={running_best:.4f}")

    lines = [
        f"# Run report — {solution_id} / {run_id}",
        "",
        "## Parameters",
        "",
        f"- Budget: {budget_summary}",
        f"- Baseline scalar: {baseline_scalar:.4f}",
        "",
        "## Health signals",
        "",
        "| Signal | Value | Status |",
        "|---|---|---|",
        _health_line("Accept rate", _pct(len(accepted), total), 0.05 <= accept_rate <= 0.50),
        _health_line("Parse failures", _pct(len(parse_failed), total), parse_fail_rate < 0.10),
        _health_line("Inadmissible", _pct(len(inadmissible), total), inadmissible_rate < 0.10),
        _health_line("Tokens per iteration", tokens_trend, tokens_trend == "flat"),
        _health_line("Total iterations", str(total), True),
        _health_line("Accepted candidates", str(len(accepted)), len(accepted) >= 1),
        "",
        "## Score trajectory",
        "",
        "```",
        *trajectory,
        "```",
        "",
        "## Accepted candidates, in full",
        "",
    ]

    for r in accepted:
        lines.append(f"### n={r['n']} (scalar {r['scalar']:.4f}, parent {r['parent_sha']})")
        lines.append("")
        lines.append(f"detail: `{r['detail']}`")
        lines.append("")

    if not accepted:
        lines.append("_No candidates were accepted this run._")

    if held_out is not None:
        lines += [
            "",
            "## Held-out check",
            "",
            f"- Held-out quality: {held_out.quality:.4f}",
            f"- Held-out scalar: {held_out.scalar:.4f}",
            f"- All held-out tasks valid: {held_out.all_valid}",
        ]

    text = "\n".join(lines) + "\n"
    out_path.write_text(text)
    return text
