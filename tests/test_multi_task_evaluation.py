"""Aggregating several per-task evaluations into one candidate fitness.

Scoring each candidate on a single randomly sampled rotation task was wrong
twice over, both measured 2026-09-28. try_insert() ranks candidates against
each other, but they were scored on different tasks, so archive placement
turned substantially on which task a candidate drew. And a candidate that
passed its one task produced no failure evidence, which starved task 4.3's
retrieved lesson tier so completely that across a full generation of 32
candidates not one received a retrieved lesson.

The two properties worth protecting here are that cost has two different
right answers (mean for the fitness scalar, total for the budget) and that a
gate-failed task's evidence survives the merge.
"""

from __future__ import annotations

from harness.fitness import COST_REF_TOKENS, Fitness
from harness.generation import _aggregate_fitness
from harness.taxonomy import extract_evidence


def _f(valid=True, quality=1.0, cost=3000, latency=40.0, descriptors=(3, 2), detail=None):
    return Fitness(
        valid=valid,
        quality=quality,
        cost_tokens=cost,
        latency_s=latency,
        descriptors=descriptors,
        detail=detail if detail is not None else {"checks": {"floor_correct": (1.0, "ok")}},
    )


def test_quality_and_latency_are_means():
    agg, _ = _aggregate_fitness([_f(quality=1.0, latency=30.0), _f(quality=0.0, latency=50.0)], ["a", "b"])
    assert agg.quality == 0.5
    assert agg.latency_s == 40.0


def test_one_invalid_task_makes_the_candidate_invalid():
    agg, _ = _aggregate_fitness([_f(valid=True), _f(valid=False, quality=0.0)], ["a", "b"])
    assert agg.valid is False
    assert agg.scalar == 0.0


def test_cost_is_the_mean_for_fitness_and_the_total_for_the_budget():
    agg, total = _aggregate_fitness([_f(cost=3000), _f(cost=3600), _f(cost=200)], ["a", "b", "c"])
    assert total == 6800, "the budget must see real spend across every task"
    assert agg.cost_tokens == 2267, "the fitness sees the per-task mean"


def test_summing_cost_into_fitness_would_have_saturated_the_penalty():
    # Why the split above exists rather than just summing. Fitness.scalar
    # penalises cost against a 4,000-token anchor and clamps at 2.0, so three
    # realistic tasks summed would peg every candidate at the maximum cost
    # penalty and leave quality as the only thing separating them.
    per_task = [_f(cost=3000), _f(cost=3600), _f(cost=3200)]
    agg, total = _aggregate_fitness(per_task, ["a", "b", "c"])
    assert total / COST_REF_TOKENS > 2.0, "summed cost is past the clamp"
    assert agg.cost_tokens / COST_REF_TOKENS < 2.0, "the mean still discriminates"


def test_descriptors_are_the_per_axis_median_not_one_task_s_luck():
    per_task = [_f(descriptors=(3, 2)), _f(descriptors=(2, 3)), _f(descriptors=(0, 5))]
    agg, _ = _aggregate_fitness(per_task, ["a", "b", "c"])
    assert agg.descriptors == (2, 3)


def test_a_gate_failed_task_keeps_its_evidence_through_the_merge():
    # The old single-task detail carried a gate failure as a top-level "gate"
    # key. Only one such key can survive merging several tasks, so gate
    # failures become failed checks instead, which is also the shape
    # extract_evidence() already reads.
    per_task = [
        _f(detail={"checks": {"floor_correct": (0.0, "expected reject got sound")}}),
        _f(valid=False, detail={"gate": "shape", "error": "judge never returned a verdict"}),
    ]
    agg, _ = _aggregate_fitness(per_task, ["t-01", "t-02"])
    evidence = extract_evidence([agg.detail], [None])
    texts = {item.text for item in evidence}
    assert "expected reject got sound" in texts
    assert "judge never returned a verdict" in texts, "gate evidence must not be dropped"


def test_check_names_are_task_scoped_so_tasks_do_not_overwrite_each_other():
    per_task = [
        _f(detail={"checks": {"floor_correct": (0.0, "first task evidence")}}),
        _f(detail={"checks": {"floor_correct": (0.0, "second task evidence")}}),
    ]
    agg, _ = _aggregate_fitness(per_task, ["t-01", "t-02"])
    assert len(agg.detail["checks"]) == 2
    assert len(extract_evidence([agg.detail], [None])) == 2


def test_completion_tokens_are_summed_because_they_are_real_decode_output():
    per_task = [
        _f(detail={"checks": {}, "completion_tokens": 500}),
        _f(detail={"checks": {}, "completion_tokens": 700}),
    ]
    agg, _ = _aggregate_fitness(per_task, ["a", "b"])
    assert agg.detail["completion_tokens"] == 1200
    assert agg.detail["n_tasks"] == 2


def test_a_single_task_still_aggregates_cleanly():
    agg, total = _aggregate_fitness([_f(cost=3000, quality=0.75)], ["only"])
    assert agg.quality == 0.75
    assert agg.cost_tokens == 3000 and total == 3000
    assert agg.detail["n_tasks"] == 1


def _judge_failed():
    return _f(valid=False, quality=0.0, descriptors=(0, 0),
              detail={"gate": "judge_failed", "error": "APITimeoutError('Request timed out.')"})


def test_a_judge_failure_is_missing_data_not_an_invalid_candidate():
    # 130 judge failures across six ablation runs each threw a candidate out
    # of the archive whose own output had passed every gate (decision 66).
    agg, total = _aggregate_fitness([_f(quality=1.0), _f(quality=0.5), _judge_failed()], ["a", "b", "c"])
    assert agg.valid is True
    assert agg.quality == 0.75, "the failed task must not count as a zero"
    assert agg.descriptors == (3, 2), "the failed task's (0, 0) must not drag the median"
    assert total == 9000, "the budget still sees the judged task's spend"


def test_a_candidate_s_own_gate_failure_still_invalidates_it():
    shape = _f(valid=False, quality=0.0, detail={"gate": "shape", "got": "rejected\naudit missing"})
    agg, _ = _aggregate_fitness([_f(), shape, _judge_failed()], ["a", "b", "c"])
    assert agg.valid is False


def test_every_judge_failing_leaves_the_candidate_invalid():
    agg, _ = _aggregate_fitness([_judge_failed(), _judge_failed()], ["a", "b"])
    assert agg.valid is False
