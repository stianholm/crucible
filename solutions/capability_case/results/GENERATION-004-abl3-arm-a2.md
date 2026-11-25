# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 69.6%
- Aggregate throughput: 93.0 tok/s (215518 completion tokens / 2317.9s)

## Archive

- Island 0: coverage 25.0%, QD score 5.517, unique ancestors 3
- Island 1: coverage 13.9%, QD score 3.137, unique ancestors 4
- Island 2: coverage 16.7%, QD score 2.944, unique ancestors 3
- Island 3: coverage 19.4%, QD score 4.807, unique ancestors 2
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.5357
- Median scalar of newly-claimed: 0.4797

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 3108396, 'max_tokens': 3000000, 'elapsed_s_total': 10902.3, 'generation_wall_s': 2317.9}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (2, 5), scalar 0.4236

parent `e28837a5ad9b01fe` -> candidate `5dcfe32dcff53244`

```diff
--- parent e28837a5ad9b01fe
+++ candidate 5dcfe32dcff53244
@@ -1,22 +1,24 @@
-You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway.
+You are evaluating a capability case that proposes eliminating per‑action human approval for an industrial operational‑change gateway.
 
-**Task** – Choose exactly one verdict: **sound**, **needs‑more‑evidence**, or **rejected**, and provide a short justification.
+**Task** – Select exactly one verdict: **sound**, **needs‑more‑evidence**, or **rejected**, then give a brief bullet‑point justification.
 
-**Evaluation checklist** (derived from Section 8 – Strategy C and the anti‑patterns in Section 9 of the IT/OT‑boundary‑as‑architecture whitepaper):
+**Checklist (derived from Section 8 – Strategy C and Section 9 anti‑patterns):**
 
-1. **Real‑world validation** – Does the submission include end‑to‑end pilots or tests on representative hardware/software that show reliable operation under normal and edge‑case conditions?
-2. **Failure‑mode & risk analysis** – Is there a documented list of plausible failures, their safety/security impact, and concrete mitigation or containment measures?
-3. **Auditability & traceability** – Is an immutable log or provenance record provided that captures inputs, decisions, and outcomes for post‑incident review?
-4. **Human‑baseline comparison** – Are the automated decisions benchmarked against expert human judgments, with performance shown to be comparable or superior?
-5. **Anti‑pattern compliance** – Verify that none of the Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, lack of manual override, unbounded autonomy, missing rollback/stop) appear. Any occurrence is a red flag.
+1. **Real‑world validation** – Does the case include end‑to‑end pilots or field tests on representative IT/OT assets showing reliable operation in normal and edge‑case scenarios?
+2. **Failure‑mode & risk analysis** – Are likely failure modes identified, their safety/security impact quantified, and concrete mitigation or containment actions described?
+3. **Auditability / traceability** – Is there an immutable log or provenance record that captures inputs, decisions, and outcomes for post‑incident review?
+4. **Human‑baseline comparison** – Are automated decisions benchmarked against expert human judgments and demonstrated to be at least equivalent in safety and effectiveness?
+5. **Anti‑pattern check** – Verify that none of the Section 9 red‑flags appear (e.g., single point of failure without fallback, opaque decision logic, missing manual override or emergency stop, unbounded autonomy, absent rollback).
 
 **Decision rules**
-- **sound** – All five checklist items are satisfied, no anti‑pattern is found, and the evidence is comprehensive.
-- **needs‑more‑evidence** – One or more items are only partially addressed or missing, but no anti‑pattern red flag is present.
-- **rejected** – Any anti‑pattern is detected, or a critical safety/security risk is left unmitigated.
+
+- **sound** – All five items are fully satisfied and no anti‑pattern is present.
+- **needs‑more‑evidence** – One or more of items 1‑4 are partially addressed or missing, **but** no anti‑pattern is found.
+- **rejected** – Any anti‑pattern is detected **or** a critical safety/security risk is left unmitigated.
 
 **Output format**
-1. Write the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`) on the first line.
-2. On the following lines, give a concise bullet‑point rationale (each bullet starts with “-”) that references the checklist items satisfied, those that are lacking, and any anti‑pattern detected.
 
-Proceed to read the submission, apply the checklist, and produce your verdict and reasoning.+1. First line: the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`).  
+2. Subsequent lines: concise bullet points (each starting with “-”) explaining which checklist items are met, which are lacking, and any anti‑pattern encountered.
+
+Produce only the verdict line and the bullet‑point rationale; no extra headings or text. Proceed to assess the submission.
```

### Island 2, cell (0, 5), scalar 0.5357

parent `26c1dfc147a82325` -> candidate `4adc70ae2ca7a789`

```diff
--- parent 26c1dfc147a82325
+++ candidate 4adc70ae2ca7a789
@@ -1,26 +1,25 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Decide, based on **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Use Section 8 (Strategy C – capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper to decide one of: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-### Required checklist
-All items must be satisfied for a **sound** verdict. Missing or partial evidence leads to **needs‑more‑evidence** unless a deal‑breaker is present, which forces **rejected**.
+### Checklist (all must be satisfied for a **sound** verdict)
 
-1. **Empirical validation** – Real‑world or production‑like end‑to‑end testing (including edge‑cases and failure‑injection) is provided.
-2. **Risk analysis** – Documented identification of failure modes, their likelihood/impact, and concrete mitigation measures.
-3. **Auditability** – Tamper‑evident logging or provenance metadata that can be inspected after the action.
-4. **Human‑parity comparison** – Quantitative or qualitative evidence that the autonomous decision matches or exceeds human operator performance.
-5. **Compliance & safety** – All relevant regulatory, safety, and IT/OT governance requirements are addressed.
-6. **Anti‑pattern check (Section 9)** – The proposal must contain **none** of the listed anti‑patterns (e.g., reliance on black‑box models without verification, no fallback human control, insufficient monitoring, etc.). Presence of any anti‑pattern is an automatic **rejected**.
+A. **Empirical validation** – End‑to‑end, production‑like testing (including edge cases and fault‑injection) is documented.  
+B. **Risk analysis** – Failure modes, their likelihood/impact, and concrete mitigation measures are identified.  
+C. **Auditability** – Tamper‑evident logs or provenance metadata that can be inspected after the action.  
+D. **Human‑parity evidence** – Quantitative or qualitative proof that the autonomous decision matches or exceeds human operator performance.  
+E. **Compliance & safety** – All relevant regulatory, safety, and IT/OT governance requirements are addressed.  
+F. **Anti‑pattern scan (Section 9)** – The proposal must contain **none** of the listed anti‑patterns (e.g., reliance on unverifiable black‑box models, no fallback human control, insufficient monitoring). Presence of any anti‑pattern triggers an automatic **rejected** verdict.
 
-### Decision rubric
-- **sound** – Every checklist item 1‑6 is fully satisfied; no anti‑patterns detected.
-- **needs‑more‑evidence** – One or more items 1‑5 are partially addressed or missing; no anti‑patterns present.
-- **rejected** – Any anti‑pattern from item 6 is found, or a critical safety/compliance violation is evident.
+### Decision rules
+1. If any anti‑pattern (F) is present, or a critical safety/compliance violation is evident → **rejected**.  
+2. Otherwise, if any of A‑E is missing or only partially addressed → **needs‑more‑evidence**.  
+3. Only when A‑E are fully satisfied and no anti‑patterns are found → **sound**.
 
-### Output format
-Respond **exactly** with two lines, no extra characters or whitespace:
+### Output
+Respond **exactly** with two lines, no extra spaces or characters:
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation that cites the relevant checklist items>
+Reasoning: <concise explanation that cites the relevant checklist items, e.g., “missing A, partial D”>
 ```
 
-Base your reasoning on the specific evidence (or lack thereof) in the submission; do not invent information. If an item is absent, state that explicitly. +Do not fabricate information; cite only evidence that appears in the submitted case.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.120 vs base 0.482, 9.7 sigma below
- Lesson 19: **kept** — precision 0.986 >= base 0.881
- Lesson 17: **kept** — precision 0.986 >= base 0.694
- Lesson 11: **kept** — precision 0.750 vs base 0.927, only 0.8 sigma below

## Held-out check (best-ever candidate)

- Candidate: `83782c894ce5ad68` (rotation scalar 0.8562)
- Held-out quality: 0.6779 (passes: 0.6666, 0.6891)
- Held-out scalar: 0.5749 (passes: 0.5645, 0.5853)
- All held-out tasks valid: True
