"""Class-balanced scoring, and why a plain mean over tasks was not enough.

Measured on capability_case 2026-10-01: every arm A elite scored 0.00 on all
nine must-reject held-out items and about 0.9 on the floor-passing ones. A plain
mean over tasks turns that into 0.59, and rotation's composition paid 0.61 for
the same never-reject policy, so multiple twenty-generation searches sat on it.
Lesson memory converged on the opposite constant, always-reject. Neither
discriminates, and no archive or quality metric could see it, because coverage,
QD score, rotation scalar and held-out quality all move freely while the policy
stays constant.
"""

from __future__ import annotations

import random
import statistics as st

from harness.scorer import class_balanced_mean, stratified_sample, task_class_of
from harness.types import Task


class _Adapter:
    def task_class(self, task: Task) -> str:
        return "must_reject" if task.expected["must_reject"] else "floor_pass"


class _Unclassed:
    """An adapter with no task_class hook, like fixture and itot_classifier."""


def _task(i: int, reject: bool) -> Task:
    return Task(task_id=f"t{i}", input="{}", expected={"must_reject": reject})


# rotation's real composition
TASKS = [_task(i, True) for i in range(7)] + [_task(100 + i, False) for i in range(11)]
NEVER = [0.0 if t.expected["must_reject"] else 0.9 for t in TASKS]
ALWAYS = [1.0 if t.expected["must_reject"] else 0.02 for t in TASKS]
GOOD = [1.0 if t.expected["must_reject"] else 0.9 for t in TASKS]


def test_a_plain_mean_pays_a_constant_policy_the_majority_share():
    # The defect, stated as a test so it cannot come back quietly.
    assert st.mean(NEVER) > 0.5, "never-rejecting scored above half under a plain mean"


def test_balancing_caps_both_degenerate_policies_near_half():
    never = class_balanced_mean(_Adapter(), TASKS, NEVER)
    always = class_balanced_mean(_Adapter(), TASKS, ALWAYS)
    assert 0.4 < never < 0.55
    assert 0.4 < always < 0.55


def test_balancing_still_rewards_a_candidate_that_discriminates():
    good = class_balanced_mean(_Adapter(), TASKS, GOOD)
    never = class_balanced_mean(_Adapter(), TASKS, NEVER)
    assert good > 0.9
    assert good - never > 0.4, "discrimination must be worth far more than a constant policy"


def test_an_adapter_without_the_hook_is_unaffected():
    # fixture and itot_classifier must score exactly as before.
    assert class_balanced_mean(_Unclassed(), TASKS, NEVER) == st.mean(NEVER)
    assert task_class_of(_Unclassed(), TASKS[0]) == ""


def test_stratified_sampling_always_covers_every_class():
    rng = random.Random(0)
    for _ in range(200):
        drawn = stratified_sample(_Adapter(), TASKS, 3, rng)
        assert len(drawn) == 3
        assert {task_class_of(_Adapter(), t) for t in drawn} == {"must_reject", "floor_pass"}


def test_uniform_sampling_would_have_missed_a_class_often():
    # Why stratification is needed and not merely tidier: balanced aggregation
    # over three tasks from one class is just a plain mean.
    rng = random.Random(0)
    single = sum(
        1 for _ in range(200)
        if len({task_class_of(_Adapter(), rng.choice(TASKS)) for _ in range(3)}) == 1
    )
    assert single > 20, "uniform k=3 draws collapse to one class often enough to matter"


def test_stratification_degrades_gracefully_without_classes():
    rng = random.Random(0)
    drawn = stratified_sample(_Unclassed(), TASKS, 3, rng)
    assert len(drawn) == 3


# --- the standing tier must not carry class-conditional advice -------------


def _lesson(lid: int, support: int, skew: float | None):
    from harness.lessons import Lesson
    return Lesson(id=lid, failure_id=f"F{lid:02d}", text=f"lesson {lid}", support=support,
                  followed=0, followed_ok=0, vector=[0.0], created_gen=0, retired_gen=None,
                  class_skew=skew)


def test_the_standing_tier_excludes_one_class_lessons(monkeypatch):
    # The failure this rule exists for: "highest support" selected
    # "When floor passes, prefer accept over reject" into the standing tier,
    # which injects it into must-reject prompts too. Derived independently
    # twice, retired twice.
    import harness.lessons as L
    lessons = [
        _lesson(1, support=334, skew=1.00),   # the harmful one: floor-pass only
        _lesson(2, support=93, skew=0.68),    # mixed, safe to inject universally
    ]
    monkeypatch.setattr(L, "active_lessons", lambda conn, sid: lessons)
    standing = L.standing_lessons(None, "s")
    assert [x.id for x in standing] == [2], "the one-class lesson must not reach the tier"


def test_a_lesson_with_no_recorded_skew_is_not_promoted(monkeypatch):
    # Unsafe by default rather than assumed safe: the optimistic default is
    # exactly what went wrong.
    import harness.lessons as L
    monkeypatch.setattr(L, "active_lessons", lambda conn, sid: [_lesson(1, 500, None)])
    assert L.standing_lessons(None, "s") == []


def test_support_still_orders_the_lessons_that_qualify(monkeypatch):
    import harness.lessons as L
    lessons = [_lesson(1, 10, 0.5), _lesson(2, 90, 0.6), _lesson(3, 50, 0.55)]
    monkeypatch.setattr(L, "active_lessons", lambda conn, sid: lessons)
    assert [x.id for x in L.standing_lessons(None, "s")] == [2, 3, 1]


def test_stratified_sample_draws_distinct_tasks_within_a_class():
    """Decision 78: no repeats until a class's pool is exhausted."""
    import random
    from types import SimpleNamespace

    from harness.scorer import stratified_sample

    adapter = SimpleNamespace(task_class=lambda t: t.cls)
    tasks = [SimpleNamespace(task_id=f"a{i}", cls="a") for i in range(18)] + \
            [SimpleNamespace(task_id=f"b{i}", cls="b") for i in range(15)]
    for seed in range(20):
        s = stratified_sample(adapter, tasks, 18, random.Random(seed))
        assert len(s) == 18 and len({t.task_id for t in s}) == 18
    small = stratified_sample(adapter, tasks[:3] + tasks[18:20], 8, random.Random(0))
    assert len(small) == 8, "beyond a class's size, replacement fills the quota"
