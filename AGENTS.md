# crucible: context for coding agents

An evolutionary harness that continuously improves whatever solution you
onboard into it, running unattended on one local GPU node. This file orients a
coding agent working in the repository: what state the project is in, where
the truth lives, and what is expensive to rediscover.

## Current state

**Built, and running unattended.** Phases 0 to 6 are complete; Phase 6's
handover closed on 2026-11-05 (decision 102). Systemd user timers run the day
window, nightly training, morning report, alerts and retention. Every solution
is dormant, so the scheduler idles by design (decision 100).

Read [TODO.md](TODO.md) first: it is what remains. The system as built is
documented in [docs/](docs/README.md), and every decision, numbered and
dated, is in [docs/decisions.md](docs/decisions.md). Code comments cite
decisions by number ("TODO.md decision N" in older code means that file) and
phases by task ("PHASE-3.md task 3.2"). The phase specifications were working
documents and are not included here; see [docs/history.md](docs/history.md).

## The fact that explains every design decision

The HP ZGX Nano G1n is memory-bandwidth-bound: 128 GB unified at 273 GB/s. A
single stream decodes at about 37 tokens per second. Aggregate throughput
rises with concurrency, capped by KV cache because gpt-oss-120b's weights take
82.8 GiB of the pool. Real generations reach about 221 at 32 in flight; the
sweep's larger requests stop at about 142 (decision 105). So throughput comes
from concurrency, and the search is a **population**: 32 candidates per
generation, proposed in parallel. If a proposed change would reduce
concurrency, it is almost certainly wrong. Check `CAPACITY.yaml` before
assuming headroom for a larger population or longer outputs.

## Decisions already made: do not relitigate

| Date | Decision |
|---|---|
| 2026-09-03 | vLLM over Ollama, because continuous batching is the entire performance argument |
| 2026-09-03 | Population search over hill climbing, for the reason above |
| 2026-09-04 | The harness **onboards** solutions by asking questions (eight since 2026-10-18, decision 80). Every row carries a `solution_id` |
| 2026-09-04 | Evaluator pluggable: in-process for text, sandboxed for code |
| 2026-09-04 | Prefer automated checks over labelled data |
| 2026-09-04 | Isolated lab machine, non-sensitive data, single operator |
| 2026-09-04 | `fixture` is the harness's permanent regression test, never scheduled |
| 2026-10-18 | The proposer is given a solution's written standard from generation 0 (decisions 79, 80) |
| 2026-10-24 | What stays manual: promoting the deployed solution, any fitness change, signing the harvest review, the weekly elite read |

Reasoning for each is in [docs/decisions.md](docs/decisions.md).

## Conventions

- **Markdown, not HTML.** `docs/` is the as-built documentation; keep it
  current in the same commit as the change it describes.
- **Diagrams are mermaid** in fenced blocks.
- **Prose style:** no em-dashes, one idea per sentence, tables for numbers,
  bold-led bullets for parallel items.
- **A decision that changes the system** is appended to
  [docs/decisions.md](docs/decisions.md) with the next number and a date, and
  propagated to every affected document in the same session.
- **Generation reports** go to `solutions/<name>/results/`.

## Expensive to rediscover

The full list, with reasons, is in [docs/platform.md](docs/platform.md).

- **Container tag is `nvcr.io/nvidia/vllm:26.08-py3`**, pinned by digest. vLLM
  does not officially target sm_121. Do not float the tag or chase upstream.
- **KV cache sizes are pinned in bytes in `compose.yaml`.** vLLM sizes the KV
  cache from whatever is resident at start; the same 0.74 utilisation produced
  0.06, 0.77 and 18.05 GiB in one evening (decision 70). Check `compose.yaml`
  for current values rather than trusting a number in a document.
- **Page cache is not free memory to CUDA.** Run `ops/evict_cache.py` and
  check `MemFree`, not `MemAvailable`. `nvidia-smi` reports memory as N/A here.
- **No third CUDA process fits** beside proposer and judge. Training stops
  both.
- **`CAPACITY.yaml` is machine-and-model level**; per-solution sizing lives in
  each `BASELINE.yaml`. Do not merge them.
- **Client timeouts must exceed 15 minutes.**
- **The judge is non-deterministic under concurrent load** (decision 71).
- **Internal services bind `127.0.0.1`**, never `0.0.0.0`. None carry auth.
- **Stop runs by process group** (`ops/kill.py`, `ops/stop.sh`), never with
  `pkill -f` (decision 83).
- **Use `crucible <module> ...`** (`ops/crucible`) to run harness commands;
  plain `python` does not exist on the machine.
- **System updates are a platform change**, not a click in the DGX
  Dashboard: a kernel or NVIDIA driver change can stop vLLM. Apply them
  through docs/change-procedures.md and a reboot check (decision 99).
- **Experiments** go through `ops/search.sh`, which refuses a non-empty live
  archive and parks its own afterwards, so they never mix with the scheduled
  search.
- **Systemd units carry `@REPO@`**; `ops/systemd/install.sh` fills in the
  path. Re-run it after editing a unit.

## Working agreements

- Give a recommendation and its reasoning, not an option list.
- Turning on anything unattended that trains, deletes or stops models is the
  operator's act: write it, test it by hand, and let them enable it.
- Do not add depth to a specification without a reason.
