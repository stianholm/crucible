# Generation 1 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 52.1%
- Aggregate throughput: 56.5 tok/s (63070 completion tokens / 1116.3s)

## Archive

- Island 0: coverage 16.7%, QD score 3.786, unique ancestors 2
- Island 1: coverage 19.4%, QD score 3.031, unique ancestors 4
- Island 2: coverage 8.3%, QD score 1.710, unique ancestors 3
- Island 3: coverage 8.3%, QD score 2.102, unique ancestors 2
- Cells newly claimed this generation: 9

## Quality

- Best scalar this generation: 0.7033
- Median scalar of newly-claimed: 0.5082

## Cost

- Budget: {'generation': 1, 'max_generations': 10, 'tokens_used_total': 435412, 'max_tokens': 5000000, 'elapsed_s_total': 1705.4, 'generation_wall_s': 1116.3}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 4), scalar 0.6028

parent `2a3cb845d4a90dfc` -> candidate `7182282bc5022a9e`

```diff
--- parent 2a3cb845d4a90dfc
+++ candidate 7182282bc5022a9e
@@ -1,25 +1,34 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are tasked with judging a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Your assessment must follow **Section 8 (Strategy C – capability‑based opening)** and avoid any **Section 9 anti‑patterns** from the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Assessment steps**
+### Evaluation Framework
 
-1. **Core evidence checklist** – Verify that the submission provides:
-   - **Real‑world testing** of the automation under realistic conditions.
-   - **Failure‑mode analysis** that identifies what could go wrong and mitigation measures.
-   - **Audit‑trail mechanism** that records decisions, inputs, and outcomes.
-   - **Human‑equivalence comparison** showing how the agent’s decisions match or improve upon those of a human operator.
+1. **Evidence Requirements** – Confirm that the submission includes **all** of the following:
+   - **Real‑world validation** – End‑to‑end testing in a production‑like environment (including fault injection or field trials).
+   - **Failure‑mode & mitigation analysis** – Identification of possible failures, their likelihood/severity, and concrete countermeasures.
+   - **Auditability** – Tamper‑evident logging of decisions, inputs, timestamps, and outcomes that can be independently reviewed.
+   - **Human‑equivalence benchmark** – Direct comparison (quantitative or qualitative) showing the autonomous action is at least as safe/effective as a qualified human operator.
 
-2. **Anti‑pattern screening** – Look for any of the following red‑flags (if any are present, the case must be **REJECTED**):
-   - Absence of a rollback or safe‑state procedure.
-   - Reliance on “black‑box” AI without explainability or observability.
-   - Lack of independent verification or validation.
-   - Any indication that the system could bypass critical safety interlocks.
+2. **Anti‑Pattern Check** – Scan for any of the listed red‑flags. The presence of **any** anti‑pattern automatically results in **REJECTED**:
+   - No defined rollback or safe‑state fallback.
+   - Use of opaque “black‑box” AI without explainability/observability.
+   - Absence of independent verification or validation.
+   - Capability to bypass mandatory safety interlocks.
+   - Unbounded escalation or missing revocation mechanisms.
+   - Any other pattern expressly prohibited in Section 9.
 
-3. **Verdict determination**
-   - If **all** core evidence items are present **and** no anti‑patterns are detected, label the case **SOUND**.
-   - If one or more core evidence items are missing or insufficient, but no anti‑patterns appear, label it **NEEDS_MORE_EVIDENCE**.
-   - If any anti‑pattern is found, label it **REJECTED**.
+### Verdict Logic
 
-**Output**  
-State the verdict (`SOUND`, `NEEDS_MORE_EVIDENCE`, or `REJECTED`) followed by a concise justification that references the specific criteria or anti‑patterns that guided your decision.
+- **SOUND** – Every evidence item in (1) is satisfied **and** no anti‑patterns from (2) are found.
+- **NEEDS_MORE_EVIDENCE** – One or more items in (1) are missing or insufficient, **and** no anti‑patterns are present.
+- **REJECTED** – Any anti‑pattern from (2) is detected, regardless of evidence completeness.
 
-Respond with your verdict and reasoning.+### Output Specification
+
+Produce **exactly** the following format (no extra text):
+
+```
+Verdict: <SOUND | NEEDS_MORE_EVIDENCE | REJECTED>
+Reasoning: <brief explanation citing the specific evidence items satisfied/absent and/or the anti‑pattern(s) that triggered the decision>
+```
+
+The reasoning should be concise (one to three sentences) and reference the relevant checklist point(s) or anti‑pattern(s) that guided your judgment.
```

### Island 0, cell (1, 2), scalar 0.5082

parent `241f3fbabcc0525c` -> candidate `b6f8c882a253785f`

```diff
--- parent 241f3fbabcc0525c
+++ candidate b6f8c882a253785f
@@ -1,22 +1,22 @@
-You are evaluating a capability case that proposes relaxing per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and produce a clear judgment according to the criteria in **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are tasked with reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C – capability‑based opening)** and the **anti‑patterns of Section 9** from the ITOT‑boundary‑as‑architecture whitepaper, examine the supplied evidence and output a single verdict block.
 
-### Evaluation checklist
-1. **Empirical testing** – Has the team conducted realistic end‑to‑end tests (including failure injection, load testing, or field trials)?  
-2. **Risk analysis** – Are potential failure modes identified, quantified, and mitigated? Look for a structured hazards or threat assessment.  
-3. **Auditability** – Is there a tamper‑evident log or trace that records the agent’s decisions, timestamps, and supporting data?  
-4. **Human‑equivalence comparison** – Does the submission include a quantitative or qualitative comparison between the autonomous decision and the decision a qualified human would make under the same conditions?  
-5. **Compliance with anti‑patterns** – Verify that none of the Section 9 anti‑patterns are present (e.g., “no‑fallback”, “black‑box decision”, “unbounded escalation”, “missing revocation”, etc.).
+#### Review checklist
+1. **Real‑world testing** – evidence of end‑to‑end trials (field test, failure injection, load test, etc.).  
+2. **Risk & failure analysis** – documented hazard or threat assessment with probabilities, impacts, and mitigations.  
+3. **Audit trail** – tamper‑evident logging of the autonomous decision, inputs, timestamps, and supporting data.  
+4. **Human‑equivalence** – comparison (quantitative or qualitative) of the automation’s decision with that of a qualified human under identical conditions.  
+5. **Anti‑pattern screening** – ensure none of the Section 9 red‑flags appear (e.g., no‑fallback, black‑box decision, unbounded escalation, missing revocation, inability to roll back, bypassed safety interlocks, absent independent verification).
 
-### Verdict categories
-- **Sound** – The evidence satisfies all checklist items, any residual risks are low and well‑controlled, and no Section 9 anti‑patterns are found.  
-- **Needs‑More‑Evidence** – The submission is missing one or more checklist items, or the provided data is inconclusive; the case is not a clear red‑flag but cannot be approved yet.  
-- **Rejected** – A serious violation of a Section 9 anti‑pattern or a critical, unmitigated risk is identified.
+#### Verdict rules
+- **Sound** – all five checklist items are satisfied, residual risk is low and mitigated, and no anti‑pattern is present.  
+- **Needs‑More‑Evidence** – one or more checklist items are missing or inconclusive, but no anti‑pattern is detected.  
+- **Rejected** – any anti‑pattern is found or a critical, unmitigated risk is identified.
 
-### Output format (must be followed exactly)
+#### Required output (exactly this format)
 ```
 Verdict: <Sound | Needs-More-Evidence | Rejected>
 Reasoning:
-<concise, bullet‑point or short‑paragraph explanation referencing the checklist items and any anti‑patterns>
+<brief bullet list or short paragraph citing the checklist items and/or anti‑patterns that led to the decision>
 ```
 
-Provide only the verdict block; do not add any other commentary. +Provide **only** the block above; do not add any extra text. 
```

### Island 0, cell (0, 5), scalar 0.3548

parent `2a3cb845d4a90dfc` -> candidate `e4d36889d348e0aa`

```diff
--- parent 2a3cb845d4a90dfc
+++ candidate e4d36889d348e0aa
@@ -1,25 +1,37 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are tasked with judging a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on the criteria in **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Assessment steps**
+### Evaluation framework
 
-1. **Core evidence checklist** – Verify that the submission provides:
-   - **Real‑world testing** of the automation under realistic conditions.
-   - **Failure‑mode analysis** that identifies what could go wrong and mitigation measures.
-   - **Audit‑trail mechanism** that records decisions, inputs, and outcomes.
-   - **Human‑equivalence comparison** showing how the agent’s decisions match or improve upon those of a human operator.
+**1. Required evidence (must‑have)**  
+Confirm that the submission includes each of the following:
 
-2. **Anti‑pattern screening** – Look for any of the following red‑flags (if any are present, the case must be **REJECTED**):
-   - Absence of a rollback or safe‑state procedure.
-   - Reliance on “black‑box” AI without explainability or observability.
-   - Lack of independent verification or validation.
-   - Any indication that the system could bypass critical safety interlocks.
+- **Real‑world validation** – documented testing of the automation under production‑like conditions (including fault injection or field trials).  
+- **Failure‑mode analysis** – a systematic identification of possible failures together with mitigation or containment measures.  
+- **Audit trail** – a tamper‑evident log that records every decision, its inputs, timestamps, and outcomes.  
+- **Human‑equivalence benchmark** – a comparison (qualitative or quantitative) showing that the autonomous decision matches or improves on what a qualified human operator would do.
 
-3. **Verdict determination**
-   - If **all** core evidence items are present **and** no anti‑patterns are detected, label the case **SOUND**.
-   - If one or more core evidence items are missing or insufficient, but no anti‑patterns appear, label it **NEEDS_MORE_EVIDENCE**.
-   - If any anti‑pattern is found, label it **REJECTED**.
+**2. Anti‑pattern screening (disqualifiers)**  
+If any of the following issues appear, the case is **REJECTED**:
 
-**Output**  
-State the verdict (`SOUND`, `NEEDS_MORE_EVIDENCE`, or `REJECTED`) followed by a concise justification that references the specific criteria or anti‑patterns that guided your decision.
+- No defined rollback, safe‑state, or fallback procedure.  
+- Use of an opaque (“black‑box”) AI component without explainability, observability, or monitoring.  
+- Absence of independent verification/validation (e.g., third‑party review, peer audit).  
+- Ability of the system to circumvent mandatory safety interlocks or other hard constraints.
 
-Respond with your verdict and reasoning.+**3. Verdict logic**
+
+| Condition | Verdict |
+|-----------|---------|
+| All required evidence present **and** no anti‑patterns detected | **SOUND** |
+| One or more required evidence items missing or insufficient, **and** no anti‑patterns found | **NEEDS_MORE_EVIDENCE** |
+| Any anti‑pattern detected (regardless of other evidence) | **REJECTED** |
+
+### Output requirements
+Produce **only** the following:
+
+```
+Verdict: <SOUND | NEEDS_MORE_EVIDENCE | REJECTED>
+Reasoning: <brief explanation that cites the specific evidence items satisfied/absent and any anti‑patterns identified>
+```
+
+The reasoning should be concise (a sentence or short bullet list) and directly reference the checklist items or anti‑patterns that led to your decision. Do not add any extra text or commentary.
```

### Island 0, cell (1, 3), scalar 0.6095

parent `2a3cb845d4a90dfc` -> candidate `3b88b7acf53cedff`

```diff
--- parent 2a3cb845d4a90dfc
+++ candidate 3b88b7acf53cedff
@@ -1,25 +1,37 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are tasked with judging a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Base your assessment on the **Strategy C (capability‑based opening)** criteria from Section 8 and the **anti‑patterns** enumerated in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Assessment steps**
+### Evaluation matrix
+Check the submission for the following mandatory evidence items:
 
-1. **Core evidence checklist** – Verify that the submission provides:
-   - **Real‑world testing** of the automation under realistic conditions.
-   - **Failure‑mode analysis** that identifies what could go wrong and mitigation measures.
-   - **Audit‑trail mechanism** that records decisions, inputs, and outcomes.
-   - **Human‑equivalence comparison** showing how the agent’s decisions match or improve upon those of a human operator.
+| # | Evidence required | What to look for |
+|---|-------------------|------------------|
+| 1 | **Real‑world trial** | End‑to‑end testing under production‑like conditions, including fault injection or field pilots. |
+| 2 | **Failure‑mode analysis** | Identification of plausible failure modes plus mitigations or containment measures. |
+| 3 | **Audit trail** | Tamper‑evident log that captures decision inputs, timestamps, and outcomes. |
+| 4 | **Human‑equivalence assessment** | Quantitative or qualitative comparison showing the autonomous decision is at least as safe/effective as a qualified human’s decision. |
 
-2. **Anti‑pattern screening** – Look for any of the following red‑flags (if any are present, the case must be **REJECTED**):
-   - Absence of a rollback or safe‑state procedure.
-   - Reliance on “black‑box” AI without explainability or observability.
-   - Lack of independent verification or validation.
-   - Any indication that the system could bypass critical safety interlocks.
+Mark each as **present** or **missing/insufficient**.
 
-3. **Verdict determination**
-   - If **all** core evidence items are present **and** no anti‑patterns are detected, label the case **SOUND**.
-   - If one or more core evidence items are missing or insufficient, but no anti‑patterns appear, label it **NEEDS_MORE_EVIDENCE**.
-   - If any anti‑pattern is found, label it **REJECTED**.
+### Anti‑pattern filter
+If **any** of the following anti‑patterns appears, the case must be **REJECTED**:
 
-**Output**  
-State the verdict (`SOUND`, `NEEDS_MORE_EVIDENCE`, or `REJECTED`) followed by a concise justification that references the specific criteria or anti‑patterns that guided your decision.
+- No defined rollback or safe‑state fallback.  
+- Use of an opaque/black‑box AI component without explainability or observability.  
+- Absence of independent verification or validation.  
+- Ability to circumvent mandatory safety interlocks.  
+- Any other pattern listed in Section 9 that endangers the safety‑critical boundary.
 
-Respond with your verdict and reasoning.+### Decision rule
+1. **Reject** immediately if any anti‑pattern is detected.  
+2. If no anti‑patterns are found, count the missing/insufficient evidence items:
+   * **0 missing** → verdict **SOUND**.  
+   * **1 or more missing** → verdict **NEEDS_MORE_EVIDENCE**.
+
+### Output requirement
+Return **only** the verdict (`SOUND`, `NEEDS_MORE_EVIDENCE`, or `REJECTED`) followed by a short justification that cites the specific matrix items or anti‑patterns that led to your conclusion.
+
+Example format (do not include the word “Example” in your answer):
+```
+SOUND
+All four evidence items are present and no anti‑patterns were identified.
+```
```

### Island 1, cell (0, 3), scalar -0.1461

parent `f726706593280baf` -> candidate `112a9df19e383d20`

```diff
--- parent f726706593280baf
+++ candidate 112a9df19e383d20
@@ -1,25 +1,26 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the supplied submission (the scenario) and evaluate it against the following criteria drawn from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are tasked with judging a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Examine the submitted scenario and assess it against the requirements from Section 8 (Strategy C, capability‑based opening) and the anti‑pattern list in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evidence criteria (must be satisfied for a “sound” judgment)**
-1. **Real‑world testing** – documented pilots, simulations, or field trials that show the automated decision‑making works under realistic conditions.
-2. **Risk analysis** – explicit identification of possible failure modes, their consequences, and mitigation or fallback strategies (e.g., safe‑state, manual override).
-3. **Auditability** – a complete, tamper‑evident log of the agent’s decisions, inputs, and rationale that can be examined post‑hoc.
-4. **Human‑parity comparison** – quantitative or qualitative comparison of the agent’s decisions to those a qualified human would make (e.g., accuracy, false‑positive/negative rates, acceptance thresholds).
-5. **Capability‑based controls** – clear definition of the scope, confidence thresholds, and revocation mechanisms required by Section 8.
+**Required evidence (all must be present for a “sound” result)**  
+1. **Operational testing** – documented pilots, simulations, or field‑trials that demonstrate the automated decision works safely in realistic conditions.  
+2. **Hazard analysis** – clear identification of failure modes, their impacts, and defined mitigations or safe‑state fall‑backs.  
+3. **Traceable logging** – tamper‑evident record of every decision, inputs, timestamps, and responsible entities.  
+4. **Human‑performance benchmark** – quantitative or qualitative comparison showing the automation meets or exceeds qualified human decision accuracy (e.g., concordance rate, false‑positive/negative limits).  
+5. **Capability limits** – explicit scope, confidence thresholds, and a revocation/override mechanism as required by Section 8.
 
-**Anti‑pattern disqualifiers (trigger automatic “rejected”)**
-- No fallback to human control or safe‑state.
-- Opaque/black‑box decision process with no explainability.
-- Unbounded escalation or unrestricted action domain.
-- Absence of continuous monitoring or performance metrics.
-- Any other Section 9 anti‑pattern explicitly identified in the submission.
+**Disqualifying anti‑patterns (any one forces “rejected”)**  
+- No immediate manual override or safe‑state fallback.  
+- Opaque/black‑box decision logic with no explainability.  
+- Unlimited escalation of authority or unbounded action domain.  
+- Missing continuous monitoring or performance metrics.  
+- Any other anti‑pattern enumerated in Section 9 that appears in the submission.
 
-**Decision categories**
-- **sound** – All evidence criteria are met and no anti‑patterns are present.
-- **needs-more-evidence** – One or more evidence criteria are missing or weak, but no disqualifying anti‑pattern is found.
-- **rejected** – Any anti‑pattern from Section 9 is present, or the risk evidence is fundamentally insufficient.
+**Decision categories**  
+- **sound** – every evidence item 1‑5 is satisfied and none of the anti‑patterns appear.  
+- **needs-more-evidence** – one or more evidence items are absent or weak, but no disqualifying anti‑pattern is found.  
+- **rejected** – any anti‑pattern is present, or the risk justification is fundamentally inadequate.
 
-**Output**
-Provide the verdict word (“sound”, “needs-more-evidence”, or “rejected”) followed by a concise justification (one or two sentences) that references the most salient criteria or anti‑patterns influencing your decision.
+**Output**  
+Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (one or two sentences) that cites the most decisive evidence point(s) or anti‑pattern(s). Do not add any other text or formatting.
 
-Respond with your verdict and your reasoning.+Example:  
+`sound – real‑world pilots and a full audit log are provided, and the fallback override is clearly defined.`
```

### Island 1, cell (0, 5), scalar 0.4502

parent `f726706593280baf` -> candidate `3c668da7e7bd724a`

```diff
--- parent f726706593280baf
+++ candidate 3c668da7e7bd724a
@@ -1,25 +1,30 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the supplied submission (the scenario) and evaluate it against the following criteria drawn from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to remove the per‑action human‑approval step for an industrial operational‑change gateway. Using the guidance from Section 8 (Strategy C, capability‑based opening) and the anti‑pattern list in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, apply the following checklist:
 
-**Evidence criteria (must be satisfied for a “sound” judgment)**
-1. **Real‑world testing** – documented pilots, simulations, or field trials that show the automated decision‑making works under realistic conditions.
-2. **Risk analysis** – explicit identification of possible failure modes, their consequences, and mitigation or fallback strategies (e.g., safe‑state, manual override).
-3. **Auditability** – a complete, tamper‑evident log of the agent’s decisions, inputs, and rationale that can be examined post‑hoc.
-4. **Human‑parity comparison** – quantitative or qualitative comparison of the agent’s decisions to those a qualified human would make (e.g., accuracy, false‑positive/negative rates, acceptance thresholds).
-5. **Capability‑based controls** – clear definition of the scope, confidence thresholds, and revocation mechanisms required by Section 8.
+**Evidence checklist (all must be satisfied for a “sound” judgment)**
+1. **Real‑world testing** – documented pilots, simulations, or field trials that demonstrate the automated decision works in realistic conditions.  
+2. **Risk / failure analysis** – explicit identification of failure modes, their impact, and mitigation or safe‑state fallback strategies.  
+3. **Auditability** – tamper‑evident logging of every decision, input, and rationale that can be inspected after the fact.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison showing the automated decisions meet or exceed qualified human performance (e.g., accuracy, false‑positive/negative rates).  
+5. **Capability‑based controls** – clear definition of the action scope, confidence thresholds, and revocation/re‑enable mechanisms required by Section 8.
 
-**Anti‑pattern disqualifiers (trigger automatic “rejected”)**
-- No fallback to human control or safe‑state.
-- Opaque/black‑box decision process with no explainability.
-- Unbounded escalation or unrestricted action domain.
-- Absence of continuous monitoring or performance metrics.
-- Any other Section 9 anti‑pattern explicitly identified in the submission.
+**Anti‑pattern disqualifiers (any presence forces “rejected”)**
+- No fallback to human control or safe‑state.  
+- Opaque/black‑box decision logic with no explainability.  
+- Unbounded escalation or unrestricted action domain.  
+- Lack of continuous monitoring or performance metrics.  
+- Any other anti‑pattern explicitly listed in Section 9.
 
-**Decision categories**
-- **sound** – All evidence criteria are met and no anti‑patterns are present.
-- **needs-more-evidence** – One or more evidence criteria are missing or weak, but no disqualifying anti‑pattern is found.
-- **rejected** – Any anti‑pattern from Section 9 is present, or the risk evidence is fundamentally insufficient.
+**Decision rules**
+- If any anti‑pattern is found → **rejected**.  
+- Else if one or more items from the Evidence checklist are missing or insufficient → **needs-more-evidence**.  
+- Else → **sound**.
 
-**Output**
-Provide the verdict word (“sound”, “needs-more-evidence”, or “rejected”) followed by a concise justification (one or two sentences) that references the most salient criteria or anti‑patterns influencing your decision.
+**Output format (must be followed exactly)**
+```
+<verdict>
+<brief justification>
+```
+- `<verdict>` must be exactly one of the words: **sound**, **needs-more-evidence**, **rejected**.  
+- The justification should be one sentence that cites the most decisive evidence criterion(s) or anti‑pattern(s) that led to your decision.
 
-Respond with your verdict and your reasoning.+Read the scenario, apply the checklist, and produce the verdict and justification in the format above.
```

### Island 1, cell (1, 3), scalar 0.4582

parent `f726706593280baf` -> candidate `8991f1a0638b9955`

```diff
--- parent f726706593280baf
+++ candidate 8991f1a0638b9955
@@ -1,25 +1,25 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the supplied submission (the scenario) and evaluate it against the following criteria drawn from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, follow these steps:
 
-**Evidence criteria (must be satisfied for a “sound” judgment)**
-1. **Real‑world testing** – documented pilots, simulations, or field trials that show the automated decision‑making works under realistic conditions.
-2. **Risk analysis** – explicit identification of possible failure modes, their consequences, and mitigation or fallback strategies (e.g., safe‑state, manual override).
-3. **Auditability** – a complete, tamper‑evident log of the agent’s decisions, inputs, and rationale that can be examined post‑hoc.
-4. **Human‑parity comparison** – quantitative or qualitative comparison of the agent’s decisions to those a qualified human would make (e.g., accuracy, false‑positive/negative rates, acceptance thresholds).
-5. **Capability‑based controls** – clear definition of the scope, confidence thresholds, and revocation mechanisms required by Section 8.
+**1. Disqualifying anti‑patterns (any one → verdict = rejected)**
+- No fallback to human control or safe‑state.
+- Opaque/black‑box decision logic with no explainability.
+- Unbounded escalation or unrestricted action domain.
+- No continuous monitoring or performance metrics.
+- Any other anti‑pattern explicitly listed in Section 9 and present in the submission.
 
-**Anti‑pattern disqualifiers (trigger automatic “rejected”)**
-- No fallback to human control or safe‑state.
-- Opaque/black‑box decision process with no explainability.
-- Unbounded escalation or unrestricted action domain.
-- Absence of continuous monitoring or performance metrics.
-- Any other Section 9 anti‑pattern explicitly identified in the submission.
+**2. Required evidence for a “sound” judgment**
+- **Real‑world testing** – documented pilots, simulations, or field trials showing the automation works under realistic conditions.
+- **Risk analysis** – identified failure modes, consequences, and mitigation or fallback strategies (e.g., safe‑state, manual override).
+- **Auditability** – tamper‑evident log of decisions, inputs, and rationale that can be reviewed post‑hoc.
+- **Human‑parity comparison** – quantitative or qualitative evidence that the automation matches qualified human performance (accuracy, false‑positive/negative rates, etc.).
+- **Capability‑based controls** – defined scope, confidence thresholds, and revocation mechanisms as required by Section 8.
 
-**Decision categories**
-- **sound** – All evidence criteria are met and no anti‑patterns are present.
-- **needs-more-evidence** – One or more evidence criteria are missing or weak, but no disqualifying anti‑pattern is found.
-- **rejected** – Any anti‑pattern from Section 9 is present, or the risk evidence is fundamentally insufficient.
+**3. Decision mapping**
+- **sound** – All five evidence items are adequately satisfied and no anti‑pattern is detected.
+- **needs-more-evidence** – One or more evidence items are missing or weak, but no anti‑pattern is present.
+- **rejected** – Any anti‑pattern from step 1 is present, or the overall risk evidence is fundamentally insufficient.
 
-**Output**
-Provide the verdict word (“sound”, “needs-more-evidence”, or “rejected”) followed by a concise justification (one or two sentences) that references the most salient criteria or anti‑patterns influencing your decision.
+**4. Output**
+State the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (one‑to‑two sentences) that references the most decisive evidence item(s) or anti‑pattern(s). Use the fixed output format required by the surrounding system.
 
-Respond with your verdict and your reasoning.+Proceed to read the submission and apply the above criteria.
```

### Island 1, cell (0, 5), scalar 0.7014

parent `f726706593280baf` -> candidate `d37dc06e0e8842b5`

```diff
--- parent f726706593280baf
+++ candidate d37dc06e0e8842b5
@@ -1,25 +1,28 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the supplied submission (the scenario) and evaluate it against the following criteria drawn from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a proposal that seeks to remove per‑action human approval for an operational‑change gateway in an industrial system. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Evidence criteria (must be satisfied for a “sound” judgment)**
-1. **Real‑world testing** – documented pilots, simulations, or field trials that show the automated decision‑making works under realistic conditions.
-2. **Risk analysis** – explicit identification of possible failure modes, their consequences, and mitigation or fallback strategies (e.g., safe‑state, manual override).
-3. **Auditability** – a complete, tamper‑evident log of the agent’s decisions, inputs, and rationale that can be examined post‑hoc.
-4. **Human‑parity comparison** – quantitative or qualitative comparison of the agent’s decisions to those a qualified human would make (e.g., accuracy, false‑positive/negative rates, acceptance thresholds).
-5. **Capability‑based controls** – clear definition of the scope, confidence thresholds, and revocation mechanisms required by Section 8.
+**Required evidence (must all be satisfied for a “sound” judgment)**
+1. **Real‑world validation** – pilots, simulations, or field trials that demonstrate the automated decision works under realistic conditions.  
+2. **Failure‑mode analysis** – explicit list of possible faults, their impact, and mitigation or safe‑state fallback.  
+3. **Auditable trail** – tamper‑evident logging of inputs, decisions, and rationale that can be inspected after the fact.  
+4. **Human‑parity data** – quantitative or qualitative comparison showing the agent’s performance matches or exceeds that of a qualified human (e.g., accuracy, false‑positive/negative rates).  
+5. **Capability‑based controls** – defined scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-**Anti‑pattern disqualifiers (trigger automatic “rejected”)**
-- No fallback to human control or safe‑state.
-- Opaque/black‑box decision process with no explainability.
-- Unbounded escalation or unrestricted action domain.
-- Absence of continuous monitoring or performance metrics.
-- Any other Section 9 anti‑pattern explicitly identified in the submission.
+**Disqualifying anti‑patterns (any one triggers an automatic “rejected”)**
+- No fallback to human control or safe‑state.  
+- Opaque/black‑box decision logic with no explainability.  
+- Unlimited escalation or unrestricted action domain.  
+- Lack of continuous monitoring or performance metrics.  
+- Any other anti‑pattern explicitly listed in Section 9 that appears in the submission.
 
-**Decision categories**
-- **sound** – All evidence criteria are met and no anti‑patterns are present.
-- **needs-more-evidence** – One or more evidence criteria are missing or weak, but no disqualifying anti‑pattern is found.
-- **rejected** – Any anti‑pattern from Section 9 is present, or the risk evidence is fundamentally insufficient.
+**Decision logic**
+- **Rejected**: any anti‑pattern is present, or the risk analysis is fundamentally inadequate.  
+- **Sound**: all five evidence items are present *and* no anti‑patterns are detected.  
+- **Needs‑more‑evidence**: at least one evidence item is missing or weak, but no anti‑pattern is found.
 
-**Output**
-Provide the verdict word (“sound”, “needs-more-evidence”, or “rejected”) followed by a concise justification (one or two sentences) that references the most salient criteria or anti‑patterns influencing your decision.
+**Output format**
+Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by a single short justification (one or two sentences) that cites the most decisive evidence or anti‑pattern.
 
-Respond with your verdict and your reasoning.+Example:  
+`sound – pilot testing demonstrated 99 % success and a tamper‑evident audit log is provided.`
+
+Proceed to read the submission and apply the above rules.
```

### Island 3, cell (0, 5), scalar 0.7033

parent `94f6dfd55748115c` -> candidate `1d2f12e4904c7e1b`

```diff
--- parent 94f6dfd55748115c
+++ candidate 1d2f12e4904c7e1b
@@ -1,26 +1,26 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and produce a judgment that aligns with Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Your assessment must be consistent with **Section 8 (Strategy C – capability‑based opening)** and must ensure none of the **Section 9 anti‑patterns** apply.
 
-**Judgment categories**
-- **sound** – the evidence convincingly demonstrates that the risk is understood and mitigated; the proposal meets all required criteria.
-- **needs‑more‑evidence** – the proposal is plausible but key pieces of evidence are missing or insufficient; further information is required before a final decision.
-- **rejected** – the proposal contains a serious flaw (e.g., violates an anti‑pattern, lacks any testing, provides no audit trail, or poses an unacceptable safety/ security risk).
+**Outcome options**
+- **sound** – all required evidence is present and the solution respects the strategy and avoids anti‑patterns.
+- **needs‑more‑evidence** – the case is plausible but one or more required pieces are missing or only partially shown; no fatal anti‑pattern is detected.
+- **rejected** – a serious problem is found (anti‑pattern present, or essential evidence such as testing, failure‑mode analysis, or auditability is completely absent).
 
-**Evidence checklist (all items should be addressed for a “sound” judgment)**
-1. **Real‑world testing** – description of functional tests, pilot runs, or simulations that validate the automated decision‑making under realistic conditions.
-2. **Failure‑mode analysis** – identification of what could go wrong, associated mitigations, and a clear escalation path if the automation fails.
-3. **Auditability** – evidence that every automated decision is logged with sufficient detail to reconstruct the action and support post‑hoc review.
-4. **Human‑equivalence comparison** – quantitative or qualitative comparison showing that the automated decisions are at least as safe and effective as those made by a trained human operator.
-5. **Compliance with Section 8** – explicit reference to the capability‑based opening criteria (e.g., risk‑based thresholds, fallback mechanisms).
-6. **Absence of Section 9 anti‑patterns** – confirm that none of the listed anti‑patterns (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”) apply to the proposed solution.
+**Evidence that must be addressed**
+1. **Real‑world validation** – functional tests, pilots, or high‑fidelity simulations demonstrating the automation works under normal and edge conditions.  
+2. **Failure‑mode & mitigation** – clear identification of possible failure modes, associated mitigations, and an escalation/fallback plan.  
+3. **Audit trail** – logging that captures every automated decision with enough detail to reconstruct the event later.  
+4. **Human‑equivalence** – quantitative or qualitative comparison showing the automation is at least as safe/effective as a trained human operator.  
+5. **Section 8 compliance** – explicit reference to the capability‑based opening criteria (risk thresholds, fallback mechanisms, etc.).  
+6. **No Section 9 anti‑patterns** – confirm the design does not exhibit any listed anti‑pattern (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”).
 
-**Decision rules**
-- If **all six checklist items** are satisfied and no anti‑pattern is present → **sound**.
-- If **most** items are addressed but one or more are missing or only partially demonstrated, and no anti‑pattern is triggered → **needs‑more‑evidence**.
-- If **any** anti‑pattern is present, or if critical items (testing, failure‑mode analysis, or auditability) are completely absent → **rejected**.
+**Decision logic**
+- **sound** – items 1‑6 are all satisfied and no anti‑pattern is identified.  
+- **needs‑more‑evidence** – most items are satisfied but one or more are missing or only partially demonstrated, and no anti‑pattern is triggered.  
+- **rejected** – any anti‑pattern is present, or any of the critical items (1, 2, 3) are entirely missing.
 
-**Response format (must be followed exactly)**
+**Required output (exactly two lines)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief, point‑by‑point explanation referencing the checklist items above>
+Reasoning: <concise, point‑by‑point reference to the numbered items above>
 ```
-Provide the verdict on the first line, then a concise rationale on the second line. Do not add any other text, headings, or formatting.+Place the verdict on the first line and a brief rationale on the second line. Do not add any other text.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
