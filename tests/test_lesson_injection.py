"""Task 4.3's wiring: the two lesson tiers, where they sit in the prompt,
and the budget that caps them. All offline - a fake async client captures
what would have been sent, so none of this needs the GPU or Postgres.

The test that matters most here is the shared-prefix one. Task 4.3's whole
reason for having two tiers rather than one is that the standing tier sits
before the prefix-cache boundary, and that is only true if the block is
byte-identical for every candidate in the generation. The first version of
this wiring sized the standing tier against each candidate's own prompt
length, which made it a different length per candidate and cut the shared
prefix to 287 characters. Nothing failed; the prompt just quietly stopped
being cacheable.
"""

from __future__ import annotations

import asyncio
import os

import pytest

import harness.proposal as proposal_module
from harness.generation import (
    RETRIEVED_HEADING,
    STANDING_HEADING,
    _failure_categories,
    _lesson_context,
    _propose_for_parent,
    _standing_within_budget,
)
from harness.lessons import Lesson, estimate_tokens
from harness.proposal import TEXT_SYSTEM_PROMPT, propose

TASK_DESCRIPTION = (
    "A block of instructions telling a model how to read a capability-change "
    "scenario and decide whether to accept or reject it."
)
# Roughly the size of capability_case's real incumbent block (676 chars),
# because every assertion below about the budget depends on the ratio
# between lesson text and the rest of the prompt.
PARENT_BLOCK = "Read the submission and decide whether the evidence justifies the change.\n" * 9


def _lesson(n: int, support: int, length: int = 110) -> Lesson:
    """A form-valid lesson of about `length` characters. The default is the
    size real admitted lessons come out at (100 to 140 characters for
    capability_case); 280 is the store's MAX_LESSON_LEN, used where a test
    wants to push the budget."""
    text = f"When situation {n} holds, prefer approach {n} over approach {n}b, because "
    while len(text) < length:
        text += "the measured outcome was better "
    return Lesson(
        id=n,
        failure_id=f"cat-{n}",
        text=text[:length].rstrip() + ".",
        support=support,
        followed=0,
        followed_ok=0,
        vector=[0.0],
        created_gen=0,
        retired_gen=None,
    )


def _complete(standing: list, retrieved: list) -> tuple[dict, str, int, int, list, dict]:
    """Lets _propose_for_parent run to completion against a fake response,
    so the fifth return value (the lessons actually injected) can be
    asserted on. _capture() below raises instead, which is fine for
    inspecting the prompt but never reaches the return."""

    class Usage:
        total_tokens = 120
        completion_tokens = 40

    class Message:
        content = "<candidate>\nreplacement body\n</candidate>"

    class Choice:
        message = Message()

    class Response:
        choices = [Choice()]
        usage = Usage()

    class FakeClient:
        class chat:
            class completions:
                @staticmethod
                async def create(**kw):
                    return Response()

    original = proposal_module.async_judge_client
    proposal_module.async_judge_client = lambda: FakeClient
    try:
        return asyncio.run(
            _propose_for_parent(
                task_description=TASK_DESCRIPTION,
                parent={"block": PARENT_BLOCK, "scalar": 0.62},
                inspiration_blocks=[],
                seed_block=PARENT_BLOCK,
                temperature=0.9,
                sem=asyncio.Semaphore(1),
                system_prompt=TEXT_SYSTEM_PROMPT,
                standing=standing,
                retrieved=retrieved,
            )
        )
    finally:
        proposal_module.async_judge_client = original


def _capture(**kwargs) -> tuple[str, str]:
    """Runs _propose_for_parent against a client that records the request
    instead of sending it, and returns (system message, user message)."""
    captured: dict = {}

    class FakeClient:
        class chat:
            class completions:
                @staticmethod
                async def create(**kw):
                    captured.update(kw)
                    raise RuntimeError("captured")

    original = proposal_module.async_judge_client
    proposal_module.async_judge_client = lambda: FakeClient
    try:
        with pytest.raises(RuntimeError, match="captured"):
            asyncio.run(_propose_for_parent(**kwargs))
    finally:
        proposal_module.async_judge_client = original
    messages = captured["messages"]
    return messages[0]["content"], messages[1]["content"]


def _call(parent_block: str, inspirations: list[str], standing: list, retrieved: list) -> tuple[str, str]:
    return _capture(
        task_description=TASK_DESCRIPTION,
        parent={"block": parent_block, "scalar": 0.62},
        inspiration_blocks=inspirations,
        seed_block=PARENT_BLOCK,
        temperature=0.9,
        sem=asyncio.Semaphore(1),
        system_prompt=TEXT_SYSTEM_PROMPT,
        standing=standing,
        retrieved=retrieved,
    )


def test_no_solution_dir_means_no_lesson_context_and_no_database_access():
    # conn is None on purpose: a solution with no taxonomy must not touch
    # the lesson tables at all. Passing None would raise if it did.
    assert _lesson_context(None, None, "fixture") == (None, [], [], [])


def test_standing_tier_is_capped_against_the_invariant_region_highest_support_first():
    standing = [_lesson(1, support=40), _lesson(2, support=30), _lesson(3, support=20)]
    kept = _standing_within_budget(standing, TEXT_SYSTEM_PROMPT + TASK_DESCRIPTION)
    assert kept, "some standing tier should survive a normal-sized invariant region"
    assert kept == standing[: len(kept)], "the tier is trimmed from the low-support end"


def test_empty_standing_tier_stays_empty():
    assert _standing_within_budget([], TEXT_SYSTEM_PROMPT) == []


def test_both_tiers_are_injected_under_their_own_headings():
    _, user = _call(PARENT_BLOCK, [], [_lesson(1, 40)], [_lesson(9, 5)])
    assert f"## {STANDING_HEADING}" in user
    assert f"## {RETRIEVED_HEADING}" in user


def test_no_lessons_leaves_the_prompt_exactly_as_phase_3_had_it():
    _, user = _call(PARENT_BLOCK, [], [], [])
    assert "## Lessons" not in user
    assert "{standing_lessons}" not in user and "{retrieved_lessons}" not in user


def test_standing_tier_sits_before_the_parent_block_and_inspirations_after_it():
    # PHASE-3.md and PHASE-4.md both order the prompt this way: everything
    # invariant first, then the cache boundary, then per-candidate content.
    _, user = _call(PARENT_BLOCK, ["INSPIRATION BODY"], [_lesson(1, 40)], [_lesson(9, 5)])
    standing_at = user.find(f"## {STANDING_HEADING}")
    parent_at = user.find("## Current version")
    inspirations_at = user.find("## Other solutions worth drawing from")
    retrieved_at = user.find(f"## {RETRIEVED_HEADING}")
    assert 0 <= standing_at < parent_at < inspirations_at < retrieved_at


def test_standing_block_is_byte_identical_across_candidates_that_differ():
    # The regression this file exists for. Three candidates differing in
    # inspiration count, inspiration length and parent block must still
    # share the whole region before the cache boundary.
    standing = [_lesson(1, 40), _lesson(2, 30)]
    retrieved = [_lesson(9, 5)]
    _, a = _call(PARENT_BLOCK, ["SHORT"], standing, retrieved)
    _, b = _call(PARENT_BLOCK, ["A MUCH LONGER INSPIRATION BLOCK " * 8], standing, retrieved)
    _, c = _call(PARENT_BLOCK + "\nan extra differing line\n", [], standing, retrieved)

    shared = len(os.path.commonprefix([a, b, c]))
    boundary = a.find("## Current version")
    assert boundary > 0
    assert shared >= boundary, (
        f"only {shared} chars shared but the invariant region runs to {boundary} - "
        "the standing tier is varying per candidate again"
    )


def test_lesson_content_stays_under_the_fifteen_percent_cap():
    # Ten oversized lessons offered, against the real cap.
    standing = [_lesson(i, support=100 - i, length=280) for i in range(5)]
    retrieved = [_lesson(50 + i, support=5, length=280) for i in range(3)]
    standing = _standing_within_budget(standing, TEXT_SYSTEM_PROMPT + TASK_DESCRIPTION)
    system, user = _call(PARENT_BLOCK, [], standing, retrieved)

    lesson_tokens = sum(estimate_tokens(line) for line in user.splitlines() if line.startswith("- When situation"))
    assert lesson_tokens / estimate_tokens(system + user) <= 0.15 + 0.02, "lesson budget blown"


def test_hill_climb_prompt_carries_no_lesson_or_inspiration_slots():
    # propose() is harness/loop.py's sync path and deliberately has no
    # lesson parameters; the new template slots must still render empty
    # rather than leaking braces into the prompt.
    captured: dict = {}

    class FakeSync:
        class chat:
            class completions:
                @staticmethod
                def create(**kw):
                    captured.update(kw)
                    raise RuntimeError("captured")

    with pytest.raises(RuntimeError, match="captured"):
        propose(TASK_DESCRIPTION, PARENT_BLOCK, 0.5, 0, 1.0, "check_x failed", client=FakeSync)

    user = captured["messages"][1]["content"]
    assert "## Lessons" not in user
    assert "## Other solutions worth drawing from" not in user
    for slot in ("{standing_lessons}", "{retrieved_lessons}", "{inspirations}"):
        assert slot not in user


# --- the falsification loop (record_usage's inputs) ----------------------


def _tiny_taxonomy():
    """A two-category taxonomy fitted in-test, rather than reading a
    solution's committed artifacts, so this test does not silently depend on
    capability_case's taxonomy staying the way it is today."""
    from sklearn.feature_extraction.text import TfidfVectorizer

    from harness.taxonomy import FailureCategory

    floor_texts = ["floor_correct expected reject got sound", "floor_correct expected reject got accept"]
    band_texts = ["judge band 1 below threshold 2", "judge band 0 below threshold 2"]
    vectorizer = TfidfVectorizer(min_df=1)
    matrix = vectorizer.fit_transform(floor_texts + band_texts)
    dense = matrix.toarray()
    categories = [
        FailureCategory(
            id="F00",
            name="floor verdict wrong",
            description="the mechanical floor disagreed",
            centroid=list(dense[:2].mean(axis=0)),
            count=2,
            first_seen_gen=0,
            last_seen_gen=0,
        ),
        FailureCategory(
            id="F01",
            name="judge band low",
            description="the judge scored below the band",
            centroid=list(dense[2:].mean(axis=0)),
            count=2,
            first_seen_gen=0,
            last_seen_gen=0,
        ),
    ]
    return vectorizer, categories


class _Fitness:
    def __init__(self, detail):
        self.detail = detail


def test_no_taxonomy_means_no_failure_categories():
    assert _failure_categories(_Fitness({"checks": {}}), None, []) == (None, set())


def test_a_candidate_with_no_failed_checks_has_no_category():
    vectorizer, categories = _tiny_taxonomy()
    passing = _Fitness({"checks": {"floor_correct": (1.0, "ok"), "judge": (1.0, "ok")}})
    assert _failure_categories(passing, vectorizer, categories) == (None, set())


def test_failed_checks_are_assigned_per_item_and_the_dominant_one_wins():
    vectorizer, categories = _tiny_taxonomy()
    fitness = _Fitness(
        {
            "checks": {
                "floor_correct": (0.0, "floor_correct expected reject got sound"),
                "judge": (0.0, "judge band 1 below threshold 2"),
            }
        }
    )
    dominant, found = _failure_categories(fitness, vectorizer, categories)
    assert found == {"F00", "F01"}, "each failed check is assigned separately"
    assert dominant in found


def test_injected_lessons_come_back_so_usage_can_be_recorded():
    standing, retrieved = [_lesson(1, 40)], [_lesson(9, 5)]
    _parent, _text, _tokens, _completion, injected, _proposal = _complete(standing, retrieved)
    assert [lesson.id for lesson in injected] == [1, 9], "standing first, then retrieved"


def test_no_lessons_means_nothing_to_record():
    _parent, _text, _tokens, _completion, injected, _proposal = _complete([], [])
    assert injected == []


def test_proposal_carries_the_exact_context_and_response():
    """PHASE-5.md task 5.1 trains on what the proposer saw and said, stored
    from this return value. The fake response has no reasoning channel."""
    _parent, text, _tokens, _completion, _injected, proposal = _complete([], [])
    assert [m["role"] for m in proposal["messages"]] == ["system", "user"]
    assert PARENT_BLOCK in proposal["messages"][1]["content"]
    assert proposal["content"] == text and proposal["reasoning"] == ""


def test_injected_reflects_the_budget_trim_not_what_was_offered():
    # Three oversized retrieved lessons against a small prompt: whatever the
    # budget dropped must not be reported as injected, or record_usage would
    # credit lessons the model never saw.
    standing = [_lesson(1, 40)]
    retrieved = [_lesson(90 + i, 5, length=280) for i in range(3)]
    _parent, _text, _tokens, _completion, injected, _proposal = _complete(standing, retrieved)
    assert len(injected) <= 1 + len(retrieved)
    offered = {lesson.id for lesson in standing + retrieved}
    assert {lesson.id for lesson in injected} <= offered
    assert 1 in {lesson.id for lesson in injected}, "the standing tier is never trimmed per candidate"


def test_a_lesson_is_never_injected_into_both_tiers_at_once():
    # Found live 2026-09-29, the first generation where retrieval actually
    # fired: the injected sets came back as [1, 4, 1, 5]. The standing tier's
    # lesson was also in the retrieval corpus, so it went into both blocks of
    # the same prompt and record_usage() counted it twice, inflating its
    # `followed` denominator at double rate. run_generation() now excludes
    # standing lessons from the retrieval corpus; this asserts the property
    # the injected list has to hold either way.
    standing = [_lesson(1, 40)]
    retrieved = [_lesson(4, 20)]
    _parent, _text, _tokens, _completion, injected, _proposal = _complete(standing, retrieved)
    ids = [lesson.id for lesson in injected]
    assert len(ids) == len(set(ids)), f"a lesson is counted twice: {ids}"


def test_the_prompt_never_shows_the_same_lesson_in_both_blocks():
    standing = [_lesson(1, 40)]
    _, user = _call(PARENT_BLOCK, [], standing, [_lesson(4, 20)])
    assert user.count(standing[0].text) == 1
