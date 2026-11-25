# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 69.8%
- Aggregate throughput: 71.0 tok/s (213683 completion tokens / 3010.6s)

## Archive

- Island 0: coverage 19.4%, QD score 4.490, unique ancestors 3
- Island 1: coverage 13.9%, QD score 3.137, unique ancestors 4
- Island 2: coverage 13.9%, QD score 2.413, unique ancestors 3
- Island 3: coverage 16.7%, QD score 4.270, unique ancestors 2
- Cells newly claimed this generation: 10

## Quality

- Best scalar this generation: 0.8562
- Median scalar of newly-claimed: 0.6704

## Cost

- Budget: {'generation': 2, 'max_generations': 30, 'tokens_used_total': 1860718, 'max_tokens': 3000000, 'elapsed_s_total': 6094.6, 'generation_wall_s': 3010.6}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 3), scalar 0.5112

parent `e2f7fad89a65d996` -> candidate `1482ad2d1b027597`

```diff
--- parent e2f7fad89a65d996
+++ candidate 1482ad2d1b027597
@@ -1,29 +1,24 @@
-You are reviewing a capability case that proposes to remove per‑action human approval for an operational‑change gateway in an industrial environment. Evaluate the submission against the criteria from **Section 8 (Strategy C – capability‑based opening)** and check for any of the anti‑patterns flagged in **Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper.
+You are assessing a capability case that seeks to eliminate per‑action human approval for an operational‑change gateway in an industrial setting. Use the criteria from **Section 8 (Strategy C – capability‑based opening)** and verify that none of the anti‑patterns listed in **Section 9** appear.
 
-**Assessment checklist**
+**Evaluation items**
 
-1. **Real‑world validation** – Does the proposal include controlled trials, pilots, or field tests that show safe operation under realistic conditions?  
-2. **Comprehensive risk analysis** – Are failure modes identified, quantified, and paired with mitigation or containment measures?  
-3. **Auditability** – Is there a verifiable, tamper‑evident log or trace that can reconstruct the automated decision after the fact?  
-4. **Human‑decision equivalence** – Are results compared to qualified human operators (quantitatively or qualitatively) to demonstrate equal or better performance?  
-5. **Anti‑pattern compliance (Section 9)** – Confirm that none of the following appear:
-   - single‑model dependency without fallback,
-   - lack of explainability for critical choices,
-   - insufficient IT/OT boundary enforcement,
-   - missing rollback or emergency‑stop capability,
-   - unvalidated stability assumptions under load or fault.
+1. **Real‑world validation** – evidence of pilots, field trials, or controlled tests showing safe operation under realistic conditions.  
+2. **Failure‑mode & risk analysis** – identified failure modes, quantitative risk assessment, and concrete mitigation or containment measures.  
+3. **Auditability** – presence of an immutable, tamper‑evident log that can reconstruct the automated decision after the fact.  
+4. **Human‑baseline comparison** – quantitative or qualitative benchmarking against qualified human operators demonstrating equal or superior performance.  
+5. **Anti‑pattern check** – ensure the submission does **not** contain any of the Section 9 anti‑patterns (e.g., single‑model dependency without fallback, opaque decision logic, missing manual override or emergency stop, inadequate IT/OT boundary enforcement, unvalidated stability under load/fault).
 
-**Decision logic**
+**Decision rules**
 
-- **sound** – every checklist item (1‑4) is fully satisfied **and** no anti‑pattern (5) is present.  
-- **needs-more-evidence** – one or more items 1‑4 are incomplete or weak, but no anti‑pattern from 5 is detected.  
-- **rejected** – any anti‑pattern from item 5 is found **or** a critical safety risk is evident.
+- **sound** – items 1‑4 are fully satisfied **and** item 5 shows no anti‑pattern.  
+- **needs‑more‑evidence** – one or more of items 1‑4 are missing or weak, but item 5 reveals no anti‑pattern.  
+- **rejected** – any anti‑pattern from item 5 is present **or** a critical safety risk is evident.
 
 **Output format**
 
-Your response must contain **exactly** two lines:
+Produce exactly two lines:
 
-1. `Verdict:` followed by `sound`, `needs-more-evidence`, or `rejected`.  
-2. `Reasoning:` a short explanation that cites the specific checklist numbers or anti‑patterns that drove your decision (e.g., “Missing real‑world validation (1) and no audit log (3).”).
+1. `Verdict:` followed by `sound`, `needs‑more‑evidence`, or `rejected`.  
+2. `Reasoning:` a brief explanation that cites the relevant item numbers or anti‑patterns (e.g., “Missing real‑world validation (1) and no audit log (3).”).
 
-Do not include any other headings, bullet points, or formatting.+Do not add any other text, headings, or formatting.
```

### Island 0, cell (0, 4), scalar 0.6511

parent `13b6b5d67fa92774` -> candidate `e072035acac0ac86`

```diff
--- parent 13b6b5d67fa92774
+++ candidate e072035acac0ac86
@@ -1,29 +1,29 @@
-You are assessing a capability case that requests the removal of per‑action human approval for an industrial operational‑change gateway action. Follow the evaluation criteria defined in **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Evaluate the submission against the requirements in **Section 8 (Strategy C – capability‑based opening)** and verify that none of the anti‑patterns from **Section 9** are present.
 
-**Evaluation checklist**
+**Checklist**
 
-1. **Evidence of real‑world testing** – Has the team performed controlled trials or pilot deployments that demonstrate the system behaves safely under realistic conditions?
-2. **Risk analysis** – Is there a thorough identification of potential failure modes, including worst‑case scenarios, and mitigation strategies for each?
-3. **Auditability** – Does the proposal provide a verifiable audit trail (logs, immutable records, or similar) that can reconstruct decisions after the fact?
-4. **Human‑decision comparison** – Are there quantitative or qualitative comparisons showing that the automated decisions align with or exceed human operator judgments?
-5. **Compliance with anti‑patterns (Section 9)** – Verify that none of the following red‑flags are present:
-   - **Over‑reliance on a single AI model** without fallback mechanisms.
-   - **Lack of explainability** for critical decisions.
-   - **Insufficient boundary enforcement** between IT and OT domains.
-   - **Absence of a clear rollback or emergency‑stop procedure**.
-   - **Unvalidated assumptions about system stability** under load or fault conditions.
+1. **Real‑world validation** – Does the proposal include controlled pilots or field trials that prove safe behavior under realistic conditions?  
+2. **Failure‑mode & risk analysis** – Are possible failure modes identified, quantified, and paired with concrete mitigation or containment measures?  
+3. **Audit trail** – Is there a tamper‑evident log or immutable record that can reconstruct every automated decision after execution?  
+4. **Human‑baseline comparison** – Are the automated decisions compared (quantitatively or qualitatively) with qualified human operators and shown to be at least equivalent?  
+5. **Anti‑pattern check (Section 9)** – Confirm that the submission does **not** contain any of the following red flags:  
+   - reliance on a single AI model without fallback,  
+   - lack of explainability for critical choices,  
+   - inadequate segregation between IT and OT boundaries,  
+   - missing rollback or emergency‑stop capability,  
+   - unverified stability assumptions under load or fault conditions.
 
-**Decision rules**
+**Decision logic**
 
-- If **all** checklist items are satisfied and no anti‑pattern is detected, classify the case as **sound**.
-- If one or more checklist items are inadequately addressed **but** no severe anti‑pattern is present, classify as **needs-more-evidence**.
-- If any anti‑pattern from Section 9 is identified, or if a critical safety risk is evident, classify as **rejected**.
+- **sound** – items 1‑4 are fully satisfied **and** no anti‑pattern from item 5 is found.  
+- **needs-more-evidence** – one or more of items 1‑4 are weak or missing, but item 5 shows no violation.  
+- **rejected** – any anti‑pattern from item 5 is present **or** a clear critical safety risk is evident.
 
-**Output requirement**
+**Output format**
 
-Provide **exactly** two sections in your response:
+Your answer must consist of exactly two lines:
 
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`.
-2. **Reasoning:** a concise explanation referencing the specific checklist items or anti‑patterns that led to your verdict.
+1. `Verdict:` followed by `sound`, `needs-more-evidence`, or `rejected`.  
+2. `Reasoning:` a brief justification that cites the checklist numbers or specific anti‑patterns that drove the decision (e.g., “Missing real‑world validation (1) and no audit trail (3).”).
 
-Do not add any other text, headings, or formatting beyond these two sections.+Do not add any other text, headings, or formatting.
```

### Island 0, cell (0, 5), scalar 0.6511

parent `13b6b5d67fa92774` -> candidate `1b4e2b36e95b2e0b`

```diff
--- parent 13b6b5d67fa92774
+++ candidate 1b4e2b36e95b2e0b
@@ -1,29 +1,26 @@
-You are assessing a capability case that requests the removal of per‑action human approval for an industrial operational‑change gateway action. Follow the evaluation criteria defined in **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to evaluate a capability case that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Apply the criteria from **Section 8 (Strategy C – capability‑based opening)** and verify that none of the anti‑patterns listed in **Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper appear.
 
-**Evaluation checklist**
+### Checklist
+1. **Real‑world validation** – Does the submission include controlled pilots, field trials, or other evidence that the system operates safely under realistic conditions?
+2. **Risk & failure‑mode analysis** – Are all plausible failure modes identified, quantified, and paired with concrete mitigation or containment measures?
+3. **Auditability** – Is there a tamper‑evident log, immutable record, or equivalent mechanism that can reconstruct each automated decision after the fact?
+4. **Human‑baseline comparison** – Are results presented that show the automated decisions are at least equal to, or better than, qualified human operator judgments (quantitative or qualitative)?
+5. **Anti‑pattern check (Section 9)** – Confirm that none of the following are present:
+   - Single‑model dependency without a fallback.
+   - Lack of explainability for safety‑critical decisions.
+   - Inadequate enforcement of the IT/OT boundary.
+   - Missing rollback or emergency‑stop capability.
+   - Unvalidated assumptions about system stability under load or fault conditions.
 
-1. **Evidence of real‑world testing** – Has the team performed controlled trials or pilot deployments that demonstrate the system behaves safely under realistic conditions?
-2. **Risk analysis** – Is there a thorough identification of potential failure modes, including worst‑case scenarios, and mitigation strategies for each?
-3. **Auditability** – Does the proposal provide a verifiable audit trail (logs, immutable records, or similar) that can reconstruct decisions after the fact?
-4. **Human‑decision comparison** – Are there quantitative or qualitative comparisons showing that the automated decisions align with or exceed human operator judgments?
-5. **Compliance with anti‑patterns (Section 9)** – Verify that none of the following red‑flags are present:
-   - **Over‑reliance on a single AI model** without fallback mechanisms.
-   - **Lack of explainability** for critical decisions.
-   - **Insufficient boundary enforcement** between IT and OT domains.
-   - **Absence of a clear rollback or emergency‑stop procedure**.
-   - **Unvalidated assumptions about system stability** under load or fault conditions.
+### Decision logic
+- **sound** – All items 1‑4 are fully satisfied **and** no anti‑pattern from item 5 is found.
+- **needs-more-evidence** – One or more of items 1‑4 are insufficient or missing, **but** no anti‑pattern from item 5 is detected.
+- **rejected** – Any anti‑pattern from item 5 is present **or** a critical safety risk is evident.
 
-**Decision rules**
+### Output format
+Return **exactly** two lines:
 
-- If **all** checklist items are satisfied and no anti‑pattern is detected, classify the case as **sound**.
-- If one or more checklist items are inadequately addressed **but** no severe anti‑pattern is present, classify as **needs-more-evidence**.
-- If any anti‑pattern from Section 9 is identified, or if a critical safety risk is evident, classify as **rejected**.
+1. `Verdict:` followed by `sound`, `needs-more-evidence`, or `rejected`.
+2. `Reasoning:` a brief statement that cites the specific checklist numbers or anti‑patterns that drove your decision (e.g., “Missing real‑world validation (1) and no audit log (3).”).
 
-**Output requirement**
-
-Provide **exactly** two sections in your response:
-
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`.
-2. **Reasoning:** a concise explanation referencing the specific checklist items or anti‑patterns that led to your verdict.
-
-Do not add any other text, headings, or formatting beyond these two sections.+Do not include any other text, headings, bullet points, or whitespace.
```

### Island 1, cell (1, 5), scalar 0.8562

parent `6ff124042c54272f` -> candidate `83782c894ce5ad68`

```diff
--- parent 6ff124042c54272f
+++ candidate 83782c894ce5ad68
@@ -1,26 +1,25 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Decide whether the case is **SOUND**, **NEEDS‑MORE‑EVIDENCE**, or **REJECTED** according to Section 8 (Strategy C) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are the reviewer for a capability case that proposes to eliminate per‑action human approval on an industrial operational‑change gateway. Judge the case using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Checklist (evaluate each item)
+### Evaluation checklist
+Assess the submission against each of the following criteria. Mark each as **Met**, **Partial**, or **Missing**.
 
-1. **Real‑world validation** – Does the submission include end‑to‑end tests in a production‑like setting, with documented results and success metrics?
-2. **Failure‑mode & mitigation** – Are potential failure modes identified (e.g., FMEA) and concrete mitigation or containment steps described for each high‑impact mode?
-3. **Auditability** – Is there an immutable, tamper‑evident log that records every automated decision, its inputs, and can be queried for post‑incident review?
-4. **Human‑baseline comparison** – Is there quantitative evidence that the automated decisions match or exceed a qualified human’s decisions (accuracy, false‑positive/false‑negative rates, etc.)?
-5. **Anti‑pattern compliance (Section 9)** – Confirm that none of the following appear:
+1. **Production‑like validation** – End‑to‑end tests performed in a realistic environment, with documented outcomes and success/failure metrics.  
+2. **Failure‑mode analysis** – Identification of plausible failure modes (e.g., FMEA) together with concrete mitigation or containment actions for each high‑impact mode.  
+3. **Tamper‑evident audit trail** – An immutable log that records every automated decision, its inputs, and that can be queried for post‑incident review.  
+4. **Human baseline comparison** – Quantitative evidence that the automated decisions meet or exceed the performance of a qualified human (accuracy, false‑positive/false‑negative rates, etc.).  
+5. **Anti‑pattern screening (Sec 9)** – Verify that none of the following appear unmitigated:
    - Single point of failure without redundancy  
-   - Black‑box decision making without explainability  
-   - Unbounded escalation beyond the declared scope  
-   - No mechanism to instantly re‑enable human approval (revocation)
+   - Opaque “black‑box” decision making lacking explainability  
+   - Unlimited escalation beyond the defined scope  
+   - Absence of an instant re‑enablement path for human approval  
 
-### Decision rules
+### Decision logic
+* **SOUND** – All items 1‑4 are **Met** and no anti‑pattern from item 5 is present.  
+* **NEEDS‑MORE‑EVIDENCE** – One or more of items 1‑4 are **Partial** or **Missing**, but no anti‑pattern is detected.  
+* **REJECTED** – Any anti‑pattern in item 5 is found, or a critical safety violation is evident.
 
-- **SOUND** – All five checklist items are fully satisfied and no anti‑pattern is present.
-- **NEEDS‑MORE‑EVIDENCE** – One or more of items 1‑4 are missing or only partially addressed, but no anti‑pattern is triggered.
-- **REJECTED** – Any anti‑pattern from item 5 is found, or the evidence directly violates safety requirements.
+### Required response
+1. Output a single word verdict: `SOUND`, `NEEDS-MORE-EVIDENCE`, or `REJECTED`.  
+2. On the next line, provide a brief rationale (1‑3 sentences) that cites the specific checklist items influencing the verdict.
 
-### Required output
-
-1. Write the verdict **exactly** as one of the three words: `SOUND`, `NEEDS-MORE-EVIDENCE`, or `REJECTED`.  
-2. Follow it with a short rationale (1‑3 sentences) that cites the checklist items influencing the decision.
-
-Make your judgment solely from the information provided in the submission; do not assume unavailable data. +Base your judgment solely on the information supplied in the submission; do not infer missing data. 
```

### Island 1, cell (0, 5), scalar 0.8539

parent `aacf87a86802d5e4` -> candidate `ba3b66a97bff67af`

```diff
--- parent aacf87a86802d5e4
+++ candidate ba3b66a97bff67af
@@ -1,30 +1,31 @@
-You are evaluating a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action. Apply the rubric below, which follows Section 8 (Strategy C, capability‑based opening) and the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Judge the case using the criteria from Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Possible verdicts** – output **exactly one** of these words:  
-- **SOUND**  
-- **NEEDS‑MORE‑EVIDENCE**  
-- **REJECTED**
+**Verdicts (choose one, uppercase, on a line by itself)**  
+- SOUND  
+- NEEDS-MORE-EVIDENCE  
+- REJECTED  
 
-**Rubric**
+**Evaluation checklist**
 
-1. **Real‑world testing** – evidence of end‑to‑end, production‑like trials with documented results (success/failure rates).  
-2. **Failure‑mode analysis** – systematic identification of failure modes and defined mitigations for each high‑impact mode.  
-3. **Auditability** – tamper‑evident audit trail that records every automated decision and its input data, and can be queried for post‑incident review.  
-4. **Human‑baseline comparison** – quantitative or qualitative comparison of the automated decisions to those of a qualified human, with performance metrics meeting the thresholds in Section 8.  
-5. **Anti‑pattern compliance (Section 9)** – the proposal must **not** contain any of the following:
+1. **Real‑world testing** – Does the submission include end‑to‑end, production‑like trials with documented success/failure metrics?  
+2. **Failure‑mode analysis** – Are high‑impact failure modes identified and paired with concrete mitigation or containment actions?  
+3. **Auditability** – Is there an immutable, tamper‑evident log that records every automated decision, its inputs, and can be queried after an incident?  
+4. **Human‑baseline comparison** – Is there quantitative (or well‑justified qualitative) evidence that the automated decisions meet or exceed the performance of a qualified human, per the thresholds in Section 8?  
+5. **Anti‑pattern screening (Section 9)** – Verify that none of the following appear:
    - Single point of failure without redundancy  
    - Black‑box decision making lacking explainability  
-   - Unbounded escalation beyond declared scope  
-   - Absence of an immediate revocation/override mechanism  
+   - Unbounded escalation beyond the declared scope  
+   - No instant revocation/override mechanism for human approval  
 
-**Decision logic**
+**Decision rules**
 
-- **REJECTED** – if any anti‑pattern in criterion 5 is present, or if the submission directly contradicts safety requirements.  
-- **SOUND** – if criteria 1‑4 are fully satisfied **and** no anti‑pattern is present.  
-- **NEEDS‑MORE‑EVIDENCE** – if at least one of criteria 1‑4 is missing or only partially addressed, while no anti‑pattern is detected.
+- **REJECTED** – any anti‑pattern from item 5 is present, or the case directly contradicts mandatory safety requirements.  
+- **SOUND** – items 1‑4 are all fully satisfied **and** no anti‑pattern is found.  
+- **NEEDS-MORE-EVIDENCE** – no anti‑pattern is detected, but at least one of items 1‑4 is missing, incomplete, or only partially addressed.
 
-**Output format**  
-1. The verdict word on its own line.  
-2. A concise rationale (1‑3 sentences) that cites the specific criterion(ia) that led to the decision.
+**Output required**
 
-Follow this structure exactly; do not add extra headings or formatting.  +1. The verdict word on the first line.  
+2. A brief rationale (1‑3 sentences) that cites the specific checklist item(s) that determined the verdict.
+
+Do not add headings, bullet symbols, or any other text beyond the two lines described.  
```

### Island 2, cell (0, 5), scalar 0.4993

parent `26c1dfc147a82325` -> candidate `7242a86bb996497d`

```diff
--- parent 26c1dfc147a82325
+++ candidate 7242a86bb996497d
@@ -1,26 +1,25 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Decide, based on **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Use **Section 8 (Strategy C – capability‑based opening)** and the **anti‑patterns listed in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper to reach a single verdict: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-### Required checklist
-All items must be satisfied for a **sound** verdict. Missing or partial evidence leads to **needs‑more‑evidence** unless a deal‑breaker is present, which forces **rejected**.
+### Checklist (must be referenced by number in your reasoning)
 
-1. **Empirical validation** – Real‑world or production‑like end‑to‑end testing (including edge‑cases and failure‑injection) is provided.
-2. **Risk analysis** – Documented identification of failure modes, their likelihood/impact, and concrete mitigation measures.
-3. **Auditability** – Tamper‑evident logging or provenance metadata that can be inspected after the action.
-4. **Human‑parity comparison** – Quantitative or qualitative evidence that the autonomous decision matches or exceeds human operator performance.
-5. **Compliance & safety** – All relevant regulatory, safety, and IT/OT governance requirements are addressed.
-6. **Anti‑pattern check (Section 9)** – The proposal must contain **none** of the listed anti‑patterns (e.g., reliance on black‑box models without verification, no fallback human control, insufficient monitoring, etc.). Presence of any anti‑pattern is an automatic **rejected**.
+1. **Empirical validation** – Demonstrated end‑to‑end testing in a production‑like setting, covering normal operation, edge cases, and failure‑injection.
+2. **Risk analysis** – Identified failure modes with likelihood/impact assessments and concrete mitigation actions.
+3. **Auditability** – Tamper‑evident logs or provenance metadata that enable post‑action review.
+4. **Human‑parity evidence** – Quantitative or qualitative comparison showing the autonomous decision meets or exceeds human operator performance.
+5. **Compliance & safety** – All applicable regulatory, safety, and IT/OT governance requirements are satisfied.
+6. **Anti‑pattern check (Section 9)** – The proposal must contain **no** anti‑patterns (e.g., black‑box model without verification, missing fallback human control, inadequate monitoring, etc.). Presence of any anti‑pattern forces a **rejected** verdict.
 
-### Decision rubric
-- **sound** – Every checklist item 1‑6 is fully satisfied; no anti‑patterns detected.
-- **needs‑more‑evidence** – One or more items 1‑5 are partially addressed or missing; no anti‑patterns present.
-- **rejected** – Any anti‑pattern from item 6 is found, or a critical safety/compliance violation is evident.
+### Decision rules
+- **sound** – Items 1‑5 are fully satisfied *and* item 6 shows no anti‑patterns.
+- **needs‑more‑evidence** – One or more of items 1‑5 are missing or only partially addressed, *and* no anti‑patterns are found.
+- **rejected** – Any anti‑pattern (item 6) is present **or** a critical safety/compliance breach (item 5) is evident.
 
-### Output format
-Respond **exactly** with two lines, no extra characters or whitespace:
+### Output
+Respond with **exactly two lines**, no extra whitespace or characters:
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation that cites the relevant checklist items>
+Reasoning: <concise explanation citing the relevant checklist item numbers, e.g., “Item 2 missing; Item 6 anti‑pattern detected.”>
 ```
 
-Base your reasoning on the specific evidence (or lack thereof) in the submission; do not invent information. If an item is absent, state that explicitly. +Do not fabricate evidence; if a required item is absent, state that explicitly. Cite the numbered items that drive your decision.
```

### Island 2, cell (1, 3), scalar 0.3629

parent `26c1dfc147a82325` -> candidate `d8df47f7c6033d29`

```diff
--- parent 26c1dfc147a82325
+++ candidate d8df47f7c6033d29
@@ -1,26 +1,20 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Decide, based on **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are assessing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using Section 8 (Strategy C) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide one of: sound, needs‑more‑evidence, or rejected.
 
-### Required checklist
-All items must be satisfied for a **sound** verdict. Missing or partial evidence leads to **needs‑more‑evidence** unless a deal‑breaker is present, which forces **rejected**.
+Checklist (all must be satisfied for “sound”):
+A. Empirical validation – end‑to‑end, production‑like testing including edge cases and fault injection.  
+B. Risk analysis – identified failure modes, their likelihood/impact, and concrete mitigation measures.  
+C. Auditability – tamper‑evident logs or provenance metadata that can be inspected after the action.  
+D. Human‑parity comparison – evidence that the autonomous decision matches or exceeds human operator performance.  
+E. Compliance & safety – all relevant regulatory, safety, and IT/OT governance requirements are addressed.  
+F. Anti‑pattern scan – the proposal must contain **none** of the Section 9 anti‑patterns (e.g., black‑box models without verification, no fallback human control, insufficient monitoring). Presence of any anti‑pattern = automatic **rejected**.
 
-1. **Empirical validation** – Real‑world or production‑like end‑to‑end testing (including edge‑cases and failure‑injection) is provided.
-2. **Risk analysis** – Documented identification of failure modes, their likelihood/impact, and concrete mitigation measures.
-3. **Auditability** – Tamper‑evident logging or provenance metadata that can be inspected after the action.
-4. **Human‑parity comparison** – Quantitative or qualitative evidence that the autonomous decision matches or exceeds human operator performance.
-5. **Compliance & safety** – All relevant regulatory, safety, and IT/OT governance requirements are addressed.
-6. **Anti‑pattern check (Section 9)** – The proposal must contain **none** of the listed anti‑patterns (e.g., reliance on black‑box models without verification, no fallback human control, insufficient monitoring, etc.). Presence of any anti‑pattern is an automatic **rejected**.
+Decision procedure  
+1. If any anti‑pattern (F) is found → Verdict = rejected.  
+2. Else if any of A‑E is missing or only partially addressed → Verdict = needs‑more‑evidence.  
+3. Else → Verdict = sound.
 
-### Decision rubric
-- **sound** – Every checklist item 1‑6 is fully satisfied; no anti‑patterns detected.
-- **needs‑more‑evidence** – One or more items 1‑5 are partially addressed or missing; no anti‑patterns present.
-- **rejected** – Any anti‑pattern from item 6 is found, or a critical safety/compliance violation is evident.
+Output  
+Return exactly two lines, no extra spaces or characters:
 
-### Output format
-Respond **exactly** with two lines, no extra characters or whitespace:
-
-```
-Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation that cites the relevant checklist items>
-```
-
-Base your reasoning on the specific evidence (or lack thereof) in the submission; do not invent information. If an item is absent, state that explicitly. +Verdict: <sound|needs-more-evidence|rejected>  
+Reasoning: <concise explanation that cites the relevant checklist items>
```

### Island 3, cell (1, 2), scalar 0.6897

parent `c313e9d0ff74bcb1` -> candidate `84788fcf82fadc3d`

```diff
--- parent c313e9d0ff74bcb1
+++ candidate 84788fcf82fadc3d
@@ -1,22 +1,19 @@
-You are to assess a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. After reviewing the submission, produce **exactly two lines** in the order shown below:
+You will evaluate a capability case that proposes removing the per‑action human‑approval step for an industrial operational‑change gateway. Check the submission against the five criteria from Sections 8 & 9 of the whitepaper:
+
+1. Real‑world validation – pilots or high‑fidelity field tests in realistic conditions.  
+2. Failure‑mode & mitigation – identified failure scenarios with concrete fallback or safety‑net measures.  
+3. Auditability – tamper‑evident log recording decision, timestamp, and responsible entity.  
+4. Human‑baseline comparison – quantitative benchmark versus qualified operators showing equal or superior safety/performance.  
+5. Anti‑pattern compliance – no disallowed patterns from Section 9 (e.g., black‑box‑only decisions, lack of manual override, unbounded autonomy, single point of failure).
+
+Decision rules:
+- **rejected** – any of criteria 1‑4 is missing/insufficient **or** any anti‑pattern (criterion 5) is present.  
+- **needs-more-evidence** – all five criteria are addressed but one or more of criteria 1‑4 lack concrete data or depth, with no anti‑pattern.  
+- **sound** – all five criteria are fully satisfied with convincing evidence and no anti‑pattern.
+
+Produce **exactly two lines**, in this order, with no extra text:
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <2‑4 concise sentences citing the relevant criteria>
-```
-
-**Criteria you must check (all refer to Sections 8 and 9 of the whitepaper):**
-
-1. **Real‑world validation** – presence of controlled pilots or field tests showing the agent works under realistic conditions.  
-2. **Failure‑mode & mitigation** – identification of plausible failure scenarios together with fallback or safety‑net measures.  
-3. **Auditability** – a tamper‑evident log that records decisions, timestamps, and responsible entities for post‑incident review.  
-4. **Human‑baseline comparison** – quantitative benchmarking of the agent against expert operators, demonstrating equal or superior safety/performance.  
-5. **Anti‑pattern compliance** – the proposal must not exhibit any disallowed patterns from Section 9 (e.g., black‑box‑only decisions, lack of manual override, unbounded autonomy, single point of failure).
-
-**Decision rules**
-
-- **sound** – every criterion is satisfied to a degree that a reasonable reviewer would deem the risk acceptable.  
-- **needs-more-evidence** – one or more criteria are addressed but lack concrete data, depth, or a complete audit mechanism; no anti‑pattern is triggered.  
-- **rejected** – any criterion is missing or contradictory, or the proposal directly violates an anti‑pattern.
-
-Do **not** add headings, bullet points, or any text beyond the two required lines. Keep the reasoning brief and reference the criteria by name.+Reasoning: <2‑4 concise sentences that cite the relevant criteria by number or name>
+```
```

### Island 3, cell (1, 1), scalar 0.7312

parent `fcfc38989740cd24` -> candidate `2e326351963745dd`

```diff
--- parent fcfc38989740cd24
+++ candidate 2e326351963745dd
@@ -1,22 +1,20 @@
-You are evaluating a capability case that proposes relaxing per‑action human approval for an industrial operational‑change gateway action, following the guidance of Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to judge a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway, in accordance with Section 8 (Strategy C) and the anti‑patterns of Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-Assess the submission against **all** of the following criteria:
+**Mandatory criteria (all must be considered):**
+1. **Real‑world / high‑fidelity testing** – documented experiments, scenario coverage, and results.
+2. **Failure‑mode & risk analysis** – identified failure modes, quantitative risk assessment, and mitigations or fallback procedures.
+3. **Audit‑trail & traceability** – tamper‑evident logging capable of reconstructing every automated decision.
+4. **Human‑baseline comparison** – quantitative benchmark of the agent against qualified human operators, with clear metrics and explanation of any gaps.
+5. **Anti‑pattern compliance** – the proposal must not exhibit any Section 9 anti‑patterns (e.g., single point of failure, unbounded autonomy, opaque logic, missing rollback, lack of manual override).
 
-1. **Empirical Validation** – Has the team performed real‑world or high‑fidelity testing? Are test scenarios, coverage, and results documented?
-2. **Risk & Failure‑Mode Analysis** – Are potential failure modes identified, quantified, and mitigated? Is the impact on safety, security, and continuity evaluated?
-3. **Audit Trail & Traceability** – Does the proposal provide a complete, tamper‑evident log that can reconstruct every automated decision?
-4. **Human‑Equivalence Comparison** – Are the agent’s decisions compared to qualified human decisions using clear metrics or thresholds? Are performance gaps explained?
-5. **Anti‑Pattern Compliance** – Verify that none of the Section 9 anti‑patterns (e.g., single point of failure, unbounded autonomy, opaque decision logic, inadequate rollback, etc.) are present or unaddressed.
+**Decision rules**
+- **sound** – every criterion is fully satisfied and no anti‑pattern is present.
+- **needs-more-evidence** – one or more criteria are partially addressed or lack sufficient data, but no anti‑pattern is triggered.
+- **rejected** – any anti‑pattern is present or the risk assessment shows an unacceptable level of danger.
 
-**Decision mapping**
-
-- **sound** – All five criteria are satisfactorily met and no anti‑pattern is triggered.
-- **needs-more-evidence** – One or more criteria are weak or missing, but no fatal anti‑pattern is identified.
-- **rejected** – Any anti‑pattern is present or the evidence shows an unacceptable level of risk.
-
-**Output format (do not deviate)**  
+**Output (exactly two lines, no extra text)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <your concise justification referencing the criteria above>
+Reasoning: <concise justification that cites the relevant criteria>
 ```
-Provide the verdict first, then a brief, logical explanation that cites the specific criteria influencing your decision.+First write the verdict line, then a brief (1‑3 sentence) justification referencing the specific criteria that drove your decision.
```

### Island 3, cell (1, 3), scalar 0.7273

parent `c313e9d0ff74bcb1` -> candidate `a166e8387873db5c`

```diff
--- parent c313e9d0ff74bcb1
+++ candidate a166e8387873db5c
@@ -1,22 +1,22 @@
-You are to assess a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. After reviewing the submission, produce **exactly two lines** in the order shown below:
+You are to evaluate a capability case that proposes removing the per‑action human‑approval step for an industrial operational‑change gateway. After reviewing the submission, output **exactly two lines** in this order:
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <2‑4 concise sentences citing the relevant criteria>
+Reasoning: <2‑4 concise sentences that cite the relevant criteria by name>
 ```
 
-**Criteria you must check (all refer to Sections 8 and 9 of the whitepaper):**
+**Evaluation criteria (all derived from Sections 8 and 9 of the whitepaper):**
 
-1. **Real‑world validation** – presence of controlled pilots or field tests showing the agent works under realistic conditions.  
-2. **Failure‑mode & mitigation** – identification of plausible failure scenarios together with fallback or safety‑net measures.  
-3. **Auditability** – a tamper‑evident log that records decisions, timestamps, and responsible entities for post‑incident review.  
-4. **Human‑baseline comparison** – quantitative benchmarking of the agent against expert operators, demonstrating equal or superior safety/performance.  
-5. **Anti‑pattern compliance** – the proposal must not exhibit any disallowed patterns from Section 9 (e.g., black‑box‑only decisions, lack of manual override, unbounded autonomy, single point of failure).
+1. **Real‑world validation** – evidence of pilots or field tests under realistic conditions.  
+2. **Failure‑mode & mitigation** – identification of plausible failures together with concrete fallback or safety‑net measures.  
+3. **Auditability** – a tamper‑evident log capturing decisions, timestamps, and responsible entities for post‑incident review.  
+4. **Human‑baseline comparison** – quantitative benchmarking against expert operators showing equal or better safety/performance.  
+5. **Anti‑pattern compliance** – absence of any disallowed patterns from Section 9 (e.g., black‑box‑only decisions, lack of manual override, unbounded autonomy, single point of failure).
 
-**Decision rules**
+**Decision mapping**
 
-- **sound** – every criterion is satisfied to a degree that a reasonable reviewer would deem the risk acceptable.  
-- **needs-more-evidence** – one or more criteria are addressed but lack concrete data, depth, or a complete audit mechanism; no anti‑pattern is triggered.  
-- **rejected** – any criterion is missing or contradictory, or the proposal directly violates an anti‑pattern.
+- **sound** – every criterion is met to a degree that a reasonable reviewer would consider the risk acceptable.  
+- **needs-more-evidence** – one or more criteria are addressed but lack sufficient data, depth, or a complete audit mechanism; no anti‑pattern is triggered.  
+- **rejected** – any criterion is missing, contradictory, or an anti‑pattern is present.
 
-Do **not** add headings, bullet points, or any text beyond the two required lines. Keep the reasoning brief and reference the criteria by name.+Do not include headings, bullet points, or any additional text in the output; only the two required lines. Reference the criteria by the names given above in your reasoning. 
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.120 vs base 0.482, 9.7 sigma below
- Lesson 19: **kept** — precision 0.986 >= base 0.881
- Lesson 17: **kept** — precision 0.986 >= base 0.694
- Lesson 11: **kept** — precision 0.750 vs base 0.927, only 0.8 sigma below
