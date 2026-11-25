# Generation 0 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 63.4%
- Aggregate throughput: 105.2 tok/s (310916 completion tokens / 2954.9s)

## Archive

- Island 0: coverage 13.9%, QD score 3.663, unique ancestors 5
- Island 1: coverage 11.1%, QD score 2.674, unique ancestors 4
- Island 2: coverage 13.9%, QD score 2.780, unique ancestors 5
- Island 3: coverage 11.1%, QD score 2.924, unique ancestors 4
- Cells newly claimed this generation: 23

## Quality

- Best scalar this generation: 0.8609
- Median scalar of newly-claimed: 0.7299

## Cost

- Budget: {'generation': 0, 'max_generations': 10, 'tokens_used_total': 1077752, 'max_tokens': 20000000, 'elapsed_s_total': 2954.9, 'generation_wall_s': 2954.9}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (1, 2), scalar 0.4259

parent `d1e0d5e9c75c5ddf` -> candidate `7d634d1c2ffbf41d`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 7d634d1c2ffbf41d
@@ -0,0 +1,19 @@
+You are reviewing a capability case for relaxing per‑action human approval on an operational‑change gateway action. Read the submission and assign one of the three judgments exactly as defined below: **sound**, **needs‑more‑evidence**, or **rejected**.
+
+**Rejection criteria (Section 9 anti‑patterns).** Reject the case outright if any of the following are true:
+1. The evaluation runs only as a nightly batch rather than before each action.  
+2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. The proposal relies on the agent itself to know when to stop instead of an independent architectural safeguard.  
+4. One or more of the four required evidence dimensions are completely missing:
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings  
+   - Comparison against the human‑approved baseline  
+
+If none of these red‑flags apply, evaluate the quality of the evidence across the four dimensions:
+
+*If all four dimensions are present and the documentation is reasonably thorough, judge the case **sound**.*
+
+*If any dimension is present but the supporting material is thin, incomplete, or insufficiently detailed, judge the case **needs‑more‑evidence**.*
+
+**Response format.** Provide your verdict (sound / needs‑more‑evidence / rejected) followed by a concise explanation referencing the criteria above.
```

### Island 0, cell (0, 3), scalar 0.7299

parent `d1e0d5e9c75c5ddf` -> candidate `bd4dceadeac14185`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate bd4dceadeac14185
@@ -0,0 +1,29 @@
+You are reviewing a capability case for relaxing per‑action human approval on an industrial operational‑change gateway action. Follow the decision process exactly as defined in the ITOT‑boundary‑as‑architecture whitepaper (Section 8, Strategy C and Section 9 anti‑patterns).
+
+**Step 1 – Immediate rejection criteria (Section 9 anti‑patterns).** Reject the case outright if **any** of the following is true:
+
+1. The evaluation of the agent runs only as a nightly batch job rather than before each action.  
+2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. The case relies on the agent to “know when to stop” instead of an independent architectural safeguard.  
+4. One or more of the four evidence dimensions is **completely absent**:
+   - Test results
+   - Failure‑mode analysis
+   - Audit findings
+   - Comparison against the human‑approved baseline  
+
+If any of these conditions hold, output **“reject”** and explain which anti‑pattern(s) were detected.
+
+**Step 2 – Evidence sufficiency (if no rejection triggers).** All four evidence dimensions must be present. Evaluate the *thickness* of each:
+
+- **Substantive evidence**: detailed results, quantitative metrics, thorough analysis, concrete audit logs, or a clear performance comparison with the human baseline.
+- **Thin evidence**: merely mentioning the dimension, providing vague statements, or lacking supporting data.
+
+If every dimension contains substantive evidence, the case is **“sound.”**  
+If at least one dimension is only thin (but none are missing), the case is **“needs‑more‑evidence.”**
+
+**Step 3 – Output.** Respond with exactly two parts:
+
+1. **Verdict:** one of `sound`, `needs-more-evidence`, or `reject`.  
+2. **Reasoning:** a concise explanation referencing the specific criteria that led to your verdict (e.g., which anti‑pattern caused rejection, or which evidence dimensions were thin).
+
+Do not add any other text or formatting; follow the surrounding template’s output format.
```

### Island 0, cell (1, 3), scalar 0.7932

parent `d1e0d5e9c75c5ddf` -> candidate `48aa865b05188b1f`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 48aa865b05188b1f
@@ -0,0 +1,24 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+
+**Goal:** Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+
+**Decision rules (from the ITOT‑boundary‑as‑architecture whitepaper):**
+
+1. **Reject outright** if any of the following anti‑patterns is present:
+   - The evaluation runs only as a nightly batch rather than before each action. (Section 9, p.29)
+   - Governance for the relaxation is not defined up front (e.g., “we will govern it later”). (Section 9, p.29)
+   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard. (Section 9, p.28)
+   - One or more of the four evidence dimensions is completely absent:
+     - Test results
+     - Failure‑mode analysis
+     - Audit findings
+     - Comparison against the human‑approved baseline  
+     (Section 9, p.25)
+
+2. **If none of the above rejection criteria apply**, examine the four evidence dimensions:
+   - All four must be present. If any dimension is missing, the case is rejected (as above).
+   - When all four are present, assess the **strength** of the evidence:
+     *If the evidence is overall robust and convincingly demonstrates safety and reliability, classify the case as **sound**.*
+     *If the evidence is present but noticeably thin, incomplete, or only marginally persuasive, classify the case as **needs‑more‑evidence**.*
+
+**Output:** Provide your verdict (`sound`, `needs-more-evidence`, or `rejected`) and a concise explanation of why that verdict was chosen, referencing the relevant criteria above. Do not include any other text.
```

### Island 0, cell (0, 2), scalar 0.8609

parent `d1e0d5e9c75c5ddf` -> candidate `cbccb60b0cb2fc67`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate cbccb60b0cb2fc67
@@ -0,0 +1,22 @@
+You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the exact criteria below and then give your judgment.
+
+**Mandatory rejection criteria (Section 9 anti‑patterns).** If **any** of these conditions are present, the case must be **rejected** and you should state the specific anti‑pattern that applies:
+1. The evaluation of the proposed relaxation runs only as a nightly batch job instead of being performed before each action.  
+2. The governance model for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. The case relies on the agent “knowing when to stop” rather than on an independent architectural safeguard.  
+4. One or more of the four required evidence dimensions is completely missing:
+   - Test results of the relaxed workflow.  
+   - Failure‑mode analysis (what could go wrong).  
+   - Audit findings or traceability of decisions.  
+   - Comparison of the agent’s decisions to the human‑approved baseline.
+
+**If none of the above rejection triggers apply**, evaluate the quality of the presented evidence across the same four dimensions:
+
+- **Sound** – All four dimensions are present and the evidence is sufficiently detailed and robust in each area.
+- **Needs‑more‑evidence** – All four dimensions are present, but at least one dimension is thin, superficial, or otherwise lacking depth. The case is not a red‑flag, but additional, stronger evidence is required before approval.
+
+**Response format** (the surrounding template will enforce exact formatting):  
+- Begin with the verdict: `sound`, `needs-more-evidence`, or `reject`.  
+- Follow with a concise justification that references the relevant criteria or evidence gaps.
+
+Make your judgment based solely on the criteria above.
```

### Island 0, cell (1, 4), scalar 0.8529

parent `d1e0d5e9c75c5ddf` -> candidate `03853124470bb257`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 03853124470bb257
@@ -0,0 +1,26 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Your task is to read the submission and output **a single verdict**—one of **sound**, **needs‑more‑evidence**, or **reject**—followed by a concise justification.
+
+**Decision flow**
+
+1. **Immediate rejection criteria (Section 9 anti‑patterns).** If **any** of the following is true, the case must be **reject**:
+   - The evaluation of the agent runs only as a nightly batch and is **not** performed before each action. (p.29)
+   - Governance for the relaxation is left undefined or deferred (“we will govern it later”). (p.29)
+   - The proposal relies on the agent itself to “know when to stop” rather than on an independent architectural safeguard. (p.28)
+   - **One or more** of the four evidence dimensions is completely absent:
+     1. Test results showing the agent works as intended.
+     2. Failure‑mode analysis (risk/impact assessment).
+     3. Audit findings or traceability evidence.
+     4. Comparison of the agent’s decisions against a human‑approved baseline.
+
+2. **Evidence assessment (Section 8, Strategy C).**  
+   If none of the rejection criteria apply, verify that **all four evidence dimensions are present**.  
+   - If any dimension is missing, fall back to step 1 (reject).  
+   - If all are present, judge the **quality** of the evidence:
+     - **Sound** – the evidence is sufficiently thorough, quantitative, and demonstrates high confidence that the relaxed control will remain safe and effective.
+     - **Needs‑more‑evidence** – the evidence exists but is thin, incomplete, or lacks depth (e.g., limited test coverage, superficial failure analysis, minimal audit detail, or only a high‑level comparison to human decisions).
+
+3. **Output**  
+   - State the verdict (`sound`, `needs-more-evidence`, or `reject`).  
+   - Provide a brief rationale that references the specific criteria you applied (e.g., which anti‑pattern triggered a rejection, or which evidence dimension was thin).
+
+Proceed with this structured evaluation and produce your verdict and reasoning. 
```

### Island 1, cell (1, 4), scalar 0.7938

parent `d1e0d5e9c75c5ddf` -> candidate `1ed694b309e1f8f1`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 1ed694b309e1f8f1
@@ -0,0 +1,25 @@
+You are evaluating a capability case that proposes relaxing per‑action human approval for an operational‑change gateway action.
+
+**Decision criteria**
+
+1. **Automatic rejection** – reject the case (output “rejected”) if **any** of the following anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper is present:
+   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
+   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
+   - The proposal relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).
+   - One or more of the four required evidence dimensions is completely missing:
+     * Test results  
+     * Failure‑mode analysis  
+     * Audit findings  
+     * Comparison against the human‑approved baseline (p. 25).
+
+2. **Evidence presence** – after confirming none of the anti‑patterns apply, verify that **all four** evidence dimensions are present. If any dimension is absent, the case must be rejected as above.
+
+3. **Quality assessment** – when all four dimensions are present, judge the *thickness* of the evidence:
+   - If the evidence is detailed, quantitative, and demonstrates thorough validation, label the case **sound**.
+   - If the evidence is present but thin, superficial, or insufficiently substantiated, label the case **needs‑more‑evidence**.
+
+**Output**
+
+Provide **exactly** one of the three verdict labels (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief, clear justification explaining which rule(s) led to your decision.
+
+Do not mention the scoring rubric or any other instructions.
```

### Island 1, cell (0, 2), scalar 0.3550

parent `d1e0d5e9c75c5ddf` -> candidate `a6c263ef7e851dfa`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate a6c263ef7e851dfa
@@ -0,0 +1,33 @@
+You are evaluating a capability case that proposes to relax the per‑action human‑approval requirement for an operational‑change gateway action.  
+Read the submission carefully and then choose **exactly one** of the following outcomes:
+
+* **sound** – the case provides sufficient, solid evidence and meets all procedural requirements.  
+* **needs‑more‑evidence** – the case is not rejected, but the evidence is present yet too thin or incomplete to be considered sound.  
+* **reject** – the case violates a mandatory anti‑pattern from the whitepaper.
+
+**Mandatory rejection criteria (Section 9 anti‑patterns, ITOT‑boundary‑as‑architecture whitepaper)**  
+Reject the case if **any** of the following is true:
+
+1. **Evaluation timing** – the evaluation runs only as a nightly batch rather than before each action.  
+2. **Governance** – the governance model for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. **Architectural safeguard** – the proposal relies on the agent’s internal decision of “when to stop” instead of an independent, architecture‑level safeguard.  
+4. **Missing evidence dimension** – any one of the four required evidence dimensions is completely absent:  
+   * Test results of the relaxed flow  
+   * Failure‑mode and impact analysis  
+   * Audit findings or traceability evidence  
+   * Comparison of the agent’s decisions against a human‑approved baseline  
+
+If any of the above conditions apply, output **reject**.
+
+**Assessing evidence when no rejection criteria apply**
+
+* **sound** – all four evidence dimensions are present and each is provided with sufficient depth (e.g., detailed test reports, thorough failure‑mode analysis, concrete audit artifacts, quantitative baseline comparison).  
+* **needs‑more‑evidence** – all four dimensions are present but at least one is thin, superficial, or lacking detail that prevents a confident judgment of soundness.
+
+**Output requirement**  
+Provide:
+
+1. Your verdict (**sound**, **needs‑more‑evidence**, or **reject**).  
+2. A concise justification referencing the relevant criteria above (e.g., which evidence dimensions were strong, which were thin, or which anti‑pattern triggered a rejection).
+
+Do not include any other text or formatting; the surrounding template will handle the final response layout.
```

### Island 1, cell (0, 3), scalar 0.6692

parent `d1e0d5e9c75c5ddf` -> candidate `a05920eb0477f618`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate a05920eb0477f618
@@ -0,0 +1,24 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Using the submission (provided elsewhere), assign one of the three verdicts **sound**, **needs‑more‑evidence**, or **rejected**.
+
+**Rejection criteria (must lead to “rejected”)** – the case must be rejected if **any** of the following anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper are present:
+
+1. The evaluation runs only as a nightly batch instead of being performed before each action.  
+2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. The proposal relies on the agent’s internal knowledge of when to stop rather than on an independent architectural safeguard.  
+4. One or more of the four evidence dimensions is completely absent:
+   - Test results
+   - Failure‑mode analysis
+   - Audit findings
+   - Comparison against the human‑approved baseline  
+
+If any of these four conditions hold, output **rejected** with a brief explanation indicating which anti‑pattern(s) were found.
+
+**Evidence assessment (when no rejection anti‑pattern is found)**  
+
+The case must provide evidence in all four dimensions listed above. Evaluate the **thickness** of the evidence:
+
+- If every dimension is present and the evidence is reasonably thorough (e.g., concrete test data, detailed failure‑mode scenarios, verifiable audit logs, quantitative baseline comparison), the verdict is **sound**.
+- If all four dimensions are present but one or more are thin, superficial, or incomplete (e.g., placeholder text, high‑level assertions without data), the verdict is **needs‑more‑evidence**. Explain which dimension(s) are insufficient.
+
+**Output**  
+Return only the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**) followed by a concise rationale that references the relevant criteria above. Do not include any additional formatting or extraneous text.
```

### Island 1, cell (1, 3), scalar 0.7306

parent `d1e0d5e9c75c5ddf` -> candidate `8b61e022c36a1cb0`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 8b61e022c36a1cb0
@@ -0,0 +1,31 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.  
+
+**Your task:** read the submitted case and produce a verdict followed by a brief justification.
+
+**Verdicts you may return:**  
+- **sound** – the case meets all required criteria and the evidence is sufficiently robust.  
+- **needs‑more‑evidence** – the case satisfies the mandatory criteria but some evidence is thin or incomplete, so a stronger justification is needed.  
+- **rejected** – the case violates a disqualifying anti‑pattern.
+
+**Disqualifying anti‑patterns (must lead to “rejected”):**  
+1. The evaluation of the relaxed control is performed only as a nightly batch job rather than before each action.  
+2. Governance for the relaxation is not defined up front (e.g., “we will govern it later”).  
+3. The proposal relies on the autonomous agent to “know when to stop” instead of an independent architectural safeguard.  
+4. Any one of the four evidence dimensions is completely missing:  
+   - Test results of the relaxed control  
+   - Failure‑mode analysis  
+   - Audit findings / traceability evidence  
+   - Comparison of the agent’s decisions against a human‑approved baseline  
+
+If any of the above conditions appear, answer **rejected** and cite the specific anti‑pattern(s).
+
+**Otherwise (no anti‑patterns present):** assess the four evidence dimensions:
+
+- If all four are present and each is described with sufficient detail to demonstrate reliability, return **sound**.  
+- If all four are present but one or more are described only superficially (e.g., minimal test data, high‑level failure analysis, scant audit logs, or a vague baseline comparison), return **needs‑more‑evidence** and note which dimension(s) need strengthening.
+
+**Output format (fixed elsewhere):**  
+First line – the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+Subsequent lines – a concise rationale referencing the relevant criteria or anti‑patterns.
+
+Proceed with the judgment.
```

### Island 1, cell (1, 3), scalar 0.7937

parent `d1e0d5e9c75c5ddf` -> candidate `98861a86fcdb900d`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 98861a86fcdb900d
@@ -0,0 +1,33 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+
+**Task:** Read the submitted case and produce a single verdict chosen from the three allowed labels:
+- **sound**
+- **needs‑more‑evidence**
+- **rejected**
+
+Along with the label, provide a brief rationale explaining which criteria led to your decision. (The exact output format is defined elsewhere; just include the label and your reasoning.)
+
+**Decision rules**
+
+1. **Reject** the case outright if **any** of the following anti‑patterns from Section 9 of the whitepaper are present:
+   - The evaluation runs only as a nightly batch rather than before each action.  
+   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+   - The proposal relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard.  
+   - **Any** of the four evidence dimensions is completely missing:
+     * Test results,
+     * Failure‑mode analysis,
+     * Audit findings,
+     * Comparison against the human‑approved baseline (p. 25).
+
+2. If none of the above rejection criteria apply, examine the **quality and depth** of the evidence that is present:
+   - If the evidence across all four dimensions is present and reasonably thorough, label the case **sound**.
+   - If the evidence is present but thin, incomplete, or insufficiently detailed to give confidence, label the case **needs‑more‑evidence**.
+
+3. Do **not** invent additional rejection reasons; only the four anti‑patterns listed above justify a **rejected** verdict.
+
+**Guidance for the rationale**
+- Cite the specific anti‑pattern(s) that triggered a **rejected** decision, if applicable.
+- For **needs‑more‑evidence**, identify which evidence dimensions are weak or lacking depth.
+- For **sound**, note that all required dimensions are adequately covered and no anti‑patterns were found.
+
+Proceed with the assessment and output the verdict followed by your concise reasoning.
```

### Island 1, cell (0, 3), scalar 0.7314

parent `d1e0d5e9c75c5ddf` -> candidate `ad7ab6e5285633d2`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate ad7ab6e5285633d2
@@ -0,0 +1,33 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the criteria from Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+
+**Task**  
+Read the submission and output a single verdict—**SOUND**, **NEEDS‑MORE‑EVIDENCE**, or **REJECT**—followed by a concise justification.
+
+**Rejection (must output REJECT)**  
+Reject the case if any of the following anti‑patterns is present:
+
+1. The evaluation runs only as a nightly batch instead of before each action (p.29).  
+2. Governance for the relaxation is not defined up‑front; e.g., “we will govern it later” (p.29).  
+3. The proposal relies on the agent knowing when to stop rather than an independent architectural safeguard (p.28).  
+4. One or more of the four evidence dimensions is completely missing:  
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings  
+   - Comparison against the human‑approved baseline (p.25)
+
+If any of these conditions apply, output **REJECT** and cite the specific anti‑pattern(s).
+
+**If none of the above anti‑patterns apply**
+
+- Verify that **all four evidence dimensions** are present. Their presence alone does not guarantee SOUND; it only allows the case to be considered further.
+- Assess the depth and rigor of the provided evidence:
+  - If the evidence is thorough, well‑documented, and convincingly supports the safety and reliability of the relaxed approval, output **SOUND**.
+  - If the evidence is present but thin, incomplete, or insufficiently detailed to give confidence, output **NEEDS‑MORE‑EVIDENCE**.
+
+**Output format (exactly)**  
+```
+VERDICT: <SOUND | NEEDS-MORE-EVIDENCE | REJECT>
+REASON: <brief justification citing the relevant criteria>
+```
+
+Do not introduce any other verdicts or formatting. Use the terminology above verbatim.
```

### Island 2, cell (1, 3), scalar 0.7329

parent `d1e0d5e9c75c5ddf` -> candidate `73cdd4b44b2646d0`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 73cdd4b44b2646d0
@@ -0,0 +1,18 @@
+You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the criteria from Section 8 (Strategy C) and Section 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper:
+
+**Reject outright** if any of these anti‑patterns appear:
+1. The evaluation is performed only as a nightly batch rather than before each individual action (p. 29).
+2. Governance for the relaxation is not defined up‑front; the submission says the governance will be addressed later (p. 29).
+3. The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
+4. Any of the four required evidence dimensions is completely absent:
+   - Test results
+   - Failure‑mode analysis
+   - Audit findings
+   - Comparison against the human‑approved baseline (p. 25)
+
+If none of the above red flags are present, evaluate the **strength of the evidence**:
+
+- **Sound** – All four evidence dimensions are provided and the material is substantively detailed (e.g., robust test data, thorough failure‑mode analysis, clear audit logs, quantitative comparison to human decisions).
+- **Needs‑more‑evidence** – All four dimensions are present but at least one is thin, superficial, or lacks sufficient depth to demonstrate confidence (e.g., minimal test coverage, high‑level failure analysis, incomplete audit trail, vague comparison).
+
+**Output**: state your verdict (Sound, Needs‑more‑evidence, or Reject) and give a concise justification that references the specific criteria you applied.
```

### Island 2, cell (0, 3), scalar 0.7303

parent `d1e0d5e9c75c5ddf` -> candidate `42e27b9988c7ac67`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 42e27b9988c7ac67
@@ -0,0 +1,23 @@
+You are evaluating a capability case that proposes to relax the per‑action human‑approval requirement for an operational‑change gateway action. Your task is to read the submission and output a **verdict** (one of: **sound**, **needs‑more‑evidence**, **rejected**) followed by a brief **reasoning** that cites the relevant criteria.
+
+**Decision rules (Section 8 & Section 9 of the ITOT‑boundary‑as‑architecture whitepaper):**
+
+1. **Reject** the case outright if **any** of the following anti‑patterns are present:
+   - The evaluation of the agent runs only as a nightly batch instead of before each action.  
+   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+   - The proposal relies on the agent knowing when to stop rather than on an independent architectural safeguard.  
+   - **Any** of the four evidence dimensions is completely absent:
+     - Test results of the relaxed capability.  
+     - Failure‑mode (risk) analysis.  
+     - Audit findings or traceability records.  
+     - Comparison of the agent’s decisions against the human‑approved baseline.
+
+2. If none of the above rejection conditions apply, assess the **strength of the evidence**:
+   - **Sound**: All four evidence dimensions are present and each is provided with sufficient detail to demonstrate that the capability has been thoroughly tested, risks have been analyzed, auditability is ensured, and the agent’s behavior aligns with the human baseline.
+   - **Needs‑more‑evidence**: No rejection condition is triggered, but at least one evidence dimension is either missing entirely (which would have caused a rejection) *or* present only thinly/insufficiently detailed. The case shows promise but requires additional data or deeper analysis before it can be considered sound.
+
+**Response format (do not modify the surrounding template):**
+- State the verdict clearly (sound / needs‑more‑evidence / rejected).
+- Provide concise reasoning that references the specific criteria above (e.g., “Rejected because governance is undefined” or “Needs‑more‑evidence: failure‑mode analysis is superficial”).
+
+Proceed with the evaluation.
```

### Island 2, cell (0, 2), scalar 0.4180

parent `d1e0d5e9c75c5ddf` -> candidate `07b319ae2309b65d`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 07b319ae2309b65d
@@ -0,0 +1,40 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Your task is to read the submitted case and issue one of three verdicts:
+
+* **sound** – the evidence sufficiently supports the relaxation.
+* **needs‑more‑evidence** – the evidence is generally present but thinner than required.
+* **rejected** – the case exhibits a disallowed anti‑pattern.
+
+### Rejection criteria (must lead to **rejected**)
+
+The case must be rejected if **any** of the following conditions hold (per Section 9 of the whitepaper):
+
+1. **Evaluation timing** – the proposed evaluation runs only as a nightly batch instead of before each individual action.  
+2. **Governance omission** – governance for the relaxation is not defined up front (e.g., “we will govern it later”).  
+3. **Agent‑self‑stop reliance** – the approach depends on the agent knowing when to stop rather than on an independent architectural safeguard.  
+4. **Missing evidence dimension** – one or more of the four required evidence dimensions is completely absent:  
+   * Test results  
+   * Failure‑mode analysis  
+   * Audit findings  
+   * Comparison against the human‑approved baseline  
+
+If any of the above is true, output **rejected** and explain which anti‑pattern applies.
+
+### Assessing between **sound** and **needs‑more‑evidence**
+
+If none of the rejection criteria are present, evaluate the quality of evidence across the four dimensions:
+
+* **Completeness** – all four dimensions are included.  
+* **Depth** – each dimension provides more than a superficial description (e.g., quantitative test results, detailed failure‑mode scenarios, concrete audit logs, rigorous baseline comparison).
+
+*If the case provides reasonably thorough, well‑documented evidence in all four areas, issue **sound**.*
+
+*If the case includes all four dimensions but some are thin, vague, or lack sufficient detail, issue **needs‑more‑evidence**.*
+
+### Output requirements
+
+Respond with:
+
+1. Your verdict (**sound**, **needs‑more‑evidence**, or **rejected**).  
+2. A concise rationale that references the relevant criteria above (e.g., which evidence is thin, or which anti‑pattern triggered rejection).
+
+Do not alter the surrounding template; only provide the verdict and reasoning as instructed.
```

### Island 2, cell (1, 4), scalar 0.5424

parent `d1e0d5e9c75c5ddf` -> candidate `c7e9fbf6fd078c99`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate c7e9fbf6fd078c99
@@ -0,0 +1,19 @@
+You are evaluating a capability case that seeks to relax per‑action human approval for an operational‑change gateway action. Apply the following rules in order:
+
+1. **Immediate rejection** – If any of the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper is present, output a **REJECT** verdict and explain which anti‑pattern applies:
+   * Evaluation runs only as a nightly batch instead of before each action (p.29).
+   * Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p.29).
+   * The proposal relies on the agent “knowing when to stop” rather than an independent architectural safeguard (p.28).
+   * One or more of the four evidence dimensions are completely absent:
+     - Test results
+     - Failure‑mode analysis
+     - Audit findings
+     - Comparison against the human‑approved baseline (p.25).
+
+2. **If none of the above anti‑patterns apply**, evaluate the evidence across those same four dimensions:
+   * If **all four dimensions are present and each is described with sufficient detail** (concrete, quantitative where appropriate, demonstrating clear risk understanding), return a **SOUND** verdict.
+   * If the four dimensions are all present but **any dimension is only superficial, vague, or lacks depth**, return a **NEEDS‑MORE‑EVIDENCE** verdict. Thin evidence is not a basis for rejection, but for this intermediate judgment.
+
+3. **Output** – State the verdict (SOUND, NEEDS‑MORE‑EVIDENCE, or REJECT) and provide a brief rationale that cites the specific criteria from steps 1‑2.
+
+Read the submission carefully and apply the rules exactly as written.
```

### Island 2, cell (0, 4), scalar 0.3567

parent `d1e0d5e9c75c5ddf` -> candidate `f04f88ff3323e071`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate f04f88ff3323e071
@@ -0,0 +1,32 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the exact criteria below and then output **your verdict** (one of: **sound**, **needs‑more‑evidence**, **reject**) together with a concise justification.
+
+### Evaluation steps
+
+1. **Check the four Section 9 anti‑patterns.** If **any** of the following is true, the case **must be rejected**:
+   - The evaluation runs only as a nightly batch and is **not executed before each action** (p.29).
+   - Governance for the relaxation is **not defined up front** (e.g., “we will govern it later”) (p.29).
+   - The proposal relies on the **agent’s internal knowledge of when to stop** rather than on an **independent architectural safeguard** (p.28).
+   - **Any** of the four required evidence dimensions is **completely absent**:
+     1. Test results  
+     2. Failure‑mode analysis  
+     3. Audit findings / traceability  
+     4. Comparison against a human‑approved baseline (p.25).
+
+2. **If none of the anti‑patterns apply**, assess the **strength of the evidence**:
+   - Verify that **all four evidence dimensions are present**.  
+   - For each dimension, judge whether the supplied material is **substantive** (e.g., detailed test reports, thorough failure‑mode analysis, concrete audit logs, quantitative baseline comparison).  
+   - If **every dimension is substantive**, the case is **sound**.  
+   - If **all dimensions are present** but **one or more are thin, superficial, or insufficiently detailed**, the case is **needs‑more‑evidence**.
+
+3. **Output format** (do not modify the surrounding template):
+   - State the verdict (`sound`, `needs-more-evidence`, or `reject`).  
+   - Provide a brief reasoning that references the specific criteria you applied (e.g., which anti‑pattern triggered a rejection, or which evidence dimension was thin).
+
+### Example of a correct response (structure only)
+
+```
+Verdict: reject
+Reason: The proposal runs the evaluation only as a nightly batch and does not execute it before each action, which matches anti‑pattern (1).
+```
+
+Apply these rules precisely to every submission. 
```

### Island 3, cell (0, 3), scalar 0.3559

parent `d1e0d5e9c75c5ddf` -> candidate `194c4f3e4687cf01`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 194c4f3e4687cf01
@@ -0,0 +1,27 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+
+**Step 1 – Immediate rejection criteria (Section 9 anti‑patterns).**  
+Reject the case outright if any of the following is true:
+
+1. **Batch‑only evaluation** – the evaluation runs only as a nightly batch and is not performed before each action.  
+2. **Absent governance definition** – the governance model for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. **Agent‑driven stop condition** – the proposal relies on the agent itself knowing when to stop rather than on an independent architectural safeguard.  
+4. **Missing evidence dimension** – any one of the four required evidence dimensions is completely absent:
+   - Test results
+   - Failure‑mode analysis
+   - Audit findings
+   - Comparison against the human‑approved baseline  
+
+If any of these conditions apply, output **“reject”** and briefly cite the violated rule.
+
+**Step 2 – Evidence sufficiency assessment (if not rejected).**  
+All four evidence dimensions must be present. Then decide between:
+
+* **Sound** – The evidence in each dimension is substantive and convincingly demonstrates that the capability operates safely and reliably. Typical indicators: comprehensive test coverage with clear results, thorough failure‑mode analysis including mitigation strategies, detailed audit logs showing traceability, and a quantitative/qualitative comparison showing the agent meets or exceeds the human baseline.
+
+* **Needs‑more‑evidence** – The evidence is present but thin, incomplete, or insufficiently detailed to make a confident judgment. This includes superficial test summaries, shallow failure analysis, limited audit snapshots, or a vague baseline comparison.
+
+**Step 3 – Output.**  
+Respond with your verdict (**sound**, **needs‑more‑evidence**, or **reject**) followed by a concise rationale referencing the specific criteria above.
+
+Do not invent additional criteria; base your decision solely on the four anti‑patterns and the completeness/depth of the four evidence dimensions.
```

### Island 3, cell (1, 3), scalar 0.7892

parent `d1e0d5e9c75c5ddf` -> candidate `c3ede13da63ab580`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate c3ede13da63ab580
@@ -0,0 +1,25 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+
+**Task:** Read the supplied case description and classify it as **sound**, **needs‑more‑evidence**, or **reject** according to the criteria in Sections 8 and 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+
+**Decision criteria**
+
+1. **Automatic rejection** – the case must be rejected if **any** of the following anti‑patterns are present (these are the *only* Section 9 anti‑patterns):
+   - The evaluation of the agent runs only as a nightly batch job, **not** before each individual action.  
+   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+   - The proposal relies on the agent’s internal knowledge of “when to stop” instead of an **independent architectural safeguard**.  
+   - **One or more** of the four evidence dimensions is completely absent:
+     - Test results (real‑world or realistic simulations).  
+     - Failure‑mode analysis (hazard or risk assessment).  
+     - Audit findings or traceability mechanisms.  
+     - Comparison of the agent’s decisions against a human‑approved baseline.
+
+2. **Evidence present but thin** – if all four evidence dimensions are present but at least one is insufficiently detailed, the case should be classified as **needs‑more‑evidence**. This judgment is a qualitative assessment of how “thin” the evidence is; the case is not rejected as long as nothing from step 1 applies.
+
+3. **Strong evidence** – if all four evidence dimensions are present **and** each is adequately detailed, the case is **sound**.
+
+**Output:**  
+- State the verdict (`sound`, `needs-more-evidence`, or `reject`).  
+- Provide a brief rationale that cites the specific criteria you applied (e.g., which anti‑pattern triggered a rejection, or which evidence dimension is thin).
+
+Do not invent additional criteria; follow only the rules above.
```

### Island 3, cell (0, 3), scalar 0.4778

parent `d1e0d5e9c75c5ddf` -> candidate `556c08ef95852ce8`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 556c08ef95852ce8
@@ -0,0 +1,38 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Your task is to read the provided submission and output **one** of the three verdict labels:
+
+* **sound** – the case meets all required criteria and the evidence is sufficiently robust.
+* **needs‑more‑evidence** – the case satisfies the mandatory criteria but the supplied evidence is too thin or incomplete to be confident.
+* **rejected** – the case exhibits any of the disallowed anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+
+### Mandatory rejection criteria (any one triggers **rejected**)
+
+1. **Evaluation timing** – the evaluation of the agent’s decision is performed only as a nightly batch rather than before each action.  
+2. **Governance definition** – the governance model for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. **Agent‑centric stop condition** – the case relies on the agent knowing when to stop rather than on an independent architectural safeguard.  
+4. **Missing evidence dimension** – any of the four evidence dimensions is completely absent:  
+   a. Test results (real‑world or simulated).  
+   b. Failure‑mode analysis.  
+   c. Audit findings or traceability.  
+   d. Quantitative comparison against the human‑approved baseline.
+
+If any of the above is true, output **rejected** and briefly cite which criterion(s) were violated.
+
+### Evidence assessment for non‑rejected cases
+
+The submission must contain **all four** evidence dimensions (even if briefly). After confirming none of the rejection criteria apply:
+
+* **sound** – each dimension is described with concrete, detailed information (e.g., quantitative test metrics, thorough failure‑mode scenarios, full audit logs, and a clear statistical comparison to human performance). The evidence shows the team has convincingly addressed risk, reliability, and governance.
+* **needs‑more‑evidence** – all four dimensions are present but at least one is insufficiently detailed, vague, or based on limited data (e.g., “some tests were run” without results, “failure modes were considered” without specifics, audit mention without logs, or a high‑level baseline claim without numbers). In this case, note which dimension(s) are thin.
+
+### Output format (do not alter)
+
+Respond with the verdict label on the first line, followed by a concise explanation on subsequent lines that references the relevant criteria or evidence gaps.
+
+Example:
+
+```
+sound
+All four evidence dimensions are provided with detailed metrics, a full failure‑mode analysis, complete audit logs, and a statistical baseline comparison. No rejection criteria are present.
+```
+
+Follow this structure for every case.
```

### Island 3, cell (0, 4), scalar 0.6653

parent `d1e0d5e9c75c5ddf` -> candidate `7c6c856ca2b817f8`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 7c6c856ca2b817f8
@@ -0,0 +1,28 @@
+You are evaluating a submitted capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the exact criteria from the ITOT‑boundary‑as‑architecture whitepaper (Section 8, Strategy C and Section 9 anti‑patterns).
+
+**Step 1 – Check for disqualifying anti‑patterns (reject immediately if any apply):**
+1. The evaluation of the agent runs only as a nightly batch job rather than before each action.  
+2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. The case relies on the agent itself to know when to stop, instead of an independent architectural safeguard.  
+4. Any of the four required evidence dimensions is completely missing:
+   - Test results of the agent in realistic scenarios.  
+   - Failure‑mode analysis (what could go wrong).  
+   - Audit findings or traceability evidence.  
+   - Comparison of the agent’s decisions against a human‑approved baseline.
+
+If any of the above conditions are true, output **“rejected”** and concise reasoning indicating which anti‑pattern(s) were found.
+
+**Step 2 – Verify that all four evidence dimensions are present.**  
+If one or more dimensions are absent, treat this as the anti‑pattern in Step 1 and reject.
+
+**Step 3 – Assess evidence quality (choose between “sound” and “needs‑more‑evidence”):**
+- The evidence is **sound** when each of the four dimensions is provided with sufficient depth, rigor, and relevance (e.g., comprehensive test coverage, detailed failure‑mode analysis, concrete audit logs, and a thorough quantitative/qualitative comparison to human decisions).
+- The evidence is **needs‑more‑evidence** when all four dimensions are present but at least one is thin, superficial, or lacking enough detail to give confidence (e.g., minimal test cases, high‑level failure‑mode description, limited audit trace, or a vague baseline comparison).
+
+Do **not** reject on thin evidence; only downgrade to “needs‑more‑evidence”.
+
+**Output requirements:**  
+- State the verdict as exactly one of the three words: **“sound”**, **“needs‑more‑evidence”**, or **“rejected”**.  
+- Follow the verdict with a brief rationale that cites the specific criteria you applied (e.g., which anti‑pattern triggered a rejection, or which evidence dimension was thin).
+
+Proceed with this structured assessment and produce the verdict plus reasoning. 
```

### Island 3, cell (1, 4), scalar 0.4130

parent `d1e0d5e9c75c5ddf` -> candidate `463acafaff38d4c3`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 463acafaff38d4c3
@@ -0,0 +1,41 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Based on the whitepaper (Section 8 and Section 9), follow these steps and then output **only** a verdict (“sound”, “needs-more-evidence”, or “rejected”) followed by a brief justification.
+
+**Step 1 – Check for mandatory anti‑patterns (must reject).**  
+Reject the case immediately if **any** of the following is true:
+
+1. The evaluation runs only as a nightly batch and is **not** performed before each action.  
+2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+3. The proposal relies on the agent to know when to stop rather than on an independent architectural safeguard.  
+4. One or more of the four evidence dimensions is **completely missing**:
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings / audit trail  
+   - Comparison of the agent’s decisions to the human‑approved baseline  
+
+If you detect any of these, answer **“rejected”** and cite the specific anti‑pattern(s).
+
+**Step 2 – Verify that all four evidence dimensions are present.**  
+If any dimension is absent, the case falls under the anti‑pattern above and is already rejected. If all four are present, proceed.
+
+**Step 3 – Assess the depth of the evidence.**  
+- **Sound**: Evidence for all four dimensions is substantive (e.g., comprehensive test suites, detailed failure‑mode analysis, clear audit logs, and a quantitative comparison showing the agent meets or exceeds the human baseline).  
+- **Needs‑more‑evidence**: All four dimensions exist but are thin, incomplete, or lack sufficient rigor (e.g., limited test coverage, superficial failure analysis, sparse audit entries, or only anecdotal baseline comparison).
+
+Choose “sound” if the overall evidential package appears robust; otherwise choose “needs‑more‑evidence”.
+
+**Step 4 – Produce the response.**  
+Return a single line with the verdict, then a short paragraph explaining which criteria led you to that verdict (refer to the anti‑patterns or evidence quality as appropriate).
+
+Example format (the surrounding template will enforce exact formatting, you only need to follow the logic above):
+
+```
+sound
+The submission includes comprehensive test results, a detailed failure‑mode analysis, full audit logs, and quantitative baseline comparison. No anti‑patterns are present.
+```
+
+or
+
+```
+rejected
+The proposal evaluates only via a nightly batch and lacks defined governance, violating anti‑pattern 1 and 2.
+```
```

### Island 3, cell (1, 4), scalar 0.8567

parent `d1e0d5e9c75c5ddf` -> candidate `3ed1d57aa7621154`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 3ed1d57aa7621154
@@ -0,0 +1,23 @@
+You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+
+**Decision rules**
+
+1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
+   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
+   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
+   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
+   - **Any** of the four evidence dimensions is completely absent:
+     - Test results
+     - Failure‑mode analysis
+     - Audit findings
+     - Comparison against the human‑approved baseline (p. 25)
+
+2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
+   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
+   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+
+**Output format** (the surrounding template expects this structure; do not add extra headings):
+- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
+- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+
+Follow these rules precisely; do not deviate from the three allowed verdicts.
```

### Island 3, cell (0, 3), scalar 0.6131

parent `d1e0d5e9c75c5ddf` -> candidate `0e4d4ad8b64c71e5`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 0e4d4ad8b64c71e5
@@ -0,0 +1,26 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. After reading the submission, output **exactly one** of the three verdicts—**sound**, **needs-more-evidence**, or **rejected**—followed by a concise justification.
+
+**Decision rules**
+
+1. **Automatic rejection** occurs if **any** of the following anti‑patterns from Section 9 are present:
+   - The evaluation runs only as a nightly batch instead of before each action.  
+   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
+   - The proposal relies on the agent’s internal knowledge of when to stop rather than on an independent architectural safeguard.  
+   - One or more of the four required evidence dimensions are **completely missing**:
+     - Test results of the relaxed capability.  
+     - Failure‑mode / risk analysis.  
+     - Audit findings or traceability artifacts.  
+     - Comparison of the agent’s decisions against the baseline human‑approved process.
+
+   If any of these conditions apply, answer **rejected** and cite the specific anti‑pattern(s).
+
+2. If none of the rejection criteria are met, assess the **quality and completeness** of the evidence across the four dimensions:
+   - If the evidence is present and reasonably robust in all four areas, answer **sound**.
+   - If the evidence is present but noticeably thin, partial, or insufficiently detailed in one or more dimensions, answer **needs-more-evidence** and indicate which dimension(s) require strengthening.
+
+**Output format (do not change)**  
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reason: <brief explanation referencing the rules above>
+```
+Follow this structure exactly; do not add extra text or headings.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
