"""PHASE-6.md's plateau ladder, solution scheduling and the scheduled gate."""

import datetime as dt

from harness import gate, ladder
from harness.scheduler import Contender, generations_that_fit, pick


def ho(q, gens=4, v="v1", passes=None):
    return {"kind": "held_out", "detail": {"quality": q, "generations": gens, "eval_version": v,
                                           "passes": passes or [q - 0.002, q + 0.002]}}


def step(k, v="v1"):
    return {"kind": "ladder", "detail": {"step": k, "eval_version": v}}


def test_gain_above_sigma_resets_and_flat_accumulates():
    st = ladder.replay([ho(0.80), ho(0.805), ho(0.809), ho(0.802)], "v1")
    assert st.best == 0.80 and st.since == 12 and st.due == 1   # +0.009 is inside one sigma (floor 0.01)
    st = ladder.replay([ho(0.80), ho(0.805), ho(0.83)], "v1")
    assert st.best == 0.83 and st.since == 0 and st.due is None


def test_ladder_climbs_in_order_and_holds_at_four():
    evts = [ho(0.8)] + [ho(0.8)] * 3
    for k in (1, 2, 3, 4):
        st = ladder.replay(evts, "v1")
        assert st.due == k
        evts += [step(k)] + [ho(0.8)] * 3
    st = ladder.replay(evts, "v1")
    assert st.dormant and st.due is None                       # never loops back
    st = ladder.replay(evts + [ho(0.8)] * 10, "v1")
    assert st.dormant and st.due is None


def test_progress_mid_ladder_returns_to_climbing():
    st = ladder.replay([ho(0.8)] + [ho(0.8)] * 3 + [step(1), ho(0.85)], "v1")
    assert st.step == 0 and st.best == 0.85


def test_new_eval_set_restarts_a_dormant_solution():
    evts = [ho(0.8), step(4)]
    assert ladder.replay(evts, "v1").dormant
    st = ladder.replay(evts, "v2")
    assert not st.dormant and st.best is None


def c(sol, dormant=False, last=None):
    st = ladder.LadderState("v", step=4 if dormant else 0)
    return Contender(sol, st, last)


def test_pick_running_keeps_the_gpu_then_priority_then_longest_wait():
    t = dt.datetime(2026, 10, 24, tzinfo=dt.timezone.utc)
    cands = [c("a", last=t), c("b", last=t - dt.timedelta(days=2)), c("n")]
    assert pick(cands, [], running="a").solution_id == "a"
    assert pick(cands, ["b"], running=None).solution_id == "b"
    assert pick(cands, [], running=None).solution_id == "n"        # never run waits longest
    assert pick([c("a", dormant=True), c("b")], [], running="a").solution_id == "b"
    assert pick([c("a", dormant=True)], [], running=None) is None


def test_a_segment_starts_only_if_it_ends_before_the_deadline():
    assert generations_that_fit(4 * 3600, 3600, 1800) == 3  # 30 min kept for held-out
    assert generations_that_fit(3600 + 1799, 3600, 1800) == 0
    assert generations_that_fit(4 * 3600, 3600) == 3        # 50 min fallback
    assert generations_that_fit(20 * 3600, 600) == 4        # capped at a segment


def test_gate_needs_all_four():
    cap = {"passes": True, "regression": 0.0}
    win = [(0.80, 0.85 + 0.001 * i) for i in range(40)]
    ok = gate.conditions(win, {"proposer": (1000, 10), "distilled": (900, 10)}, [1.0, 0.95], cap)
    assert all(v["pass"] for v in ok.values())
    flat = [(0.80, 0.80 + (0.01 if i % 2 else -0.01)) for i in range(40)]
    assert not gate.conditions(flat, {"proposer": (1000, 10), "distilled": (900, 10)}, [1.0], cap)["quality"]["pass"]
    dear = gate.conditions(win, {"proposer": (1000, 10), "distilled": (1300, 10)}, [1.0], cap)
    assert not dear["cost"]["pass"]
    narrow = gate.conditions(win, {"proposer": (1000, 10), "distilled": (900, 10)}, [0.85], cap)
    assert not narrow["diversity"]["pass"]
    forgot = gate.conditions(win, {"proposer": (1000, 10), "distilled": (900, 10)}, [1.0], {"passes": False})
    assert not forgot["capability"]["pass"]


def test_a_solution_can_set_its_own_sigma_floor():
    evts = [ho(0.941, passes=[0.9410, 0.9411])] + [ho(0.941, passes=[0.9410, 0.9411])] * 3 + [ho(0.9499, passes=[0.9493, 0.9506])]
    assert ladder.replay(evts, "v1").best == 0.941               # +0.009 is under the default 0.01
    st = ladder.replay(evts, "v1", sigma_floor=0.003)
    assert st.best == 0.9499 and st.since == 0                   # counted under a measured floor
