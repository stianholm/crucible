"""The lesson store. See PHASE-4.md task 4.2.

Three rules keep it from becoming a dumping ground of plausible-sounding
advice that costs prompt tokens on every proposal forever:

1. Lessons are earned, not observed - support from at least MIN_SUPPORT
   distinct failures before admission.
2. The judge writes lessons, never the proposer - a proposer that writes
   its own guidance and follows it never contacts ground truth.
3. A lesson must be actionable, enforced mechanically - the When/prefer/
   over/because template, checked by regex, not by a model's opinion of
   itself.

`vector` here is a TF-IDF vector (harness/taxonomy.py's vectorizer), not a
real semantic embedding - see harness/persistence.py's schema comment for
why PHASE-4.md's pgvector column isn't available on this hardware.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

import numpy as np
import psycopg

from harness.judge import judge_client
from harness.persistence import ensure_schema

MIN_SUPPORT = 5

TEMPLATE = re.compile(r"^When .+?, prefer .+? over .+?, because .+?\.$", re.S)
HEDGES = ("be careful", "make sure", "try to", "consider", "keep in mind")
MAX_LESSON_LEN = 300

WRITING_PROMPT = """You are writing one actionable lesson from a recurring failure pattern in an \
automated search system, for a future attempt to read before it tries again.

You must respond with EXACTLY one sentence, in EXACTLY this form, nothing else:
When <situation>, prefer <the better approach> over <the failing approach>, because <the reason>.

Rules:
- One sentence only. No preamble, no explanation, no markdown.
- Be specific and directive. Do not hedge ("be careful", "make sure", "try to", "consider").
- Ground it only in what the samples below actually show - do not invent a fix they don't support.

Failure samples (all from the same recurring category):
{samples}
"""


@dataclass
class Lesson:
    id: int
    failure_id: str
    text: str
    support: int
    followed: int
    followed_ok: int
    vector: list[float]
    created_gen: int
    retired_gen: int | None
    class_skew: float | None = None  # 1.0 = the category occurs on one task class only


# The task's own output vocabulary. A lesson that advises changing one of
# these is reasoning about the scoring machinery rather than about the work.
OUTPUT_LABELS = ("band",)

# Verbs that act on the *submission* rather than on the verdict. The candidate
# judges capability cases; it cannot add a rollback mechanism to one.
SUBMITTER_VERBS = (
    "including", "implementing", "adding", "retaining", "satisfying",
    "providing", "establishing", "defining", "finalising", "finalizing",
)

# Words that name a verdict, which is what a judging lesson should steer.
VERDICT_WORDS = ("reject", "accept", "sound", "needs_more_evidence", "needs more evidence")


def admissible_lesson(text: str) -> tuple[bool, str]:
    """Rule three, enforced mechanically - a lesson is checked the same
    way a candidate is, not trusted because a judge wrote it.

    The first three checks (template, length, hedging) check *form*. Two
    derivations against real data showed that form is not the problem: of 14
    lessons admitted across them, 10 were wrong in kind while being perfectly
    well-formed. The two checks below target the two error modes that actually
    recurred, both mechanically detectable:

    **Output-label advice.** Three separate lessons advised changing the judge
    rubric's own BAND value ("prefer BAND:2 over BAND:0", "prefer avoiding BAND
    values over using them"). That is reasoning about the scoring machinery, not
    about judging a capability case.

    **Submitter advice.** Four lessons advised changing the submission rather
    than reaching a verdict ("prefer including a clearly executable manual
    override mechanism over omitting it"). The candidate evaluates submissions;
    it cannot add features to them. Detected as a construction verb in the
    prefer-clause with no verdict word anywhere - so a lesson that says "prefer
    reject over needs_more_evidence" passes, and one that says "prefer including
    them" does not.

    Neither check can catch a lesson that is well-formed, verdict-shaped and
    simply wrong, which is why PHASE-6.md's human read stays in the loop."""
    t = " ".join(text.split())
    if not TEMPLATE.match(t):
        return False, "not in the When/prefer/over/because form"
    if len(t) > MAX_LESSON_LEN:
        return False, "too long to act on"
    if any(h in t.lower() for h in HEDGES):
        return False, "hedging rather than directing"
    low = t.lower()
    if any(label in low for label in OUTPUT_LABELS):
        return False, "advises changing the rubric's own output label, not the work"
    # The advice is what sits between "prefer" and "because" - scanning the
    # whole sentence is defeated by the because-clause, which routinely
    # contains a verdict word while the advice itself does not: "prefer fully
    # satisfying all checklist items over partial addressing, because partial
    # addressing leads to rejection" passed a whole-sentence check on the word
    # "rejection" while advising the submitter. Found testing this rule against
    # the real lessons rather than inventing cases for it.
    advice = low.split("prefer", 1)[1] if "prefer" in low else low
    advice = advice.split("because", 1)[0]
    if any(v in advice for v in SUBMITTER_VERBS) and not any(v in advice for v in VERDICT_WORDS):
        return False, "advises changing the submission rather than reaching a verdict"
    return True, "ok"


def write_lesson(samples: list[str]) -> str:
    """Rule two - only ever called with the judge role, never the
    proposer. One call per candidate lesson, not per failure."""
    prompt = WRITING_PROMPT.format(samples="\n".join(f"- {s[:300]}" for s in samples))
    r = judge_client().chat.completions.create(
        model="judge",
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )
    text = r.choices[0].message.content or ""
    if "</think>" in text:
        text = text.split("</think>", 1)[-1]
    return " ".join(text.strip().split())


def propose_lesson(failure_id: str, samples: list[str]) -> tuple[str | None, str]:
    """Rule one - only called by the caller once support >= MIN_SUPPORT
    has already been confirmed. Returns (text, reason) - text is None if
    the mechanical check (rule three) rejected the judge's attempt."""
    text = write_lesson(samples)
    ok, reason = admissible_lesson(text)
    return (text if ok else None), reason


def admit_lesson(
    conn: psycopg.Connection,
    solution_id: str,
    failure_id: str,
    text: str,
    support: int,
    vector: list[float],
    created_gen: int,
    class_skew: float | None = None,
) -> int:
    ensure_schema(conn)  # matches IterationWriter's own pattern - the lesson table may not exist yet
    # Rule one says lessons are "earned, deduplicated and retired", and
    # deduplication was never implemented. Two derivations against the same
    # categories produced byte-identical text (lessons 10 and 17, both from
    # F02), which would have been injected together and double-counted in the
    # falsification loop. Normalised comparison, since the only difference
    # between regenerations is usually whitespace.
    normalised = " ".join(text.split())
    with conn.cursor() as cur:
        cur.execute(
            "select id from lesson where solution_id = %s and retired_gen is null",
            (solution_id,),
        )
        existing_ids = [r[0] for r in cur.fetchall()]
        if existing_ids:
            cur.execute(
                "select id, text from lesson where id = any(%s)",
                (existing_ids,),
            )
            for lid, existing in cur.fetchall():
                if " ".join(existing.split()) == normalised:
                    return lid  # already in the store, active; nothing to admit
    with conn.cursor() as cur:
        cur.execute(
            """
            insert into lesson (solution_id, failure_id, text, support, vector, created_gen, class_skew)
            values (%s, %s, %s, %s, %s, %s, %s)
            returning id
            """,
            (solution_id, failure_id, text, support, vector, created_gen, class_skew),
        )
        lesson_id = cur.fetchone()[0]
    conn.commit()
    return lesson_id


def active_lessons(conn: psycopg.Connection, solution_id: str) -> list[Lesson]:
    # No ensure_schema() here, nor in base_avoidance_rate() below. Both are
    # read-only, and ensure_schema() issues DDL that takes an ACCESS EXCLUSIVE
    # lock on `iteration` even when every column already exists. A read issued
    # from a second process while a run holds a transaction open then blocks on
    # that lock and queues the run's own next statement behind it - measured
    # 2026-09-29, 153 seconds before it had to be cancelled. Writers still call
    # it; IterationWriter.__init__ has already run it on the run's connection,
    # and it is now idempotent per connection.
    with conn.cursor() as cur:
        cur.execute(
            """
            select id, failure_id, text, support, followed, followed_ok, vector, created_gen, retired_gen,
                   class_skew
            from lesson where solution_id = %s and retired_gen is null
            """,
            (solution_id,),
        )
        return [Lesson(*row) for row in cur.fetchall()]


def record_usage(conn: psycopg.Connection, lesson_id: int, avoided_failure: bool) -> None:
    """Called once per generation a lesson was injected into a proposal,
    after that candidate's evaluation is known - the falsification loop
    retirement depends on."""
    ensure_schema(conn)
    with conn.cursor() as cur:
        cur.execute(
            "update lesson set followed = followed + 1, followed_ok = followed_ok + %s where id = %s",
            (1 if avoided_failure else 0, lesson_id),
        )
    conn.commit()


def retire_manually(conn: psycopg.Connection, lesson_id: int, gen: int, reason: str) -> None:
    """The weekly-elite-read escape hatch (PHASE-6.md's "What stays manual,
    permanently"): a human judging a lesson nonsensical or wrong before it
    has ever accumulated enough `followed` count for retire_underperforming
    to see it. The mechanical admissible_lesson() filter only checks form
    (When/prefer/over/because, length, no hedge words) - it cannot and does
    not check whether a form-valid lesson actually makes sense. Found
    needing this for real, not hypothetically: task 4.2's own first real
    verification against capability_case data admitted "When BAND is 0,
    prefer BAND:2 over BAND:0, because BAND:2 indicates a higher quality
    result" - perfectly-formed, meaningless, because it mistook the judge's
    own output label for something actionable."""
    ensure_schema(conn)
    with conn.cursor() as cur:
        cur.execute(
            "update lesson set retired_gen = %s, retired_reason = %s where id = %s and retired_gen is null",
            (gen, reason, lesson_id),
        )
    conn.commit()


def base_avoidance_rate(conn: psycopg.Connection, solution_id: str, lesson_id: int) -> tuple[float | None, int]:
    """The rate one lesson has to beat, computed per lesson rather than once
    store-wide, and returned with the size of the control group it came from.

    PHASE-4.md's retirement SQL takes a single `base_avoidance_rate` for the
    whole store. That number cannot be measured the way the phase document
    implies. Its meaning is "how often candidates that never received this
    lesson avoided the failure anyway", and most scored candidates avoid
    every category simply by passing their sampled task - roughly 28 in 40
    on real capability_case data - so a store-wide rate mostly measures how
    often candidates pass, not anything about a lesson.

    Per lesson it is measurable, because injection is per candidate: the
    control group is candidates that did not receive this lesson, and
    avoidance means this lesson's own category is absent from their
    evidence. Rows are restricted to those that went through task 4.3's
    recording path at all (`failure_id` computed), since every row written
    before 2026-09-28 has the column NULL because it did not exist, and
    counting those as avoidances would return 1.0 for everything.

    Returns (None, 0) when there is no control group, which is the honest
    answer for a standing-tier lesson: the standing tier goes into every
    candidate's prompt by construction, so nothing within a lessons-on run
    is a control for it. That comparison needs task 4.5's arm A."""
    with conn.cursor() as cur:
        cur.execute("select failure_id from lesson where id = %s", (lesson_id,))
        row = cur.fetchone()
        if row is None:
            return None, 0
        failure_id = row[0]
        # Avoidance means this lesson's category is absent from the whole
        # category set, matching how _record_lesson_outcome() scores a treated
        # candidate. Comparing against failure_id (the dominant category) here
        # while the treated side used the full set is what biased every lesson
        # toward retirement; both sides now read failure_ids. A row with no
        # failure evidence has failure_ids NULL, which is an avoidance.
        cur.execute(
            """
            select count(*) filter (
                     where failure_ids is null or not (failure_ids @> array[%s]::text[])
                   ),
                   count(*)
              from iteration
             where solution_id = %s
               and status = 'scored'
               and lessons_injected is not null
               and not (lessons_injected @> array[%s]::integer[])
               -- Only rows from runs recorded under the failure_ids scheme.
               --
               -- Excluding pre-column rows individually is not enough, and
               -- measuring it showed why: a pre-column row that *had*
               -- failures is identifiable (failure_id set, failure_ids NULL)
               -- and gets dropped, but one with no failures is
               -- indistinguishable from a new-scheme row and survives. That
               -- leaves a control group made only of candidates that never
               -- failed, and every base rate reads exactly 1.0 - a selection
               -- bias worse than the asymmetry this was meant to fix. The
               -- whole run has to be in or out.
               and run_id in (
                     select run_id from iteration
                      where solution_id = %s and failure_ids is not null
                   )
            """,
            (failure_id, solution_id, lesson_id, solution_id),
        )
        avoided, total = cur.fetchone()
    return (avoided / total if total else None), total


def retire_underperforming(
    conn: psycopg.Connection,
    solution_id: str,
    gen: int,
    base_avoidance_rate: float,
    min_followed: int = 20,
) -> list[int]:
    """A lesson that does no better than the base rate for candidates that
    never received it is retired - the part that is almost always skipped,
    and what stops the store rotting."""
    ensure_schema(conn)
    with conn.cursor() as cur:
        cur.execute(
            """
            update lesson
               set retired_gen = %s
             where solution_id = %s
               and retired_gen is null
               and followed >= %s
               and followed_ok::real / followed < %s
            returning id
            """,
            (gen, solution_id, min_followed, base_avoidance_rate),
        )
        retired = [row[0] for row in cur.fetchall()]
    conn.commit()
    return retired


# --- Retirement that asks whether the shortfall is real --------------------

RETIREMENT_SIGMAS = 2.0


def underperforms(
    followed: int,
    followed_ok: int,
    base_rate: float | None,
    control_group: int,
    sigmas: float = RETIREMENT_SIGMAS,
) -> tuple[bool, str]:
    """Whether a lesson does measurably worse than candidates that never
    received it, by a two-proportion test at `sigmas` standard errors.

    This supersedes retire_underperforming()'s `min_followed` threshold for
    the ordinary case. A fixed threshold is a guess standing in for a
    confidence judgement, and the guess was badly wrong: 20 is cleared by a
    single generation, because 32 candidates each carry the standing tier, so
    the rule could retire a lesson on eight-tenths of a sigma. Raising it to a
    few hundred would have been another guess. The test below needs no
    threshold at all - a small sample produces a large standard error and so
    never clears the bar, which is the sufficiency check the threshold was
    reaching for.

    It also has to be a *difference* test rather than a ratio comparison,
    because per-category base rates run 0.94 to 0.99 on real data (any one
    failure category is individually rare), and comparing a raw ratio against
    a number that high would retire almost every lesson.

    Returns (verdict, one-line reason), because a retirement nobody can read
    the reasoning for is one nobody will trust."""
    if base_rate is None or control_group == 0:
        return False, "no control group (standing tier: needs PHASE-4.md task 4.5 arm A)"
    if followed == 0:
        return False, "never injected"
    precision = followed_ok / followed
    if precision >= base_rate:
        return False, f"precision {precision:.3f} >= base {base_rate:.3f}"
    se = math.sqrt(
        precision * (1 - precision) / followed + base_rate * (1 - base_rate) / control_group
    )
    if se == 0:
        return False, "zero variance in both arms, nothing to test"
    shortfall = (base_rate - precision) / se
    if shortfall > sigmas:
        return True, f"precision {precision:.3f} vs base {base_rate:.3f}, {shortfall:.1f} sigma below"
    return False, f"precision {precision:.3f} vs base {base_rate:.3f}, only {shortfall:.1f} sigma below"


def retire_underperforming_significant(
    conn: psycopg.Connection,
    solution_id: str,
    gen: int,
    sigmas: float = RETIREMENT_SIGMAS,
    dry_run: bool = False,
) -> list[tuple[int, bool, str]]:
    """Every active lesson judged against its own control group. Returns
    (lesson_id, retired, reason) for all of them, not just the retired ones,
    so a run's report can say why each lesson survived.

    dry_run evaluates without writing, which is what to use before trusting
    this against a store that matters."""
    verdicts = []
    for lesson in active_lessons(conn, solution_id):
        base_rate, control_group = base_avoidance_rate(conn, solution_id, lesson.id)
        retire, reason = underperforms(
            lesson.followed, lesson.followed_ok, base_rate, control_group, sigmas
        )
        verdicts.append((lesson.id, retire, reason))
        if retire and not dry_run:
            retire_manually(conn, lesson.id, gen, f"underperforming: {reason}")
    return verdicts


# --- Task 4.3: retrieval, injection, and the prompt budget -----------------
#
# Two tiers, per PHASE-4.md's own diagram. Standing lessons are the
# highest-support lessons store-wide, computed once per generation (same
# for every candidate that generation, so they sit before the point where
# per-candidate content starts varying the prompt). Retrieved lessons are
# similarity-matched per candidate, against the parent's own recent failure
# evidence, and sit later, alongside the other per-candidate content.
#
# Token budget here is a character-count approximation (roughly 4
# characters per token for English text), not a real tokenizer count - the
# harness runs on the host, which has no tokenizer for gpt-oss-120b
# installed (installing one, e.g. via transformers, is a real dependency
# for a proposal-time budget check, not done here). Disclosed as an
# approximation, not presented as exact the way every other token count
# this session has been corrected to be.

STANDING_LESSON_COUNT = 5
RETRIEVED_LESSON_COUNT = 3
LESSON_BUDGET_FRACTION = 0.15
CHARS_PER_TOKEN_ESTIMATE = 4


def estimate_tokens(text: str) -> int:
    """A character-count proxy, not a real tokenizer - see the module note
    above. Good enough to enforce a soft budget, not precise enough to
    trust for anything this project already corrected to real token
    counts (decisions 30, 33)."""
    return len(text) // CHARS_PER_TOKEN_ESTIMATE


MAX_STANDING_CLASS_SKEW = 0.7


def standing_lessons(conn: psycopg.Connection, solution_id: str, k: int = STANDING_LESSON_COUNT) -> list[Lesson]:
    """The highest-support active lessons that are safe to inject universally.

    Support alone was the wrong rule, and it failed the same way twice. The
    tier goes into every candidate's prompt regardless of what that candidate
    is being asked to judge, so a lesson whose advice depends on the task's
    class is inverted for half of them. Support follows the most common failure
    category, and failure categories are overwhelmingly class-specific - 8 of
    capability_case's 12 are more than 90% one class, which is structural rather
    than incidental, since the mechanical floor fixes a task's class and a
    candidate that over-rejects can only fail on floor-passing items. So
    "highest support" reliably selected the most class-conditional lesson
    available: "When floor passes (no disqualifier), prefer accept over reject"
    was promoted into must-reject prompts twice, derived independently each
    time.

    class_skew is the fraction of a category's evidence in its dominant class,
    so 1.0 is one-class-only and 0.5 is balanced. Above MAX_STANDING_CLASS_SKEW
    a lesson is class-conditional and belongs in the retrieved tier only, where
    it is matched against the parent's own failure evidence and therefore
    reaches candidates whose failures are in that class. A lesson with no
    recorded skew is treated as unsafe for the tier rather than assumed safe:
    this rule exists because the optimistic default was wrong.
    """
    lessons = active_lessons(conn, solution_id)
    safe = [
        lesson
        for lesson in lessons
        if lesson.class_skew is not None and lesson.class_skew <= MAX_STANDING_CLASS_SKEW
    ]
    return sorted(safe, key=lambda lesson: lesson.support, reverse=True)[:k]


def retrieve_lessons(
    text: str, vectorizer, lessons: list[Lesson], k: int = RETRIEVED_LESSON_COUNT
) -> list[Lesson]:
    """Nearest lessons to the given text (the parent's recent failure
    evidence) by cosine similarity in the shared TF-IDF space - the same
    vectorizer harness/taxonomy.py fit the failure categories with.
    No model call; this is what "classify cheaply" (task 4.1) buys."""
    if not lessons or not text:
        return []
    from sklearn.metrics.pairwise import cosine_similarity

    vec = vectorizer.transform([text])
    vectors = np.array([lesson.vector for lesson in lessons])
    sims = cosine_similarity(vec, vectors)[0]
    ranked = sorted(zip(lessons, sims), key=lambda pair: pair[1], reverse=True)
    return [lesson for lesson, sim in ranked[:k] if sim > 0]


def format_lessons(lessons: list[Lesson], heading: str) -> str:
    if not lessons:
        return ""
    bullets = "\n".join(f"- {lesson.text}" for lesson in lessons)
    return f"## {heading}\n{bullets}\n"


def apply_budget(
    non_lesson_text: str,
    standing: list[Lesson],
    retrieved: list[Lesson],
    max_fraction: float = LESSON_BUDGET_FRACTION,
) -> tuple[list[Lesson], list[Lesson]]:
    """Caps combined lesson content at roughly max_fraction of the full
    prompt, dropping the lowest-priority items first (lowest support for
    standing lessons, lowest similarity for retrieved - both lists are
    expected pre-sorted best-first). Standing lessons are trimmed only
    after every retrieved lesson is already gone, since PHASE-4.md's own
    diagram treats standing lessons as the more durable, generation-level
    tier and retrieved lessons as the more disposable, per-candidate one."""
    non_lesson_tokens = estimate_tokens(non_lesson_text)
    budget = max_fraction * non_lesson_tokens / (1 - max_fraction)

    def total_tokens(s: list[Lesson], r: list[Lesson]) -> int:
        return estimate_tokens(format_lessons(s, "x") + format_lessons(r, "x"))

    standing, retrieved = list(standing), list(retrieved)
    while total_tokens(standing, retrieved) > budget and retrieved:
        retrieved.pop()
    while total_tokens(standing, retrieved) > budget and standing:
        standing.pop()
    return standing, retrieved
