"""Generate ot_change_scheduler's instances and their exact optima.

    python -m solutions.ot_change_scheduler.checks.generate_tasks

Instances are generated from a seed per instance id, so the set rebuilds
byte-identically. Each instance's `expected` is the optimum of a MILP that
encodes the same five rules as checks/model.py, solved with SciPy's HiGHS;
the optimal plan is then re-checked by verify(), so the solver and the
verifier cannot silently disagree. The split is harness.split's sha256 rule,
and held-out is sealed with a hash, as for every solution.

Sized so that demand exceeds capacity (total crew-hours are 55 to 75% of the
work requested): every instance forces a choice, which is where a heuristic
gains or loses value.
"""

from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

from harness.split import split_of
from solutions.ot_change_scheduler.checks.model import verify

SOL_DIR = Path(__file__).resolve().parent.parent
N_INSTANCES = 100
MILP_TIME_LIMIT_S = 300   # v2's largest probe instance proved optimal in 109 s


# Eval set versions, by instance id prefix. v1 (otcs-) saturated in one day:
# the proposer's heuristics reached 0.998 of the exact optimum (decision 96).
# v2 (otcs2-) is larger and tighter; the v1 winner scores 0.932 on it, the
# seed 0.741 (decision 97).
SIZES = {
    "otcs-": {"w": (4, 8), "z": (4, 8), "c": (20, 55), "cap": (0.55, 0.75), "dep_p": 0.3, "deps": (1, 2),
              "deadline_p": 0.3, "conflict_p": 0.25, "id_width": 2},
    "otcs2-": {"w": (8, 16), "z": (6, 12), "c": (80, 200), "cap": (0.40, 0.60), "dep_p": 0.4, "deps": (1, 3),
               "deadline_p": 0.35, "conflict_p": 0.3, "id_width": 3},
}
VERSION_PREFIX = "otcs2-"


def generate(instance_id: str) -> dict:
    k = next(p for p in sorted(SIZES, key=len, reverse=True) if instance_id.startswith(p))
    z = SIZES[k]
    r = random.Random(instance_id)
    n_w, n_z, n_c = r.randint(*z["w"]), r.randint(*z["z"]), r.randint(*z["c"])
    zones = [f"Z{i + 1}" for i in range(n_z)]
    windows = [{"id": f"W{i + 1}", "order": i + 1, "crew_hours": 0, "max_outages": r.randint(1, 3)}
               for i in range(n_w)]
    changes = []
    for i in range(n_c):
        tier = r.random()
        value = r.randint(7, 10) if tier < 0.2 else r.randint(4, 7) if tier < 0.6 else r.randint(1, 4)
        deps = sorted(r.sample([c["id"] for c in changes], k=min(len(changes), r.randint(*z["deps"])))) \
            if changes and r.random() < z["dep_p"] else []
        changes.append({
            "id": f"C{i + 1:0{z['id_width']}d}", "zone": r.choice(zones), "hours": r.randint(2, 12), "value": value,
            "outage": r.random() < 0.5, "depends_on": deps,
            "deadline": f"W{r.randint(1, n_w - 1)}" if r.random() < z["deadline_p"] else None,
        })
    demand = sum(c["hours"] for c in changes)
    capacity = demand * r.uniform(*z["cap"])
    shares = [r.uniform(0.6, 1.4) for _ in windows]
    for w, s in zip(windows, shares):
        w["crew_hours"] = max(6, round(capacity * s / sum(shares)))
    conflicts = [[a, b] for i, a in enumerate(zones) for b in zones[i + 1:] if r.random() < z["conflict_p"]]
    r.shuffle(changes)  # ids do not reveal the dependency order
    return {"instance_id": instance_id, "windows": windows, "zones": zones, "conflicts": conflicts,
            "changes": changes}


def optimum(inst: dict) -> tuple[int, dict, bool]:
    """(value, plan, proven optimal) by MILP over x[c,w] and y[z,w]."""
    W = inst["windows"]
    C = inst["changes"]
    Z = inst["zones"]
    order = {w["id"]: w["order"] for w in W}
    x = {(c["id"], w["id"]): k for k, (c, w) in enumerate(
        (c, w) for c in C for w in W if not c["deadline"] or w["order"] <= order[c["deadline"]])}
    y = {(z, w["id"]): len(x) + k for k, (z, w) in enumerate((z, w) for z in Z for w in W)}
    n = len(x) + len(y)
    rows, lb, ub = [], [], []

    def row(coefs: dict[int, float], lo: float, hi: float) -> None:
        a = np.zeros(n)
        for i, v in coefs.items():
            a[i] += v
        rows.append(a); lb.append(lo); ub.append(hi)

    by_id = {c["id"]: c for c in C}
    for c in C:                                            # (1) at most one window
        row({x[k]: 1 for k in x if k[0] == c["id"]}, -np.inf, 1)
    for w in W:                                            # (2) capacity, (4) outage count
        row({x[k]: by_id[k[0]]["hours"] for k in x if k[1] == w["id"]}, -np.inf, w["crew_hours"])
        row({y[(z, w["id"])]: 1 for z in Z}, -np.inf, w["max_outages"])
        for a, b in inst["conflicts"]:                     # (4) conflicts
            row({y[(a, w["id"])]: 1, y[(b, w["id"])]: 1}, -np.inf, 1)
    for (cid, wid), i in x.items():
        c = by_id[cid]
        if c["outage"]:                                    # (4) outage takes the zone down
            row({i: 1, y[(c["zone"], wid)]: -1}, -np.inf, 0)
        for d in c["depends_on"]:                          # (3) dependency strictly earlier
            coefs = {i: 1}
            for (did, dw), j in x.items():
                if did == d and order[dw] < order[wid]:
                    coefs[j] = -1
            row(coefs, -np.inf, 0)
    cost = np.zeros(n)
    for (cid, _), i in x.items():                          # (5) deadlines: no variable after one
        cost[i] = -by_id[cid]["value"]
    res = milp(cost, constraints=LinearConstraint(np.array(rows), lb, ub), integrality=np.ones(n),
               bounds=Bounds(0, 1), options={"time_limit": MILP_TIME_LIMIT_S})
    plan = {cid: wid for (cid, wid), i in x.items() if res.x[i] > 0.5}
    return int(round(-res.fun)), plan, res.status == 0


def _solve(iid: str) -> tuple[str, dict, int, bool]:
    inst = generate(iid)
    value, plan, proven = optimum(inst)
    violations, checked = verify(inst, plan)
    assert not violations and checked == value, (iid, violations, checked, value)
    return iid, inst, value, proven


def build(workers: int = 8) -> dict[str, int]:
    from multiprocessing import Pool

    for split in ("dev", "rotation", "held_out"):
        for f in (SOL_DIR / "data" / split).glob("*.json"):
            f.unlink()  # the previous version stays in git history
    counts = {"dev": 0, "rotation": 0, "held_out": 0}
    unproven = []
    ids = [f"{VERSION_PREFIX}{i + 1:04d}" for i in range(N_INSTANCES)]
    with Pool(workers) as pool:
        for iid, inst, value, proven in pool.imap(_solve, ids):
            if not proven:
                unproven.append(iid)
            split = split_of(iid)
            counts[split] += 1
            task = {"task_id": iid, "input": json.dumps(inst),
                    "expected": {"optimum": value, "proven": proven}}
            (SOL_DIR / "data" / split / f"{iid}.json").write_text(json.dumps(task, indent=1) + "\n")
    h = hashlib.sha256()
    for f in sorted((SOL_DIR / "data" / "held_out").glob("*.json")):
        h.update(f.read_bytes())
    (SOL_DIR / "data" / "held_out.sha256").write_text(h.hexdigest() + "\n")
    print(counts, "unproven:", unproven or "none")
    return counts


if __name__ == "__main__":
    build()
