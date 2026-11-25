# crucible

An evolutionary harness that keeps improving whatever solution you onboard
into it, unattended, on one desk-sized GPU node: an HP ZGX Nano G1n (NVIDIA
GB10, 128 GB unified memory).

You onboard a solution by answering eight questions: a code module or a block
of instructions, with a frozen entrypoint and a way to tell good from bad.
The harness then runs generations. gpt-oss-120b proposes 32 variants at once,
code runs in locked-down sandboxes, a small judge model scores the rest, a
quality-diversity archive across four islands keeps the best, and winners are
checked on a held-out set the search never sees. A plateau ladder decides
what happens when progress stops, a morning report says whether to trust the
night, and a nightly window can distil the search's own successful proposals
into a LoRA adapter for the proposer.

**Status: a finished case study, published as-is.** It was built in about
seven weeks in autumn 2026 and ran unattended for nine scheduled days. It is
shared so others can read how it was built and what it found. No support is
offered, and issues and pull requests may go unanswered.

## What it found

| Finding | Evidence |
|---|---|
| **Throughput comes from concurrency, not speed** | One stream decodes at about 37 tok/s; 32 in flight reach a median 221 tok/s. So the search is a population, never one agent reasoning in a sequence |
| **Memory, not the Arm CPU, is the limit** | gpt-oss-120b's weights take 82.8 of 121.6 GiB. No third model fits beside the proposer and judge; training stops both |
| **Population search beat hill climbing** | On an equal wall-clock budget (decision 28) |
| **Telling the proposer the written standard beat searching for it** | `capability_case` reached 0.972 on held-out tests in one generation once the proposer was given the rule it had spent weeks rediscovering (decision 79) |
| **A search finds what the fitness does not measure** | Reading the winners found every serious fitness gap ([docs/search.md](docs/search.md)) |
| **Reflection and distillation are built, not proven** | Lessons lifted scores by 0.15 to 0.19, significant in none of three looks. The one distilled adapter was rejected by its gate |

The full account is in [docs/history.md](docs/history.md), and every decision,
numbered and dated, is in [docs/decisions.md](docs/decisions.md).

## The solutions

| Solution | What evolves | Held-out |
|---|---|---|
| `fixture` | A Python dispatcher over 12 small operations; the harness's own regression test | Not scored |
| `itot_classifier` | An IT/OT gateway classifier | 1.0 |
| `capability_case` | Instructions for judging an AI capability case | 0.972 |
| `capability_case_author` | Instructions for writing a capability case from evidence notes | 0.978 |
| `ot_change_scheduler` | A heuristic scheduling OT changes into maintenance windows, scored against the exact optimum | 0.998, then 0.950 on a harder set |

The IT/OT and capability-case solutions encode the decision procedures in
Stian Holm, *The IT/OT Boundary as Architecture: A Pattern Language for
Agentic AI* ([SSRN 6866600](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6866600)).
All task data is synthetic. Each solution's generation reports are in its
`results/` folder, and [docs/solutions.md](docs/solutions.md) describes each.

## What you need to run it

It was built for one machine, and its sizing is measured on that machine
([CAPACITY.yaml](CAPACITY.yaml)). On other hardware, re-measure before
trusting any number.

- **An NVIDIA GB10 system** (HP ZGX Nano, DGX Spark or similar) with DGX OS,
  Docker and the NVIDIA Container Toolkit.
- **NVIDIA's vLLM container**, `nvcr.io/nvidia/vllm:26.08-py3`, pinned by
  digest in `.container-digest`. Upstream vLLM does not target sm_121.
- **A Hugging Face token** for `openai/gpt-oss-120b` and `Qwen/Qwen3-4B`.
- **Python 3.12** for the harness.

## Getting started

Clone into a folder named `crucible`: the scripts address containers by
Compose's default names, such as `crucible-postgres-1`.

```bash
cp .env.example .env                       # fill in every value
docker build -t harness/runner:1 sandbox/  # the code sandbox
docker compose up -d                       # models (about 7 min to load), LiteLLM, Langfuse, Postgres, MinIO, Prometheus, Grafana
python3 -m venv .venv && .venv/bin/pip install -e .
ln -s "$PWD/ops/crucible" ~/.local/bin/crucible

crucible cli onboard                       # onboard a solution: eight questions
ops/search.sh first 3 fixture              # a 3-generation search on the regression solution
```

To run unattended, install the timers with `ops/systemd/install.sh` (after
`loginctl enable-linger`). Every service binds `127.0.0.1` without
authentication. The design assumes an isolated lab machine with
non-sensitive data; read [docs/security.md](docs/security.md) first.

## Documentation

Start at [docs/README.md](docs/README.md). The day-to-day manual is
[docs/operations.md](docs/operations.md), and the traps that cost the most to
find are in [docs/platform.md](docs/platform.md). [AGENTS.md](AGENTS.md)
orients a coding agent working in the repository.

## Licence

[MIT](LICENSE). The models, containers and paper keep their own licences.
