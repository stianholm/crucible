# Generation 7 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 30
- Prefix cache hit rate: 55.4%
- Aggregate throughput: 114.2 tok/s (187645 completion tokens / 1642.8s)

## Archive

- Island 0: coverage 25.0%, QD score 5.593, unique ancestors 5
- Island 1: coverage 11.1%, QD score 2.667, unique ancestors 3
- Island 2: coverage 11.1%, QD score 3.199, unique ancestors 4
- Island 3: coverage 8.3%, QD score 2.260, unique ancestors 2
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.8422
- Median scalar of newly-claimed: 0.7342

## Cost

- Budget: {'generation': 7, 'max_generations': 10, 'tokens_used_total': 4859553, 'max_tokens': 5000000, 'elapsed_s_total': 15802.8, 'generation_wall_s': 1642.8}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 4), scalar 0.7342

parent `5e9075c63c8db2f6` -> candidate `8ad105c705af0885`

```diff
--- parent 5e9075c63c8db2f6
+++ candidate 8ad105c705af0885
@@ -1,24 +1,20 @@
-You are reviewing a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway action. Evaluate the submission against the criteria below and assign one of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper (Section 8, Strategy C) and its anti‑patterns (Section 9).
+You are reviewing a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway action. Assess the submission against the numbered criteria below and output the required verdict.
 
-### Evaluation criteria (must be addressed in the submission)
+**Criteria (must be evaluated)**  
+1. **Real‑world testing** – pilots, field trials, or high‑fidelity simulation with quantitative results.  
+2. **Failure‑mode analysis** – identified plausible failures, their likelihood, and concrete mitigation or fallback.  
+3. **Audit & accountability** – immutable logging of decisions, timestamps, rationales, and a defined review process.  
+4. **Human‑decision benchmark** – quantitative comparison showing the system meets or exceeds qualified human performance.  
+5. **Anti‑pattern scan** – the case must contain none of the Section 9 anti‑patterns (automation bias, black‑box opacity, single‑point failure, unbounded authority, or similar fatal flaws).
 
-1. **Real‑world testing** – Controlled pilots, field trials, or high‑fidelity simulations with quantitative results.  
-2. **Failure‑mode analysis** – Identification of plausible failures, their likelihood, and concrete mitigation or fallback strategies.  
-3. **Audit & accountability** – Immutable logging of decisions, timestamps, rationales, and a defined review process.  
-4. **Human‑decision benchmark** – Comparative data (e.g., confusion matrix, error‑rate) showing the system meets or exceeds expert human performance.  
-5. **Anti‑pattern compliance** – No occurrence of the Section 9 anti‑patterns: automation bias, black‑box opacity, single‑point failure, unbounded authority, or any similar fatal flaw.
+**Decision hierarchy**  
+- If any anti‑pattern from criterion 5 is present → **Verdict: rejected**.  
+- Else if criteria 1‑4 are all satisfactorily addressed → **Verdict: sound**.  
+- Otherwise (no anti‑patterns but one or more of 1‑4 are missing or inadequate) → **Verdict: needs‑more‑evidence**.
 
-### Decision rules
-
-- **Rejected** – Any anti‑pattern from criterion 5 is present.  
-- **Sound** – All five criteria (1‑4) are sufficiently satisfied **and** no anti‑pattern is detected.  
-- **Needs‑more‑evidence** – No anti‑pattern is found, but one or more of criteria 1‑4 are incomplete or insufficient.
-
-### Output format (exactly two lines)
-
+**Output (exactly two lines)**  
 ```
-Verdict: <sound|needs‑more‑evidence|rejected>
-Reasoning: <concise justification that cites the numbered criteria (e.g., “fails criterion 2; no mitigation plan”)>
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <brief justification citing the relevant criterion numbers, e.g., “fails criterion 2; no mitigation plan”>
 ```
-
-Provide the verdict first, then a brief reason referencing the specific criteria that led to your decision. Do not add any other text or formatting. +Provide only these two lines, no extra text or formatting.
```

### Island 0, cell (0, 5), scalar 0.7300

parent `5e9075c63c8db2f6` -> candidate `d78344abddb5fce6`

```diff
--- parent 5e9075c63c8db2f6
+++ candidate d78344abddb5fce6
@@ -1,24 +1,22 @@
-You are reviewing a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway action. Evaluate the submission against the criteria below and assign one of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper (Section 8, Strategy C) and its anti‑patterns (Section 9).
+You are tasked with assessing a proposal that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Using the evidence supplied (accessible elsewhere), judge the case according to the white‑paper sections 8 (Strategy C) and 9 (anti‑patterns). Address each of the following numbered points in your reasoning:
 
-### Evaluation criteria (must be addressed in the submission)
+1. **Real‑world validation** – Evidence of pilots, field tests, or high‑fidelity simulations with measurable outcomes.  
+2. **Failure‑mode treatment** – Clear list of possible failure modes, their probabilities, and concrete mitigation or fallback measures.  
+3. **Auditability** – Immutable logs capturing decisions, timestamps, rationales, and a defined review/override process.  
+4. **Human‑performance baseline** – Quantitative comparison (e.g., error rates, confusion matrices) showing the automated action meets or exceeds qualified human operators.  
+5. **Anti‑pattern check** – Confirmation that none of the Section 9 anti‑patterns appear (automation bias, opaque black‑box, single point of failure, unbounded authority, etc.).
 
-1. **Real‑world testing** – Controlled pilots, field trials, or high‑fidelity simulations with quantitative results.  
-2. **Failure‑mode analysis** – Identification of plausible failures, their likelihood, and concrete mitigation or fallback strategies.  
-3. **Audit & accountability** – Immutable logging of decisions, timestamps, rationales, and a defined review process.  
-4. **Human‑decision benchmark** – Comparative data (e.g., confusion matrix, error‑rate) showing the system meets or exceeds expert human performance.  
-5. **Anti‑pattern compliance** – No occurrence of the Section 9 anti‑patterns: automation bias, black‑box opacity, single‑point failure, unbounded authority, or any similar fatal flaw.
+**Decision matrix**
 
-### Decision rules
+- **Rejected** – any anti‑pattern is identified (failure of point 5).  
+- **Sound** – points 1‑4 are each adequately satisfied **and** point 5 is clean.  
+- **Needs‑more‑evidence** – no anti‑pattern (point 5 passes) but one or more of points 1‑4 are missing, incomplete, or insufficient.
 
-- **Rejected** – Any anti‑pattern from criterion 5 is present.  
-- **Sound** – All five criteria (1‑4) are sufficiently satisfied **and** no anti‑pattern is detected.  
-- **Needs‑more‑evidence** – No anti‑pattern is found, but one or more of criteria 1‑4 are incomplete or insufficient.
-
-### Output format (exactly two lines)
+**Required output (exactly two lines, no extra text)**
 
 ```
 Verdict: <sound|needs‑more‑evidence|rejected>
-Reasoning: <concise justification that cites the numbered criteria (e.g., “fails criterion 2; no mitigation plan”)>
+Reasoning: <brief justification citing the relevant numbered points, e.g., “fails point 2; mitigation absent”>
 ```
 
-Provide the verdict first, then a brief reason referencing the specific criteria that led to your decision. Do not add any other text or formatting. +State the verdict first, then a concise reason that references the numbered criteria responsible for the decision. Do not add any other wording or formatting.
```

### Island 2, cell (3, 5), scalar 0.8422

parent `8246b7606f7b20bf` -> candidate `87053b0190fc1cb8`

```diff
--- parent 8246b7606f7b20bf
+++ candidate 87053b0190fc1cb8
@@ -1,23 +1,24 @@
-You are reviewing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Choose **exactly one** of the following verdicts:
+You are evaluating a capability case that proposes waiving per‑action human approval for an industrial operational‑change gateway. Choose **exactly one** verdict:
 
-* **sound**
-* **needs-more-evidence**
-* **rejected**
+- **sound**
+- **needs-more-evidence**
+- **rejected**
 
-### Checklist (must be addressed in order, one bullet per item)
+Assess the submission against the following checklist **in order**, providing one bullet point for each item (state explicitly if the evidence is missing or insufficient).
 
-1. **Real‑world testing** – Are controlled pilots or simulations that reflect production conditions provided, with clear metrics and results?  
-2. **Failure‑mode analysis** – Does the submission list plausible failure scenarios (e.g., sensor fault, network loss, worst‑case decision) and describe mitigation or containment measures?  
-3. **Auditability** – Is there a reliable, immutable audit trail (logs, provenance data) that would allow reconstruction of decisions after execution?  
-4. **Human‑decision benchmark** – Is there quantitative or qualitative evidence comparing the autonomous action to that of a qualified human operator, showing comparable or better safety/performance?  
-5. **Anti‑pattern check (Section 9)** – Confirm that none of the listed anti‑patterns appear (single point of failure without fallback, opaque logic, lack of manual override/rollback, unbounded authority, etc.).
+1. **Real‑world testing** – Are pilots or simulations that mirror production conditions supplied, with clear metrics and results?  
+2. **Failure‑mode analysis** – Does the case list plausible failure scenarios (e.g., sensor fault, network loss) and describe mitigation or containment steps?  
+3. **Auditability** – Is there an immutable audit trail (logs, provenance data) that would let an auditor reconstruct decisions after execution?  
+4. **Human‑benchmark** – Is there quantitative or qualitative evidence that the autonomous action matches or exceeds the performance of a qualified human operator?  
+5. **Anti‑pattern check (Section 9)** – Verify that none of the listed anti‑patterns appear (single point of failure without fallback, opaque/black‑box logic, lack of manual override or rollback, unbounded authority, etc.).
 
-### Decision rules
-* **sound** – Items 1‑4 are fully satisfied and no anti‑pattern from item 5 is present.  
-* **needs-more-evidence** – One or more of items 1‑4 is missing or insufficient, but no anti‑pattern is detected.  
-* **rejected** – Any anti‑pattern from item 5 is present, or the evidence is fundamentally inadequate (e.g., no testing, no audit trail, no failure analysis).
+**Decision rules**
 
-### Required output (exactly this format)
+- **sound** – Items 1‑4 are fully satisfied and no anti‑pattern from item 5 is present.  
+- **needs-more-evidence** – One or more of items 1‑4 is missing or weak, but no anti‑pattern is detected.  
+- **rejected** – Any anti‑pattern from item 5 is present, or essential evidence (testing, audit trail, failure analysis) is fundamentally absent.
+
+**Required output (exactly this format)**
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
@@ -29,4 +30,4 @@
 - <bullet for item 5>
 ```
 
-Provide at least one bullet for each checklist item; if an item is missing or weak, state that explicitly in its bullet. Use plain text only—no extra headings, sections, or commentary. Base the final verdict on the overall balance of the evidence and any red‑flag anti‑patterns.+Provide at least one bullet for each checklist item; if an item is missing or weak, state that explicitly in its bullet. Use only plain text—no extra headings, sections, or commentary. Base the final verdict on the overall balance of the evidence and any red‑flag anti‑patterns.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

## Held-out check (best-ever candidate)

- Candidate: `538eeb22a6cc1ca6` (rotation scalar 0.8545)
- Held-out quality: 0.6875
- Held-out scalar: 0.6056
- All held-out tasks valid: True
