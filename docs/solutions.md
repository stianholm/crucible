# Solutions

The harness improves whatever is onboarded into it. This is how a solution is
defined, what is onboarded today, and how to add one.

---

## Onboarding

`crucible cli onboard` asks eight questions and writes
`solutions/<id>/SOLUTION.md` and `solution.yaml`:

| # | Question | Notes |
|---|---|---|
| 1 | What should get better? | One sentence; becomes the proposer's task description |
| 2 | What form does the artifact take? | Code module, instructions text, config |
| 3 | How is it invoked? | **Frozen forever.** Changing it makes every score incomparable; onboard a new solution instead |
| 4 | What may the proposer change? | The `EVOLVE-BLOCK` region; everything else is scaffolding |
| 5 | How is good told from bad? | Even informally |
| 6 | How will it be measured? | `automated_checks` (preferred), `labelled_examples`, `judge`, `none_yet` |
| 7 | Does evaluating it run code? | Yes: sandboxed. No: in-process |
| 8 | Is there a written standard? | Optional. Given to the proposer from generation 0 (decision 80) |

The wizard creates the directory. The rest is built per solution:

| File | Holds |
|---|---|
| `adapter.py` | The plugin: `materialise`, `invoke`, `shape_ok`, `programmatic_checks`, `needs_judgement`, `descriptors`; optional `max_growth`, `eval_timeout_s`, `task_class`, `rubric` |
| `candidate/` | The incumbent, with `EVOLVE-BLOCK-START` and `EVOLVE-BLOCK-END` markers |
| `checks/` | Ground truth: a reference, a verifier, a task generator |
| `data/dev`, `rotation`, `held_out` | Tasks as JSON, split by hash; `held_out.sha256` seals the held-out set |
| `BASELINE.yaml` | Measured baseline, noise, cost, `tasks_per_candidate` |
| `solution.yaml` `status:` | Human-readable state; the scheduler reads the event log, not this |

**Every row in the system carries `solution_id`.** The candidate never
reaches the evaluator: not by import, path or network.

---

## The roster on 2026-11-05

| Solution | Artifact | Measured by | Held-out | Scheduler state |
|---|---|---|---|---|
| `fixture` | Python dispatcher over 12 small ops | Exact checks | Regression test | Never scheduled |
| `itot_classifier` | Python classifier, gateway routing (whitepaper Section 5) | Exact checks | 1.0 | Dormant |
| `capability_case` | Instructions: judge a capability case (Section 8) | Mechanical floor plus judge at 30% | 0.972 | Dormant |
| `capability_case_author` | Instructions: write a capability case from evidence notes | Five mechanical checks, judge off | 0.978 | Dormant |
| `ot_change_scheduler` | Python heuristic: schedule OT changes into maintenance windows | Value over exact MILP optimum, any rule broken scores 0 | v1 saturated at 0.998; v2 best 0.950 | Dormant since 2026-10-28 (decision 100) |

### Notes per solution

- **`fixture`** is the harness's own regression test, kept static on purpose.
  Run it by hand after a harness change.
- **`itot_classifier`** was solved in one iteration because its task
  description was close to a complete algorithm. Only new tasks give it
  headroom.
- **`capability_case`** was the project's long test bed. Its headroom turned
  out to be the proposer not knowing the standard; stated, the first
  generation reached 0.972 (decision 79). Its judge is non-deterministic
  under concurrent load (decision 71).
- **`capability_case_author`** is the inverse task. Its first winner gamed a
  gap in the fitness (decision 84); a restart from the original seed escaped
  a local optimum (decisions 85, 86). Judge calibration: 8 of 8 human labels
  agreed, all the same band, so the judge stays off as uninformative
  (decision 88).
- **`ot_change_scheduler`** was onboarded for Phase 6 because it has real
  headroom that no standard can shortcut: the rules say what is allowed, not
  how to choose. 100 generated instances, each with an exact optimum from
  SciPy's MILP solver, re-checked by the same verifier that scores
  candidates. A throwaway 2-second local search reached 0.946, so the
  gradient runs from the seed's 0.79 to about 0.95 to 1.0 (decision 94). The proposer
  closed that gradient in a day (0.998, decision 96), so eval set v2 has
  larger, tighter instances (80 to 200 changes), still with exact optima. The
  v1 winner is the incumbent and scores 0.947 on it (decision 97).

---

**Calibrating headroom by hand underestimates the proposer.** A 2-second
probe search reached 0.946 on v1; the search reached 0.998 in a day. Size an
eval set so that the best candidate you can get, not a quick probe, still
falls clearly short.

## Adding a solution

1. Prefer a task where correctness can be checked automatically and where no
   paragraph states the answer. A solution whose quality a written rule fully
   specifies saturates in one generation.
2. Run the wizard; answer question eight if a standard exists.
3. Build `checks/` with ground truth, generate tasks, split, seal held-out.
4. Write the adapter. Make an invalid output score 0, not partial credit for
   form.
5. Write a deliberately plain seed between the markers.
6. Measure the seed on all three splits and write `BASELINE.yaml`.
7. Calibrate headroom: a quick hand-written stronger approach shows whether
   there is a gradient to climb.
8. Add tests (`tests/test_<id>.py`) for the rules and the score.
9. The scheduler picks it up on its own: a new solution enters contention at
   once.

Changing a solution's fitness, eval set or invocation later invalidates
scores; see [change-procedures.md](change-procedures.md).
