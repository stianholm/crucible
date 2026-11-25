"""Metrics of learning. See PHASE-4.md task 4.6.

The score going up is not proof that reflection worked, because the score was
going up in Phase 3 too. These measure learning directly.

Four things, as the phase document asks: repeat-failure rate, lesson
precision per lesson, the count of still-active failure categories, and the
prompt tokens spent on lessons per generation.

**One correction to the specified SQL.** PHASE-4.md's own query reads

    from iteration where valid = false and failure_id is not null

and `valid = false` is wrong for this metric. An invalid candidate is one
that failed a *gate* - it produced nothing usable at all. The task 4.1
taxonomy is built by harness/taxonomy.py's extract_evidence(), which is
mostly failed *checks* on candidates that ran perfectly well, and those are
the failures the lessons are actually about. On real 2026-09-29 data, 30 of
32 candidates carried failure evidence while 27 were valid, so the specified
filter would compute a repeat rate from the handful of gate failures per
generation and ignore the large majority of what the taxonomy describes. The
filter here is "has failure evidence", which is `failure_id is not null`
alone.

**A limit worth stating rather than discovering later.** `iteration.failure_id`
was added 2026-09-28, so no run before that has it, and nothing here can
recover a retrospective trend. Every series below starts at the first
generation run under the recording path.
"""

from __future__ import annotations

from dataclasses import dataclass

import psycopg

from harness.lessons import estimate_tokens

REPEAT_WINDOW = 5  # "already appeared in the previous five", per PHASE-4.md


def latest_run_id(conn: psycopg.Connection, solution_id: str) -> str | None:
    """Generation numbering restarts at 0 for every run, so a series computed
    across runs silently merges each run's generation 0 into one bucket.
    Observed doing exactly that on 2026-09-29: four separate single-generation
    runs became a single "generation 0" with 96 failures. Every metric here
    therefore scopes to one run, and defaults to the most recent."""
    with conn.cursor() as cur:
        cur.execute(
            "select run_id from iteration where solution_id = %s order by created_at desc limit 1",
            (solution_id,),
        )
        row = cur.fetchone()
    return row[0] if row else None


@dataclass
class LessonPrecision:
    lesson_id: int
    failure_id: str
    followed: int
    followed_ok: int
    precision: float | None  # followed_ok / followed, None when never followed
    base_rate: float | None  # the control-group rate this has to beat
    control_group: int  # candidates that did not receive it, and so could form one
    retired_gen: int | None


def repeat_rate_from_rows(
    rows: list[tuple[int, str]], window: int = REPEAT_WINDOW
) -> list[tuple[int, int, float | None]]:
    """(generation, n_failures, repeat_rate) from (generation, failure_id) rows.

    A failure is a repeat when its category also appeared in any of the
    `window` generations before it. Pure so it can be tested without a
    database; repeat_failure_rate() below supplies the rows.

    The rate is None, not 0.0, for a generation with no earlier generation to
    repeat from. Nothing in the first generation of a run *can* be a repeat,
    so a 0.000 there is the absence of a measurement rather than a good
    result, and including it made the first real ten-generation series read as
    "rising 53%" when generations 1 to 9 were in fact flat. trend() skips
    them."""
    by_generation: dict[int, list[str]] = {}
    for generation, failure_id in rows:
        by_generation.setdefault(generation, []).append(failure_id)

    seen_in: dict[str, set[int]] = {}
    for generation, ids in by_generation.items():
        for failure_id in ids:
            seen_in.setdefault(failure_id, set()).add(generation)

    generations = sorted(by_generation)
    out: list[tuple[int, int, float | None]] = []
    for generation in generations:
        ids = by_generation[generation]
        # Undefined only for the earliest generation in the series, which has
        # nothing at all behind it. A later generation whose window happens to
        # contain no recorded failures does have a rate: every failure in it is
        # new *relative to the window*, which is what the metric asks.
        if not ids or generation == generations[0]:
            out.append((generation, len(ids), None))
            continue
        repeats = sum(
            1
            for failure_id in ids
            if any(g in seen_in[failure_id] for g in range(generation - window, generation))
        )
        out.append((generation, len(ids), repeats / len(ids)))
    return out


def repeat_failure_rate(
    conn: psycopg.Connection,
    solution_id: str,
    run_id: str | None = None,
    window: int = REPEAT_WINDOW,
) -> list[tuple[int, int, float]]:
    """The headline metric. Should fall. If it is flat, reflection is not
    working no matter what the score does.

    Scoped to one run: see latest_run_id() for why aggregating across runs is
    meaningless."""
    run_id = run_id or latest_run_id(conn, solution_id)
    sql = """
        select generation, failure_id
          from iteration
         where solution_id = %s
           and failure_id is not null
           and generation is not null
    """
    params: list = [solution_id]
    if run_id is not None:
        sql += " and run_id = %s"
        params.append(run_id)
    with conn.cursor() as cur:
        cur.execute(sql, params)
        rows = cur.fetchall()
    return repeat_rate_from_rows(rows, window)


def lesson_precision(conn: psycopg.Connection, solution_id: str) -> list[LessonPrecision]:
    """Per lesson, how often the failure it was written about stayed away,
    next to the rate for candidates that never received it.

    A standing-tier lesson has no control group by construction, so its
    base_rate comes back None with control_group 0. That is the honest
    answer, not a gap: the standing tier goes into every prompt, and the
    comparison needs task 4.5's arm A."""
    from harness.lessons import base_avoidance_rate

    with conn.cursor() as cur:
        cur.execute(
            """
            select id, failure_id, followed, followed_ok, retired_gen
              from lesson where solution_id = %s order by id
            """,
            (solution_id,),
        )
        rows = cur.fetchall()

    out = []
    for lesson_id, failure_id, followed, followed_ok, retired_gen in rows:
        rate, control = base_avoidance_rate(conn, solution_id, lesson_id)
        out.append(
            LessonPrecision(
                lesson_id=lesson_id,
                failure_id=failure_id,
                followed=followed,
                followed_ok=followed_ok,
                precision=(followed_ok / followed) if followed else None,
                base_rate=rate,
                control_group=control,
                retired_gen=retired_gen,
            )
        )
    return out


def active_categories_per_generation(
    conn: psycopg.Connection, solution_id: str, run_id: str | None = None
) -> list[tuple[int, int]]:
    """Distinct failure categories seen per generation. Falling alongside a
    falling repeat rate is the shape that means categories are being closed
    out rather than merely recurring less often by chance."""
    run_id = run_id or latest_run_id(conn, solution_id)
    sql = """
        select generation, count(distinct failure_id)
          from iteration
         where solution_id = %s and failure_id is not null and generation is not null
    """
    params: list = [solution_id]
    if run_id is not None:
        sql += " and run_id = %s"
        params.append(run_id)
    sql += " group by generation order by generation"
    with conn.cursor() as cur:
        cur.execute(sql, params)
        return [(g, n) for g, n in cur.fetchall()]


def lesson_tokens_per_generation(
    conn: psycopg.Connection, solution_id: str, run_id: str | None = None
) -> list[tuple[int, int, int]]:
    """(generation, injections, estimated prompt tokens spent on lessons).

    An estimate, not a measurement: harness.lessons.estimate_tokens() is a
    four-characters-per-token proxy, because the harness runs on the host and
    has no tokenizer for gpt-oss-120b. The injection count is exact; only the
    token figure is approximate. Task 4.7 reads this against wall clock and
    quality to decide whether the lessons pay for themselves."""
    run_id = run_id or latest_run_id(conn, solution_id)
    with conn.cursor() as cur:
        cur.execute("select id, text from lesson where solution_id = %s", (solution_id,))
        cost = {lesson_id: estimate_tokens(text) for lesson_id, text in cur.fetchall()}

        sql = """
            select generation, lessons_injected
              from iteration
             where solution_id = %s and lessons_injected is not null and generation is not null
        """
        params: list = [solution_id]
        if run_id is not None:
            sql += " and run_id = %s"
            params.append(run_id)
        cur.execute(sql, params)
        rows = cur.fetchall()

    per_generation: dict[int, list[int]] = {}
    for generation, injected in rows:
        per_generation.setdefault(generation, []).extend(injected or [])
    return [
        (generation, len(ids), sum(cost.get(i, 0) for i in ids))
        for generation, ids in sorted(per_generation.items())
    ]



# --- Instruments that are not saturated ------------------------------------
#
# The repeat-failure rate above is a ratio whose window covers the whole
# taxonomy once six or seven of eleven categories appear per generation, which
# is what capability_case does. Measured 2026-09-29 it sat flat at 0.95 for ten
# generations and could not have done otherwise. The two below are counts
# rather than ratios against that window, so they can move.


def volume_from_details(rows: list[tuple[int, dict]]) -> list[tuple[int, int, int, float]]:
    """(generation, candidates, candidates with any failure, mean failed
    checks per candidate) from (generation, detail) rows.

    Failed checks rather than candidates-that-failed: a candidate going from
    four failed checks to one is learning, and the coarser count cannot see
    it. Pure, so the arithmetic is testable without a database."""
    from harness.taxonomy import extract_evidence

    by_generation: dict[int, list[int]] = {}
    for generation, detail in rows:
        n_failures = len(extract_evidence([detail or {}], [None]))
        by_generation.setdefault(generation, []).append(n_failures)
    return [
        (
            generation,
            len(counts),
            sum(1 for c in counts if c > 0),
            sum(counts) / len(counts) if counts else 0.0,
        )
        for generation, counts in sorted(by_generation.items())
    ]


def failure_volume_per_generation(
    conn: psycopg.Connection, solution_id: str, run_id: str | None = None
) -> list[tuple[int, int, int, float]]:
    """How much candidates fail, not how novel their failures are."""
    run_id = run_id or latest_run_id(conn, solution_id)
    sql = """
        select generation, detail from iteration
         where solution_id = %s and status = 'scored' and generation is not null
    """
    params: list = [solution_id]
    if run_id is not None:
        sql += " and run_id = %s"
        params.append(run_id)
    with conn.cursor() as cur:
        cur.execute(sql, params)
        rows = cur.fetchall()
    return volume_from_details(rows)


def category_intensity(
    conn: psycopg.Connection, solution_id: str, run_id: str | None = None
) -> dict[str, dict[int, int]]:
    """{category: {generation: candidates failing in it}}.

    A category can stay present while hurting fewer candidates, which is what
    learning looks like when the taxonomy is small. The repeat-failure rate
    cannot see that at all: the category is still "seen before" either way.

    Reads failure_ids, the full set, falling back to failure_id for rows
    recorded before that column existed."""
    run_id = run_id or latest_run_id(conn, solution_id)
    sql = """
        select generation, coalesce(failure_ids, array[failure_id]) from iteration
         where solution_id = %s and generation is not null
           and (failure_ids is not null or failure_id is not null)
    """
    params: list = [solution_id]
    if run_id is not None:
        sql += " and run_id = %s"
        params.append(run_id)
    with conn.cursor() as cur:
        cur.execute(sql, params)
        rows = cur.fetchall()

    out: dict[str, dict[int, int]] = {}
    for generation, ids in rows:
        for category in ids or []:
            if category is None:
                continue
            out.setdefault(category, {}).setdefault(generation, 0)
            out[category][generation] += 1
    return out

def _bar(value: float, width: int = 20) -> str:
    return "#" * round(value * width)


def trend(series: list[float | None], window: int = 3) -> str:
    """Whether the metric is going the way it should, stated conservatively.
    Compares the mean of the first `window` points against the last.

    Drops None entries first: a generation with no earlier generation to
    repeat from has no rate, and treating it as 0.0 turns "no data yet" into
    an apparent improvement."""
    series = [x for x in series if x is not None]
    if len(series) < window * 2:
        return "too few generations to call"
    first = sum(series[:window]) / window
    last = sum(series[-window:]) / window
    if first == 0:
        return "flat at zero"
    change = (last - first) / first
    if change < -0.10:
        return f"falling ({first:.2f} -> {last:.2f}, {change:+.0%})"
    if change > 0.10:
        return f"RISING ({first:.2f} -> {last:.2f}, {change:+.0%})"
    return f"flat ({first:.2f} -> {last:.2f}, {change:+.0%})"


def render_markdown(conn: psycopg.Connection, solution_id: str, run_id: str | None = None) -> str:
    """The whole set, as markdown. PHASE-4.md task 4.6's Verify asks for the
    repeat-failure rate graphed per generation; this project's convention is
    markdown over HTML, so the graph is a table with a bar column. Grafana is
    already deployed if a live panel is wanted later."""
    run_id = run_id or latest_run_id(conn, solution_id)
    repeat = repeat_failure_rate(conn, solution_id, run_id)
    categories = dict(active_categories_per_generation(conn, solution_id, run_id))
    tokens = {g: (n, t) for g, n, t in lesson_tokens_per_generation(conn, solution_id, run_id)}

    lines = [f"# Metrics of learning — {solution_id}", ""]
    if run_id:
        lines += [f"Run `{run_id}`.", ""]
    lines += [
        "`failure_id` only exists from 2026-09-28, so this series cannot reach",
        "further back than the first generation run under that recording path.",
        "",
        "## Repeat-failure rate",
        "",
        "Fraction of a generation's failures whose category also appeared in the",
        f"previous {REPEAT_WINDOW} generations. Counted over every candidate carrying failure",
        "evidence, not only gate failures — see this module's docstring for why",
        "that differs from the SQL in PHASE-4.md.",
        "",
        "| Gen | Failures | Categories | Repeat rate | |",
        "|---|---|---|---|---|",
    ]
    for generation, n_failures, rate in repeat:
        shown = f"{rate:.3f}" if rate is not None else "n/a (no prior generation)"
        lines.append(
            f"| {generation} | {n_failures} | {categories.get(generation, 0)} | "
            f"{shown} | `{_bar(rate) if rate is not None else ''}` |"
        )
    lines += ["", f"**Trend:** {trend([r for _, _, r in repeat])}", ""]

    volume = failure_volume_per_generation(conn, solution_id, run_id)
    lines += [
        "## Failure volume",
        "",
        "Failed checks per candidate, which unlike the ratio above is not bounded",
        "by how much of the taxonomy the window covers. This is the series to read",
        "for whether candidates are failing less.",
        "",
        "| Gen | Candidates | With any failure | Mean failed checks |",
        "|---|---|---|---|",
    ]
    for generation, candidates, with_failures, mean_failed in volume:
        lines.append(f"| {generation} | {candidates} | {with_failures} | {mean_failed:.2f} |")
    lines += ["", f"**Trend:** {trend([m for _g, _c, _w, m in volume])}", ""]

    intensity = category_intensity(conn, solution_id, run_id)
    if intensity:
        generations = sorted({g for per_gen in intensity.values() for g in per_gen})
        lines += [
            "## Per-category intensity",
            "",
            "Candidates failing in each category per generation. A category can stay",
            "present while hurting fewer candidates, which the repeat-failure rate",
            "cannot see.",
            "",
            "| Category | " + " | ".join(str(g) for g in generations) + " | Trend |",
            "|---" * (len(generations) + 2) + "|",
        ]
        for category in sorted(intensity):
            per_gen = intensity[category]
            counts = [per_gen.get(g, 0) for g in generations]
            lines.append(
                f"| {category} | " + " | ".join(str(c) for c in counts)
                + f" | {trend([float(c) for c in counts])} |"
            )
        lines.append("")

    lines += ["## Lesson precision", "", "| Lesson | Category | Followed | Avoided | Precision | Base rate | Control | Retired |", "|---|---|---|---|---|---|---|---|"]
    for p in lesson_precision(conn, solution_id):
        precision = f"{p.precision:.3f}" if p.precision is not None else "—"
        base = f"{p.base_rate:.3f}" if p.base_rate is not None else "none (standing tier)"
        lines.append(
            f"| {p.lesson_id} | {p.failure_id} | {p.followed} | {p.followed_ok} | {precision} | "
            f"{base} | {p.control_group} | {p.retired_gen if p.retired_gen is not None else '—'} |"
        )

    lines += ["", "## Lesson token cost per generation", "",
              "Estimated at four characters per token; the injection count is exact.", "",
              "| Gen | Injections | Est. lesson tokens |", "|---|---|---|"]
    for generation in sorted(tokens):
        n, t = tokens[generation]
        lines.append(f"| {generation} | {n} | {t:,} |")

    return "\n".join(lines) + "\n"
