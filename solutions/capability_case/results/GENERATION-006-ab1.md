# Generation 6 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 27
- Prefix cache hit rate: 60.7%
- Aggregate throughput: 97.2 tok/s (222745 completion tokens / 2292.4s)

## Archive

- Island 0: coverage 25.0%, QD score 4.970, unique ancestors 4
- Island 1: coverage 30.6%, QD score 5.502, unique ancestors 7
- Island 2: coverage 30.6%, QD score 5.690, unique ancestors 6
- Island 3: coverage 33.3%, QD score 6.637, unique ancestors 4
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.8479
- Median scalar of newly-claimed: 0.6977

## Cost

- Budget: {'generation': 6, 'max_generations': 10, 'tokens_used_total': 4311230, 'max_tokens': 8000000, 'elapsed_s_total': 17673.2, 'generation_wall_s': 2292.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 3), scalar 0.8479

parent `da0bb0773709f7f9` -> candidate `a2a3249e08f32e4b`

```diff
--- parent da0bb0773709f7f9
+++ candidate a2a3249e08f32e4b
@@ -1,23 +1,31 @@
-You are an expert reviewer assessing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action, in accordance with Section 8 (Strategy C, capability‑based opening) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Your assessment must follow Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evidence required for a “sound” verdict (all must be satisfied):**
-1. Real‑world testing – documented controlled trials or production‑like simulations with scope, environment, and results.  
-2. Failure‑mode analysis – identified plausible failures together with mitigations or safe‑fallbacks.  
-3. Audit‑trail / observability – reliable recording of inputs, decisions, and outcomes.  
-4. Human‑parity benchmark – quantitative or qualitative evidence that automation matches or exceeds human operators.
+### Evidence that must be fully satisfied for a **sound** verdict
+| # | Evidence | What counts as satisfied |
+|---|----------|--------------------------|
+| 1 | **Real‑world testing** | Controlled trials or production‑like simulations are documented, include scope, environment, fault‑injection, and clear results showing safe operation. |
+| 2 | **Failure‑mode analysis** | All plausible failure modes are identified together with mitigation measures or safe‑fallback procedures. |
+| 3 | **Audit‑trail / observability** | Tamper‑evident logging records inputs, decisions, and outcomes; the logs are accessible for post‑hoc review. |
+| 4 | **Human‑parity benchmark** | Quantitative or qualitative comparison demonstrates the automation matches or exceeds the performance of qualified human operators. |
 
-**Anti‑patterns (any one triggers “rejected”):**
-- Over‑automation without a clear rollback or manual override.  
-- No bounded safety case or fail‑safe.  
-- Opaque/black‑box AI lacking explainability.  
-- Missing monitoring or alerts for out‑of‑spec behavior.  
-- Inadequate segregation of duties or conflict‑of‑interest hazards.
+All four rows must be **completely met** for a “sound” decision.
 
-**Decision rules**
-- **sound** – all four evidence items are fully satisfied **and** no anti‑pattern is present.  
+### Anti‑patterns (any one forces a **rejected** verdict)
+- No manual rollback or operator override.  
+- Absence of a bounded safety case or fail‑safe mechanism.  
+- Opaque/black‑box AI without explainability.  
+- No monitoring, alerts, or anomaly detection for out‑of‑spec behaviour.  
+- Violation of segregation of duties or conflict‑of‑interest hazards.
+
+### Decision logic
+- **sound** – every evidence item (1‑4) is fully satisfied **and** no anti‑pattern is present.  
 - **needs‑more‑evidence** – one or more evidence items are missing or only partially addressed, **and** no anti‑pattern is present.  
-- **rejected** – any anti‑pattern is identified, or a fatal safety/security gap (e.g., no fail‑safe, no audit trail) exists.
+- **rejected** – any anti‑pattern is identified, or a critical safety/security gap (e.g., missing audit‑trail) exists, regardless of the other evidence.
 
-**Output** – Respond with exactly two lines, no extra text or formatting:  
+### Output format
+Respond with **exactly two lines**, no extra text, no markdown:
+
 1. `Verdict: <sound|needs-more-evidence|rejected>`  
-2. `Reasoning: <concise justification referencing the specific evidence items or anti‑patterns that drove your decision>`+2. `Reasoning: <brief justification naming the specific evidence items missing/partial or the anti‑pattern(s) that drove the decision>`
+
+Do not add anything else.
```

### Island 3, cell (2, 5), scalar 0.5474

parent `0856e7f78af25618` -> candidate `dae5b25ab53430e9`

```diff
--- parent 0856e7f78af25618
+++ candidate dae5b25ab53430e9
@@ -1,22 +1,23 @@
-You are an analyst reviewing a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action. Use Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper as your frame of reference.
+You are an analyst tasked with reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your judgment must be based on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-Evaluate the submission against the following criteria:
+**Decision procedure**
 
-1. **Real‑world testing** – Has the team performed functional tests in conditions that reflect actual operation?
-2. **Failure‑mode analysis** – Does the case identify plausible ways the automated decision could go wrong and propose mitigations?
-3. **Audit trail** – Is there a verifiable record of the agent’s decisions and the data used to make them?
-4. **Human‑equivalence comparison** – Are the agent’s actions benchmarked against how a qualified human operator would decide in the same situations?
-5. **Anti‑pattern compliance** – Does the proposal avoid the anti‑patterns from Section 9 (e.g., “no‑fallback”, “hidden‑state”, “unbounded‑automation”, etc.)?
+1. **Anti‑pattern scan (Section 9)** – Look for any of the listed anti‑patterns (e.g., “no‑fallback”, “hidden‑state”, “unbounded‑automation”, “black‑box AI”, “bypassed safety interlock”, etc.).  
+   *If any anti‑pattern is present, the case is **rejected** immediately, regardless of other evidence.*
 
-Based on this assessment, produce a verdict that is **exactly one** of the three allowed categories:
+2. **Evidence checklist (Section 8)** – If no anti‑pattern is found, evaluate the following five criteria:
+   - **Real‑world testing** – functional tests performed in conditions that mimic actual operation.  
+   - **Failure‑mode analysis** – identification of plausible failure modes together with mitigation measures.  
+   - **Audit trail** – a verifiable, tamper‑evident record of the agent’s decisions and the data used.  
+   - **Human‑equivalence comparison** – benchmarking of the agent’s actions against decisions a qualified human operator would make in the same situations.  
+   - **Anti‑pattern compliance** – confirmation that none of the Section 9 anti‑patterns apply (re‑check for completeness).
 
-- **sound** – The evidence collectively satisfies the criteria, and no anti‑pattern is present.
-- **needs-more-evidence** – The case is generally promising but one or more criteria are insufficiently addressed or a minor anti‑pattern is present.
-- **rejected** – A critical anti‑pattern is evident, or essential testing/failure‑mode analysis is missing, making the risk unacceptable.
+   *If all five criteria are satisfied, the verdict is **sound**.*  
+   *If one or more criteria are missing or insufficient, the verdict is **needs-more-evidence**.*
 
-**Output format:**  
-1. First line: the chosen verdict word (sound, needs-more-evidence, or rejected).  
-2. One blank line.  
-3. One or more sentences explaining the reasoning, explicitly referencing any criteria that led to your decision.
+**Output format (strict)**  
+1. First line: the verdict word in lower‑case exactly as one of: `sound`, `needs-more-evidence`, `rejected`.  
+2. Second line: a completely blank line.  
+3. Third line and onward: one or more sentences that explain the decision, explicitly naming any criteria that were missing or any anti‑pattern that caused a rejection.
 
-Do not include any additional text, headings, or symbols.+Do **not** add headings, bullet points, or any other text outside this structure.
```


## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 15 | 15 | 15 | 0.5898 | 13.3% | 2200 |
| `proposer-distilled@/adapters/20261017` | 16 | 16 | 16 | 0.5690 | 0.0% | 2205 |

Paired difference, distilled minus stock, over 15 complete pairs: mean -0.0309 (sd 0.1732, se 0.0447), **-0.69 sigma**, p 0.501; distilled ahead in 6, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 112 | 108 | 108 | 0.4722 | 43.5% | 2125 |
| `proposer-distilled@/adapters/20261017` | 112 | 110 | 110 | 0.4753 | 37.3% | 2095 |

Paired difference, distilled minus stock, over 105 complete pairs: mean +0.0025 (sd 0.1837, se 0.0179), **+0.14 sigma**, p 0.889; distilled ahead in 53, tied in 0.

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

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
