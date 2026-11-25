# Operations

How crucible runs without you, what it asks of you, and what to do when
something is wrong. The specification behind this was PHASE-6.md, one of the
planning documents not included in this repository (see
[history.md](history.md)).

---

## The daily cycle

Five systemd user timers, installed by `ops/systemd/install.sh`, which writes
the repository's path into each unit. Re-run it after editing a unit or moving
the repository. Lingering is
enabled for the user, so they fire without a login and catch up after a
missed boot where marked.

| Time | Timer | Runs | Does |
|---|---|---|---|
| Every 5 min | `crucible-alerts` | `ops/alerts.sh` | Checks the immediate alert signals |
| 00:30 | `crucible-nightly` | `ops/nightly.sh 06:00` | Trains on a signed, not yet trained selection; otherwise exits in seconds |
| 06:30 | `crucible-day` | `ops/daily.sh 23:00` | The scheduler runs generations until 23:00 |
| 08:00 | `crucible-morning` | `ops/morning.sh` | Writes the morning report (catches up after boot) |
| 23:00 | `crucible-retention` | `ops/retention.sh` | Expires old data (catches up after boot) |

Check them with `systemctl --user list-timers 'crucible-*'`. Logs are in
`logs/`: `day-<date>.log`, `nightly-<date>.log`, `alerts.log`,
`retention.log`, `morning.log`.

---

## The scheduler and the plateau ladder

`harness/scheduler.py` runs the day as segments of up to four generations,
each ending in a two-pass held-out check. Before each segment it:

1. stops if halted, or if the daily token cap (`schedule.yaml`, 35M) is spent;
   waits, polling each minute, while the proposer does not answer, so an
   outage cannot race segments or climb the ladder (decision 95);
2. picks a solution: the one running keeps the GPU until it goes dormant,
   then operator priority (`priority:` in `schedule.yaml`), then the longest
   wait;
3. takes the ladder step that is due;
4. runs paired stock against distilled if an adapter is loaded and ungated;
5. starts only if the segment and its held-out check fit before 23:00.

**The ladder** (`harness/ladder.py`): 12 generations without a held-out gain
above one sigma move a solution one step. Sigma is the held-out passes'
spread, floored at 0.01 unless the solution's `BASELINE.yaml` sets a measured
`ladder: sigma_floor:` (ot_change_scheduler: 0.003, decision 98).

| Step | Action |
|---|---|
| 1 | Mutation temperature 0.9 to 1.1 |
| 2 | Park the weakest island's elites and reseed it from the first committed seed |
| 3 | Ask you for a distillation round (in the morning report) |
| 4 | Dormant: the GPU goes to the next solution with headroom |

It never loops. A held-out gain returns a solution to climbing; a changed
held-out set restarts it. The state is replayed from the `event` table, so the
scheduler and the report always agree.

```bash
crucible scheduler status              # every solution's state, and what runs next
crucible scheduler reenter <solution>  # lift a dormant solution by hand
```

Generation reports from scheduled segments go to
`reports/generations/<solution>/`.

---

## The morning report

`reports/morning/<date>.md`, at 08:00. The first line is the verdict:
`HEALTHY`, `DEGRADED` with the failing signals named, or `HALTED` with the
reason. Then the would-stop signals, what changed, numbers, solutions, and
what it wants from you.

| Signal | Not ok when |
|---|---|
| attention | The previous report was not marked read |
| jobs | Any crucible timer job's last run failed |
| models | Proposer or judge down |
| activity | No generations in 24 hours, unless the scheduler recorded that every solution is dormant (decision 100) |
| budget | The daily token cap is spent |
| failures | More than 10% of the day's rows not scored |
| plateau | A solution reached ladder step 3 |
| held-out | A score fell more than 0.03 below the best on the same eval set |
| gate | The last three adapters were all rejected |
| capability | The newest adapter regresses more than 5% |
| disk | Above 85% |
| backup | No backup younger than 35 days (decision 103) |
| diversity | Proposal diversity down more than 10% week on week |

Thresholds are constants in `harness/morning.py`. Changing one is a gate
change: record it in [decisions.md](decisions.md) with a date and a reason.

```bash
crucible morning read                       # mark the latest report read
crucible morning elite-read "what you found" # record the weekly elite read
crucible morning ack <event id>             # acknowledge an alert or a request
crucible morning write                      # write a report now
```

---

## Alerts

Two tiers only. The morning report is one. The other is immediate:
`harness/alerts.py`, every five minutes.

| Signal | Fires when |
|---|---|
| models | Proposer or judge unreachable for 15 minutes, outside a nightly window |
| disk | Above 85% |
| leak | A sandbox container older than 15 minutes |
| capability | The newest adapter regresses more than 5% |
| budget | The daily cap spent before 18:00 (from the scheduler) |

An alert fires once per incident, waits in the morning report until
acknowledged, and sends "resolved" when it clears. It always goes to the event
table and `logs/alerts.log`, to the desktop when a session is open, and to
your phone through ntfy (`NTFY_URL` in `.env`, set and tested 2026-10-25). Test with
`crucible alerts test`.

Checks are samples, five minutes apart, so two outages separated by less than
five minutes read as one: on 2026-10-25 two back-to-back tests fired a
"15 minutes down" alert after two short outages (decision 95). Times in alert
messages are local.

Resist adding a tier. A new signal belongs in one of the two.

---

## The kill switch

```bash
ops/kill.py "reason"   # halt
ops/kill.py --status   # halted, and why
ops/kill.py --clear    # lift the halt; only a person does this
```

It writes `state/HALT`, stops every crucible run by process group, cancels
requests a dead client left decoding (by restarting LiteLLM and waiting for
it), stops a training container, removes sandbox containers, and restores
the models if it interrupted a nightly window. It prints a fingerprint of
every parked archive before and after, and the git state of the deployed
candidates. While halted, `ops/search.sh` refuses to start and a running
search stops at the next generation.

**Tested live seven times** by 2026-10-27 (decisions 89, 94, 95, 97, 98): on
running searches, to restart runs onto fixes and an eval set change, and once
on an interrupted nightly window,
where it stopped the training container and restored proposer then judge in
9 minutes. Archives were byte-identical before and after every time.

---

## Retention

| Data | Kept |
|---|---|
| `iteration`, `elite`, `lesson`, `event` rows | Forever |
| Candidate artifacts | Elites and anything ever claimed forever, the rest 30 days |
| LoRA adapters, benchmark results | Forever |
| Langfuse traces and raw events | 90 days |
| ClickHouse system logs | 7 days (found holding 9 GB, decision 93) |
| Container images | Reported, never removed automatically |

`crucible retention sweep --dry-run` shows what a sweep would do.

---

## What stays manual, permanently

- **Promoting the deployed solution.** The gate says whether a candidate is
  better; you decide whether better is enough. Promotion means copying the
  winner's block into `solutions/<id>/candidate/`, re-measuring
  `BASELINE.yaml`, and committing.
- **Any change to a fitness function.** See
  [change-procedures.md](change-procedures.md).
- **Signing the harvest review** before any training.
- **The weekly elite read.** Thirty minutes reading the top candidates. It is
  the only check that asks whether a score rose for a reason you endorse.

## The quarterly review

Every three months, ask the three questions the daily report cannot. The
first is due around 2027-02-05.

- **Is it still improving?** Plot held-out across the whole history,
  annotated with eval-set versions. A flat quarter is a real answer.
- **Is the improvement worth what it costs?** Power, disk, attention and the
  nightly window, against what the same effort would buy elsewhere.
- **Has the fitness drifted from what you want?** Read the top elites from
  three months ago and today side by side. If today's score better and you
  prefer the older ones, the metric has come loose from the goal.

Review every threshold change in [decisions.md](decisions.md) at the same
time, so the gates do not loosen one small step at a time.

---

## What a model outage does

Measured by the chaos test, 2026-10-25 (decision 95): the proposer restarted
mid-generation and was back after eight minutes.

| | Behaviour |
|---|---|
| The generation in flight | Its proposals fail and are recorded as `propose_failed`; the segment ends |
| The plateau ladder | Unaffected: only generations that scored something count |
| The scheduler | Waits, polling each minute, until the proposer answers |
| Recovery | The next segment starts within a minute of the proposer returning |
| Alert | Fires only if the outage lasts 15 minutes |
| Morning report | The failed rows show in the `failures` signal |

## Running things by hand

```bash
ops/daily.sh 23:00                                 # a day window now, deadline 23:00
ops/search.sh <tag> [generations] [solution] [git-rev]   # a one-off experiment, parked as <solution>_<tag>
ops/stop.sh <solution> <tag>                       # stop a search started by ops/search.sh
ops/nightly.sh 06:00                               # a training window now
ops/backup.sh [dest]                               # a backup; `ops/backup.sh verify <dir>` restores and compares
crucible cli onboard                               # a new solution
.venv/bin/python -m pytest -q --ignore=tests/test_sandbox_abuse.py   # the test suite
```

`ops/search.sh` refuses to start on a non-empty live archive and parks its
archive afterwards, so experiments never mix with the scheduled search.

**`crucible <module> ...`** runs any harness command from any directory: it is
`ops/crucible`, linked into `~/.local/bin`, and sets up the repository root,
`.env` and the project's Python. Plain `python` does not exist on this machine.
To link it again on a new machine: `ln -s $PWD/ops/crucible ~/.local/bin/crucible`.

---

## When something is wrong

| Symptom | Likely cause | What to do |
|---|---|---|
| Report says `idle: no generations and no scheduler check` | The day timer did not fire or the window failed ("idle by design" with every solution dormant is ok) | `harness.scheduler status`; `systemctl --user list-timers` |
| Many `propose_failed` rows | LiteLLM or the proposer down, or restarting | Check `curl localhost:4000/health/liveliness` and `:8000/v1/models` |
| Many `inadmissible` rows "grew Nx" | The solution's `max_growth` too low for its seed | Raise it in the adapter (decision 94) |
| A model will not start | Page cache holding memory, or both engines starting at once | `python3 ops/evict_cache.py`, check `MemFree`, start proposer before judge |
| Judge scores differ between runs | Concurrent batching makes it non-deterministic | Expected (decision 71); compare within one run |
| Disk climbing | A store the sweep does not cover | `docker system df -v`, then add it to `harness/retention.py` |
| Report says `jobs: last run failed: <job>` | That timer job's last run exited with an error | Read `logs/<job>.log` (or `logs/alerts-check.log`) and `systemctl --user status <job>.service` |
| `Command 'python' not found` | Plain `python` does not exist here | Use `crucible <module> ...` |
| The DGX Dashboard offers updates | Can include kernel and NVIDIA driver; the last batch went in 2026-11-05 (decision 105) | Do not click Update; apply them through [change-procedures.md](change-procedures.md) and a reboot check, after a backup (decision 99) |

The platform's own traps are in [platform.md](platform.md).
