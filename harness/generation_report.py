"""Generation report. See PHASE-3.md task 3.8.

Written automatically at the end of each generation. The "Content" row —
the newly claimed elites with diffs against their parents — is not
optional: sixty-four candidates per generation is sixty-four attempts to
find something the fitness function rewards but wasn't intended. Nobody
reads all of them any more; the report surfaces the ones that won.
"""

from __future__ import annotations

import difflib
import statistics
from pathlib import Path

import psycopg

from harness.archive import coverage, qd_score, unique_ancestors
from harness.generation import GenerationResult
from harness.islands import N_ISLANDS
from harness.storage import get_candidate


def _throughput_line(completion_tokens: int, wall_s: float | None) -> str:
    """Decode-only tokens/second - completion_tokens, not the
    prompt+completion total_tokens that made task 3.1's original 437.8
    tok/s figure untrustworthy (TODO.md decision, and decision 30's
    identical pattern in the token-accounting bug). Added 2026-09-25 to
    finally give PHASE-3.md's "aggregate throughput above 250 tokens per
    second" a number worth trusting."""
    if not wall_s:
        return "n/a"
    return f"{completion_tokens / wall_s:.1f} tok/s ({completion_tokens} completion tokens / {wall_s:.1f}s)"


def _diff(parent_sha: str, candidate_sha: str) -> str:
    parent_text = get_candidate(parent_sha) or ""
    cand_text = get_candidate(candidate_sha) or ""
    lines = difflib.unified_diff(
        parent_text.splitlines(keepends=True),
        cand_text.splitlines(keepends=True),
        fromfile=f"parent {parent_sha}",
        tofile=f"candidate {candidate_sha}",
    )
    return "".join(lines) or "(no textual diff — identical after normalisation)"


def generate_generation_report(
    conn: psycopg.Connection,
    solution_id: str,
    result: GenerationResult,
    budget_summary: dict,
    prefix_cache_hit_rate: float | None,
    queue_depth_samples: list[int],
    grid_size: int,
    n_islands: int,
    out_path: Path,
) -> str:
    lines = [
        f"# Generation {result.generation} — {solution_id}",
        "",
        "## Throughput",
        "",
        f"- Peak queue depth: {max(queue_depth_samples) if queue_depth_samples else 'n/a'}",
        f"- Sustained (median) queue depth: {statistics.median(queue_depth_samples) if queue_depth_samples else 'n/a'}",
        f"- Prefix cache hit rate: {f'{prefix_cache_hit_rate:.1%}' if prefix_cache_hit_rate is not None else 'n/a'}",
        f"- Aggregate throughput: {_throughput_line(result.completion_tokens, budget_summary.get('generation_wall_s'))}",
        "",
        "## Archive",
        "",
    ]

    for island_id in range(n_islands):
        cov = coverage(conn, solution_id, island_id, grid_size)
        qd = qd_score(conn, solution_id, island_id)
        ua = unique_ancestors(conn, solution_id, island_id)
        lines.append(f"- Island {island_id}: coverage {cov:.1%}, QD score {qd:.3f}, unique ancestors {ua}")

    lines += [
        f"- Cells newly claimed this generation: {result.n_claimed}",
        "",
        "## Quality",
        "",
    ]
    if result.newly_claimed:
        scalars = [c["scalar"] for c in result.newly_claimed]
        lines.append(f"- Best scalar this generation: {max(scalars):.4f}")
        lines.append(f"- Median scalar of newly-claimed: {statistics.median(scalars):.4f}")
    else:
        lines.append("- No cells claimed this generation.")

    lines += [
        "",
        "## Cost",
        "",
        f"- Budget: {budget_summary}",
        f"- Candidates proposed: {result.n_candidates}",
        f"- Parsed: {result.n_parsed} ({100 * result.n_parsed / max(1, result.n_candidates):.1f}%)",
        f"- Admissible: {result.n_admissible} ({100 * result.n_admissible / max(1, result.n_candidates):.1f}%)",
        f"- Scored: {result.n_scored}",
        "",
        "## Content — newly claimed elites",
        "",
    ]

    if not result.newly_claimed:
        lines.append("_Nothing claimed this generation._")
    else:
        for c in result.newly_claimed:
            lines.append(
                f"### Island {c['island_id']}, cell {c['cell']}, scalar {c['scalar']:.4f}"
            )
            lines.append("")
            lines.append(f"parent `{c['parent_sha']}` -> candidate `{c['candidate_sha']}`")
            lines.append("")
            lines.append("```diff")
            lines.append(_diff(c["parent_sha"], c["candidate_sha"]))
            lines.append("```")
            lines.append("")

    if result.migration_log:
        lines.append("## Migration")
        lines.append("")
        for m in result.migration_log:
            lines.append(
                f"- island {m['from_island']} -> island {m['to_island']}: "
                f"cell {m['cell']}, scalar {m['scalar']:.4f}, claimed={m['claimed']}"
            )

    text = "\n".join(lines) + "\n"
    out_path.write_text(text)
    return text
