# History

How crucible was built: what each phase set out to do, what it delivered, and
what it found. The phase specifications this summarises (`PLAN.md`,
`PHASE-0.md` to `PHASE-6.md`, `MEMORY.md`, `THREAT-MODEL.md`) were working
documents, retired as each phase closed. They are not included in this
repository; this page and [decisions.md](decisions.md) record what came of
them.

Code comments that say "See PHASE-3.md task 3.2" refer to those documents.

---

## Timeline

| Phase | Dates | Planned | Outcome |
|---|---|---|---|
| Planning | to 2026-09-09 | | Twelve specifications, about 26,500 words |
| 0, bring up the node | 09-09 to 09-19 | 2 to 3 days | Done |
| 1, define better | to 09-21 | 2 weeks | Done |
| 2, hill climb | to 09-22 | 1 week | Done |
| 3, go parallel | 09-22 to 09-26 | 1 to 2 weeks | Substantially done |
| 4, add reflection | 09-27 to 10-13 | 1 week | Built; thesis unproven |
| 5, close the slow loop | 10-16 to 10-24 | 2 weeks | Built; thesis untested |
| 6, let it run | 10-24 to 11-05 | Ongoing | Done: nine scheduled days, handover closed 11-05 |

The plan said eight weeks from bare machine to unattended; the build took
about seven.

---

## Phase by phase

### Phase 0: bring up the node

**Planned exit:** the machine's own throughput curve. **Delivered:** two vLLM
servers under a pinned container, LiteLLM routing by role, Langfuse receiving
traces, Prometheus scraping queue depth, an 8-point sweep for two profiles,
`CAPACITY.yaml` and a measured memory budget.

**Found:** the aggregate ceiling is about 201 tok/s at concurrency 64, not the
863 at 256 a published benchmark showed, because gpt-oss-120b's 82.8 GiB of
weights leave little room for KV cache. Langfuse had to stay on v3 (decision
8). The two engines failed to cold-start together (decision 11); a reboot
test on 2026-10-27 started them together successfully (decision 99), so the
risk is real but not certain.

### Phase 1: define better

**Planned exit:** a baseline reproducible twice. **Delivered:** the
onboarding wizard, the adapter contract, both evaluators, the `fixture`
regression solution, the frozen `fitness.py` vector, the three-tier scorer, a
measured noise floor (sigma 0.0), an adversarial suite, `BASELINE.yaml`.
Sandboxing used Docker, not rootless Podman (decision 14).

### Phase 2: hill climb

**Planned exit:** beat the baseline once, unattended. **Delivered:** the
proposal contract, validation ladder, sandbox slot, greedy loop, Postgres
persistence, budget governor and automatic `RUN.md`. `itot_classifier`, the
first real solution, was solved at 1.0 in one iteration because its task
description was nearly a complete algorithm.

### Phase 3: go parallel

**Planned exit:** sustained throughput and a diversity metric that is not
collapsing. **Delivered:** the concurrent fan-out, MAP-Elites archive, four
islands with migration, parent selection, an 8-slot sandbox pool, diversity
metrics, the generation report. Population search beat hill climbing on an
equal wall-clock budget (decision 28).

**Not built:** Temporal, deliberately (decision 18). **Amended:** the 250
tok/s throughput target, which exceeded the machine's measured ceiling
(decision 33). **Deferred:** the chaos test, which moved into Phase 6's
handover and passed there on 2026-10-25 (decision 95).

### Phase 4: add reflection

**Planned exit:** a lift over Phase 3 above two sigma at equal compute.
**Delivered:** the failure taxonomy (TF-IDF, because no embedding model fits,
decision 34), the lesson store with retirement, two-tier injection, metrics of
learning. **Not delivered:** the lift. Three looks on a sound configuration
put lessons ahead by 0.15 to 0.19, significant in none, so they are off by
default. GEPA was not built.

**What the phase was really worth** was its measurement: search run-to-run
variance (sd 0.0228, decision 48), the prefix-cache gain from prompt ordering
(33.7% to 61.5%, decision 49), and four measurement defects in earlier phases.
It also found that `capability_case` was mis-wired: a 4B worker could not
execute the conditional rule the search was evolving (decision 56).

### Phase 5: close the slow loop

**Planned exit:** a distilled proposer that beats stock, promoted by the gate.
**Delivered:** every piece of the round, run unattended once; the gate
rejected the first adapter (+0.37 sigma, 13% dearer). See
[distillation.md](distillation.md).

**The finding that changed the project:** `capability_case` reached held-out
0.972 in one generation once the proposer was told the written standard
(decision 79). Most of its headroom had been the proposer not knowing the
rule. The wizard gained an eighth question for it (decision 80). A third
solution, `capability_case_author`, reached 0.977 after the search exposed and
the fitness closed a gap (decisions 84 to 86). With both saturated, the
distillation thesis was left untested, not refuted (decision 88).

### Phase 6: let it run

Built 2026-10-24 and 25: the kill switch, the morning report and event log,
the scheduler with the plateau ladder and an in-day promotion gate, immediate
alerts, the retention sweep, and `ot_change_scheduler`, a solution with a deep
gradient so the fourteen days have real work (decisions 89 to 94). The chaos test and
the kill switch's nightly-window path passed against the live system before
day 1 (decision 95). On the first scheduled day `ot_change_scheduler` saturated at 0.998
and the ladder climbed two steps unattended; it moved to a harder eval set and
the fourteen days restarted; two more defects on the next day moved day 1 to
2026-10-28 (decisions 96 to 98). A deliberate reboot before day 1 passed, and
317 pending system updates, including a new kernel and NVIDIA driver, were
found not to install themselves and deferred until Phase 6 ends (decision 99).
`ot_change_scheduler` went dormant on day 1 after the ladder took all four
steps unattended; every solution has been dormant since, which counts as a
scheduled day (decision 100). With the box idle, the scheduled days were
shortened to ten (decision 101), and the operator closed the handover on
2026-11-05, day 9, against the written recommendation to keep the date
(decision 102).

**Outcome:** every checklist line was met as amended. Nine days ran without
intervention and nine reports were read. A real problem, the 10-27 deadlock,
was caught by the morning report. One elite read was done, adopted from a
prepared read. Two things were not shown. The phone tier never fired
on a real problem. The idle box measured nothing about slow drift under load.
The plan's exit criterion was "it improves something while you sleep and you
believe the log the next morning". The second half held. The first half held
for one day, until the search exhausted what its fitness rewards, and the
ladder said so.
See [operations.md](operations.md). What is left is in
[TODO.md](../TODO.md).

---

## Lessons that held across phases

- **Measure before building on an assumption.** The capacity ceiling, the
  memory budget, the embedding model, KV sizing and judge determinism were
  all different from what was planned.
- **A search finds what the fitness does not measure.** Reading the winners
  found every serious fitness gap ([search.md](search.md)).
- **Tell the proposer the standard.** Search should spend its effort on what
  cannot be written down.
- **Instruments fail quietly.** Most of the project's corrections came from
  running a metric and checking it against raw rows, not from reasoning about
  it.
- **Concurrency is the architecture.** Every component that would have
  serialised the loop was either rejected or fixed.
