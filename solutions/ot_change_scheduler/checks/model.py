"""The scheduling rules, checked. The one place they are implemented: the
adapter scores with verify(), and generate_tasks.py's MILP encodes the same
five rules, cross-checked by verify() on every optimum it records.

Never imported by a candidate; the sandbox mounts only candidate/.
"""

from __future__ import annotations


def verify(inst: dict, plan: object) -> tuple[list[str], int]:
    """(violations, value). Any violation makes the plan worthless."""
    if not isinstance(plan, dict):
        return [f"plan is {type(plan).__name__}, not an object of change_id -> window_id"], 0
    windows = {w["id"]: w for w in inst["windows"]}
    changes = {c["id"]: c for c in inst["changes"]}
    v: list[str] = []
    for cid, wid in plan.items():
        if cid not in changes:
            v.append(f"unknown change {cid!r}")
        elif not isinstance(wid, str) or wid not in windows:
            v.append(f"{cid} placed in unknown window {wid!r}")
    if v:
        return v, 0
    order = {wid: windows[wid]["order"] for wid in windows}

    for wid, w in windows.items():
        placed = [changes[c] for c, x in plan.items() if x == wid]
        hours = sum(c["hours"] for c in placed)
        if hours > w["crew_hours"]:
            v.append(f"{wid}: {hours} crew-hours scheduled, capacity {w['crew_hours']}")
        down = sorted({c["zone"] for c in placed if c["outage"]})
        if len(down) > w["max_outages"]:
            v.append(f"{wid}: {len(down)} zones down ({', '.join(down)}), max {w['max_outages']}")
        for a, b in inst["conflicts"]:
            if a in down and b in down:
                v.append(f"{wid}: conflicting zones {a} and {b} both down")
    for cid, wid in plan.items():
        c = changes[cid]
        for d in c["depends_on"]:
            if d not in plan:
                v.append(f"{cid} depends on {d}, which is not scheduled")
            elif order[plan[d]] >= order[wid]:
                v.append(f"{cid} in {wid} depends on {d} in {plan[d]}, not strictly earlier")
        if c["deadline"] and order[wid] > order[c["deadline"]]:
            v.append(f"{cid} in {wid} is after its deadline {c['deadline']}")
    value = 0 if v else sum(changes[c]["value"] for c in plan)
    return v, value
