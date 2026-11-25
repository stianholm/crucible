# Generation 9 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 61.2%
- Aggregate throughput: 100.6 tok/s (224923 completion tokens / 2236.1s)

## Archive

- Island 0: coverage 25.0%, QD score 5.141, unique ancestors 3
- Island 1: coverage 30.6%, QD score 5.674, unique ancestors 6
- Island 2: coverage 30.6%, QD score 5.690, unique ancestors 6
- Island 3: coverage 33.3%, QD score 6.637, unique ancestors 4
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.8473
- Median scalar of newly-claimed: 0.7375

## Cost

- Budget: {'generation': 9, 'max_generations': 10, 'tokens_used_total': 6184513, 'max_tokens': 8000000, 'elapsed_s_total': 25828.8, 'generation_wall_s': 2236.1}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 2), scalar 0.6278

parent `da0bb0773709f7f9` -> candidate `97df1f0ae3dbbc6b`

```diff
--- parent da0bb0773709f7f9
+++ candidate 97df1f0ae3dbbc6b
@@ -1,23 +1,23 @@
-You are an expert reviewer assessing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action, in accordance with Section 8 (Strategy C, capability‑based opening) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a proposal to drop per‑action human approval for an industrial operational‑change gateway, as described in Section 8 (Strategy C) and measured against the anti‑patterns of Section 9 in the IT/OT‑boundary‑as‑architecture whitepaper.
 
-**Evidence required for a “sound” verdict (all must be satisfied):**
-1. Real‑world testing – documented controlled trials or production‑like simulations with scope, environment, and results.  
-2. Failure‑mode analysis – identified plausible failures together with mitigations or safe‑fallbacks.  
-3. Audit‑trail / observability – reliable recording of inputs, decisions, and outcomes.  
-4. Human‑parity benchmark – quantitative or qualitative evidence that automation matches or exceeds human operators.
+**Evidence that must be fully present for a “sound” decision**
+- **Real‑world test** – controlled trial or production‑like simulation with documented scope, environment, and outcomes.  
+- **Failure‑mode analysis** – identified plausible failures together with mitigations or safe fall‑backs.  
+- **Audit/observability** – reliable logging of inputs, decisions, and results that enables post‑hoc review.  
+- **Human‑parity data** – quantitative or qualitative proof that the automated action is at least as safe/effective as a qualified human.
 
-**Anti‑patterns (any one triggers “rejected”):**
-- Over‑automation without a clear rollback or manual override.  
-- No bounded safety case or fail‑safe.  
+**Disqualifying anti‑patterns (any one ⇒ “rejected”)**
+- Automation without a clear manual rollback or override.  
+- No bounded safety case or fail‑safe mechanism.  
 - Opaque/black‑box AI lacking explainability.  
-- Missing monitoring or alerts for out‑of‑spec behavior.  
-- Inadequate segregation of duties or conflict‑of‑interest hazards.
+- Absence of monitoring or alerts for out‑of‑spec behavior.  
+- Inadequate segregation of duties or conflict‑of‑interest risk.
 
-**Decision rules**
-- **sound** – all four evidence items are fully satisfied **and** no anti‑pattern is present.  
-- **needs‑more‑evidence** – one or more evidence items are missing or only partially addressed, **and** no anti‑pattern is present.  
-- **rejected** – any anti‑pattern is identified, or a fatal safety/security gap (e.g., no fail‑safe, no audit trail) exists.
+**Decision hierarchy**
+1. If any anti‑pattern is found → **rejected**.  
+2. Else if every evidence item above is satisfied → **sound**.  
+3. Else → **needs‑more‑evidence**.
 
-**Output** – Respond with exactly two lines, no extra text or formatting:  
+**Output (exactly two lines, no extra text)**
 1. `Verdict: <sound|needs-more-evidence|rejected>`  
-2. `Reasoning: <concise justification referencing the specific evidence items or anti‑patterns that drove your decision>`+2. `Reasoning: <brief justification citing the specific evidence item(s) or anti‑pattern(s) that determined the verdict>`
```

### Island 1, cell (0, 5), scalar 0.8473

parent `ef22049c50aaac35` -> candidate `c32a461e812cfa25`

```diff
--- parent ef22049c50aaac35
+++ candidate c32a461e812cfa25
@@ -1,33 +1,26 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway. After reviewing the submitted material, select **exactly one** verdict from the three defined in the white‑paper (Section 8):
+You are to judge a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway. Use the white‑paper criteria below.
 
-- **sound**
-- **needs-more-evidence**
-- **rejected**
+**Verdicts (choose exactly one):** sound, needs-more-evidence, rejected.
 
-### Required evidence for a **sound** verdict  
-All four items must be **clearly documented and sufficient**:
+**Evidence required for a sound verdict (all four must be present and sufficient):**  
+A. Operational testing – pilots, simulations, or field trials that prove safe autonomous execution.  
+B. Failure‑mode analysis – identified failure scenarios with concrete mitigations or fallback procedures.  
+C. Auditable record – immutable, tamper‑evident logs or provenance data capturing inputs, decision logic, and outcomes for each execution.  
+D. Human‑performance benchmark – quantitative (or well‑justified qualitative) comparison showing the automation meets or exceeds a qualified human’s performance under identical conditions.
 
-1. **Operational testing** – results from pilots, simulations, or field trials that demonstrate safe autonomous execution.  
-2. **Failure‑mode & mitigation** – identified failure scenarios together with concrete mitigation or fallback procedures.  
-3. **Auditable record** – immutable, tamper‑evident logs or provenance data capturing inputs, decision logic, and outcomes for each execution.  
-4. **Human‑performance benchmark** – quantitative (or well‑justified qualitative) comparison showing the automation meets or exceeds a qualified human’s performance under identical conditions.
+**Anti‑patterns that force a rejected verdict (any one triggers rejection, per Section 9):**  
+1. Black‑box logic with no observability or diagnostics.  
+2. Claim of “zero risk” because the action is rare.  
+3. Deployment of an untested AI in a safety‑critical role.  
+4. Absence of a manual override or rapid rollback capability.  
+5. Any other anti‑pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Anti‑patterns that force a **rejected** verdict  
-If any of the following is present, the case is automatically **rejected** (Section 9):
+**Decision hierarchy:**  
+1. If any anti‑pattern (1‑5) is detected → **rejected**.  
+2. Otherwise, if any evidence item (A‑D) is missing, incomplete, or vague → **needs-more-evidence**.  
+3. Otherwise → **sound**.
 
-- Black‑box logic with no observability or diagnostics.  
-- Claim of “zero risk” because the action is rare.  
-- Deployment of an untested AI in a safety‑critical role.  
-- Absence of a manual override or rapid rollback capability.  
-- Any other anti‑pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
-
-### Decision hierarchy  
-1. **Reject** if any anti‑pattern is detected.  
-2. Otherwise, **needs-more-evidence** if any required evidence item is missing, incomplete, or vague.  
-3. Otherwise, **sound**.
-
-### Output format (must be obeyed exactly)  
-- **Line 1:** the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
-- **Line 2:** a concise rationale (1–2 sentences) that references the specific evidence items or anti‑patterns influencing the decision. No extra lines, headings, or prose.
-
+**Output (exactly two lines, no extra whitespace):**  
+Line 1: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+Line 2: a concise rationale (1–2 sentences) naming the specific anti‑pattern or evidence item(s) that determined the verdict.
 Proceed with the evaluation.
```


## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 15 | 15 | 15 | 0.5683 | 0.0% | 2139 |
| `proposer-distilled@/adapters/20261017` | 16 | 16 | 16 | 0.6002 | 12.5% | 2119 |

Paired difference, distilled minus stock, over 15 complete pairs: mean +0.0301 (sd 0.1297, se 0.0335), **+0.90 sigma**, p 0.384; distilled ahead in 8, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 160 | 153 | 153 | 0.4731 | 31.4% | 2164 |
| `proposer-distilled@/adapters/20261017` | 160 | 158 | 158 | 0.4793 | 27.2% | 2128 |

Paired difference, distilled minus stock, over 150 complete pairs: mean +0.0054 (sd 0.1803, se 0.0147), **+0.37 sigma**, p 0.712; distilled ahead in 74, tied in 0.

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
| 9 | 0.555 | 0.556 | 1.00 |

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below

## Held-out check (best-ever candidate)

- Candidate: `0e857b2c169f75f4` (rotation scalar 0.8616)
- Held-out quality: 0.5521 (passes: 0.5492, 0.5551)
- Held-out scalar: 0.4413 (passes: 0.4385, 0.4441)
- All held-out tasks valid: True
