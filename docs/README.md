# crucible, as built

An evolutionary harness that continuously improves whatever solution is
onboarded into it, running unattended on one HP ZGX Nano G1n. It proposes
candidates in parallel with gpt-oss-120b, scores them against checks it never
lets them see, keeps a quality-diversity archive, and promotes only what holds
up on a sealed held-out set. A nightly window can distil the search's own
successful proposals into a LoRA adapter for the proposer.

**State on 2026-11-05:** built and running unattended. Phases 0 to 6 are
complete; Phase 6's handover closed after nine scheduled days (decision 102).
What is left is in [TODO.md](../TODO.md).

This is a finished case study, published as-is. Start with the repository's
[README](../README.md) for what it found and how to run it.

---

## Read in this order

| Document | Covers |
|---|---|
| [architecture.md](architecture.md) | The constraint behind the design, services, serving flags, harness modules, data stores, planned against built |
| [operations.md](operations.md) | The daily cycle, scheduler and ladder, morning report, alerts, kill switch, retention, runbook |
| [search.md](search.md) | How a generation works, scoring, the archive, reflection, what the searches found |
| [solutions.md](solutions.md) | Onboarding, the solution contract, the five onboarded solutions, adding one |
| [distillation.md](distillation.md) | The slow loop: harvest, review, nightly training, A/B, gates, round 1 |
| [platform.md](platform.md) | Hardware, pinned containers, measured capacity and memory, the traps |
| [security.md](security.md) | Containment of generated code, controls, accepted risks |
| [backup.md](backup.md) | What is backed up, how to restore, and the restore check |
| [change-procedures.md](change-procedures.md) | What a model, fitness, container, eval set or judge change invalidates |
| [history.md](history.md) | Each phase planned against delivered |
| [decisions.md](decisions.md) | Every decision, numbered, dated, verbatim |

At the repository root: [TODO.md](../TODO.md), the roadmap, and
[AGENTS.md](../AGENTS.md), context for coding agents. The phase
specifications were working documents and are not included (see
[history.md](history.md)). `CAPACITY.yaml` and each solution's `BASELINE.yaml`
are the measured data the documents cite; each solution's generation reports
are in its `results/` folder.

## Conventions

Markdown, mermaid for diagrams, no em-dashes, tables for numbers. When a
decision changes the system, append it to [decisions.md](decisions.md) and
update the document it affects in the same commit.
