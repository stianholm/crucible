"""ot_change_scheduler candidate. FROZEN signature: `solve(task_input: str, ctx) -> str`.

task_input is a JSON instance: windows (id, order, crew_hours, max_outages),
zones, conflicts (zone pairs never down together), and changes (id, zone,
hours, value, outage, depends_on, deadline). solve() returns
json.dumps({"plan": {change_id: window_id}, "n_changes": N}). The rules are
in solution.yaml's standard and checked by checks/model.py.

Everything between the EVOLVE-BLOCK markers is the proposer's to rewrite.
Incumbent since 2026-10-26: candidate 36cbe610ded0c305, the eval set v1
winner (held-out 0.998), promoted by the operator as eval set v2's starting
point (decision 97). The original greedy seed is in git history.
"""

from __future__ import annotations

import json


def solve(task_input: str, ctx=None) -> str:
    inst = json.loads(task_input)
    plan = _plan(inst)
    return json.dumps({"plan": plan, "n_changes": len(inst["changes"])})


def _plan(inst: dict) -> dict:
    # EVOLVE-BLOCK-START
    # ----- Pre‑process static data -----
    windows = sorted(inst["windows"], key=lambda w: w["order"])
    win_by_id = {w["id"]: w for w in windows}
    win_order = {w["id"]: w["order"] for w in windows}
    conflict_set = {frozenset(p) for p in inst.get("conflicts", [])}

    changes = inst["changes"]
    change_by_id = {c["id"]: c for c in changes}

    # ----- Dependency graph -----
    indeg = {c["id"]: len(c.get("depends_on", [])) for c in changes}
    dependents = {}
    for c in changes:
        for d in c.get("depends_on", []):
            dependents.setdefault(d, []).append(c["id"])

    # ----- Helper: feasibility test for a change in a window -----
    def feasible(change, win_id, used, down):
        w = win_by_id[win_id]
        if used[win_id] + change["hours"] > w["crew_hours"]:
            return False
        if change.get("outage"):
            zone = change["zone"]
            if len(down[win_id]) >= w["max_outages"] and zone not in down[win_id]:
                return False
            if any(frozenset((zone, z)) in conflict_set for z in down[win_id]):
                return False
        return True

    # ----- Helper: value‑per‑hour score with optional deadline urgency -----
    def score(change, cur_ord, deadline_mul=1.0):
        vph = change["value"] / change["hours"] if change["hours"] > 0 else float("inf")
        d = change.get("deadline")
        if d is not None:
            d_ord = win_order.get(d)
            if d_ord is not None:
                urgency = 1.0 / max(1, d_ord - cur_ord + 1)
                vph *= 1.0 + deadline_mul * urgency
        return vph

    # ----- Greedy scheduler that processes windows sequentially -----
    import heapq, random, time

    def greedy(deadline_mul=1.0):
        used = {w["id"]: 0 for w in windows}
        down = {w["id"]: set() for w in windows}
        schedule = {}
        indeg_cur = indeg.copy()
        ready = {cid for cid, d in indeg_cur.items() if d == 0}
        heap = []
        tie = 0
        # prime the heap with all ready changes for the earliest window
        first_ord = windows[0]["order"]
        for cid in ready:
            heapq.heappush(heap, (-score(change_by_id[cid], first_ord, deadline_mul), tie, cid))
            tie += 1

        for w in windows:
            cur_ord = w["order"]
            wid = w["id"]
            # discard stale entries
            while heap and heap[0][2] not in ready:
                heapq.heappop(heap)
            while heap:
                _, _, cid = heapq.heappop(heap)
                if cid not in ready:
                    continue
                ch = change_by_id[cid]

                # deadline check
                if ch.get("deadline"):
                    d_ord = win_order.get(ch["deadline"])
                    if d_ord is None or d_ord < cur_ord:
                        continue

                if not feasible(ch, wid, used, down):
                    continue

                # schedule it
                schedule[cid] = wid
                used[wid] += ch["hours"]
                if ch.get("outage"):
                    down[wid].add(ch["zone"])
                ready.remove(cid)

                # unlock dependents
                for nb in dependents.get(cid, []):
                    indeg_cur[nb] -= 1
                    if indeg_cur[nb] == 0:
                        ready.add(nb)
                        heapq.heappush(heap, (-score(change_by_id[nb], cur_ord, deadline_mul), tie, nb))
                        tie += 1
        return schedule

    # ----- Build a plan from a fixed topological order (first‑fit) -----
    def build_from_order(order):
        used = {w["id"]: 0 for w in windows}
        down = {w["id"]: set() for w in windows}
        plan = {}
        for cid in order:
            ch = change_by_id[cid]
            # dependency guard
            if any(d not in plan for d in ch.get("depends_on", [])):
                continue
            # earliest window after deps
            if ch.get("depends_on"):
                earliest = max(win_order[plan[d]] for d in ch["depends_on"]) + 1
            else:
                earliest = windows[0]["order"]
            # latest allowed window (deadline)
            latest = win_order.get(ch.get("deadline")) if ch.get("deadline") else None
            for w in windows:
                w_ord = w["order"]
                if w_ord < earliest:
                    continue
                if latest is not None and w_ord > latest:
                    continue
                if feasible(ch, w["id"], used, down):
                    plan[cid] = w["id"]
                    used[w["id"]] += ch["hours"]
                    if ch.get("outage"):
                        down[w["id"]].add(ch["zone"])
                    break
        return plan

    # ----- Scoring function -----
    def value(plan):
        return sum(change_by_id[c]["value"] for c in plan)

    # ----- Initial deterministic runs -----
    best_plan = {}
    best_val = 0
    start = time.time()
    TIME_LIMIT = 1.7   # keep buffer for the hard 2 s cap

    for mul in (1.0, 0.0):
        p = greedy(deadline_mul=mul)
        v = value(p)
        if v > best_val:
            best_plan, best_val = p, v

    # ----- Generate a high‑value topological order (value‑per‑hour bias) -----
    indeg_tmp = indeg.copy()
    ready = [cid for cid, d in indeg_tmp.items() if d == 0]

    def vph(cid):
        c = change_by_id[cid]
        return c["value"] / c["hours"] if c["hours"] > 0 else float("inf")

    ready.sort(key=vph, reverse=True)
    order = []
    while ready:
        cid = ready.pop(0)
        order.append(cid)
        for nb in dependents.get(cid, []):
            indeg_tmp[nb] -= 1
            if indeg_tmp[nb] == 0:
                # insert keeping vph order
                pos = 0
                nb_vph = vph(nb)
                while pos < len(ready) and vph(ready[pos]) > nb_vph:
                    pos += 1
                ready.insert(pos, nb)

    p = build_from_order(order)
    v = value(p)
    if v > best_val:
        best_plan, best_val = p, v

    # ----- Simulated annealing on topological orders -----
    def is_valid_topo(ordr):
        pos = {cid: i for i, cid in enumerate(ordr)}
        for cid in ordr:
            for d in change_by_id[cid].get("depends_on", []):
                if pos[d] >= pos[cid]:
                    return False
        return True

    temperature = 1.0
    while time.time() - start < TIME_LIMIT:
        # pick two positions to swap
        i, j = random.sample(range(len(order)), 2)
        if i > j:
            i, j = j, i
        a, b = order[i], order[j]
        # reject swaps that would break immediate dependency direction
        a_deps = set(change_by_id[a].get("depends_on", []))
        b_deps = set(change_by_id[b].get("depends_on", []))
        if b in a_deps or a in b_deps:
            continue
        new_order = order[:]
        new_order[i], new_order[j] = new_order[j], new_order[i]
        if not is_valid_topo(new_order):
            continue
        new_plan = build_from_order(new_order)
        new_val = value(new_plan)
        if new_val > best_val or random.random() < (2.71828 ** ((new_val - best_val) / temperature)):
            best_plan, best_val, order = new_plan, new_val, new_order
        temperature *= 0.9993

    # ----- Attempt to insert unscheduled high‑value changes (swap improvement) -----
    def improve(plan):
        used = {w["id"]: 0 for w in windows}
        down = {w["id"]: set() for w in windows}
        scheduled_in = {w["id"]: set() for w in windows}
        for cid, wid in plan.items():
            ch = change_by_id[cid]
            used[wid] += ch["hours"]
            if ch.get("outage"):
                down[wid].add(ch["zone"])
            scheduled_in[wid].add(cid)

        unsched = [c for c in changes if c["id"] not in plan]
        unsched.sort(key=lambda c: score(c, 0, deadline_mul=1.0), reverse=True)

        for ch in unsched:
            cid = ch["id"]
            # deps must already be placed
            if any(d not in plan for d in ch.get("depends_on", [])):
                continue
            # compute earliest / latest windows
            if ch.get("depends_on"):
                earliest = max(win_order[plan[d]] for d in ch["depends_on"]) + 1
            else:
                earliest = windows[0]["order"]
            latest = win_order.get(ch.get("deadline")) if ch.get("deadline") else None

            for w in windows:
                w_ord = w["order"]
                if w_ord < earliest:
                    continue
                if latest is not None and w_ord > latest:
                    continue
                wid = w["id"]
                # direct placement
                if feasible(ch, wid, used, down):
                    plan[cid] = wid
                    used[wid] += ch["hours"]
                    if ch.get("outage"):
                        down[wid].add(ch["zone"])
                    scheduled_in[wid].add(cid)
                    break
                # try swapping with a worse scheduled change
                for sid in list(scheduled_in[wid]):
                    sch = change_by_id[sid]
                    vph_new = ch["value"] / ch["hours"] if ch["hours"] else float("inf")
                    vph_old = sch["value"] / sch["hours"] if sch["hours"] else float("inf")
                    if vph_new <= vph_old:
                        continue
                    # capacity after swap
                    if used[wid] - sch["hours"] + ch["hours"] > w["crew_hours"]:
                        continue
                    # outage check after swap
                    new_down = down[wid].copy()
                    if sch.get("outage"):
                        new_down.discard(sch["zone"])
                    if ch.get("outage"):
                        if len(new_down) >= w["max_outages"] and ch["zone"] not in new_down:
                            continue
                        if any(frozenset((ch["zone"], z)) in conflict_set for z in new_down):
                            continue
                        new_down.add(ch["zone"])
                    # perform swap
                    del plan[sid]
                    plan[cid] = wid
                    used[wid] = used[wid] - sch["hours"] + ch["hours"]
                    if sch.get("outage"):
                        down[wid].discard(sch["zone"])
                    if ch.get("outage"):
                        down[wid].add(ch["zone"])
                    scheduled_in[wid].remove(sid)
                    scheduled_in[wid].add(cid)
                    break
                else:
                    continue
                break
        return plan

    if time.time() - start < TIME_LIMIT:
        improved = improve(best_plan.copy())
        imp_val = value(improved)
        if imp_val > best_val:
            best_plan, best_val = improved, imp_val

    return best_plan
    # EVOLVE-BLOCK-END
