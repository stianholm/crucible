# Generation 8 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 61.2%
- Aggregate throughput: 76.5 tok/s (222531 completion tokens / 2909.8s)

## Archive

- Island 0: coverage 25.0%, QD score 4.970, unique ancestors 4
- Island 1: coverage 30.6%, QD score 5.567, unique ancestors 7
- Island 2: coverage 30.6%, QD score 5.690, unique ancestors 6
- Island 3: coverage 33.3%, QD score 6.637, unique ancestors 4
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.6173
- Median scalar of newly-claimed: 0.6173

## Cost

- Budget: {'generation': 8, 'max_generations': 10, 'tokens_used_total': 5570356, 'max_tokens': 8000000, 'elapsed_s_total': 23592.6, 'generation_wall_s': 2909.8}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (0, 4), scalar 0.6173

parent `e4c8d08a60d3e84b` -> candidate `3553ac16c71f9c5b`

```diff
--- parent e4c8d08a60d3e84b
+++ candidate 3553ac16c71f9c5b
@@ -1,23 +1,22 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Decide on a single verdict **Sound**, **Needs More Evidence**, or **Rejected** based on the checklist below.
+You are evaluating a capability case that proposes to eliminate per‑action human approval for an industrial operational‑change gateway. Use the checklist below and the decision hierarchy to produce a verdict.
 
 **Checklist**
 
-1. **Real‑world testing** – have functional, integration and stress tests been run in an environment that mirrors production?
-2. **Failure‑mode analysis** – are plausible failure scenarios identified, their impacts evaluated, and mitigations defined?
-3. **Auditability** – does the design provide a tamper‑evident, reconstructable log of every automated decision and any overrides?
-4. **Human‑baseline comparison** – is there quantitative evidence that the automated decisions match or exceed those of a qualified human operator?
-5. **Anti‑pattern compliance (Section 9)** – does the proposal avoid all listed anti‑patterns (e.g., single‑point automation failure, unbounded escalation, opaque logic, no fallback)?
-6. **Rollback / manual intervention** – are rapid rollback or manual‑intervention mechanisms specified, tested, and ready to deploy?
+1. **Real‑world testing** – Are functional, integration and stress tests performed in a production‑like environment?
+2. **Failure‑mode analysis** – Are plausible failure scenarios identified, their impact assessed, and mitigations defined?
+3. **Auditability** – Does the design provide a tamper‑evident, reconstructable log of every automated decision and any overrides?
+4. **Human‑baseline comparison** – Is there quantitative evidence that the automated decisions meet or exceed those of a qualified human operator?
+5. **Anti‑pattern compliance (Section 9)** – Does the proposal avoid all listed anti‑patterns (e.g., single‑point automation failure, unbounded escalation, opaque logic, no fallback)?
+6. **Rollback / manual intervention** – Are rapid rollback or manual‑intervention mechanisms specified, tested, and ready to deploy?
 
-**Decision rules**
+**Decision hierarchy**
 
-- If any item in (5) is violated, output **Rejected**.
-- Else if any of items (1)–(4) or (6) are missing, insufficient, or only partially addressed, output **Needs More Evidence**.
-- Else output **Sound**.
+- If any item in (5) is violated, the verdict is **Rejected**.
+- Otherwise, if any of items (1)–(4) or (6) is missing, insufficient, or only partially addressed, the verdict is **Needs More Evidence**.
+- Only when every item is fully satisfied is the verdict **Sound**.
 
-**Output**
+**Output (exactly two lines)**  
+1. The verdict word: **Sound**, **Needs More Evidence**, or **Rejected**.  
+2. A brief rationale naming the decisive checklist item number(s) (e.g., “Item 5 – anti‑pattern violation”).
 
-- First line: the verdict word exactly **Sound**, **Needs More Evidence**, or **Rejected**.
-- Second line: one‑to‑two sentence rationale naming the most decisive checklist item(s) that led to your verdict.
-
-Provide only these two lines, no extra headings or commentary. +Provide only these two lines, with no extra headings, whitespace, or commentary. 
```


## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 15 | 15 | 15 | 0.5223 | 6.7% | 2344 |
| `proposer-distilled@/adapters/20261017` | 16 | 16 | 16 | 0.4819 | 0.0% | 2291 |

Paired difference, distilled minus stock, over 15 complete pairs: mean -0.0356 (sd 0.2072, se 0.0535), **-0.66 sigma**, p 0.517; distilled ahead in 5, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 144 | 138 | 138 | 0.4628 | 34.8% | 2166 |
| `proposer-distilled@/adapters/20261017` | 144 | 142 | 142 | 0.4654 | 28.9% | 2129 |

Paired difference, distilled minus stock, over 135 complete pairs: mean +0.0027 (sd 0.1852, se 0.0159), **+0.17 sigma**, p 0.866; distilled ahead in 66, tied in 0.

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
| 8 | 0.545 | 0.583 | 1.07 |

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
