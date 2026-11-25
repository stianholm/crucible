"""PHASE-5.md task 5.4: per-arm and paired results of a stock-versus-distilled A/B.

    python -m harness.ab <run_id>          # whole run, all generations

Two views, because they answer different questions:

- **Per arm** (the task's Verify line): proposals, parse and admission rates,
  mean rotation scalar of valid scored candidates, cell-claim rate and prompt
  tokens. Claims are comparable between arms only because _expand_arms
  shuffles which arm of each pair is scored first.
- **Paired**: for every pair where both candidates were scored and valid, the
  distilled scalar minus the stock scalar. Both came from the same parent with
  the same prompt and were scored on the same tasks, so the difference is the
  proposer's, and its standard error is what "a two sigma win" is measured
  against. This is rotation evidence; the promotion gate (task 5.6) decides on
  held-out.
"""

from __future__ import annotations

import math
import statistics
import sys

from scipy import stats

STOCK = "proposer"


def arm_stats(conn, run_id, generation: int | None = None) -> list[dict]:
    where, args = "run_id = %s and proposer_model is not null", [run_id]
    if generation is not None:
        where += " and generation = %s"
        args.append(generation)
    rows = conn.execute(
        f"""select proposer_model,
                   count(*),
                   count(*) filter (where status not in ('propose_failed', 'parse_failed')),
                   count(*) filter (where status = 'scored'),
                   avg(scalar) filter (where status = 'scored' and valid),
                   count(*) filter (where accepted),
                   avg(prompt_tokens)
            from iteration where {where} group by 1 order by 1""",
        args,
    ).fetchall()
    return [
        {"arm": r[0], "proposed": r[1], "parsed": r[2], "scored": r[3],
         "mean_scalar": None if r[4] is None else float(r[4]),
         "claim_rate": r[5] / r[3] if r[3] else None,
         "prompt_tokens": None if r[6] is None else float(r[6])}
        for r in rows
    ]


def paired(conn, run_id, generation: int | None = None) -> dict | None:
    """Distilled minus stock scalar over complete pairs."""
    where, args = "run_id = %s and pair_id is not null", [run_id]
    if generation is not None:
        where += " and generation = %s"
        args.append(generation)
    rows = conn.execute(
        f"""select generation, pair_id, proposer_model, scalar from iteration
            where {where} and status = 'scored' and valid""",
        args,
    ).fetchall()
    by_pair: dict = {}
    for gen, pair, model, scalar in rows:
        by_pair.setdefault((gen, pair), {})[STOCK if model == STOCK else "distilled"] = scalar
    diffs = [p["distilled"] - p[STOCK] for p in by_pair.values() if len(p) == 2]
    if len(diffs) < 2:
        return None
    mean, sd = statistics.mean(diffs), statistics.stdev(diffs)
    se = sd / math.sqrt(len(diffs))
    t, p = stats.ttest_1samp(diffs, 0.0)
    return {"pairs": len(diffs), "mean_diff": mean, "sd": sd, "se": se,
            "sigma": mean / se if se else float("inf"), "t": float(t), "p": float(p),
            "distilled_better": sum(d > 0 for d in diffs), "ties": sum(d == 0 for d in diffs)}


def render(conn, run_id, generation: int | None = None) -> str:
    scope = "this generation" if generation is not None else "the whole run"
    lines = [f"## A/B, stock versus distilled ({scope})", "",
             "| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |",
             "|---|---|---|---|---|---|---|"]
    fmt = lambda v, f: "n/a" if v is None else f.format(v)
    for a in arm_stats(conn, run_id, generation):
        lines.append(f"| `{a['arm']}` | {a['proposed']} | {a['parsed']} | {a['scored']} | "
                     f"{fmt(a['mean_scalar'], '{:.4f}')} | {fmt(a['claim_rate'], '{:.1%}')} | "
                     f"{fmt(a['prompt_tokens'], '{:.0f}')} |")
    p = paired(conn, run_id, generation)
    lines.append("")
    if p is None:
        lines.append("Paired difference: fewer than two complete pairs.")
    else:
        lines.append(f"Paired difference, distilled minus stock, over {p['pairs']} complete pairs: "
                     f"mean {p['mean_diff']:+.4f} (sd {p['sd']:.4f}, se {p['se']:.4f}), "
                     f"**{p['sigma']:+.2f} sigma**, p {p['p']:.3f}; distilled ahead in "
                     f"{p['distilled_better']}, tied in {p['ties']}.")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    from harness.persistence import connect

    with connect() as c:
        print(render(c, sys.argv[1]))
