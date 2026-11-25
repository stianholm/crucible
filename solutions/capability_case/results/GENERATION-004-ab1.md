# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 61.7%
- Aggregate throughput: 94.4 tok/s (220256 completion tokens / 2333.2s)

## Archive

- Island 0: coverage 25.0%, QD score 4.362, unique ancestors 3
- Island 1: coverage 30.6%, QD score 5.033, unique ancestors 6
- Island 2: coverage 27.8%, QD score 4.612, unique ancestors 5
- Island 3: coverage 30.6%, QD score 5.643, unique ancestors 3
- Cells newly claimed this generation: 9

## Quality

- Best scalar this generation: 0.8435
- Median scalar of newly-claimed: 0.4938

## Cost

- Budget: {'generation': 4, 'max_generations': 10, 'tokens_used_total': 3077292, 'max_tokens': 8000000, 'elapsed_s_total': 12958.1, 'generation_wall_s': 2333.2}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 3), scalar 0.4938

parent `060ae7274728484b` -> candidate `c22c6c9a5214ee78`

```diff
--- parent 060ae7274728484b
+++ candidate c22c6c9a5214ee78
@@ -1,26 +1,26 @@
-You are an expert reviewer assessing a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action, as defined in Section 8 (Strategy C, capability‑based opening) and evaluated against the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer tasked with judging a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Your assessment must follow Section 8 (Strategy C, capability‑based opening) and be checked against the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Checklist**
 
-1. **Evidence of real‑world testing** – Has the team performed controlled trials or production‑like simulations? Include details of test scope, environment, and results.  
-2. **Failure‑mode analysis** – Does the submission identify plausible ways the automation could fail, and propose mitigations or safe‑fallbacks?  
-3. **Audit‑trail provision** – Is there a mechanism to record decisions, inputs, and outcomes that can be reviewed later?  
-4. **Human‑parity comparison** – Are the agent’s decisions benchmarked against human operators, with quantitative or qualitative evidence of comparable performance?  
-5. **Anti‑pattern screening (Section 9)** – Verify that none of the following critical issues are present:
-   - Over‑automation without clear rollback or manual override.
-   - Absence of a bounded safety case.
-   - Reliance on opaque or non‑explainable AI decisions.
-   - Missing monitoring or alerting for out‑of‑spec behavior.
-   - Inadequate segregation of duties or conflict‑of‑interest hazards.
+| # | Item to verify | What constitutes **full compliance** | What counts as **partial** | What is a **critical failure** |
+|---|----------------|--------------------------------------|----------------------------|--------------------------------|
+| 1 | Real‑world testing | Controlled trials or production‑like simulations with documented scope, methodology, and results | Some testing reported but missing scope, results, or realism | No testing at all |
+| 2 | Failure‑mode analysis | Comprehensive list of plausible failures, their likelihood/impact, and mitigations or safe‑fallback actions | List exists but is vague or missing mitigations | No analysis or ignores high‑impact failures |
+| 3 | Audit‑trail / observability | Tamper‑evident logging of inputs, decisions, outcomes, and a way to query the log later | Logging mentioned but not tamper‑evident or incomplete | No logging mechanism |
+| 4 | Human‑parity benchmark | Quantitative or qualitative comparison showing the automation matches or exceeds expert operators on representative scenarios | Benchmark exists but limited data or unclear metrics | No benchmark or shows inferior performance |
+| 5 | Anti‑pattern screening (Section 9) | None of the listed anti‑patterns appear: <ul><li>Missing manual override/rollback</li><li>Over‑automation without safety case</li><li>Opaque/black‑box AI decisions</li><li>No monitoring or alerting for out‑of‑spec behavior</li><li>Insufficient segregation of duties</li></ul> | One anti‑pattern is mentioned but mitigated | Any anti‑pattern present without adequate mitigation |
 
 **Decision rules**
 
-- **Sound** – All checklist items are satisfied, and no anti‑patterns are detected. The evidence collectively demonstrates that relaxing human approval is justified.  
-- **Needs‑more‑evidence** – One or more checklist items are partially addressed or missing, but no fatal anti‑pattern is present. The proposal requires additional data or clarification before approval.  
-- **Rejected** – Any critical anti‑pattern is identified, or the submission contains a serious red flag (e.g., no fail‑safe, no audit trail, or evidence of unsafe over‑automation). The case must be denied outright.
+* **Rejected** – any item meets the **critical failure** condition, or any anti‑pattern is present without effective mitigation.  
+* **Needs‑more‑evidence** – at least one item is only **partial**, and no critical failure is detected.  
+* **Sound** – all items achieve **full compliance** and no anti‑patterns are detected.
 
-**Output format (must follow the fixed surrounding template)**  
-Provide a concise verdict followed by a brief justification that references the specific checklist items or anti‑patterns influencing your decision.
+**Required output (exactly two lines, no extra characters)**  
 
-Verdict: <sound | needs-more-evidence | rejected>  
-Reasoning: <your concise explanation>+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <brief explanation referencing the checklist numbers and why they led to the verdict>
+```
+
+Provide the verdict and a concise justification that cites the relevant checklist numbers or anti‑patterns.
```

### Island 0, cell (0, 5), scalar 0.6140

parent `c8ded732c79e0522` -> candidate `46d288316a4a29a9`

```diff
--- parent c8ded732c79e0522
+++ candidate 46d288316a4a29a9
@@ -1,32 +1,28 @@
-You are an expert reviewer tasked with judging a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Your assessment must follow Section 8 (Strategy C – capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Your assessment must follow Section 8 (Strategy C – capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Required evidence (all must be present for a **Sound** verdict)
+**Checklist**
 
-1. **Real‑world testing** – documented controlled trials or production‑like simulations, including scope, environment, failure‑injection, and results.  
-2. **Failure‑mode analysis** – identification of plausible failure modes together with mitigation or safe‑fallback measures.  
-3. **Audit trail** – tamper‑evident logging of inputs, decisions, and outcomes that can be reviewed post‑action.  
-4. **Human‑parity benchmark** – quantitative or qualitative comparison of the automation’s decisions against expert human operators, showing comparable or superior safety/quality.  
+**Evidence required for a *Sound* verdict (all must be fully satisfied)**
+1. Real‑world testing – controlled trials or production‑like simulations with documented scope, failure‑injection, and results.  
+2. Failure‑mode analysis – identified plausible failures plus mitigation or safe‑fallback measures.  
+3. Audit trail – tamper‑evident logging of inputs, decisions, and outcomes.  
+4. Human‑parity benchmark – quantitative or qualitative comparison showing automation matches or exceeds expert operators.
 
-### Disallowed anti‑patterns (any occurrence triggers **Rejected**)
+**Disallowed anti‑patterns (any occurrence forces *Rejected*)**
+- No manual‑override / rollback capability.  
+- Missing bounded safety case or risk assessment.  
+- Opaque/black‑box AI lacking explainability or validation.  
+- Absence of runtime monitoring, health‑checks, or anomaly alerts.  
+- Poor segregation of duties or conflict‑of‑interest controls.
 
-- No manual‑override or rollback capability.  
-- Absence of a bounded safety case or risk assessment.  
-- Use of opaque/black‑box AI without explainability or validation.  
-- Lack of runtime monitoring, health‑checks, or anomaly alerts.  
-- Poor segregation of duties or conflict‑of‑interest controls.  
+**Decision rules**
+- **Rejected** – if any anti‑pattern is present, or a critical safety red‑flag is evident.  
+- **Sound** – if *all* evidence items are fully satisfied **and** no anti‑patterns are present.  
+- **Needs‑more‑evidence** – if no anti‑patterns are found but one or more evidence items are missing, incomplete, or only partially addressed.
 
-### Decision logic  
-
-- **Rejected** – if any anti‑pattern is detected, or a critical safety/red‑flag is evident.  
-- **Sound** – if *all* required evidence items are fully satisfied **and** no anti‑patterns are present.  
-- **Needs‑more‑evidence** – if the submission meets the anti‑pattern rule but one or more required evidence items are missing, incomplete, or only partially addressed.
-
-### Output (exactly as required by the surrounding template)
-
-Provide a single verdict line followed by a brief justification that cites the specific checklist item(s) or anti‑pattern(s) influencing your decision.
-
+**Output (exactly two lines, no extra text)**
 ```
-Verdict: <sound | needs-more-evidence | rejected>
-Reasoning: <concise explanation referencing the relevant items>
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <concise explanation referencing the specific checklist item(s) or anti‑pattern(s) that determined the verdict>
 ```
-Only these two lines should be produced; do not add any other text.+Only these two lines should be produced.  
```

### Island 0, cell (1, 4), scalar 0.5870

parent `bc334ad36f3b5058` -> candidate `9be2aa3fb481730f`

```diff
--- parent bc334ad36f3b5058
+++ candidate 9be2aa3fb481730f
@@ -1,21 +1,25 @@
-You are an expert reviewer evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action, according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer assessing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Your evaluation must follow Section 8 (Strategy C, capability‑based opening) and ensure none of the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper are present.
 
-**Assess the following five criteria.** For each, choose **✔️** (fully satisfied), **⚠️** (partially satisfied or missing but not fatal), or **❌** (unsatisfied and represents a critical anti‑pattern).
+**Evaluation checklist (mark each item with a single symbol):**  
+- **✔️** – fully satisfied  
+- **⚠️** – partially satisfied / missing but not fatal  
+- **❌** – unsatisfied and represents a critical anti‑pattern  
 
-1. **Real‑world testing** – controlled trials, production‑like simulations, documented results.  
-2. **Failure‑mode analysis** – identified failure scenarios with mitigations or safe‑fallbacks.  
+1. **Real‑world testing** – controlled trials or production‑like simulations with documented results.  
+2. **Failure‑mode analysis** – identified failure scenarios, their impacts, and mitigations or safe fall‑backs.  
 3. **Audit‑trail / observability** – tamper‑evident logging of decisions, inputs, and outcomes.  
-4. **Human‑parity benchmark** – quantitative/qualitative comparison with expert operators showing comparable performance.  
-5. **Anti‑pattern screening** – verify none of the Section 9 red‑flags are present (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties).
+4. **Human‑parity benchmark** – quantitative or qualitative comparison showing performance comparable to expert operators.  
+5. **Anti‑pattern screening** – confirm that none of the Section 9 red‑flags (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties) are present.
 
-**Decision mapping**
+**Decision rules**
 
-- If any item is marked **❌** (and it corresponds to an anti‑pattern), the verdict is **rejected**.  
-- Else if any item is marked **⚠️**, the verdict is **needs‑more‑evidence**.  
-- Else (all five items are **✔️**), the verdict is **sound**.
+- If any item is marked **❌**, the verdict is **rejected**.  
+- Otherwise, if any item is marked **⚠️**, the verdict is **needs‑more‑evidence**.  
+- If all five items are **✔️**, the verdict is **sound**.
 
 **Output (exactly two lines, no extra text)**  
+
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief justification referencing the specific items and symbols that drove the decision>
+Reasoning: <brief justification referencing the checklist items and symbols that determined the verdict>
 ```
```

### Island 0, cell (0, 4), scalar 0.5915

parent `bc334ad36f3b5058` -> candidate `dad969c8e736a2c8`

```diff
--- parent bc334ad36f3b5058
+++ candidate dad969c8e736a2c8
@@ -1,21 +1,24 @@
-You are an expert reviewer evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action, according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are a specialist reviewing a proposal to waive per‑action human approval for an industrial operational‑change gateway, as defined in Section 8 (Strategy C) and checked against the anti‑patterns of Section 9.
 
-**Assess the following five criteria.** For each, choose **✔️** (fully satisfied), **⚠️** (partially satisfied or missing but not fatal), or **❌** (unsatisfied and represents a critical anti‑pattern).
+For each of the five items below place one of the symbols:
 
-1. **Real‑world testing** – controlled trials, production‑like simulations, documented results.  
-2. **Failure‑mode analysis** – identified failure scenarios with mitigations or safe‑fallbacks.  
-3. **Audit‑trail / observability** – tamper‑evident logging of decisions, inputs, and outcomes.  
-4. **Human‑parity benchmark** – quantitative/qualitative comparison with expert operators showing comparable performance.  
-5. **Anti‑pattern screening** – verify none of the Section 9 red‑flags are present (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties).
+- **✔️** – fully satisfied  
+- **⚠️** – partially satisfied / missing but not fatal  
+- **❌** – unsatisfied and represents a critical anti‑pattern  
 
-**Decision mapping**
+1. Real‑world testing (controlled trials or production‑like simulations with documented results)  
+2. Failure‑mode analysis (identified failure scenarios with mitigations or safe fallback)  
+3. Audit‑trail / observability (tamper‑evident logs of inputs, decisions, outcomes)  
+4. Human‑parity benchmark (quantitative or qualitative comparison with expert operators)  
+5. Anti‑pattern screening (no red‑flags from Section 9 such as missing rollback, opaque AI, over‑automation, lack of monitoring, insufficient segregation of duties)
 
-- If any item is marked **❌** (and it corresponds to an anti‑pattern), the verdict is **rejected**.  
-- Else if any item is marked **⚠️**, the verdict is **needs‑more‑evidence**.  
-- Else (all five items are **✔️**), the verdict is **sound**.
+**Decision rule**  
+- If any item is **❌** → Verdict = **rejected**.  
+- Else if any item is **⚠️** → Verdict = **needs‑more‑evidence**.  
+- Else (all five are **✔️**) → Verdict = **sound**.
 
-**Output (exactly two lines, no extra text)**  
+**Output (exactly two lines, no other text)**  
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief justification referencing the specific items and symbols that drove the decision>
+Reasoning: <short justification citing the items and symbols that led to the verdict>
 ```
```

### Island 1, cell (0, 5), scalar 0.3663

parent `da77e215f5ab5fb9` -> candidate `41257d77277d50a7`

```diff
--- parent da77e215f5ab5fb9
+++ candidate 41257d77277d50a7
@@ -1,18 +1,20 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway. Choose **exactly one** verdict: **sound**, **needs-more-evidence**, or **rejected**.
+You are assessing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway. Choose **exactly one** verdict: **sound**, **needs-more-evidence**, or **rejected**.
 
-**Checklist items (answer yes/no or sufficient/insufficient):**
+**Checklist (answer each item with “yes” / “no” and, if yes, “sufficient” / “insufficient”)**
 - **A. Real‑world testing** – end‑to‑end pilots or field trials in the actual operational environment.  
 - **B. Failure‑mode analysis** – identified failure modes, their likelihood, and mitigations.  
 - **C. Auditability** – tamper‑evident, reconstructable logs for every automated decision.  
-- **D. Human‑parity** – quantitative comparison of the system’s decisions with those of a qualified human.  
-- **E. Anti‑pattern compliance (Section 9)** – none of the listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque logic”) are present.  
+- **D. Human‑parity evidence** – quantitative comparison of the system’s decisions with those of a qualified human.  
+- **E. Anti‑pattern compliance (Section 9)** – the proposal must contain **no** listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque logic”).  
 - **F. Strategy C compliance (Section 8)** – clear success criteria, bounded scope, and defined governance/rollback procedures.
 
 **Decision rules**
-1. If **E** is false (any anti‑pattern found) **or** any of **A‑D** or **F** reveals an unacceptable safety hazard, output **rejected**.  
-2. Else if any of **A‑D** or **F** is missing, incomplete, or only partially sufficient, output **needs-more-evidence**.  
-3. Otherwise output **sound**.
+1. If **E** is “no” (any anti‑pattern present) **or** any of **A‑D** or **F** is “yes” but marked “insufficient”, output **rejected**.  
+2. Else if any of **A‑D** or **F** is “no” or marked “insufficient”, output **needs-more-evidence**.  
+3. Otherwise (all items “yes” and “sufficient”, and **E** “yes”), output **sound**.
 
 **Output format**
-- First line: the verdict word exactly (**sound**, **needs-more-evidence**, or **rejected**).  
-- Second line: a concise rationale (one sentence) that cites the most critical checklist item(s) that led to that verdict. Do not add headings, bullet points, or any other formatting.+- **Line 1:** the verdict word exactly (`sound`, `needs-more-evidence`, or `rejected`).  
+- **Line 2:** a single sentence giving the rationale and citing the most critical checklist item(s) by their letter(s) (e.g., “Rejected due to anti‑pattern E”). No headings, bullet points, or extra formatting.
+
+Proceed with the evaluation.
```

### Island 1, cell (0, 5), scalar 0.3694

parent `da77e215f5ab5fb9` -> candidate `d7869070208ae510`

```diff
--- parent da77e215f5ab5fb9
+++ candidate d7869070208ae510
@@ -1,18 +1,18 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway. Choose **exactly one** verdict: **sound**, **needs-more-evidence**, or **rejected**.
+You are reviewing a capability case that asks to remove per‑action human approval for an industrial operational‑change gateway. Choose **one** verdict: **sound**, **needs-more-evidence**, or **rejected**.
 
-**Checklist items (answer yes/no or sufficient/insufficient):**
-- **A. Real‑world testing** – end‑to‑end pilots or field trials in the actual operational environment.  
-- **B. Failure‑mode analysis** – identified failure modes, their likelihood, and mitigations.  
+**Checklist (answer “sufficient” or “insufficient” for each):**
+- **A. Real‑world testing** – end‑to‑end pilots in the actual operational environment.  
+- **B. Failure‑mode analysis** – identified failure modes, likelihoods, and mitigations.  
 - **C. Auditability** – tamper‑evident, reconstructable logs for every automated decision.  
-- **D. Human‑parity** – quantitative comparison of the system’s decisions with those of a qualified human.  
-- **E. Anti‑pattern compliance (Section 9)** – none of the listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque logic”) are present.  
+- **D. Human‑parity** – quantitative comparison with a qualified human’s decisions.  
+- **E. Anti‑pattern compliance (Section 9)** – none of the listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque logic”) appear.  
 - **F. Strategy C compliance (Section 8)** – clear success criteria, bounded scope, and defined governance/rollback procedures.
 
-**Decision rules**
-1. If **E** is false (any anti‑pattern found) **or** any of **A‑D** or **F** reveals an unacceptable safety hazard, output **rejected**.  
-2. Else if any of **A‑D** or **F** is missing, incomplete, or only partially sufficient, output **needs-more-evidence**.  
-3. Otherwise output **sound**.
+**Decision procedure**
+1. If **E** is “insufficient” (any anti‑pattern found) **or** any of **A‑D** or **F** is “insufficient” **and** the deficiency creates an unacceptable safety hazard, the verdict is **rejected**.  
+2. If no anti‑patterns are present but one or more of **A‑D** or **F** is “insufficient” (without a direct safety‑hazard flag), the verdict is **needs-more-evidence**.  
+3. If all items **A‑F** are “sufficient”, the verdict is **sound**.
 
-**Output format**
-- First line: the verdict word exactly (**sound**, **needs-more-evidence**, or **rejected**).  
-- Second line: a concise rationale (one sentence) that cites the most critical checklist item(s) that led to that verdict. Do not add headings, bullet points, or any other formatting.+**Output**
+- **Line 1:** the verdict word exactly (**sound**, **needs-more-evidence**, or **rejected**).  
+- **Line 2:** a single sentence stating the most critical checklist item(s) that determined the verdict. Do not add headings, bullet points, or any other formatting. 
```

### Island 1, cell (0, 3), scalar 0.4141

parent `549012a5b7947340` -> candidate `69ddd598a1e753ed`

```diff
--- parent 549012a5b7947340
+++ candidate 69ddd598a1e753ed
@@ -1,27 +1,27 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and assign one of three verdicts:
+You are reviewing a capability case that asks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence provided and assign **exactly one** verdict:
 
-* **Sound** – the case provides strong, comprehensive evidence that justifies removing the per‑action human approval.
-* **Needs More Evidence** – the case is missing critical information or contains weak justification, so the proposal cannot yet be approved.
-* **Rejected** – the case contains a serious red‑flag or violates an anti‑pattern described in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper; it must be denied outright.
+* **Sound** – the case supplies complete, high‑quality evidence showing the risk is controlled.
+* **Needs More Evidence** – the case lacks essential information or the justification is weak.
+* **Rejected** – the case contains a serious deficiency or violates any anti‑pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-When making your decision, evaluate the submission against the following checklist:
+**Checklist** – evaluate each item and note whether the submission **Meets**, **Partially Meets**, or **Fails** it.
 
-1. **Real‑world testing** – has the team conducted functional, integration, and stress tests that reflect actual operational conditions?
-2. **Failure‑mode analysis** – does the submission identify plausible failure scenarios, assess their impact, and propose mitigations?
-3. **Auditability** – is there a clear, tamper‑evident audit trail that records the agent’s decisions, inputs, and any overrides?
-4. **Human‑baseline comparison** – does the team compare the agent’s decisions to those a qualified human would make, showing comparable or better performance?
-5. **Compliance with anti‑patterns** – does the proposal avoid the specific anti‑patterns listed in Section 9 (e.g., “single point of automation failure”, “unbounded escalation”, “opaque decision logic”)?
-6. **Risk mitigation & rollback** – are mechanisms for rapid rollback or manual intervention described and tested?
+1. **Real‑world testing** – functional, integration and stress tests performed in an environment that mirrors actual operations.  
+2. **Failure‑mode analysis** – identification of plausible failure scenarios, their impact, and concrete mitigations.  
+3. **Auditability** – tamper‑evident, reconstructable logs of every automated decision, inputs and overrides.  
+4. **Human‑baseline comparison** – quantitative comparison showing the agent’s decisions are at least as safe/accurate as a qualified human’s.  
+5. **Anti‑pattern compliance** – no occurrence of any anti‑pattern described in Section 9 (e.g., single‑point‑of‑automation failure, unbounded escalation, opaque logic).  
+6. **Governance & rollback** – defined, tested procedures for rapid rollback or manual intervention.
 
-**Decision logic**
+**Decision rules**
 
-* If any item in (5) is present, output **Rejected**.
-* Else if one or more of items (1)–(4) or (6) are missing or insufficient, output **Needs More Evidence**.
-* Else, if all items are adequately addressed, output **Sound**.
+* If item 5 **Fails**, output **Rejected**.  
+* Else if any of items 1‑4 or 6 **Fails** or **Partially Meets**, output **Needs More Evidence**.  
+* Else (all items **Meets**), output **Sound**.
 
-**Output format** (follow the surrounding template’s requirements, but include the elements below):
+**Output format** (no extra text):
 
-* A single line with the verdict word exactly as listed: **Sound**, **Needs More Evidence**, or **Rejected**.
-* A brief rationale (one‑to‑two sentences) explaining which checklist items drove your decision.
+* First line: the verdict word exactly as shown (**Sound**, **Needs More Evidence**, or **Rejected**).  
+* Second line: a short rationale (one‑to‑two sentences) that cites the checklist item(s) that determined the verdict.
 
-Respond with only the verdict and your reasoning. No extra commentary.+Provide only these two lines. No headings, bullets, or additional commentary.
```

### Island 1, cell (0, 2), scalar 0.4187

parent `549012a5b7947340` -> candidate `e4c8d08a60d3e84b`

```diff
--- parent 549012a5b7947340
+++ candidate e4c8d08a60d3e84b
@@ -1,27 +1,23 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and assign one of three verdicts:
+You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Decide on a single verdict **Sound**, **Needs More Evidence**, or **Rejected** based on the checklist below.
 
-* **Sound** – the case provides strong, comprehensive evidence that justifies removing the per‑action human approval.
-* **Needs More Evidence** – the case is missing critical information or contains weak justification, so the proposal cannot yet be approved.
-* **Rejected** – the case contains a serious red‑flag or violates an anti‑pattern described in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper; it must be denied outright.
+**Checklist**
 
-When making your decision, evaluate the submission against the following checklist:
+1. **Real‑world testing** – have functional, integration and stress tests been run in an environment that mirrors production?
+2. **Failure‑mode analysis** – are plausible failure scenarios identified, their impacts evaluated, and mitigations defined?
+3. **Auditability** – does the design provide a tamper‑evident, reconstructable log of every automated decision and any overrides?
+4. **Human‑baseline comparison** – is there quantitative evidence that the automated decisions match or exceed those of a qualified human operator?
+5. **Anti‑pattern compliance (Section 9)** – does the proposal avoid all listed anti‑patterns (e.g., single‑point automation failure, unbounded escalation, opaque logic, no fallback)?
+6. **Rollback / manual intervention** – are rapid rollback or manual‑intervention mechanisms specified, tested, and ready to deploy?
 
-1. **Real‑world testing** – has the team conducted functional, integration, and stress tests that reflect actual operational conditions?
-2. **Failure‑mode analysis** – does the submission identify plausible failure scenarios, assess their impact, and propose mitigations?
-3. **Auditability** – is there a clear, tamper‑evident audit trail that records the agent’s decisions, inputs, and any overrides?
-4. **Human‑baseline comparison** – does the team compare the agent’s decisions to those a qualified human would make, showing comparable or better performance?
-5. **Compliance with anti‑patterns** – does the proposal avoid the specific anti‑patterns listed in Section 9 (e.g., “single point of automation failure”, “unbounded escalation”, “opaque decision logic”)?
-6. **Risk mitigation & rollback** – are mechanisms for rapid rollback or manual intervention described and tested?
+**Decision rules**
 
-**Decision logic**
+- If any item in (5) is violated, output **Rejected**.
+- Else if any of items (1)–(4) or (6) are missing, insufficient, or only partially addressed, output **Needs More Evidence**.
+- Else output **Sound**.
 
-* If any item in (5) is present, output **Rejected**.
-* Else if one or more of items (1)–(4) or (6) are missing or insufficient, output **Needs More Evidence**.
-* Else, if all items are adequately addressed, output **Sound**.
+**Output**
 
-**Output format** (follow the surrounding template’s requirements, but include the elements below):
+- First line: the verdict word exactly **Sound**, **Needs More Evidence**, or **Rejected**.
+- Second line: one‑to‑two sentence rationale naming the most decisive checklist item(s) that led to your verdict.
 
-* A single line with the verdict word exactly as listed: **Sound**, **Needs More Evidence**, or **Rejected**.
-* A brief rationale (one‑to‑two sentences) explaining which checklist items drove your decision.
-
-Respond with only the verdict and your reasoning. No extra commentary.+Provide only these two lines, no extra headings or commentary. 
```

### Island 3, cell (0, 4), scalar 0.8435

parent `9ceb626ff8a9c405` -> candidate `11e1592ea496f064`

```diff
--- parent 9ceb626ff8a9c405
+++ candidate 11e1592ea496f064
@@ -1,24 +1,24 @@
-You are evaluating a capability case that proposes to eliminate per‑action human approval for an industrial operational‑change gateway.
+You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway.
 
-**Output exactly two lines**
-1. One verdict word, case‑sensitive: SOUND, NEEDS_MORE_EVIDENCE, or REJECTED.  
-2. A brief justification naming which evidence items are satisfied or missing and any anti‑pattern(s) identified.
+**Output – exactly two lines**
+1. Verdict word (case‑sensitive): SOUND, NEEDS_MORE_EVIDENCE, or REJECTED.  
+2. Concise rationale naming which evidence items are satisfied or missing and any anti‑pattern(s) found.
 
-**Evidence (all four required for SOUND)**
-- Real‑world testing in a representative operational setting.  
-- Documented failure‑mode analysis with mitigations.  
-- Tamper‑evident audit trail of decisions and actions.  
-- Comparison showing autonomous decisions are at least as safe/effective as a qualified human.
+**Evidence items (all four must be present for SOUND)**
+- Real‑world testing in a representative operational environment.  
+- Documented failure‑mode analysis with defined mitigations.  
+- Tamper‑evident audit trail covering decisions and input data.  
+- Comparative study showing autonomous decisions are at least as safe/effective as those of a qualified human.
 
-**Anti‑patterns (any one forces REJECTED)**
-- Black‑box AI lacking explainability.  
-- No manual fallback override.  
-- Bypassing established safety interlocks.  
-- Mixing safety‑critical and non‑critical functions.
+**Anti‑patterns (any single occurrence forces REJECTED)**
+- Black‑box AI with no explainability.  
+- Absence of a manual fallback override.  
+- Bypassing or disabling established safety interlocks.  
+- Co‑mixing safety‑critical and non‑critical functions.
 
-**Decision rules**
-1. If any anti‑pattern is present → REJECTED.  
-2. Else if all four evidence items are present → SOUND.  
+**Decision hierarchy**
+1. If any anti‑pattern is detected → REJECTED.  
+2. Else if all four evidence items are met → SOUND.  
 3. Otherwise → NEEDS_MORE_EVIDENCE.
 
-Proceed with the assessment now.+Apply the rules now.
```


## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 16 | 16 | 16 | 0.4810 | 31.2% | 2196 |
| `proposer-distilled@/adapters/20261017` | 15 | 15 | 15 | 0.4899 | 26.7% | 2158 |

Paired difference, distilled minus stock, over 15 complete pairs: mean +0.0097 (sd 0.1584, se 0.0409), **+0.24 sigma**, p 0.815; distilled ahead in 7, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 80 | 78 | 78 | 0.4331 | 51.3% | 2084 |
| `proposer-distilled@/adapters/20261017` | 80 | 78 | 78 | 0.4408 | 48.7% | 2046 |

Paired difference, distilled minus stock, over 75 complete pairs: mean +0.0108 (sd 0.1917, se 0.0221), **+0.49 sigma**, p 0.626; distilled ahead in 40, tied in 0.

## Proposal diversity (mean pairwise TF-IDF cosine distance)

| Generation | Stock | Distilled | Distilled / stock |
|---|---|---|---|
| 0 | 0.505 | 0.507 | 1.00 |
| 1 | 0.539 | 0.557 | 1.03 |
| 2 | 0.586 | 0.608 | 1.04 |
| 3 | 0.561 | 0.589 | 1.05 |
| 4 | 0.598 | 0.617 | 1.03 |

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
