"""Task 4.6's repeat-failure rate, tested on the pure core.

The metric is the one PHASE-4.md says decides whether reflection worked at
all, so the arithmetic is worth pinning down independently of a database.
`repeat_rate_from_rows` takes the (generation, failure_id) rows the query
produces, which is everything the definition needs.
"""

from __future__ import annotations

from harness.learning_metrics import (
    REPEAT_WINDOW,
    repeat_rate_from_rows,
    trend,
    volume_from_details,
)


def test_the_first_generation_has_no_rate_at_all():
    # Not 0.0: nothing in the first generation of a run *can* be a repeat, so a
    # zero there is the absence of a measurement. Scoring it as zero made the
    # first real ten-generation series read as "rising 53%" when generations 1
    # to 9 were flat.
    rows = [(0, "F00"), (0, "F01")]
    assert repeat_rate_from_rows(rows) == [(0, 2, None)]


def test_a_category_seen_in_an_earlier_generation_is_a_repeat():
    rows = [(0, "F00"), (1, "F00")]
    assert repeat_rate_from_rows(rows) == [(0, 1, None), (1, 1, 1.0)]


def test_a_category_repeated_within_one_generation_is_not_counted_against_itself():
    # Two candidates failing the same way in the same generation is not a
    # repeat: the window is the generations strictly before this one. Needs a
    # prior generation present so the rate is defined at all.
    rows = [(0, "F09"), (1, "F00"), (1, "F00")]
    by_generation = dict((g, rate) for g, _n, rate in repeat_rate_from_rows(rows))
    assert by_generation[1] == 0.0


def test_the_window_has_an_edge():
    # F00 in generation 0 and again in 6 is outside a five-generation window,
    # so generation 6 counts it as new rather than as a repeat. The rate is
    # still defined: generation 6 has a generation behind it, even though the
    # window itself is empty.
    rows = [(0, "F00"), (6, "F00")]
    result = dict((g, rate) for g, _n, rate in repeat_rate_from_rows(rows, window=REPEAT_WINDOW))
    assert result[6] == 0.0
    rows = [(0, "F00"), (5, "F00")]
    result = dict((g, rate) for g, _n, rate in repeat_rate_from_rows(rows, window=REPEAT_WINDOW))
    assert result[5] == 1.0


def test_a_mixed_generation_gives_a_fraction():
    rows = [(0, "F00"), (1, "F00"), (1, "F01"), (1, "F02"), (1, "F03")]
    by_generation = dict((g, rate) for g, _n, rate in repeat_rate_from_rows(rows))
    assert by_generation[1] == 0.25, "one of four categories was seen before"


def test_generations_with_no_failures_simply_do_not_appear():
    # Nothing to divide by, and inventing a 0.0 for a generation where every
    # candidate passed would drag the trend down for the wrong reason.
    rows = [(0, "F00"), (2, "F00")]
    assert [g for g, _n, _r in repeat_rate_from_rows(rows)] == [0, 2]


def test_trend_ignores_the_undefined_first_generation():
    # The bug this pair of changes exists for: a structural None at the start
    # must not read as an improvement from zero.
    series = [None, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95]
    assert trend(series).startswith("flat")


def test_trend_refuses_to_call_a_short_series():
    assert "too few" in trend([1.0, 0.5])


def test_trend_names_the_direction():
    assert trend([1.0, 1.0, 1.0, 0.2, 0.2, 0.2]).startswith("falling")
    assert trend([0.2, 0.2, 0.2, 1.0, 1.0, 1.0]).startswith("RISING")
    assert trend([0.5] * 6).startswith("flat")


# --- instruments that are not saturated ------------------------------------


def test_failure_volume_counts_checks_not_candidates():
    # A candidate going from four failed checks to one is learning, and
    # counting candidates-that-failed cannot see it.
    rows = [
        (0, {"checks": {"a": (0.0, "x"), "b": (0.0, "y"), "c": (1.0, "ok")}}),
        (0, {"checks": {"a": (1.0, "ok")}}),
        (1, {"checks": {"a": (0.0, "x")}}),
        (1, {"checks": {"a": (1.0, "ok")}}),
    ]
    assert volume_from_details(rows) == [(0, 2, 1, 1.0), (1, 2, 1, 0.5)]


def test_failure_volume_survives_a_missing_detail():
    rows = [(0, None), (0, {"checks": {"a": (0.0, "x")}})]
    generation, candidates, with_failures, mean_failed = volume_from_details(rows)[0]
    assert (candidates, with_failures, mean_failed) == (2, 1, 0.5)


def test_failure_volume_counts_a_gate_failure_as_a_failure():
    rows = [(0, {"gate": "shape", "error": "no verdict"})]
    assert volume_from_details(rows) == [(0, 1, 1, 1.0)]
