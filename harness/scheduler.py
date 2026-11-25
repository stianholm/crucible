"""The daily generation window. See PHASE-6.md, "The daily cycle", "Plateau
handling" and "Solution scheduling".

    crucible scheduler day [--until 23:00]   run segments until the deadline
    crucible scheduler status                what would run, and why
    crucible scheduler reenter SOLUTION      lift a dormant solution by hand

The day is a sequence of segments. A segment is one run_population call of
up to SEGMENT_GENS generations on one solution, ending with its held-out
check, which is what the ladder reads. Before each segment the scheduler:

1. stops if halted (ops/kill.py) or the daily token cap is spent;
2. picks a solution: the one already running keeps the GPU until it goes
   dormant; otherwise operator priority (schedule.yaml), then whichever has
   waited longest;
3. takes the ladder step that is due, if any;
4. runs paired stock-against-distilled if an adapter is loaded and ungated,
   and gates it after GATE_GENERATIONS paired generations;
5. starts the segment only if it can finish before the deadline.

Departure from PHASE-6.md's clock: the gate evaluation is the day's paired
generations, not a 04:00 to 06:00 slot. Two hours hold about two generations
here, and decision 77 needed ten to resolve 0.029.
"""

from __future__ import annotations

import argparse
import datetime
import statistics
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import yaml

from harness import events, gate, ladder
from harness.halt import halted
from harness.held_out import eval_set_version

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEDULE = REPO_ROOT / "schedule.yaml"
REPORT_ROOT = REPO_ROOT / "reports" / "generations"
SEGMENT_GENS = 4
TEMPERATURE = 0.9
WIDE_TEMPERATURE = 1.1          # ladder step 1
CANDIDATES_PER_ISLAND = 8       # ops/search.sh's sizing
PAIRED_CANDIDATES_PER_ISLAND = 4  # two arms per parent: same proposal count (round 1)
HELD_OUT_FALLBACK_S = 3000      # the closing held-out check, two passes: 40 min measured 2026-10-24
FALLBACK_GENERATION_S = 3900    # capability_case_author s4: about 65 minutes


@dataclass
class Contender:
    solution_id: str
    state: ladder.LadderState
    last_segment: datetime.datetime | None


def roster() -> list[str]:
    """Every onboarded solution but the fixture, which is the harness's own
    regression test and never scheduled (PHASE-6.md)."""
    return sorted(d.name for d in (REPO_ROOT / "solutions").iterdir()
                  if (d / "solution.yaml").exists() and d.name != "fixture")


def contenders(conn) -> list[Contender]:
    out = []
    for sol in roster():
        evts = [e for e in events.since(conn, 24 * 3650, ("held_out", "ladder")) if e["solution_id"] == sol]
        seg = events.latest(conn, "segment", sol)
        out.append(Contender(sol, ladder.replay(evts, eval_set_version(REPO_ROOT / "solutions" / sol),
                                                sigma_floor(sol)),
                             seg[0]["at"] if seg else None))
    return out


def sigma_floor(sol: str) -> float:
    """The smallest held-out gain that counts, per solution: `ladder:
    sigma_floor:` in its BASELINE.yaml, from measured noise, else the
    default. Changing it changes when a plateau is declared, so it is a
    threshold change: record it in docs/decisions.md (decision 98)."""
    f = REPO_ROOT / "solutions" / sol / "BASELINE.yaml"
    doc = (yaml.safe_load(f.read_text()) or {}) if f.exists() else {}
    return float((doc.get("ladder") or {}).get("sigma_floor") or ladder.SIGMA_FLOOR)


def pick(cands: list[Contender], priority: list[str], running: str | None) -> Contender | None:
    """Pure. The running solution keeps every generation until dormant; then
    operator priority; then the longest wait, never-run first."""
    live = [c for c in cands if not c.state.dormant]
    if not live:
        return None
    for c in live:
        if c.solution_id == running:
            return c
    ranked = sorted(live, key=lambda c: (
        priority.index(c.solution_id) if c.solution_id in priority else len(priority),
        c.last_segment.timestamp() if c.last_segment else float("-inf"),
    ))
    return ranked[0]


def generations_that_fit(seconds_left: float, generation_s: float, held_out_s: float = HELD_OUT_FALLBACK_S) -> int:
    return max(0, min(SEGMENT_GENS, int((seconds_left - held_out_s) // generation_s)))


def _held_out_s(conn, sol: str) -> float:
    """How long the closing held-out check takes for this solution: from the
    run's last row to its held_out event, the longest of the last five, plus
    a fifth. The tail is one long request decoding alone, so it varies."""
    rows = conn.execute(
        """select extract(epoch from e.at - max(i.created_at)) from event e
           join iteration i on i.run_id = (e.detail->>'run_id')::uuid
           where e.kind = 'held_out' and e.solution_id = %s and e.detail ? 'run_id'
             and not coalesce((e.detail->>'backfilled')::boolean, false)
           group by e.id order by e.id desc limit 5""", (sol,)).fetchall()
    walls = [float(r[0]) for r in rows if r[0] and r[0] > 0]
    return 1.2 * max(walls) if walls else HELD_OUT_FALLBACK_S


def _generation_s(conn, sol: str) -> float:
    rows = conn.execute(
        """select run_id, generation, max(created_at) from iteration
           where solution_id = %s and created_at > now() - interval '30 days' and generation is not null
           group by 1, 2 order by 1, 2""", (sol,)).fetchall()
    walls = [(t2 - t1).total_seconds() for (r1, g1, t1), (r2, g2, t2) in zip(rows, rows[1:])
             if r1 == r2 and g2 == g1 + 1]
    if not walls:
        # A one-generation run has no consecutive pair, so time its generation
        # 0 from the segment event that started it. Without this, a solution
        # whose segments were all one generation never left the 65-minute
        # fallback: on 2026-10-25 a 5-minute solution stopped with an hour
        # of its window left.
        walls = [float(r[0]) for r in conn.execute(
            """select extract(epoch from (select max(i.created_at) from iteration i
                                          where i.run_id = (h.detail->>'run_id')::uuid and i.generation = 0)
                                - (select max(s.at) from event s where s.kind = 'segment'
                                   and s.solution_id = h.solution_id and s.at < h.at))
               from event h where h.kind = 'held_out' and h.solution_id = %s and h.detail ? 'run_id'
                 and h.at > now() - interval '30 days'""", (sol,)).fetchall() if r[0] and r[0] > 0]
    return statistics.median(walls) if walls else FALLBACK_GENERATION_S


def _schedule() -> dict:
    return (yaml.safe_load(SCHEDULE.read_text()) or {}) if SCHEDULE.exists() else {}


def _tokens_24h(conn) -> int:
    return conn.execute(
        "select coalesce(sum(coalesce(prompt_tokens, 0) + coalesce(cost_tokens, 0)), 0) from iteration "
        "where created_at > now() - interval '24 hours'").fetchone()[0]


def original_seed(sol: str) -> str:
    """The EVOLVE block as first committed: the 'early archive snapshot' of
    ladder step 2. Decision 85 found a restart from the original seed escaped
    a local optimum the incumbent's descendants could not leave."""
    cand = next((REPO_ROOT / "solutions" / sol / "candidate").iterdir())
    rel = str(cand.relative_to(REPO_ROOT))
    first = subprocess.run(["git", "-C", str(REPO_ROOT), "log", "--diff-filter=A", "--format=%H", "--", rel],
                           capture_output=True, text=True, check=True).stdout.split()[-1]
    text = subprocess.run(["git", "-C", str(REPO_ROOT), "show", f"{first}:{rel}"],
                          capture_output=True, text=True, check=True).stdout
    return text.split("EVOLVE-BLOCK-START")[1].split("EVOLVE-BLOCK-END")[0].strip("\n")


def take_step(conn, sol: str, state: ladder.LadderState, step: int) -> str | None:
    """Record ladder step `step` and do what it needs before the next segment.
    Returns a seed block for step 2, else None."""
    detail = {"step": step, "action": ladder.STEPS[step], "eval_version": state.eval_version,
              "best": state.best, "generations_without_gain": state.since}
    seed = None
    if step == 2:
        weakest = conn.execute(
            "select island_id from elite where solution_id = %s group by 1 order by max(scalar) limit 1", (sol,)
        ).fetchone()
        if weakest:
            parked = f"{sol}_reseed_{datetime.date.today():%Y%m%d}_i{weakest[0]}"
            conn.execute("update elite set solution_id = %s where solution_id = %s and island_id = %s",
                         (parked, sol, weakest[0]))
            conn.commit()
            detail.update(island=weakest[0], parked_as=parked)
        seed = original_seed(sol)
    needs_ack = step >= 3
    if step == 3:
        detail["wants"] = (f"add {sol}'s archive to train/harvest.yaml, run `python -m train.harvest review`, "
                           "and sign it; the nightly window trains on it")
    events.record(conn, "ladder", sol, needs_ack=needs_ack, **detail)
    print(f"ladder {sol}: step {step}, {ladder.STEPS[step]}", flush=True)
    return seed


def gate_if_due(conn, adapter_root: str) -> str | None:
    """Decide on the loaded adapter once it has GATE_GENERATIONS paired
    generations. Returns the decision, or None if still measuring."""
    if gate.paired_generations(conn, gate.label(adapter_root)) < gate.GATE_GENERATIONS:
        return None
    c = gate.evaluate(conn, adapter_root, REPO_ROOT)
    failed = [k for k, v in c.items() if not v["pass"]]
    decision = "rejected" if failed else "held_out_pending"
    events.record(conn, "gate", None, needs_ack=not failed, adapter=adapter_root.rsplit("/", 1)[-1],
                  decision=decision, failed=failed, conditions=c)
    if failed:
        gate.unload()
    print(f"gate {adapter_root}: {decision} {failed or ''}", flush=True)
    return decision


def _proposer_up() -> bool:
    import urllib.request

    try:
        with urllib.request.urlopen("http://localhost:8000/v1/models", timeout=10):
            return True
    except OSError:
        return False


def _ungated(conn) -> str | None:
    root = gate.loaded_adapter()
    if not root:
        return None
    name = root.rsplit("/", 1)[-1]
    done = conn.execute("select 1 from event where kind = 'gate' and detail->>'adapter' = %s", (name,)).fetchone()
    return None if done else root


def day(until: str = "23:00") -> None:
    from harness.persistence import connect
    from harness.run_population import run_population

    hh, mm = map(int, until.split(":"))
    deadline = datetime.datetime.now().replace(hour=hh, minute=mm, second=0, microsecond=0)
    conn = connect()
    running: str | None = None
    while True:
        if reason := halted():
            print(f"halted: {reason}", flush=True)
            break
        # Wait out a proposer outage rather than run segments into it: every
        # proposal would fail in seconds, and the segments would race. The
        # immediate alert fires at 15 minutes (harness/alerts.py).
        if not _proposer_up():
            if datetime.datetime.now() >= deadline:
                break
            print(f"{datetime.datetime.now():%H:%M} proposer down: waiting", flush=True)
            time.sleep(60)
            continue
        cap = _schedule().get("daily_token_cap")
        spent = _tokens_24h(conn)
        if cap and spent >= cap:
            now = datetime.datetime.now()
            events.record(conn, "alert", None, needs_ack=True, signal="budget",
                          message=f"daily token cap {cap:,} spent ({spent:,}) at {now:%H:%M}",
                          immediate=now.hour < 18)
            break
        choice = pick(contenders(conn), _schedule().get("priority") or [], running)
        if choice is None:
            # One record per day window: windows open 24 h apart, and the
            # morning report counts an idle day only with this record (decision 100).
            if not events.since(conn, 12, ("idle",)):
                events.record(conn, "idle", None, reason="every solution is dormant")
            print("idle: every solution is dormant", flush=True)
            break
        sol, state, seed = choice.solution_id, choice.state, None
        if (step := state.due) is not None:
            seed = take_step(conn, sol, state, step)
            if step == ladder.DORMANT:
                running = None
                continue
            state.step = step
        adapter = _ungated(conn)
        if adapter and gate_if_due(conn, adapter):
            adapter = None
        held_out_s = _held_out_s(conn, sol)
        gens = generations_that_fit((deadline - datetime.datetime.now()).total_seconds(), _generation_s(conn, sol),
                                    held_out_s)
        if gens == 0:
            print("no time left for a generation before the deadline", flush=True)
            break
        temperature = WIDE_TEMPERATURE if state.step >= 1 else TEMPERATURE
        models = ("proposer", "proposer-distilled") if adapter else ("proposer",)
        tag = f"{datetime.datetime.now():%Y%m%d-%H%M}"
        events.record(conn, "segment", sol, generations=gens, temperature=temperature, step=state.step,
                      proposer_models=list(models), tag=tag)
        print(f"segment {sol}: {gens} generations, temperature {temperature}, models {models}", flush=True)
        run_population(sol, None, max_generations=gens, max_tokens=max(1, (cap or 10**12) - spent),
                       max_wall_s=(deadline - datetime.datetime.now()).total_seconds() - held_out_s,
                       patience=gens, temperature=temperature, seed_block=seed, proposer_models=models,
                       candidates_per_island=PAIRED_CANDIDATES_PER_ISLAND if adapter else CANDIDATES_PER_ISLAND,
                       report_dir=REPORT_ROOT / sol, report_tag=tag)
        running = sol
    conn.close()


def status() -> None:
    from harness.persistence import connect

    with connect() as conn:
        cands = contenders(conn)
        for c in cands:
            s = c.state
            mode = "dormant" if s.dormant else (f"step {s.step}" if s.step else "climbing")
            best = f"{s.best:.3f}" if s.best is not None else "none"
            print(f"{c.solution_id:28} {mode:10} best held-out {best:6} {s.since:3} generations without gain"
                  f"  eval set {s.eval_version}")
        choice = pick(cands, _schedule().get("priority") or [], None)
        print(f"next: {choice.solution_id if choice else 'nothing (every solution dormant)'}")
        print(f"halted: {halted() or 'no'}; adapter awaiting the gate: {_ungated(conn) or 'none'}")


def main() -> int:
    ap = argparse.ArgumentParser(description="PHASE-6.md's daily generation window")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("day")
    p.add_argument("--until", default="23:00")
    sub.add_parser("status")
    p = sub.add_parser("reenter")
    p.add_argument("solution")
    a = ap.parse_args()
    if a.cmd == "day":
        day(a.until)
    elif a.cmd == "status":
        status()
    else:
        from harness.persistence import connect

        with connect() as conn:
            v = eval_set_version(REPO_ROOT / "solutions" / a.solution)
            events.record(conn, "ladder", a.solution, step=0, action="re-entered by hand", eval_version=v)
            print(f"{a.solution} re-enters contention at step 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
