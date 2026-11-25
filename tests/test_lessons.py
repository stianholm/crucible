"""See PHASE-4.md task 4.2's three rules. admissible_lesson is rule
three's mechanical enforcement - the one that has to actually reject
things, or it isn't a filter.
"""

from __future__ import annotations

from harness.lessons import MAX_LESSON_LEN, admissible_lesson, underperforms


def test_well_formed_lesson_is_admitted():
    ok, reason = admissible_lesson(
        "When the evidence dimension is entirely absent, prefer an automatic reject "
        "over needs_more_evidence, because absence is a floor violation, not a weak dimension."
    )
    assert ok, reason


def test_rejects_text_not_in_template_form():
    ok, reason = admissible_lesson("Always double check the evidence dimensions before answering.")
    assert not ok
    assert "form" in reason


def test_rejects_hedging_language():
    # matches the When/prefer/over/because shape, so this exercises the
    # hedge check specifically, not the template check
    ok, reason = admissible_lesson(
        "When evidence seems thin, prefer to try to reject over accepting, because it might be safer."
    )
    assert not ok
    assert "hedg" in reason


def test_rejects_overlong_text():
    filler = "extremely " * 40
    text = f"When the case is {filler}unclear, prefer reject over sound, because it is too long to act on cleanly."
    assert len(text) > MAX_LESSON_LEN
    ok, reason = admissible_lesson(text)
    assert not ok
    assert "long" in reason


def test_collapses_internal_whitespace_before_checking():
    ok, _ = admissible_lesson(
        "When   the floor  fails,\nprefer reject   over sound, because the floor is unconditional."
    )
    assert ok


# --- retirement as a significance test, not a threshold --------------------


def test_a_single_generation_of_data_never_retires_anything():
    # The case that made min_followed = 20 wrong. 32 candidates each carry the
    # standing tier, so one generation clears that threshold, and 25 of 32
    # against a base rate of 0.835 is only 0.7 sigma below it. A fixed
    # threshold retires here; the test must not.
    retire, reason = underperforms(followed=32, followed_ok=25, base_rate=0.835, control_group=100)
    assert retire is False
    assert "0.7 sigma" in reason


def test_the_same_shortfall_retires_once_there_is_enough_of_it():
    retire, reason = underperforms(followed=320, followed_ok=250, base_rate=0.835, control_group=1000)
    assert retire is True
    assert "sigma below" in reason


def test_a_lesson_beating_its_base_rate_is_never_retired():
    retire, reason = underperforms(followed=100, followed_ok=95, base_rate=0.835, control_group=100)
    assert retire is False
    assert ">=" in reason


def test_a_standing_tier_lesson_cannot_be_retired_and_says_why():
    # It goes into every prompt by construction, so nothing in a lessons-on
    # run is a control for it. PHASE-4.md task 4.5's arm A is the only way.
    retire, reason = underperforms(followed=500, followed_ok=400, base_rate=None, control_group=0)
    assert retire is False
    assert "arm A" in reason


def test_a_lesson_that_was_never_injected_is_not_judged():
    retire, reason = underperforms(followed=0, followed_ok=0, base_rate=0.9, control_group=100)
    assert retire is False
    assert reason == "never injected"


def test_a_tiny_control_group_widens_the_error_and_protects_the_lesson():
    # Same precision and base rate, different control-group size. The
    # comparison has to account for uncertainty on both sides, not just the
    # treated arm.
    big = underperforms(followed=200, followed_ok=150, base_rate=0.9, control_group=1000)
    small = underperforms(followed=200, followed_ok=150, base_rate=0.9, control_group=3)
    assert big[0] is True
    assert small[0] is False, "three control candidates cannot condemn a lesson"
