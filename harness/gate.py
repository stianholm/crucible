"""The promotion gate, applied by the scheduler. See PHASE-5.md task 5.6.

All four conditions, or no promotion:

| Condition | Here |
|---|---|
| Quality, paired | distilled minus stock rotation scalar over complete pairs, above GATE_SIGMA |
| General capability | the adapter's capability.json, written by the nightly window |
| Proposal diversity | distilled/stock mean pairwise distance, at least DIVERSITY_FLOOR |
| Cost | proposal tokens per claimed cell, distilled not above stock |

A rotation win is not a promotion. It records a `held_out_pending` decision
that needs acknowledgement: the paired held-out confirmation is run by hand
until an adapter first wins on rotation, since no adapter has, and a
procedure that has never run is not worth automating blind (PHASE-6.md, do
not add depth without a reason). A rejection unloads the adapter.
"""

from __future__ import annotations

import json
import statistics
import urllib.request
from pathlib import Path

GATE_GENERATIONS = 10   # decision 77: ten paired generations resolve about 0.029
GATE_SIGMA = 2.0
DIVERSITY_FLOOR = 0.90
PROPOSER_URL = "http://localhost:8000"
STOCK = "proposer"


def loaded_adapter() -> str | None:
    """The adapter directory vLLM serves as "distilled", e.g. /adapters/20261017."""
    try:
        with urllib.request.urlopen(f"{PROPOSER_URL}/v1/models", timeout=10) as r:
            entries = json.load(r)["data"]
    except OSError:
        return None
    return next((m.get("root") for m in entries if m["id"] == "distilled"), None)


def unload() -> None:
    req = urllib.request.Request(f"{PROPOSER_URL}/v1/unload_lora_adapter", method="POST",
                                 data=json.dumps({"lora_name": "distilled"}).encode(),
                                 headers={"content-type": "application/json"})
    urllib.request.urlopen(req, timeout=60).read()


def label(adapter_root: str) -> str:
    return f"proposer-distilled@{adapter_root}"


def paired_generations(conn, adapter_label: str) -> int:
    return conn.execute(
        "select count(distinct (run_id, generation)) from iteration where proposer_model = %s", (adapter_label,)
    ).fetchone()[0]


def conditions(pairs: list[tuple[float, float]], cost: dict[str, tuple[int, int]],
               diversity_ratios: list[float], capability: dict) -> dict:
    """Pure: pairs are (stock, distilled) scalars; cost maps arm to (proposal
    tokens, claims)."""
    diffs = [d - s for s, d in pairs]
    mean = statistics.mean(diffs) if diffs else 0.0
    se = statistics.stdev(diffs) / len(diffs) ** 0.5 if len(diffs) > 1 else float("inf")
    z = mean / se if se and se != float("inf") else 0.0
    per_claim = {arm: (t / c if c else float("inf")) for arm, (t, c) in cost.items()}
    div = statistics.mean(diversity_ratios) if diversity_ratios else None
    return {
        "quality": {"pairs": len(diffs), "mean_diff": mean, "se": se, "sigma": z, "pass": z > GATE_SIGMA},
        "capability": {"regression": capability.get("regression"), "pass": bool(capability.get("passes"))},
        "diversity": {"ratio": div, "pass": div is not None and div >= DIVERSITY_FLOOR},
        "cost": {"tokens_per_claim": per_claim,
                 "pass": per_claim.get("distilled", float("inf")) <= per_claim.get(STOCK, 0)},
    }


def evaluate(conn, adapter_root: str, repo_root: Path) -> dict:
    from harness.diversity import by_generation

    lab = label(adapter_root)
    runs = [r[0] for r in conn.execute(
        "select distinct run_id from iteration where proposer_model = %s", (lab,)).fetchall()]
    rows = conn.execute(
        """select run_id, generation, pair_id, proposer_model, scalar from iteration
           where run_id = any(%s) and pair_id is not null and proposer_model in (%s, %s)
             and status = 'scored' and valid""",
        (runs, STOCK, lab),
    ).fetchall()
    by_pair: dict = {}
    for run, gen, pair, model, scalar in rows:
        by_pair.setdefault((run, gen, pair), {})[STOCK if model == STOCK else "distilled"] = scalar
    pairs = [(p[STOCK], p["distilled"]) for p in by_pair.values() if len(p) == 2]
    cost = {}
    for arm, model in ((STOCK, STOCK), ("distilled", lab)):
        t, c = conn.execute(
            "select coalesce(sum(prompt_tokens), 0), count(*) filter (where accepted) from iteration "
            "where run_id = any(%s) and proposer_model = %s", (runs, model)).fetchone()
        cost[arm] = (int(t), int(c))
    ratios = [g["ratio"] for run in runs for g in by_generation(conn, run) if g["ratio"] is not None]
    cap_file = repo_root / adapter_root.lstrip("/")
    capability = json.loads((cap_file / "capability.json").read_text()) if (cap_file / "capability.json").exists() else {}
    return conditions(pairs, cost, ratios, capability)
