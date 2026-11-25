"""PHASE-5.md task 5.5: proposal diversity per generation and arm, and the
reseed rule.

    python -m harness.diversity <run_id>

Diversity is the mean pairwise cosine distance between the candidate texts an
arm proposed in one generation, in a TF-IDF space fitted on that generation's
candidates from both arms. Task 5.5 asks for embedding distance; no embedding
model fits beside proposer and judge (TODO.md decision 34), and TF-IDF is what
the taxonomy and the harvest dedup already use. Fitting the vocabulary on both
arms together keeps the two numbers in one space, so they compare.

The stock reference is the stock arm of the same generation, which the paired
A/B (task 5.4) provides for free: same parents, same prompts, same moment.
"""

from __future__ import annotations

import statistics
import sys
from itertools import combinations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances

STOCK = "proposer"
# Task 5.5: reseed after four rounds, or when diversity falls more than 15%
# below the stock reference. The promotion gate (task 5.6) is stricter, 10%.
RESEED_ROUNDS = 4
RESEED_DROP = 0.15


def mean_pairwise_distance(vectors) -> float | None:
    if vectors.shape[0] < 2:
        return None
    d = cosine_distances(vectors)
    return float(statistics.mean(d[i, j] for i, j in combinations(range(d.shape[0]), 2)))


def by_generation(conn, run_id) -> list[dict]:
    """Per generation: diversity of each arm and the distilled/stock ratio."""
    rows = conn.execute(
        """select generation, proposer_model, proposal->>'content'
           from iteration where run_id = %s and proposal is not null and proposer_model is not null
           order by generation, id""",
        (run_id,),
    ).fetchall()
    gens: dict = {}
    for gen, model, content in rows:
        if content:
            gens.setdefault(gen, {}).setdefault(STOCK if model == STOCK else "distilled", []).append(content)
    out = []
    for gen, arms in sorted(gens.items()):
        texts = [t for ts in arms.values() for t in ts]
        if len(texts) < 4:
            continue
        X = TfidfVectorizer().fit_transform(texts)
        start, d = 0, {}
        for arm, ts in arms.items():
            d[arm] = mean_pairwise_distance(X[start:start + len(ts)])
            start += len(ts)
        ratio = d["distilled"] / d[STOCK] if d.get("distilled") and d.get(STOCK) else None
        out.append({"generation": gen, "stock": d.get(STOCK), "distilled": d.get("distilled"), "ratio": ratio})
    return out


def reseed_due(rounds_since_reseed: int, ratios: list[float]) -> tuple[bool, str]:
    """Task 5.5's rule, mechanically. ratios are distilled/stock diversity
    over the current round's generations; their mean is the round's figure."""
    if rounds_since_reseed >= RESEED_ROUNDS:
        return True, f"{rounds_since_reseed} rounds since the last reseed (limit {RESEED_ROUNDS})"
    if ratios:
        drop = 1 - statistics.mean(ratios)
        if drop > RESEED_DROP:
            return True, f"diversity {drop:.1%} below the stock reference (limit {RESEED_DROP:.0%})"
    return False, "within limits"


def render(conn, run_id) -> str:
    rows = by_generation(conn, run_id)
    lines = ["## Proposal diversity (mean pairwise TF-IDF cosine distance)", "",
             "| Generation | Stock | Distilled | Distilled / stock |", "|---|---|---|---|"]
    f = lambda v, s: "n/a" if v is None else s.format(v)
    for r in rows:
        lines.append(f"| {r['generation']} | {f(r['stock'], '{:.3f}')} | {f(r['distilled'], '{:.3f}')} | {f(r['ratio'], '{:.2f}')} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    from harness.persistence import connect

    with connect() as c:
        print(render(c, sys.argv[1]))
