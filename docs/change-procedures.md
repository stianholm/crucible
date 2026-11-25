# Change procedures

What survives, what is invalidated, and what to do, for the four changes that
break comparability.

Moved from `CHANGE-PROCEDURES.md` on 2026-10-25 and updated to the as-built system. **Related:** [operations.md](operations.md), [backup.md](backup.md), [decisions.md](decisions.md)

---

## The rule underneath all four

A score is only meaningful against the thing that produced it. Every procedure
below is a variation on one question: after this change, which recorded numbers
still mean what they meant yesterday?

Two answers recur, and they are worth stating once because they are not
obvious:

- **Candidate scores survive a change to the model that wrote them.** Fitness
  measures the artifact, not its author. A better proposer does not make
  yesterday's candidate better or worse. This was written as "a model change"
  and narrowed 2026-09-28, because it is only true of the proposer: where a
  model grades the artifact rather than writing it, that model is part of the
  fitness function, and section 5 below is the measured consequence.
- **Candidate scores do not survive a fitness change.** Obvious in retrospect,
  routinely forgotten in practice, and the reason score histories quietly become
  meaningless.

Back up before any of these. See [backup.md](backup.md).

---

## 1. Base model refresh

A better model ships. You want it.

| Survives | Invalidated |
|---|---|
| The archive and every candidate score | Every LoRA adapter, absolutely |
| Lineage, descriptors, cell assignments | `CAPACITY.yaml` in full |
| The task set and all three splits | |
| `BASELINE.yaml`'s solution baseline | The proposer's cost and latency figures |
| The lesson store, mostly | |

Adapters are trained against specific base weights and do not transfer. Do not
attempt to carry them across. Evolved text candidates are the interesting case:
they encode both genuine task knowledge and accommodations to the old model's
quirks, and for a text solution whose worker is the proposer model, a model
change is also a fitness change (section 2).

**Procedure**

1. Back up.
2. Pull the new model. Keep the old one on disk, you will need it for the
   comparison and possibly for a rollback.
3. Re-run the Phase 0 concurrency sweep. Different model, different active
   parameter count, different memory footprint, therefore a different knee and a
   different generation size. Write a new `CAPACITY.yaml` and keep the old one.
4. Serve both models simultaneously and run paired generations, exactly as
   [distillation.md](distillation.md) describes for adapters. Same parents, same
   evaluator, same generation.
5. Discard all adapters. Retrain from the new base against the accumulated
   archive on the next nightly window.
6. Annotate the score history with a model-change marker: record an `event`
   row so the morning report shows it.

**Do not skip step 3.** The temptation is to assume a newer model is at least as
fast. On a bandwidth-bound machine a model with more active parameters is slower
per stream regardless of its benchmark scores, and generation sizing depends
directly on that number.

---

## 2. Fitness function change

You discovered the metric rewards something you did not intend, or the task
moved, or a new quality axis matters.

This is the most disruptive change in the project.

| Survives | Invalidated |
|---|---|
| Candidate artifacts themselves | Every score in the archive |
| Lineage and `root_sha` | `BASELINE.yaml` in full, including `noise_sigma` |
| The task set, if unchanged | Every cell assignment in `elite` |
| Adapters, technically | The comparability of all history before and after |

**Re-score the elites, not the archive.** With four islands of thirty-six cells,
that is roughly 144 evaluations, or two to three generations' worth of compute.
Affordable. Re-scoring thousands of archive rows is not, and it is not necessary,
because non-elite rows exist for lineage and for training data rather than for
comparison.

**Procedure**

1. Back up. This one especially.
2. Version the fitness function: `fitness_version` in `BASELINE.yaml`. (The
   per-row `fitness_version` column this step once called for was never added;
   archives are instead parked by relabelling `elite.solution_id`, decision 41.)
3. Re-score all elites under the new function. Rebuild the `elite` table from
   the results, because cells were claimed under the old definition and some
   occupants will change.
4. Mark every pre-change `iteration` row as stale for comparison purposes.
   Do not delete them. They remain valid lineage and valid training data.
5. Re-measure `noise_sigma` from scratch. A new fitness function has a new noise
   floor, and Phase 2's two-sigma significance test is meaningless until it is
   remeasured.
6. Re-baseline the incumbent solution.
7. Annotate the score history with a hard discontinuity. Make the morning report
   refuse to draw a trend line across it.

**The check that this was worth doing:** re-score the three elites you were most
suspicious of, the ones that scored well but that you did not endorse when you
read them. If they still score well under the new function, the change did not
fix what you thought it fixed.

---

## 3. Container tag upgrade

New vLLM container from NVIDIA. Routine, but not free.

| Survives | Invalidated |
|---|---|
| Everything about the search | `CAPACITY.yaml` |
| All scores, all lineage | Any flag that changed name or default |
| Adapters, usually | |

**Procedure**

1. Read NVIDIA's release notes for the new tag before pulling anything. This is
   where the platform-specific caveats appear, and it is how the Nemotron
   sequence cap and the unified-memory OOM guidance were found in the first
   place.
2. Pull the new tag. Keep the old digest. Do not delete the old image.
3. Re-run the Phase 0 sweep. Container-level changes to attention backends,
   quantisation kernels and scheduling move throughput by tens of percent in
   both directions.
4. Compare against the old `CAPACITY.yaml`, after checking that its KV cache
   sizes match the ones you just ran. If they differ, compare at equal running
   counts in vLLM's logs instead (decision 105). If the knee moved, generation
   sizing moves with it.
5. Run the sandbox abuse suite. Unrelated in theory, five minutes in practice,
   and container runtime changes are exactly the sort of thing that quietly
   breaks containment.
6. Update `.container-digest` and the compose file together.

Roll back by pinning the old digest. This is why step 2 says keep it.

---

## 4. Eval set change

Covered operationally in PHASE-6.md under drift (a planning document not
included here, see [history.md](history.md)). The mechanical
part belongs here.

**Built:** every held-out result is stamped with `eval_set_version()`, a hash
of the held-out files, and the morning report and the plateau ladder compare
scores only within one version. A changed held-out set restarts a solution's
ladder, which is how a plateaued solution re-enters contention.

| Survives | Invalidated |
|---|---|
| Candidate artifacts and lineage | Scores, to the degree the set changed |
| The fitness function itself | `BASELINE.yaml` |
| Adapters and prompts | Cross-version score comparisons |

A rotation reshuffle inside an unchanged set is not a change and needs nothing.
Adding, removing or relabelling items is.

**Procedure**

1. Version the eval set. `eval_set_version` stamped on every score.
2. Preserve the split rule. Phase 1's hash-based split means new items land in a
   split deterministically, so the boundary stays honest without manual sorting.
3. Never move an item between splits. An item that was ever in `held_out` is
   burned for `rotation` forever, because the loop has effectively seen it
   through the promotion gate.
4. Re-baseline, and re-measure `noise_sigma` if the set changed size
   meaningfully.
5. Re-checksum the held-out set and back it up before doing anything else.

---

## 5. Judge restart, for a judged solution

Added 2026-09-28, from measurement rather than from planning. The four
procedures above were written before any solution scored by a model existed.
`capability_case` is one, and for it the judge model is not a tool that observes
fitness, it **is** the fitness function. That makes restarting the judge
container a fitness change in the only sense that matters, even when no flag,
no model and no tag changed.

| Survives | Invalidated |
|---|---|
| Candidate artifacts and lineage | Cross-restart score comparisons |
| The rubric, the checks, the eval set | Any trend line spanning the restart |
| Scores measured within one container lifetime | `noise_sigma` as a cross-restart bound |

**The measurement.** Candidate `a3f0dde310a6cffc` was scored against
`capability_case`'s 22 held-out tasks four times between 2026-09-24 and
2026-09-25, giving quality 0.7727 every time. The judge container was recreated
2026-09-26 20:03 UTC to add the healthcheck it had been missing, with its model,
its flags and its `--max-model-len` all unchanged. Re-scored three times on
2026-09-28, the same candidate gave quality 0.7273, and all three repeats were
identical on all 22 tasks, so the new value is as reproducible as the old one.
Every file in the evaluation path was last modified in the same commit that
produced one of the 0.7727 reports, and the held-out set has not changed since
2026-09-22, so no code or data difference explains it. Quality here is
effectively binary per task because the mechanical floor gates it, and the shift
is exactly one task's full point: one scenario's verdict flipped, at temperature
zero, across a container restart.

**Why this matters more than its size suggests.** `noise_sigma` is 0.0 for this
solution, measured over seven identical repeat runs, and that number is correct.
The two-sigma significance test therefore treats any nonzero gap as significant.
A comparison whose two halves straddle a judge restart can manufacture a
significant result out of roughly 0.045 quality of pure container state.

**Procedure**

1. Record the judge container's start time alongside every score. Without it,
   there is no way to tell afterwards which lifetime a number came from.
2. Re-baseline after any judge container recreation, including one that changes
   nothing but a healthcheck.
3. Never compare scores across a restart boundary. Re-measure the older side.
4. Treat `noise_sigma` as a within-lifetime bound only.

Task 3.9's population-versus-hill-climb conclusion was checked against this and
holds: its two halves are 0.7727 and 0.641, a gap of 0.132, and both were
measured inside the 2026-09-22 to 2026-09-26 container lifetime.

**Qualified 2026-10-16 (decision 71).** The identical within-lifetime
repeats above came from `score_over`, which sends one request at a time.
Population search and every batch re-score send 32 at once, and under that
load the judge is not deterministic within a lifetime either: 60 recorded
judge requests replayed twice at temperature 0 gave identical text on 3 and
the same BAND on 45 (75%). Replayed against their originals from an earlier
lifetime, 47 matched (78%). So for concurrent scoring, a restart adds nothing
measurable beyond the noise batching already causes, and the boundary this
section guards is not the dominant effect. The procedure stands, since
recording start times costs nothing and sequential scoring still shows the
restart effect, but the nightly window ([distillation.md](distillation.md)) restarts the
judge on this basis. Both servers' KV caches are also pinned now
(`compose.yaml`), which removes one source of difference between lifetimes.

---

## Quick reference

| Change | Archive scores | Adapters | Prompts | `CAPACITY.yaml` | `BASELINE.yaml` |
|---|---|---|---|---|---|
| Base model | survive (text solutions: see section 1) | **discard** | re-evolve | **re-measure** | proposer half |
| Fitness function | **invalid** | survive | survive | survives | **rebuild** |
| Container tag | survive | survive | survive | **re-measure** | survives |
| Eval set | partial | survive | survive | survives | **rebuild** |
| Judge restart | survive, **not comparable across it** | survive | survive | survives | **re-baseline** |

Every row in that table implies an annotation in the score history. A trend line
that crosses one of these without saying so is not a trend, and it will
eventually be used to justify a decision it cannot support.
