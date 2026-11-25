# Generation 5 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 46.8%
- Aggregate throughput: 53.3 tok/s (62603 completion tokens / 1174.0s)

## Archive

- Island 0: coverage 16.7%, QD score 2.107, unique ancestors 3
- Island 1: coverage 11.1%, QD score 0.798, unique ancestors 2
- Island 2: coverage 13.9%, QD score 2.207, unique ancestors 4
- Island 3: coverage 11.1%, QD score 1.400, unique ancestors 3
- Cells newly claimed this generation: 0

## Quality

- No cells claimed this generation.

## Cost

- Budget: {'generation': 5, 'max_generations': 30, 'tokens_used_total': 1422235, 'max_tokens': 2000000, 'elapsed_s_total': 5221.4, 'generation_wall_s': 1174.0}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

_Nothing claimed this generation._
## Migration

- island 0 -> island 1: cell (1, 1), scalar 0.5133, claimed=True
- island 1 -> island 2: cell (0, 1), scalar 0.5141, claimed=True
- island 2 -> island 3: cell (1, 1), scalar 0.5085, claimed=False
- island 3 -> island 0: cell (0, 1), scalar 0.5160, claimed=True

## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
