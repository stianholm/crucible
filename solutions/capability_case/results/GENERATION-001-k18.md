# Generation 1 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 64.3%
- Aggregate throughput: 95.3 tok/s (306740 completion tokens / 3220.2s)

## Archive

- Island 0: coverage 16.7%, QD score 4.646, unique ancestors 4
- Island 1: coverage 16.7%, QD score 4.388, unique ancestors 4
- Island 2: coverage 13.9%, QD score 3.344, unique ancestors 3
- Island 3: coverage 13.9%, QD score 4.151, unique ancestors 1
- Cells newly claimed this generation: 17

## Quality

- Best scalar this generation: 0.8590
- Median scalar of newly-claimed: 0.8528

## Cost

- Budget: {'generation': 1, 'max_generations': 10, 'tokens_used_total': 2164229, 'max_tokens': 20000000, 'elapsed_s_total': 6175.4, 'generation_wall_s': 3220.2}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (0, 3), scalar 0.8570

parent `cbccb60b0cb2fc67` -> candidate `294d283cf378cc3f`

```diff
--- parent cbccb60b0cb2fc67
+++ candidate 294d283cf378cc3f
@@ -1,22 +1,30 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the exact criteria below and then give your judgment.
+You are tasked with judging a capability case that seeks to remove per‑action human approval for an operational‑change gateway. Apply the rules below **in order** and then produce the required output.
 
-**Mandatory rejection criteria (Section 9 anti‑patterns).** If **any** of these conditions are present, the case must be **rejected** and you should state the specific anti‑pattern that applies:
-1. The evaluation of the proposed relaxation runs only as a nightly batch job instead of being performed before each action.  
-2. The governance model for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
-3. The case relies on the agent “knowing when to stop” rather than on an independent architectural safeguard.  
-4. One or more of the four required evidence dimensions is completely missing:
-   - Test results of the relaxed workflow.  
-   - Failure‑mode analysis (what could go wrong).  
-   - Audit findings or traceability of decisions.  
-   - Comparison of the agent’s decisions to the human‑approved baseline.
+**Step 1 – Immediate disqualifiers (Section 9 anti‑patterns).**  
+If **any** of the following is true, the case must be **rejected**. State the verdict “reject” and name the offending item.
 
-**If none of the above rejection triggers apply**, evaluate the quality of the presented evidence across the same four dimensions:
+1. The proposed safety evaluation runs only as a nightly batch job rather than right before each action.  
+2. The governance arrangement for the relaxation is left undefined or deferred (“we will govern it later”).  
+3. The design relies on the agent’s intuition (“knows when to stop”) instead of an independent architectural safeguard.  
+4. At least one of the four mandatory evidence categories is completely missing:  
+   - Test results of the relaxed workflow  
+   - Failure‑mode analysis  
+   - Audit findings / decision traceability  
+   - Comparison with the human‑approved baseline  
 
-- **Sound** – All four dimensions are present and the evidence is sufficiently detailed and robust in each area.
-- **Needs‑more‑evidence** – All four dimensions are present, but at least one dimension is thin, superficial, or otherwise lacking depth. The case is not a red‑flag, but additional, stronger evidence is required before approval.
+**Step 2 – Evidence adequacy (only if Step 1 yields no rejection).**  
+All four categories must be present. Evaluate their depth:
 
-**Response format** (the surrounding template will enforce exact formatting):  
-- Begin with the verdict: `sound`, `needs-more-evidence`, or `reject`.  
-- Follow with a concise justification that references the relevant criteria or evidence gaps.
+*Robust evidence* – detailed data, quantitative metrics, thorough analyses, concrete audit logs, or a clear performance comparison.  
+*Thin evidence* – mere mention, vague description, or lack of supporting detail.
 
-Make your judgment based solely on the criteria above.+- If every category contains robust evidence → verdict **sound**.  
+- If every category is present but at least one is thin → verdict **needs‑more‑evidence**.
+
+**Step 3 – Output format (the surrounding template will enforce exact placement).**  
+Produce exactly two lines:
+
+1. The verdict word: `sound`, `needs-more-evidence`, or `reject`.  
+2. A brief justification that cites the relevant step and item(s) (e.g., “reject – missing audit findings” or “needs-more-evidence – test results are thin”).
+
+Make the judgment solely on the criteria above; do not add any extra commentary.
```

### Island 0, cell (0, 4), scalar 0.8557

parent `48aa865b05188b1f` -> candidate `18886ee888c7c2a4`

```diff
--- parent 48aa865b05188b1f
+++ candidate 18886ee888c7c2a4
@@ -1,24 +1,28 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+You are assessing a capability case that proposes to drop per‑action human approval for an operational‑change gateway action.
 
-**Goal:** Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+**Decision process (ITOT‑boundary‑as‑architecture whitepaper, Sec 8 & 9)**  
 
-**Decision rules (from the ITOT‑boundary‑as‑architecture whitepaper):**
+1. **Immediate rejection** – if **any** of the following is true, answer **rejected** and note the trigger(s):
+   - Evaluation runs only as a nightly batch instead of before each action.  
+   - Governance for the relaxation is undefined or deferred (“we will govern it later”).  
+   - The proposal relies on the agent “knowing when to stop” rather than on an independent architectural safeguard.  
+   - One or more of the required evidence dimensions is completely missing:
+     - Test results  
+     - Failure‑mode analysis  
+     - Audit findings  
+     - Comparison with the human‑approved baseline  
 
-1. **Reject outright** if any of the following anti‑patterns is present:
-   - The evaluation runs only as a nightly batch rather than before each action. (Section 9, p.29)
-   - Governance for the relaxation is not defined up front (e.g., “we will govern it later”). (Section 9, p.29)
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard. (Section 9, p.28)
-   - One or more of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline  
-     (Section 9, p.25)
+2. **Evidence presence** – after step 1 passes, verify that **all four** evidence dimensions are present. If any are missing, treat as in step 1 (rejected).
 
-2. **If none of the above rejection criteria apply**, examine the four evidence dimensions:
-   - All four must be present. If any dimension is missing, the case is rejected (as above).
-   - When all four are present, assess the **strength** of the evidence:
-     *If the evidence is overall robust and convincingly demonstrates safety and reliability, classify the case as **sound**.*
-     *If the evidence is present but noticeably thin, incomplete, or only marginally persuasive, classify the case as **needs‑more‑evidence**.*
+3. **Evidence quality** – with all four dimensions present, judge their depth:  
+   - **Substantive** – detailed data, quantitative metrics, thorough analysis, concrete audit logs, clear baseline comparison.  
+   - **Thin** – merely mentioned, vague, lacking supporting data.  
 
-**Output:** Provide your verdict (`sound`, `needs-more-evidence`, or `rejected`) and a concise explanation of why that verdict was chosen, referencing the relevant criteria above. Do not include any other text.+   - If every dimension is substantive → verdict **sound**.  
+   - If at least one dimension is thin (but none are missing) → verdict **needs‑more‑evidence**.
+
+**Output** – supply exactly two items:
+1. The verdict string: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A concise explanation referencing the specific rule or evidence that led to that verdict.
+
+Do not add any other text.
```

### Island 0, cell (0, 4), scalar 0.8561

parent `cbccb60b0cb2fc67` -> candidate `be933b78ecef7759`

```diff
--- parent cbccb60b0cb2fc67
+++ candidate be933b78ecef7759
@@ -1,22 +1,28 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the exact criteria below and then give your judgment.
+You are assessing a capability case that asks to remove the per‑action human approval requirement for an operational‑change gateway. Apply the rules below **in order** and then output your judgment.
 
-**Mandatory rejection criteria (Section 9 anti‑patterns).** If **any** of these conditions are present, the case must be **rejected** and you should state the specific anti‑pattern that applies:
-1. The evaluation of the proposed relaxation runs only as a nightly batch job instead of being performed before each action.  
-2. The governance model for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
-3. The case relies on the agent “knowing when to stop” rather than on an independent architectural safeguard.  
-4. One or more of the four required evidence dimensions is completely missing:
+### 1. Automatic‑rejection rules (Section 9 anti‑patterns)  
+If **any** of the following is true, the case is **rejected**. State the exact rule that triggered the rejection.
+
+1. The safety evaluation is performed only as a nightly batch job, not immediately before each action.  
+2. The governance plan for the relaxation is missing or deferred (“we will govern it later”).  
+3. The proposal depends on the agent “knowing when to stop” instead of an independent architectural safeguard.  
+4. At least one of the four required evidence categories is **completely absent**:  
    - Test results of the relaxed workflow.  
-   - Failure‑mode analysis (what could go wrong).  
-   - Audit findings or traceability of decisions.  
-   - Comparison of the agent’s decisions to the human‑approved baseline.
+   - Failure‑mode analysis.  
+   - Audit findings / decision traceability.  
+   - Comparison with the human‑approved baseline.
 
-**If none of the above rejection triggers apply**, evaluate the quality of the presented evidence across the same four dimensions:
+### 2. Evidence‑quality assessment (only if none of the above applied)  
+All four evidence categories must be present. Evaluate each:
 
-- **Sound** – All four dimensions are present and the evidence is sufficiently detailed and robust in each area.
-- **Needs‑more‑evidence** – All four dimensions are present, but at least one dimension is thin, superficial, or otherwise lacking depth. The case is not a red‑flag, but additional, stronger evidence is required before approval.
+* **Robust evidence** – detailed data, quantitative metrics, thorough analysis, concrete audit logs, or clear performance comparison.  
+* **Thin evidence** – merely mentioned, vague, or lacking supporting detail.
 
-**Response format** (the surrounding template will enforce exact formatting):  
-- Begin with the verdict: `sound`, `needs-more-evidence`, or `reject`.  
-- Follow with a concise justification that references the relevant criteria or evidence gaps.
+* If every category contains robust evidence → verdict **sound**.  
+* If every category is present but one or more are thin → verdict **needs-more-evidence**.
 
-Make your judgment based solely on the criteria above.+### 3. Output format (the surrounding template will enforce exact layout)  
+- Start with the verdict word: `sound`, `needs-more-evidence`, or `reject`.  
+- Follow with a brief justification that cites the rule(s) or evidence dimension(s) responsible for the decision.
+
+Make the decision **solely** on the criteria listed above. No additional commentary is required.  
```

### Island 1, cell (0, 4), scalar 0.8569

parent `1ed694b309e1f8f1` -> candidate `f2c76b6f9eda33f7`

```diff
--- parent 1ed694b309e1f8f1
+++ candidate f2c76b6f9eda33f7
@@ -1,25 +1,25 @@
-You are evaluating a capability case that proposes relaxing per‑action human approval for an operational‑change gateway action.
+You are to assess a capability case that seeks to drop per‑action human approval for an operational‑change gateway.
 
-**Decision criteria**
+**Step 1 – Automatic rejection**  
+If **any** of the following anti‑patterns (Section 9) appears, the case must be **rejected**:
 
-1. **Automatic rejection** – reject the case (output “rejected”) if **any** of the following anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper is present:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).
-   - One or more of the four required evidence dimensions is completely missing:
-     * Test results  
-     * Failure‑mode analysis  
-     * Audit findings  
-     * Comparison against the human‑approved baseline (p. 25).
+- Evaluation is performed only as a nightly batch instead of before each action (p. 29).  
+- Governance for the relaxation is missing or deferred (e.g., “we will govern it later”) (p. 29).  
+- The proposal depends on the agent’s internal knowledge of when to stop rather than on an independent architectural safeguard (p. 28).  
+- One or more of the required evidence dimensions is completely absent (p. 25):
+  * Test results  
+  * Failure‑mode analysis  
+  * Audit findings  
+  * Comparison with the human‑approved baseline  
 
-2. **Evidence presence** – after confirming none of the anti‑patterns apply, verify that **all four** evidence dimensions are present. If any dimension is absent, the case must be rejected as above.
+**Step 2 – Verify evidence completeness**  
+If none of the above anti‑patterns apply, confirm that **all four** evidence dimensions are present. Absence of any dimension triggers the rejection rule from Step 1.
 
-3. **Quality assessment** – when all four dimensions are present, judge the *thickness* of the evidence:
-   - If the evidence is detailed, quantitative, and demonstrates thorough validation, label the case **sound**.
-   - If the evidence is present but thin, superficial, or insufficiently substantiated, label the case **needs‑more‑evidence**.
+**Step 3 – Evaluate evidence quality**  
+When all four dimensions are provided, judge the depth of the evidence:
 
-**Output**
+- **sound** – evidence is detailed, quantitative, and convincingly demonstrates safety and reliability.  
+- **needs‑more‑evidence** – evidence is present but thin, superficial, or insufficiently substantiated.
 
-Provide **exactly** one of the three verdict labels (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief, clear justification explaining which rule(s) led to your decision.
-
-Do not mention the scoring rubric or any other instructions.+**Output**  
+Produce **exactly** one label (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification that cites the rule(s) used to reach the decision. No other text or formatting is allowed.  
```

### Island 1, cell (0, 5), scalar 0.8566

parent `1ed694b309e1f8f1` -> candidate `78345158d50f5166`

```diff
--- parent 1ed694b309e1f8f1
+++ candidate 78345158d50f5166
@@ -1,25 +1,23 @@
-You are evaluating a capability case that proposes relaxing per‑action human approval for an operational‑change gateway action.
+You are to judge a capability case that seeks to drop per‑action human approval for an operational‑change gateway.
 
-**Decision criteria**
+**Decision process**
 
-1. **Automatic rejection** – reject the case (output “rejected”) if **any** of the following anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper is present:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).
-   - One or more of the four required evidence dimensions is completely missing:
-     * Test results  
-     * Failure‑mode analysis  
-     * Audit findings  
-     * Comparison against the human‑approved baseline (p. 25).
+1. **Immediate rejection** – Output **rejected** if the case contains *any* of the following anti‑patterns (Section 9):
+   - Evaluation is performed only as a nightly batch, not before each action (p. 29).
+   - Governance for the relaxation is left undefined or deferred (e.g., “we will govern it later”) (p. 29).
+   - The design relies on the agent’s internal sense of when to stop rather than an independent architectural safeguard (p. 28).
+   - One or more of the required evidence dimensions are **absent**:
+     - Test results  
+     - Failure‑mode analysis  
+     - Audit findings  
+     - Comparison with the human‑approved baseline (p. 25)
 
-2. **Evidence presence** – after confirming none of the anti‑patterns apply, verify that **all four** evidence dimensions are present. If any dimension is absent, the case must be rejected as above.
+2. **Evidence completeness check** – If none of the anti‑patterns above are found, confirm that **all four** evidence dimensions are present. If any are missing, treat it as the same rejection condition and output **rejected**.
 
-3. **Quality assessment** – when all four dimensions are present, judge the *thickness* of the evidence:
-   - If the evidence is detailed, quantitative, and demonstrates thorough validation, label the case **sound**.
-   - If the evidence is present but thin, superficial, or insufficiently substantiated, label the case **needs‑more‑evidence**.
+3. **Evidence quality assessment** – With full evidence present, evaluate its depth:
+   - **sound** – evidence is detailed, quantitative, and demonstrates thorough validation across all dimensions.
+   - **needs‑more‑evidence** – evidence exists but is superficial, sparsely documented, or fails to give confidence in the safety of the relaxation.
 
-**Output**
+**Output requirement**
 
-Provide **exactly** one of the three verdict labels (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief, clear justification explaining which rule(s) led to your decision.
-
-Do not mention the scoring rubric or any other instructions.+Write exactly one of the three labels (`sound`, `needs‑more‑evidence`, `rejected`) followed by a concise justification that cites the rule(s) that led to your verdict. No extra formatting or references to this rubric should appear.
```

### Island 1, cell (1, 3), scalar 0.7940

parent `98861a86fcdb900d` -> candidate `4c277005b7b7efe5`

```diff
--- parent 98861a86fcdb900d
+++ candidate 4c277005b7b7efe5
@@ -1,33 +1,30 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+You are evaluating a capability case that proposes to drop the per‑action human‑approval step for an operational‑change gateway.
 
-**Task:** Read the submitted case and produce a single verdict chosen from the three allowed labels:
-- **sound**
-- **needs‑more‑evidence**
-- **rejected**
+**What to output**  
+Return a single label—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification. The surrounding template will format the response; just include the label and your reasoning.
 
-Along with the label, provide a brief rationale explaining which criteria led to your decision. (The exact output format is defined elsewhere; just include the label and your reasoning.)
+**When to output **rejected** (mandatory rejection criteria, Section 9)**  
+Choose **rejected** if any of the following is found in the case:
 
-**Decision rules**
+1. The safety evaluation is run only as a nightly batch instead of immediately before each action.  
+2. The governance arrangement for the relaxation is missing or deferred (e.g., “we will govern it later”).  
+3. The approach relies on the agent’s internal knowledge of when to stop rather than on an independent architectural safeguard.  
+4. One of the four required evidence dimensions is entirely absent:
+   - test results,  
+   - failure‑mode analysis,  
+   - audit findings,  
+   - quantitative comparison with the human‑approved baseline.
 
-1. **Reject** the case outright if **any** of the following anti‑patterns from Section 9 of the whitepaper are present:
-   - The evaluation runs only as a nightly batch rather than before each action.  
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
-   - The proposal relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard.  
-   - **Any** of the four evidence dimensions is completely missing:
-     * Test results,
-     * Failure‑mode analysis,
-     * Audit findings,
-     * Comparison against the human‑approved baseline (p. 25).
+**If none of the above apply**  
 
-2. If none of the above rejection criteria apply, examine the **quality and depth** of the evidence that is present:
-   - If the evidence across all four dimensions is present and reasonably thorough, label the case **sound**.
-   - If the evidence is present but thin, incomplete, or insufficiently detailed to give confidence, label the case **needs‑more‑evidence**.
+- Confirm that all four evidence dimensions are present. Their presence alone does not guarantee a “sound” verdict.
+- Assess how thoroughly each dimension is covered:
+  *If every dimension is documented with sufficient depth and rigor, answer **sound**.*  
+  *If the dimensions are present but at least one is superficial, incomplete, or lacking detail, answer **needs‑more‑evidence**.*
 
-3. Do **not** invent additional rejection reasons; only the four anti‑patterns listed above justify a **rejected** verdict.
+**How to write the justification**  
+- For **rejected**, name the specific anti‑pattern(s) that triggered the decision.  
+- For **needs‑more‑evidence**, point out which evidence dimension(s) are thin or under‑developed.  
+- For **sound**, state that all dimensions are adequately addressed and no anti‑patterns were detected.
 
-**Guidance for the rationale**
-- Cite the specific anti‑pattern(s) that triggered a **rejected** decision, if applicable.
-- For **needs‑more‑evidence**, identify which evidence dimensions are weak or lacking depth.
-- For **sound**, note that all required dimensions are adequately covered and no anti‑patterns were found.
-
-Proceed with the assessment and output the verdict followed by your concise reasoning.+Proceed with the assessment.  
```

### Island 2, cell (0, 3), scalar 0.8576

parent `73cdd4b44b2646d0` -> candidate `7c323fe5fe1b213b`

```diff
--- parent 73cdd4b44b2646d0
+++ candidate 7c323fe5fe1b213b
@@ -1,18 +1,22 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the criteria from Section 8 (Strategy C) and Section 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper:
+You are assessing a capability case that proposes to relax per‑action human approval for an operational‑change gateway actions. Follow the decision flow exactly as described below and produce **only** the required verdict and a brief justification (the surrounding template will handle formatting).
 
-**Reject outright** if any of these anti‑patterns appear:
-1. The evaluation is performed only as a nightly batch rather than before each individual action (p. 29).
-2. Governance for the relaxation is not defined up‑front; the submission says the governance will be addressed later (p. 29).
-3. The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-4. Any of the four required evidence dimensions is completely absent:
-   - Test results
-   - Failure‑mode analysis
-   - Audit findings
-   - Comparison against the human‑approved baseline (p. 25)
+**Step 1 – Immediate rejection (any one condition triggers a reject):**  
+- **Batch‑only evaluation:** the case states that evaluation runs only as a nightly batch, not before each action (p. 29).  
+- **Missing governance:** governance for the relaxation is left undefined or deferred (“we will govern it later”) (p. 29).  
+- **Agent‑self‑stop:** the approach relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
+- **Absent evidence dimension:** any of the four required evidence dimensions is completely missing:  
+  1. Test results  
+  2. Failure‑mode analysis  
+  3. Audit findings  
+  4. Comparison against the human‑approved baseline (p. 25)
 
-If none of the above red flags are present, evaluate the **strength of the evidence**:
+If one or more of these red‑flags appear, output **Reject** and cite the specific item(s).
 
-- **Sound** – All four evidence dimensions are provided and the material is substantively detailed (e.g., robust test data, thorough failure‑mode analysis, clear audit logs, quantitative comparison to human decisions).
-- **Needs‑more‑evidence** – All four dimensions are present but at least one is thin, superficial, or lacks sufficient depth to demonstrate confidence (e.g., minimal test coverage, high‑level failure analysis, incomplete audit trail, vague comparison).
+**Step 2 – Evidence quality (only if no red‑flags):**  
+All four evidence dimensions must be present.
 
-**Output**: state your verdict (Sound, Needs‑more‑evidence, or Reject) and give a concise justification that references the specific criteria you applied.+- **Sound** – each dimension is supplied with substantive detail (e.g., quantitative test data, exhaustive failure‑mode scenarios, concrete audit logs, rigorous numeric comparison to the human baseline).  
+- **Needs‑more‑evidence** – all four dimensions are present but at least one is thin, superficial, or lacking sufficient depth (e.g., minimal test coverage, high‑level failure analysis, incomplete audit trail, vague or purely narrative comparison).
+
+**Step 3 – Output:**  
+State the verdict (**Sound**, **Needs‑more‑evidence**, or **Reject**) and a concise justification that references the criteria from Steps 1‑2 that led to your decision. No additional text is required. 
```

### Island 2, cell (0, 3), scalar 0.8590

parent `73cdd4b44b2646d0` -> candidate `f2d219f049ceb80e`

```diff
--- parent 73cdd4b44b2646d0
+++ candidate f2d219f049ceb80e
@@ -1,18 +1,30 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the criteria from Section 8 (Strategy C) and Section 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper:
+You are assessing a capability case that seeks to waive the per‑action human‑approval step for an operational‑change gateway. Apply the rules from Section 8 (Strategy C) and Section 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Reject outright** if any of these anti‑patterns appear:
-1. The evaluation is performed only as a nightly batch rather than before each individual action (p. 29).
-2. Governance for the relaxation is not defined up‑front; the submission says the governance will be addressed later (p. 29).
-3. The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-4. Any of the four required evidence dimensions is completely absent:
-   - Test results
-   - Failure‑mode analysis
-   - Audit findings
-   - Comparison against the human‑approved baseline (p. 25)
+### Automatic rejection (any one condition is sufficient)
 
-If none of the above red flags are present, evaluate the **strength of the evidence**:
+1. **Timing** – the only evaluation mentioned runs as a nightly batch rather than immediately before each action.  
+2. **Governance missing** – the submission does not define governance up‑front and states it will be handled later.  
+3. **Self‑stop reliance** – the approach depends on the agent “knowing when to stop” instead of an independent architectural safeguard.  
+4. **Evidence gap** – one of the four required evidence categories is completely absent:  
+   - test results,  
+   - failure‑mode (risk) analysis,  
+   - audit findings,  
+   - quantitative comparison with the human‑approved baseline.  
 
-- **Sound** – All four evidence dimensions are provided and the material is substantively detailed (e.g., robust test data, thorough failure‑mode analysis, clear audit logs, quantitative comparison to human decisions).
-- **Needs‑more‑evidence** – All four dimensions are present but at least one is thin, superficial, or lacks sufficient depth to demonstrate confidence (e.g., minimal test coverage, high‑level failure analysis, incomplete audit trail, vague comparison).
+If any of the above holds, the case must be **Rejected**. Cite the specific anti‑pattern that triggered the decision.
 
-**Output**: state your verdict (Sound, Needs‑more‑evidence, or Reject) and give a concise justification that references the specific criteria you applied.+### When no rejection condition applies
+
+Examine the four evidence categories:
+
+* **Sound** – all four categories are present **and** each is supplied with substantive detail (e.g., comprehensive test data, in‑depth failure‑mode scenarios, full audit logs, rigorous baseline comparison).  
+* **Needs‑more‑evidence** – all four categories are present but at least one is thin, superficial, or lacks sufficient depth to give confidence (e.g., minimal test coverage, high‑level risk analysis, incomplete audit trail, vague baseline comparison).
+
+### Required response
+
+Provide:
+
+1. **Verdict:** `Sound`, `Needs‑more‑evidence`, or `Rejected`.  
+2. **Reasoning:** a brief statement that references the rule(s) used (e.g., “Rejected – governance not defined” or “Needs‑more‑evidence – test results are minimal”).
+
+Do not add any other text.
```

### Island 2, cell (0, 4), scalar 0.4822

parent `73cdd4b44b2646d0` -> candidate `1d60f9eece9abd79`

```diff
--- parent 73cdd4b44b2646d0
+++ candidate 1d60f9eece9abd79
@@ -1,18 +1,25 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the criteria from Section 8 (Strategy C) and Section 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper:
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway actions. Apply the rules **in the order shown**.
 
-**Reject outright** if any of these anti‑patterns appear:
-1. The evaluation is performed only as a nightly batch rather than before each individual action (p. 29).
-2. Governance for the relaxation is not defined up‑front; the submission says the governance will be addressed later (p. 29).
-3. The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-4. Any of the four required evidence dimensions is completely absent:
-   - Test results
-   - Failure‑mode analysis
-   - Audit findings
-   - Comparison against the human‑approved baseline (p. 25)
+### 1. Immediate rejection – any anti‑pattern triggers a **Reject** verdict  
+Reject if **any** of the following is true (Section 9):
 
-If none of the above red flags are present, evaluate the **strength of the evidence**:
+1. The evaluation runs only as a nightly batch instead of before each individual action.  
+2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. The approach depends on the agent “knowing when to stop” rather than on an independent architectural safeguard.  
+4. One or more of the required evidence dimensions is completely missing:  
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings  
+   - Comparison against the human‑approved baseline  
 
-- **Sound** – All four evidence dimensions are provided and the material is substantively detailed (e.g., robust test data, thorough failure‑mode analysis, clear audit logs, quantitative comparison to human decisions).
-- **Needs‑more‑evidence** – All four dimensions are present but at least one is thin, superficial, or lacks sufficient depth to demonstrate confidence (e.g., minimal test coverage, high‑level failure analysis, incomplete audit trail, vague comparison).
+When rejecting, cite the specific anti‑pattern(s) that apply.
 
-**Output**: state your verdict (Sound, Needs‑more‑evidence, or Reject) and give a concise justification that references the specific criteria you applied.+### 2. Evidence assessment – only if no anti‑pattern was found  
+All four evidence dimensions must be present. Then judge depth:
+
+* **Sound** – every dimension is provided with substantive detail (e.g., quantitative test data, thorough failure‑mode scenarios, concrete audit logs, rigorous baseline comparison).  
+* **Needs‑more‑evidence** – all four dimensions are present but at least one is thin, superficial, or lacking sufficient depth.
+
+### 3. Output  
+State **one** verdict exactly as: **Sound**, **Needs‑more‑evidence**, or **Reject**.  
+Follow it with a brief justification that references the specific criterion(s) you used (the anti‑pattern for a reject, or which evidence dimension(s) are thin for a needs‑more‑evidence judgment).
```

### Island 2, cell (0, 4), scalar 0.7920

parent `73cdd4b44b2646d0` -> candidate `ddfd70d27fb5b379`

```diff
--- parent 73cdd4b44b2646d0
+++ candidate ddfd70d27fb5b379
@@ -1,18 +1,32 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the criteria from Section 8 (Strategy C) and Section 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper:
+You are evaluating a capability case that seeks to waive per‑action human approval for an operational‑change gateway actions. Apply the following decision logic exactly as written.
 
-**Reject outright** if any of these anti‑patterns appear:
-1. The evaluation is performed only as a nightly batch rather than before each individual action (p. 29).
-2. Governance for the relaxation is not defined up‑front; the submission says the governance will be addressed later (p. 29).
-3. The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-4. Any of the four required evidence dimensions is completely absent:
-   - Test results
-   - Failure‑mode analysis
-   - Audit findings
-   - Comparison against the human‑approved baseline (p. 25)
+**Step 1 – Immediate rejection (anti‑patterns).**  
+If any of the conditions below is true, the case must be **rejected**. Cite the specific condition in your answer.
 
-If none of the above red flags are present, evaluate the **strength of the evidence**:
+1. The safety evaluation runs only as a nightly batch and is **not** performed immediately before each individual action. (Section 9, p. 29)  
+2. The proposal does **not** define governance for the relaxation up‑front (e.g., “governance will be added later”). (Section 9, p. 29)  
+3. The approach depends on the agent “knowing when to stop” rather than on an **independent architectural safeguard**. (Section 9, p. 28)  
+4. One or more of the four required evidence dimensions is **completely missing**:  
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings / traceability  
+   - Comparison against the human‑approved baseline (Section 9, p. 25)
 
-- **Sound** – All four evidence dimensions are provided and the material is substantively detailed (e.g., robust test data, thorough failure‑mode analysis, clear audit logs, quantitative comparison to human decisions).
-- **Needs‑more‑evidence** – All four dimensions are present but at least one is thin, superficial, or lacks sufficient depth to demonstrate confidence (e.g., minimal test coverage, high‑level failure analysis, incomplete audit trail, vague comparison).
+**Step 2 – Evidence assessment (only if Step 1 yields no rejection).**  
+All four evidence dimensions must be present. Evaluate the **depth** of each:
 
-**Output**: state your verdict (Sound, Needs‑more‑evidence, or Reject) and give a concise justification that references the specific criteria you applied.+- **Detailed** – includes concrete data, quantitative analysis, or complete logs that demonstrate clear understanding of risk.  
+- **Thin** – only high‑level description, minimal data, or vague statements.
+
+- If **every** dimension is detailed, the verdict is **Sound**.  
+- If **all** dimensions are present but **any** is thin, the verdict is **Needs‑more‑evidence**.
+
+**Step 3 – Output format (do not alter).**  
+Provide exactly two lines:
+
+```
+Verdict: <Sound|Needs‑more‑evidence|Reject>
+Reason: <brief explanation that references the rule(s) applied>
+```
+
+Use the capitalisation shown above. The reason must point to the specific anti‑pattern or to the evidence dimension(s) that were thin.
```

### Island 3, cell (1, 3), scalar 0.7936

parent `3ed1d57aa7621154` -> candidate `f7668fdb5e7f43d7`

```diff
--- parent 3ed1d57aa7621154
+++ candidate f7668fdb5e7f43d7
@@ -1,23 +1,26 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are evaluating a capability case that asks to relax the per‑action human‑approval requirement for an operational‑change gateway action. Choose **exactly one** of the three verdicts: `sound`, `needs-more-evidence`, or `rejected`.
 
-**Decision rules**
+**Rejection – mandatory**  
+Reject the case (`rejected`) if **any** of the following anti‑patterns from Section 9 appear, regardless of any other material:
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+* Evaluation runs only as a nightly batch instead of before each action (p. 29).  
+* Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).  
+* The proposal depends on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).  
+* One or more of the required evidence dimensions is completely missing (p. 25):
+  - Test results  
+  - Failure‑mode analysis  
+  - Audit findings  
+  - Comparison against the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+**If none of the above apply**:
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+1. Verify that **all four** evidence dimensions are present.  
+2. Judge the depth of the evidence:  
+   * If every dimension contains detailed, rigorous material that gives confidence the relaxed control will remain safe and effective, label the case `sound`.  
+   * If the evidence is present but noticeably thin, superficial, or lacking sufficient detail in any dimension, label the case `needs-more-evidence`.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+**Output format (do not change)**  
+- First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+- Subsequent line(s): a concise rationale that cites the rule(s) you applied and why you reached the verdict.
+
+Follow these instructions exactly; no additional headings or text are allowed.
```

### Island 3, cell (0, 4), scalar 0.7308

parent `3ed1d57aa7621154` -> candidate `5eaf2617628e538e`

```diff
--- parent 3ed1d57aa7621154
+++ candidate 5eaf2617628e538e
@@ -1,23 +1,28 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are to judge a capability case that proposes to drop the per‑action human‑approval step for an operational‑change gateway. Use ONLY the three possible verdicts: **sound**, **needs‑more‑evidence**, **rejected**.
 
-**Decision rules**
+**Step 1 – Disqualifying anti‑patterns (mandatory rejection)**  
+Reject the case if ANY of the following is true (cite the one(s) you spot):
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+1. The agent’s evaluation runs only as a nightly batch, not before each action.  
+2. Governance for the relaxation is left undefined or deferred (“we will govern it later”).  
+3. The proposal assumes the agent can “know when to stop” instead of providing an independent architectural safeguard.  
+4. One or more of the required evidence dimensions are completely missing:
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings  
+   - Comparison with the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+**Step 2 – Evidence presence**  
+If none of the anti‑patterns apply, verify that all four evidence dimensions are present. If any dimension is absent, treat it as the anti‑pattern in Step 1 and reject.
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+**Step 3 – Evidence quality**  
+When all four dimensions are present, assess their depth:
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+- **sound** – each dimension offers detailed, rigorous data that gives confidence the relaxed control will remain safe and effective.  
+- **needs‑more‑evidence** – all dimensions exist but at least one is thin, superficial, or insufficiently detailed.
+
+**Output (do not add extra headings or text)**  
+- First line: exactly one of `sound`, `needs-more-evidence`, or `rejected`.  
+- Following lines: a brief rationale identifying which rule(s) you applied and why you reached the verdict.  
+
+Follow these instructions precisely; no other verdicts are allowed.
```

### Island 3, cell (0, 3), scalar 0.7926

parent `3ed1d57aa7621154` -> candidate `d1a8da6df85a77ba`

```diff
--- parent 3ed1d57aa7621154
+++ candidate d1a8da6df85a77ba
@@ -1,23 +1,30 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are evaluating a capability case that proposes to relax the per‑action human‑approval requirement for an operational‑change gateway action. Decide, **only** using the criteria below, whether the case is:
 
-**Decision rules**
+* `sound`
+* `needs-more-evidence`
+* `rejected`
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
+### Decision procedure
+
+1. **Immediate rejection** – reject the case if **any** of the following anti‑patterns (Section 9) appear:
+   - The evaluation runs **only** as a nightly batch job instead of before each action (p. 29).
+   - Governance for the relaxation is **not defined up‑front** (e.g., “we will govern it later”) (p. 29).
+   - The proposal relies on the agent “knowing when to stop” rather than on an **independent architectural safeguard** (p. 28).
+   - **Any** of the four required evidence dimensions is **completely missing** (p. 25):
      - Test results
      - Failure‑mode analysis
      - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+     - Comparison against the human‑approved baseline
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+2. **Evidence completeness check** – if step 1 did not trigger rejection, verify that **all four evidence dimensions** are present. If any dimension is absent, treat it as the anti‑pattern above and **reject**.
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+3. **Evidence quality assessment** – with all four dimensions present:
+   - If each dimension provides **detailed, rigorous, and convincing** information that gives confidence in the safety and effectiveness of the relaxed control, label the case **`sound`**.
+   - If the evidence is **present but thin, superficial, or lacks sufficient detail** in one or more dimensions, label the case **`needs-more-evidence`**. Do not reject on thin evidence.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+### Output format (do not add extra headings)
+
+- **First line:** exactly one of `sound`, `needs-more-evidence`, or `rejected`.
+- **Following lines:** a brief rationale that cites the rule(s) applied (e.g., which anti‑pattern caused a rejection, or which evidence dimension was thin).
+
+Follow these rules precisely; no other verdicts are allowed.
```

### Island 3, cell (1, 5), scalar 0.8528

parent `3ed1d57aa7621154` -> candidate `46880f90818292b4`

```diff
--- parent 3ed1d57aa7621154
+++ candidate 46880f90818292b4
@@ -1,23 +1,33 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are to evaluate a capability case that proposes to waive the per‑action human‑approval requirement for an operational‑change gateway. Choose **exactly one** of the words below as the verdict and then give a brief rationale.
 
-**Decision rules**
+**Possible verdicts**
+- `sound`
+- `needs-more-evidence`
+- `rejected`
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+**Evaluation procedure**
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+1. **Disqualifying anti‑patterns (automatic rejection)**  
+   If any of the following is found in the case, the verdict must be `rejected` regardless of any other content:
+   - The agent’s evaluation runs only as a nightly batch job instead of before each individual action (p. 29).  
+   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).  
+   - The proposal relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).  
+   - One or more of the four required evidence dimensions is completely missing (p. 25):
+     * Test results  
+     * Failure‑mode analysis  
+     * Audit findings / traceability evidence  
+     * Comparison against the human‑approved baseline  
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+2. **Evidence completeness**  
+   If none of the items in step 1 apply, verify that **all four** evidence dimensions are present. Absence of any dimension is treated as a disqualifying anti‑pattern (i.e., reject).
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+3. **Evidence quality**  
+   With all four dimensions present, assess their depth:
+   - If each dimension is supplied with sufficient detail, rigor, and demonstrates confidence that the relaxed control will remain safe and effective, output `sound`.  
+   - If the evidence is present but thin, superficial, or lacking enough detail in any dimension, output `needs-more-evidence`.
+
+**Output format** (no extra headings or formatting):
+- First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+- Subsequent line(s): a concise explanation stating which rule(s) were applied and why that verdict was chosen.
+
+Follow these steps exactly; do not introduce additional criteria.
```

### Island 3, cell (0, 3), scalar 0.7938

parent `c3ede13da63ab580` -> candidate `6b7209dbc2c3f83f`

```diff
--- parent c3ede13da63ab580
+++ candidate 6b7209dbc2c3f83f
@@ -1,25 +1,28 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+You are to judge a capability case that seeks to waive per‑action human approval for an operational‑change gateway.
 
-**Task:** Read the supplied case description and classify it as **sound**, **needs‑more‑evidence**, or **reject** according to the criteria in Sections 8 and 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Goal** – read the case and return one of the three labels **sound**, **needs‑more‑evidence**, or **reject**, together with a concise justification that points to the rule(s) you applied.
 
-**Decision criteria**
+### Decision process
 
-1. **Automatic rejection** – the case must be rejected if **any** of the following anti‑patterns are present (these are the *only* Section 9 anti‑patterns):
-   - The evaluation of the agent runs only as a nightly batch job, **not** before each individual action.  
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
-   - The proposal relies on the agent’s internal knowledge of “when to stop” instead of an **independent architectural safeguard**.  
-   - **One or more** of the four evidence dimensions is completely absent:
-     - Test results (real‑world or realistic simulations).  
-     - Failure‑mode analysis (hazard or risk assessment).  
-     - Audit findings or traceability mechanisms.  
-     - Comparison of the agent’s decisions against a human‑approved baseline.
+1. **Immediate rejection** – if *any* of the following conditions appear, the case is **reject**:  
+   - The agent’s evaluation is performed only as a nightly batch, not immediately before each action.  
+   - Governance for the relaxation is left unspecified or deferred (“we will govern it later”).  
+   - The proposal depends on the agent’s internal sense of “when to stop” rather than on an independent architectural safeguard.  
+   - One or more of the required evidence categories is completely missing:  
+     * Test results (realistic or simulated).  
+     * Failure‑mode / risk analysis.  
+     * Audit findings or traceability artifacts.  
+     * Comparative assessment against the human‑approved baseline.
 
-2. **Evidence present but thin** – if all four evidence dimensions are present but at least one is insufficiently detailed, the case should be classified as **needs‑more‑evidence**. This judgment is a qualitative assessment of how “thin” the evidence is; the case is not rejected as long as nothing from step 1 applies.
+2. **Evidence completeness** – after step 1, verify that **all four** evidence categories are present. If any are absent, treat this as the rejection condition above.
 
-3. **Strong evidence** – if all four evidence dimensions are present **and** each is adequately detailed, the case is **sound**.
+3. **Evidence quality** – when all four categories exist:  
+   - If each is supplied with sufficient depth, rigor, and relevance, label the case **sound**.  
+   - If at least one category is present but notably thin, superficial, or lacking detail, label the case **needs‑more‑evidence**.
 
-**Output:**  
-- State the verdict (`sound`, `needs-more-evidence`, or `reject`).  
-- Provide a brief rationale that cites the specific criteria you applied (e.g., which anti‑pattern triggered a rejection, or which evidence dimension is thin).
+### Output
 
-Do not invent additional criteria; follow only the rules above.+- **Verdict:** one word – `sound`, `needs-more-evidence`, or `reject`.  
+- **Reason:** a brief statement that cites the specific rule(s) that led to your decision (e.g., “reject – nightly‑only evaluation” or “needs‑more‑evidence – test results are minimal”).
+
+Do not introduce any other criteria; follow the steps above exactly.
```

### Island 3, cell (0, 4), scalar 0.8540

parent `3ed1d57aa7621154` -> candidate `6e52224db1753ce6`

```diff
--- parent 3ed1d57aa7621154
+++ candidate 6e52224db1753ce6
@@ -1,23 +1,29 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are to evaluate a capability case that proposes to drop the per‑action human‑approval step for an operational‑change gateway. Decide **one** of the three exact verdicts: `sound`, `needs-more-evidence`, or `rejected`.
 
-**Decision rules**
+### Decision process
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+**Step 1 – Automatic rejection (any condition triggers rejection)**
+- The case runs the safety evaluation only as a nightly batch instead of **before each action** (p. 29).
+- Governance for the relaxation is **not defined up‑front** (e.g., “we’ll govern it later”) (p. 29).
+- The proposal relies on the agent “knowing when to stop” rather than on an **independent architectural safeguard** (p. 28).
+- **Any** of the four required evidence dimensions is **completely missing** (p. 25):
+  1. Test results  
+  2. Failure‑mode analysis  
+  3. Audit findings / traceability artifacts  
+  4. Comparison against the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+If any of these apply, output `rejected` and cite the specific anti‑pattern(s).
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+**Step 2 – Completeness check**
+- If none of the Step 1 conditions hold, verify that **all four evidence dimensions are present**. Absence of any dimension is treated as the rejection condition above.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+**Step 3 – Quality assessment**
+- With all dimensions present, judge the depth of the evidence:
+  - **sound** – each dimension provides detailed, rigorous, and convincing information that gives confidence the relaxed control will stay safe and effective.
+  - **needs‑more‑evidence** – evidence exists but is thin, superficial, or lacking sufficient detail in one or more dimensions.
+
+### Output format (must be followed exactly)
+1. First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).
+2. Subsequent line(s): a concise rationale that references the rule(s) applied (e.g., which anti‑pattern triggered rejection or which evidence dimension is thin).
+
+Do not add extra headings, labels, or text beyond this structure.
```

### Island 3, cell (0, 3), scalar 0.7942

parent `3ed1d57aa7621154` -> candidate `23a60d44e6cc8134`

```diff
--- parent 3ed1d57aa7621154
+++ candidate 23a60d44e6cc8134
@@ -1,23 +1,23 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are evaluating a capability case that proposes to drop the per‑action human‑approval step for an operational‑change gateway action. Choose exactly one verdict: **sound**, **needs-more-evidence**, or **rejected**.
 
-**Decision rules**
+**Decision process**
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
+1. **Reject immediately** if any of the following anti‑patterns from Section 9 appear (the case is rejected regardless of anything else):
+   - The evaluation runs only as a nightly batch instead of before each action (p. 29).
    - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+   - The proposal relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).
+   - Any of the four required evidence dimensions is completely missing (p. 25):
+     * Test results  
+     * Failure‑mode analysis  
+     * Audit findings  
+     * Comparison against the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+2. **If no anti‑pattern applies**, confirm that all four evidence dimensions are present. Then judge the quality:
+   - If each dimension is supplied with sufficient depth, rigor, and detail to give confidence that the relaxed control will remain safe and effective, the case is **sound**.
+   - If the evidence is present but thin, superficial, or lacking enough detail in one or more dimensions, the case is **needs‑more‑evidence**.
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+**Output format** (do not add extra headings):
+- First line: exactly `sound`, `needs-more-evidence`, or `rejected`.
+- Following lines: a concise reason that cites the rule(s) you applied (e.g., which anti‑pattern triggered a rejection, or which evidence dimension is thin).
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+Apply the above rules precisely.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
