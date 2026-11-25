# Generation 7 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 27.5
- Prefix cache hit rate: 61.0%
- Aggregate throughput: 82.2 tok/s (247309 completion tokens / 3009.3s)

## Archive

- Island 0: coverage 25.0%, QD score 4.970, unique ancestors 4
- Island 1: coverage 30.6%, QD score 5.502, unique ancestors 7
- Island 2: coverage 30.6%, QD score 5.690, unique ancestors 6
- Island 3: coverage 33.3%, QD score 6.637, unique ancestors 4
- Cells newly claimed this generation: 0

## Quality

- No cells claimed this generation.

## Cost

- Budget: {'generation': 7, 'max_generations': 10, 'tokens_used_total': 4946369, 'max_tokens': 8000000, 'elapsed_s_total': 20682.7, 'generation_wall_s': 3009.3}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

_Nothing claimed this generation._

## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 15 | 15 | 15 | 0.3353 | 0.0% | 2290 |
| `proposer-distilled@/adapters/20261017` | 16 | 16 | 16 | 0.3820 | 0.0% | 2202 |

Paired difference, distilled minus stock, over 15 complete pairs: mean +0.0422 (sd 0.1770, se 0.0457), **+0.92 sigma**, p 0.371; distilled ahead in 8, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 128 | 123 | 123 | 0.4555 | 38.2% | 2145 |
| `proposer-distilled@/adapters/20261017` | 128 | 126 | 126 | 0.4633 | 32.5% | 2109 |

Paired difference, distilled minus stock, over 120 complete pairs: mean +0.0075 (sd 0.1827, se 0.0167), **+0.45 sigma**, p 0.654; distilled ahead in 61, tied in 0.

## Proposal diversity (mean pairwise TF-IDF cosine distance)

| Generation | Stock | Distilled | Distilled / stock |
|---|---|---|---|
| 0 | 0.505 | 0.507 | 1.00 |
| 1 | 0.539 | 0.557 | 1.03 |
| 2 | 0.586 | 0.608 | 1.04 |
| 3 | 0.561 | 0.589 | 1.05 |
| 4 | 0.598 | 0.617 | 1.03 |
| 5 | 0.568 | 0.591 | 1.04 |
| 6 | 0.552 | 0.562 | 1.02 |
| 7 | 0.601 | 0.548 | 0.91 |

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
