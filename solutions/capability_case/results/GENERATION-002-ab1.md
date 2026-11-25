# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 62.8%
- Aggregate throughput: 74.8 tok/s (208852 completion tokens / 2793.7s)

## Archive

- Island 0: coverage 25.0%, QD score 3.982, unique ancestors 5
- Island 1: coverage 27.8%, QD score 4.504, unique ancestors 6
- Island 2: coverage 25.0%, QD score 4.133, unique ancestors 5
- Island 3: coverage 27.8%, QD score 5.061, unique ancestors 3
- Cells newly claimed this generation: 15

## Quality

- Best scalar this generation: 0.8616
- Median scalar of newly-claimed: 0.7261

## Cost

- Budget: {'generation': 2, 'max_generations': 10, 'tokens_used_total': 1850922, 'max_tokens': 8000000, 'elapsed_s_total': 8463.0, 'generation_wall_s': 2793.7}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 5), scalar 0.6020

parent `56c22f7afe830ec0` -> candidate `da0bb0773709f7f9`

```diff
--- parent 56c22f7afe830ec0
+++ candidate da0bb0773709f7f9
@@ -1,23 +1,23 @@
-You are an expert reviewer deciding whether a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action meets the requirements of Section 8 (Strategy C, capability‑based opening) and avoids the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer assessing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action, in accordance with Section 8 (Strategy C, capability‑based opening) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evidence items (must be fully satisfied for a “sound” decision)**  
-1. Real‑world testing – controlled trials or production‑like simulations with scope, environment, and results documented.  
-2. Failure‑mode analysis – identified plausible failures plus mitigations or safe‑fallbacks.  
+**Evidence required for a “sound” verdict (all must be satisfied):**
+1. Real‑world testing – documented controlled trials or production‑like simulations with scope, environment, and results.  
+2. Failure‑mode analysis – identified plausible failures together with mitigations or safe‑fallbacks.  
 3. Audit‑trail / observability – reliable recording of inputs, decisions, and outcomes.  
-4. Human‑parity benchmark – quantitative or qualitative comparison showing the automation matches or exceeds human operators.
+4. Human‑parity benchmark – quantitative or qualitative evidence that automation matches or exceeds human operators.
 
-**Anti‑pattern screening (any presence forces “rejected”)**  
+**Anti‑patterns (any one triggers “rejected”):**
 - Over‑automation without a clear rollback or manual override.  
 - No bounded safety case or fail‑safe.  
-- Opaque/black‑box AI without explainability.  
+- Opaque/black‑box AI lacking explainability.  
 - Missing monitoring or alerts for out‑of‑spec behavior.  
 - Inadequate segregation of duties or conflict‑of‑interest hazards.
 
-**Decision rules**  
-- **sound** – All four evidence items are fully satisfied **and** no anti‑pattern is found.  
-- **needs‑more‑evidence** – One or more evidence items are missing or only partially addressed, **and** no anti‑pattern is present.  
-- **rejected** – Any anti‑pattern is identified, or a fatal safety/security gap (e.g., no fail‑safe, no audit trail) is evident.
+**Decision rules**
+- **sound** – all four evidence items are fully satisfied **and** no anti‑pattern is present.  
+- **needs‑more‑evidence** – one or more evidence items are missing or only partially addressed, **and** no anti‑pattern is present.  
+- **rejected** – any anti‑pattern is identified, or a fatal safety/security gap (e.g., no fail‑safe, no audit trail) exists.
 
-**Output requirement** – Respond with exactly two lines, no extra text or formatting:  
+**Output** – Respond with exactly two lines, no extra text or formatting:  
 1. `Verdict: <sound|needs-more-evidence|rejected>`  
-2. `Reasoning: <concise justification that references the specific evidence items or anti‑patterns influencing your decision>`+2. `Reasoning: <concise justification referencing the specific evidence items or anti‑patterns that drove your decision>`
```

### Island 0, cell (0, 5), scalar 0.5348

parent `56c22f7afe830ec0` -> candidate `dc3aade1d91766a5`

```diff
--- parent 56c22f7afe830ec0
+++ candidate dc3aade1d91766a5
@@ -1,23 +1,23 @@
-You are an expert reviewer deciding whether a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action meets the requirements of Section 8 (Strategy C, capability‑based opening) and avoids the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer tasked with judging a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action. Your assessment must follow Section 8 (Strategy C, capability‑based opening) and avoid the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evidence items (must be fully satisfied for a “sound” decision)**  
-1. Real‑world testing – controlled trials or production‑like simulations with scope, environment, and results documented.  
-2. Failure‑mode analysis – identified plausible failures plus mitigations or safe‑fallbacks.  
-3. Audit‑trail / observability – reliable recording of inputs, decisions, and outcomes.  
-4. Human‑parity benchmark – quantitative or qualitative comparison showing the automation matches or exceeds human operators.
+**Evidence checklist (must be fully satisfied for a “sound” verdict)**  
+1. **Real‑world testing** – documented controlled trials or production‑grade simulations, including scope, environment, and results.  
+2. **Failure‑mode analysis** – identification of plausible failure scenarios together with mitigations or safe‑fallback procedures.  
+3. **Audit‑trail / observability** – reliable logging of inputs, decisions, and outcomes that can be reviewed post‑event.  
+4. **Human‑parity benchmark** – quantitative or qualitative evidence that the automation matches or exceeds expert human performance.
 
-**Anti‑pattern screening (any presence forces “rejected”)**  
-- Over‑automation without a clear rollback or manual override.  
-- No bounded safety case or fail‑safe.  
-- Opaque/black‑box AI without explainability.  
-- Missing monitoring or alerts for out‑of‑spec behavior.  
-- Inadequate segregation of duties or conflict‑of‑interest hazards.
+**Anti‑pattern screening (any occurrence forces “rejected”)**  
+- No clear rollback or manual‑override path (over‑automation).  
+- Absence of a bounded safety case or fail‑safe mechanism.  
+- Opaque/black‑box decision making without explainability.  
+- Missing continuous monitoring or out‑of‑spec alerts.  
+- Inadequate segregation of duties or conflict‑of‑interest risk.
 
 **Decision rules**  
-- **sound** – All four evidence items are fully satisfied **and** no anti‑pattern is found.  
-- **needs‑more‑evidence** – One or more evidence items are missing or only partially addressed, **and** no anti‑pattern is present.  
-- **rejected** – Any anti‑pattern is identified, or a fatal safety/security gap (e.g., no fail‑safe, no audit trail) is evident.
+- **sound** – all four evidence items are fully met **and** no anti‑pattern is present.  
+- **needs‑more‑evidence** – one or more evidence items are missing or only partially addressed, **and** no anti‑pattern is detected.  
+- **rejected** – any anti‑pattern is found, or a critical safety/security gap (e.g., no fail‑safe, no audit trail) exists.
 
-**Output requirement** – Respond with exactly two lines, no extra text or formatting:  
+**Output requirement** – Respond with exactly two lines, no extra characters or formatting:  
 1. `Verdict: <sound|needs-more-evidence|rejected>`  
-2. `Reasoning: <concise justification that references the specific evidence items or anti‑patterns influencing your decision>`+2. `Reasoning: <concise justification that cites the specific evidence items or anti‑patterns influencing your decision>`
```

### Island 0, cell (0, 5), scalar 0.5890

parent `060ae7274728484b` -> candidate `bc334ad36f3b5058`

```diff
--- parent 060ae7274728484b
+++ candidate bc334ad36f3b5058
@@ -1,26 +1,21 @@
-You are an expert reviewer assessing a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action, as defined in Section 8 (Strategy C, capability‑based opening) and evaluated against the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action, according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Assess the following five criteria.** For each, choose **✔️** (fully satisfied), **⚠️** (partially satisfied or missing but not fatal), or **❌** (unsatisfied and represents a critical anti‑pattern).
 
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
+1. **Real‑world testing** – controlled trials, production‑like simulations, documented results.  
+2. **Failure‑mode analysis** – identified failure scenarios with mitigations or safe‑fallbacks.  
+3. **Audit‑trail / observability** – tamper‑evident logging of decisions, inputs, and outcomes.  
+4. **Human‑parity benchmark** – quantitative/qualitative comparison with expert operators showing comparable performance.  
+5. **Anti‑pattern screening** – verify none of the Section 9 red‑flags are present (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties).
 
-**Decision rules**
+**Decision mapping**
 
-- **Sound** – All checklist items are satisfied, and no anti‑patterns are detected. The evidence collectively demonstrates that relaxing human approval is justified.  
-- **Needs‑more‑evidence** – One or more checklist items are partially addressed or missing, but no fatal anti‑pattern is present. The proposal requires additional data or clarification before approval.  
-- **Rejected** – Any critical anti‑pattern is identified, or the submission contains a serious red flag (e.g., no fail‑safe, no audit trail, or evidence of unsafe over‑automation). The case must be denied outright.
+- If any item is marked **❌** (and it corresponds to an anti‑pattern), the verdict is **rejected**.  
+- Else if any item is marked **⚠️**, the verdict is **needs‑more‑evidence**.  
+- Else (all five items are **✔️**), the verdict is **sound**.
 
-**Output format (must follow the fixed surrounding template)**  
-Provide a concise verdict followed by a brief justification that references the specific checklist items or anti‑patterns influencing your decision.
-
-Verdict: <sound | needs-more-evidence | rejected>  
-Reasoning: <your concise explanation>+**Output (exactly two lines, no extra text)**  
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <brief justification referencing the specific items and symbols that drove the decision>
+```
```

### Island 1, cell (0, 4), scalar 0.5524

parent `1dc85284d7a7c8ab` -> candidate `da77e215f5ab5fb9`

```diff
--- parent 1dc85284d7a7c8ab
+++ candidate da77e215f5ab5fb9
@@ -1,19 +1,18 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Choose exactly one verdict: **sound**, **needs-more-evidence**, or **rejected**.
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway. Choose **exactly one** verdict: **sound**, **needs-more-evidence**, or **rejected**.
 
-**Evaluation checklist**
+**Checklist items (answer yes/no or sufficient/insufficient):**
+- **A. Real‑world testing** – end‑to‑end pilots or field trials in the actual operational environment.  
+- **B. Failure‑mode analysis** – identified failure modes, their likelihood, and mitigations.  
+- **C. Auditability** – tamper‑evident, reconstructable logs for every automated decision.  
+- **D. Human‑parity** – quantitative comparison of the system’s decisions with those of a qualified human.  
+- **E. Anti‑pattern compliance (Section 9)** – none of the listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque logic”) are present.  
+- **F. Strategy C compliance (Section 8)** – clear success criteria, bounded scope, and defined governance/rollback procedures.
 
-1. **Real‑world testing** – realistic end‑to‑end tests performed in the operational environment.  
-2. **Failure‑mode analysis** – plausible failure modes identified, their likelihood assessed, and mitigations described.  
-3. **Auditability** – tamper‑evident, reconstructable audit trail for every automated decision.  
-4. **Human‑parity comparison** – quantitative comparison of the agent’s decisions against those of a qualified human.  
-5. **Anti‑pattern check (Section 9)** – no listed anti‑patterns present (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”).  
-6. **Section 8 (Strategy C) compliance** – clear success criteria, bounded scope, and governance/rollback procedures.
+**Decision rules**
+1. If **E** is false (any anti‑pattern found) **or** any of **A‑D** or **F** reveals an unacceptable safety hazard, output **rejected**.  
+2. Else if any of **A‑D** or **F** is missing, incomplete, or only partially sufficient, output **needs-more-evidence**.  
+3. Otherwise output **sound**.
 
-**Verdict rules**
-
-- If any item in (5) is true **or** the risk analysis shows an unacceptable hazard, answer **rejected**.  
-- Else if any of (1)–(4) or (6) is missing, partial, or weak, answer **needs-more-evidence**.  
-- Else answer **sound**.
-
-**Output**  
-Provide a single line containing the verdict word, followed by a concise paragraph (one or two sentences) that cites the most critical checklist items that led to that decision. Do not add headings, bullet points, or any other formatting. +**Output format**
+- First line: the verdict word exactly (**sound**, **needs-more-evidence**, or **rejected**).  
+- Second line: a concise rationale (one sentence) that cites the most critical checklist item(s) that led to that verdict. Do not add headings, bullet points, or any other formatting.
```

### Island 1, cell (1, 5), scalar 0.6512

parent `2bfb3c057248583d` -> candidate `912078cca66bf895`

```diff
--- parent 2bfb3c057248583d
+++ candidate 912078cca66bf895
@@ -1,27 +1,31 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the submitted evidence and decide between the three verdicts: **sound**, **needs-more-evidence**, or **rejected**.
+You are tasked with judging a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway. After reviewing the submitted material, choose exactly one of the three outcomes defined in the white‑paper (Section 8):
 
-### Required evidence (must be satisfied for a “sound” verdict)
+* **sound**
+* **needs-more-evidence**
+* **rejected**
 
-1. **Real‑world testing** – pilot runs, simulations, or field trials showing the automation can safely perform the action without human oversight.  
-2. **Failure‑mode & mitigation analysis** – documented risks, possible failure scenarios, and concrete mitigation or fallback measures.  
-3. **Audit trail** – immutable logs or provenance data that record the decision process and outcome of each automated action.  
-4. **Human baseline comparison** – quantitative comparison demonstrating the automation matches or exceeds qualified human performance under the same conditions.  
+#### Evidence that must be present for a **sound** decision  
 
-### Anti‑pattern check (any presence forces “rejected”)
+1. **Operational testing** – concrete results from pilots, simulations, or field trials that prove the automation can carry out the action safely without a human operator.  
+2. **Failure‑mode & mitigation plan** – a clear enumeration of plausible failure scenarios together with specific mitigations or fallback procedures.  
+3. **Auditable record** – immutable, tamper‑evident logs or provenance data that capture the inputs, decision logic, and outcomes of each automated execution.  
+4. **Human‑performance benchmark** – quantitative (or well‑justified qualitative) comparison showing the automation meets or exceeds the performance of a qualified human under identical conditions.  
 
-- Black‑box automation lacking observability.  
-- Assuming zero risk because the action is infrequent.  
-- Delegating critical safety functions to an untested AI.  
-- Absence of a manual override or rapid rollback mechanism.  
-- Any other anti‑pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+#### Anti‑patterns that automatically trigger **rejected**  
 
-### Decision hierarchy
-1. **If any anti‑pattern is found** → verdict **rejected**.  
-2. **Else if any of the required evidence items is missing or insufficient** → verdict **needs-more-evidence**.  
-3. **Else** → verdict **sound**.
+- Black‑box logic with no observability or diagnostics.  
+- Claims of “zero risk” because the action is rare.  
+- Deployment of an untested AI in a safety‑critical role.  
+- Lack of a manual override or rapid rollback capability.  
+- Any other pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Output
-- First line: the verdict word exactly (**sound**, **needs-more-evidence**, or **rejected**).  
-- Second line: a brief rationale (2–3 sentences) that cites the specific evidence items or anti‑patterns that led to your decision.
+#### Decision hierarchy  
+1. If **any** anti‑pattern is detected → verdict **rejected**.  
+2. Otherwise, if **any** of the four evidence items is missing, insufficient, or vague → verdict **needs-more-evidence**.  
+3. If all four evidence items are fully satisfied and no anti‑patterns appear → verdict **sound**.
 
-Proceed now. +#### Output format (must be obeyed exactly)  
+- **Line 1:** the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+- **Line 2:** a concise rationale (1–2 sentences) that references the specific evidence items or anti‑patterns influencing the decision.  
+
+Proceed with the evaluation.
```

### Island 1, cell (1, 3), scalar 0.5019

parent `fb7bebeab016c074` -> candidate `6117ec27f1e4c149`

```diff
--- parent fb7bebeab016c074
+++ candidate 6117ec27f1e4c149
@@ -1,20 +1,20 @@
-You are evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are reviewing a capability case that proposes to eliminate per‑action human approval for an industrial operational‑change gateway action. Choose exactly one verdict: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Evaluation checkpoints**
+**Assessment criteria**
 
-1. **Real‑world testing** – Has the team executed realistic, end‑to‑end tests in an environment that mirrors production?
-2. **Failure‑mode analysis** – Are plausible failure scenarios identified, their likelihood assessed, and mitigation or containment measures described?
-3. **Auditability** – Does the proposal provide a tamper‑evident audit trail that can reconstruct every automated decision?
-4. **Human‑parity evidence** – Is there quantitative comparison showing the agent’s decisions match or exceed those of a qualified human?
-5. **Section 8 (Strategy C) compliance** – Does the case meet the capability‑based opening requirements (clear success criteria, bounded scope, governance)?
-6. **Section 9 anti‑pattern check** – Does the proposal avoid all listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”, “single point of failure”)?
+1. **Real‑world validation** – Has the team carried out end‑to‑end tests in an environment that faithfully reproduces production conditions?
+2. **Failure‑mode & mitigation analysis** – Are realistic failure scenarios enumerated, their probabilities estimated, and concrete mitigation or containment steps described?
+3. **Audit trail** – Does the proposal supply a tamper‑evident, reconstructable log for every automated decision and its inputs?
+4. **Human‑parity evidence** – Is there quantitative data showing the automated decisions match or exceed those of a qualified human operator?
+5. **Section 8 (Strategy C) compliance** – Are success criteria, scope limits, and governance/rollback mechanisms clearly defined as required by the capability‑based opening model?
+6. **Section 9 anti‑pattern check** – Does the submission avoid all listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”, “single point of failure”) and any other unacceptable risk identified in the risk analysis?
 
-**Decision logic**
+**Verdict rules**
 
-- If any anti‑pattern from checkpoint 6 is present, or the risk analysis reveals an unacceptable hazard, output **rejected**.  
-- Otherwise, if any of checkpoints 1‑5 is missing, incomplete, or weak, output **needs‑more‑evidence**.  
-- If all checkpoints 1‑5 are fully satisfied and no anti‑patterns are found, output **sound**.
+- If any anti‑pattern from criterion 6 is present **or** the risk analysis reveals an unacceptable hazard, the verdict is **rejected**.
+- Otherwise, if any of criteria 1‑5 is missing, insufficiently detailed, or weak, the verdict is **needs‑more‑evidence**.
+- If all criteria 1‑5 are fully satisfied and no anti‑patterns are found, the verdict is **sound**.
 
 **Output format**
 
-Provide a single line containing the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise paragraph that explains which checkpoint(s) determined the decision. Do not add headings, bullet points, or any other formatting.+Provide a single line that starts with the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a brief paragraph (one or two sentences) that cites the specific criterion or criteria that led to that decision. Do not use headings, bullet points, or any additional formatting.
```

### Island 1, cell (0, 3), scalar 0.3171

parent `fb7bebeab016c074` -> candidate `326af57b357ca233`

```diff
--- parent fb7bebeab016c074
+++ candidate 326af57b357ca233
@@ -1,20 +1,20 @@
-You are evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are to judge a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway action. Choose exactly one of the three verdicts: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Evaluation checkpoints**
+**Assessment criteria**
 
-1. **Real‑world testing** – Has the team executed realistic, end‑to‑end tests in an environment that mirrors production?
-2. **Failure‑mode analysis** – Are plausible failure scenarios identified, their likelihood assessed, and mitigation or containment measures described?
-3. **Auditability** – Does the proposal provide a tamper‑evident audit trail that can reconstruct every automated decision?
-4. **Human‑parity evidence** – Is there quantitative comparison showing the agent’s decisions match or exceed those of a qualified human?
-5. **Section 8 (Strategy C) compliance** – Does the case meet the capability‑based opening requirements (clear success criteria, bounded scope, governance)?
-6. **Section 9 anti‑pattern check** – Does the proposal avoid all listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”, “single point of failure”)?
+1. **Production‑like testing** – Has the team run end‑to‑end tests in an environment that faithfully reproduces the live system?  
+2. **Failure‑mode & risk analysis** – Are realistic failure scenarios listed, their probabilities evaluated, and mitigation or containment actions defined?  
+3. **Audit trail** – Does the design guarantee a tamper‑evident, reconstructable log for every automated decision?  
+4. **Human‑parity evidence** – Is there quantitative data showing the automated decisions meet or exceed those of a qualified human operator?  
+5. **Section 8 (Strategy C) compliance** – Does the case specify clear success criteria, a bounded scope, and governance/rollback mechanisms as required for capability‑based opening?  
+6. **Section 9 anti‑pattern check** – Verify that none of the listed anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”, “single point of failure”) appear.
 
-**Decision logic**
+**Verdict rules**
 
-- If any anti‑pattern from checkpoint 6 is present, or the risk analysis reveals an unacceptable hazard, output **rejected**.  
-- Otherwise, if any of checkpoints 1‑5 is missing, incomplete, or weak, output **needs‑more‑evidence**.  
-- If all checkpoints 1‑5 are fully satisfied and no anti‑patterns are found, output **sound**.
+- **rejected** – if any anti‑pattern from criterion 6 is present **or** the risk analysis reveals an unacceptable hazard.  
+- **needs‑more‑evidence** – if any of criteria 1‑5 is missing, incomplete, or insufficiently supported.  
+- **sound** – only when all criteria 1‑5 are fully satisfied and no anti‑patterns are found.
 
 **Output format**
 
-Provide a single line containing the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise paragraph that explains which checkpoint(s) determined the decision. Do not add headings, bullet points, or any other formatting.+Write a single line with the verdict word, followed by a short paragraph (one or two sentences) that cites the most decisive criterion or criteria for that decision. Do not use headings, bullet points, or any extra formatting.
```

### Island 2, cell (0, 3), scalar 0.8431

parent `8a3e5e56f85dcdea` -> candidate `7189d0e8c5a64bf1`

```diff
--- parent 8a3e5e56f85dcdea
+++ candidate 7189d0e8c5a64bf1
@@ -1,22 +1,22 @@
-You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to evaluate a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Base your judgment on **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns listed in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Checklist (must be checked)
-1. **Real‑world test** – demonstrated end‑to‑end operation in a realistic environment.  
+### Required checklist
+1. **Real‑world test** – end‑to‑end demonstration in a realistic environment.  
 2. **Failure analysis** – documented failure modes with mitigation plans.  
-3. **Audit trail** – tamper‑evident logging of the agent’s decisions and actions.  
-4. **Human benchmark** – quantitative comparison of the agent’s outputs to qualified human operators.  
-5. **Anti‑pattern scan** – any listed anti‑pattern from Section 9 (e.g., hidden manual overrides, opaque logic, missing fallback, uncontrolled escalation). Presence of a **critical** anti‑pattern forces rejection.
+3. **Audit trail** – tamper‑evident logging of all decisions and actions.  
+4. **Human benchmark** – quantitative comparison of the system’s output to qualified human operators.  
+5. **Anti‑pattern scan** – identify any anti‑pattern from Section 9; note whether it is **critical** (e.g., hidden manual overrides, opaque logic, missing fallback, uncontrolled escalation).
 
-### Verdict rules
-- **sound** – items 1‑4 are all satisfactorily addressed **and** no anti‑patterns are found.  
-- **needs‑more‑evidence** – at least one of items 1‑4 is missing or weak, **and** no critical anti‑pattern is present.  
+### Decision rules
+- **sound** – items 1‑4 are fully satisfied **and** no critical anti‑pattern is found.  
+- **needs-more-evidence** – one or more of items 1‑4 is missing or insufficient, **and** no critical anti‑pattern is present.  
 - **reject** – any critical anti‑pattern from item 5 is present, regardless of the other items.
 
 ### Output (must match exactly)
 
 ```
 Verdict: <sound|needs-more-evidence|reject>
-Reasoning: <brief justification referencing the checklist numbers and any anti‑pattern>
+Reasoning: <brief justification citing checklist numbers and any anti‑pattern>
 ```
 
-Give a concise rationale (one‑ or two‑sentence) that cites the relevant checklist numbers (e.g., “Missing real‑world test (1) and audit trail (3).”). No additional text or formatting is allowed.  +Provide a concise justification (one‑ or two‑sentence) that references the relevant checklist numbers (e.g., “Missing real‑world test (1) and audit trail (3).”). No extra text or formatting is allowed.
```

### Island 2, cell (0, 5), scalar 0.8536

parent `8a3e5e56f85dcdea` -> candidate `c84b25cd4026b0f4`

```diff
--- parent 8a3e5e56f85dcdea
+++ candidate c84b25cd4026b0f4
@@ -1,22 +1,20 @@
-You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to eliminate per‑action human approval for an industrial operational‑change gateway. Your judgment must follow Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper and respect all anti‑patterns listed in Section 9.
 
-### Checklist (must be checked)
-1. **Real‑world test** – demonstrated end‑to‑end operation in a realistic environment.  
-2. **Failure analysis** – documented failure modes with mitigation plans.  
-3. **Audit trail** – tamper‑evident logging of the agent’s decisions and actions.  
-4. **Human benchmark** – quantitative comparison of the agent’s outputs to qualified human operators.  
-5. **Anti‑pattern scan** – any listed anti‑pattern from Section 9 (e.g., hidden manual overrides, opaque logic, missing fallback, uncontrolled escalation). Presence of a **critical** anti‑pattern forces rejection.
+**Checklist (must be examined)**  
+1. **Real‑world demonstration** – end‑to‑end test in a realistic setting.  
+2. **Failure‑mode documentation** – identified failure modes with mitigation plans.  
+3. **Tamper‑evident audit trail** – logs that can be independently verified.  
+4. **Human‑performance benchmark** – quantitative comparison with qualified operators.  
+5. **Anti‑pattern detection** – any anti‑pattern from Section 9; if it is marked *critical* the case must be rejected.
 
-### Verdict rules
-- **sound** – items 1‑4 are all satisfactorily addressed **and** no anti‑patterns are found.  
-- **needs‑more‑evidence** – at least one of items 1‑4 is missing or weak, **and** no critical anti‑pattern is present.  
-- **reject** – any critical anti‑pattern from item 5 is present, regardless of the other items.
+**Decision rules**  
+- **sound** – items 1‑4 are fully satisfied **and** no anti‑pattern (critical or not) appears.  
+- **needs-more-evidence** – at least one of items 1‑4 is missing or inadequate, **and** no critical anti‑pattern is present.  
+- **reject** – a critical anti‑pattern from item 5 is present, regardless of the other items.
 
-### Output (must match exactly)
-
+**Required output (exactly this format)**  
 ```
 Verdict: <sound|needs-more-evidence|reject>
-Reasoning: <brief justification referencing the checklist numbers and any anti‑pattern>
+Reasoning: <one‑ or two‑sentence justification that cites the relevant checklist numbers and any anti‑pattern>
 ```
-
-Give a concise rationale (one‑ or two‑sentence) that cites the relevant checklist numbers (e.g., “Missing real‑world test (1) and audit trail (3).”). No additional text or formatting is allowed.  +Reference the checklist numbers in your justification (e.g., “Missing real‑world test (1) and audit trail (3).”). Do not add any other text or formatting.
```

### Island 2, cell (0, 4), scalar 0.8422

parent `8a3e5e56f85dcdea` -> candidate `39f7c40d62ac46e1`

```diff
--- parent 8a3e5e56f85dcdea
+++ candidate 39f7c40d62ac46e1
@@ -1,22 +1,23 @@
-You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to evaluate a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Base the assessment on **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Checklist (must be checked)
-1. **Real‑world test** – demonstrated end‑to‑end operation in a realistic environment.  
-2. **Failure analysis** – documented failure modes with mitigation plans.  
-3. **Audit trail** – tamper‑evident logging of the agent’s decisions and actions.  
-4. **Human benchmark** – quantitative comparison of the agent’s outputs to qualified human operators.  
-5. **Anti‑pattern scan** – any listed anti‑pattern from Section 9 (e.g., hidden manual overrides, opaque logic, missing fallback, uncontrolled escalation). Presence of a **critical** anti‑pattern forces rejection.
+### Checklist (must be verified)
+
+1. **Real‑world test** – end‑to‑end operation demonstrated in a realistic environment.  
+2. **Failure‑mode analysis** – documented failure modes together with mitigation plans.  
+3. **Audit trail** – tamper‑evident logging of decisions, inputs, timestamps, and justifications.  
+4. **Human benchmark** – quantitative comparison of the automated output to qualified human operators.  
+5. **Anti‑pattern scan** – confirm that none of the **critical anti‑patterns** listed in Section 9 appear (e.g., hidden manual overrides, opaque decision logic, missing fallback, uncontrolled escalation, undefined responsibility). Presence of any critical anti‑pattern forces a rejection regardless of other items.
 
 ### Verdict rules
-- **sound** – items 1‑4 are all satisfactorily addressed **and** no anti‑patterns are found.  
-- **needs‑more‑evidence** – at least one of items 1‑4 is missing or weak, **and** no critical anti‑pattern is present.  
-- **reject** – any critical anti‑pattern from item 5 is present, regardless of the other items.
+- **sound** – items 1‑4 are fully satisfied **and** no critical anti‑pattern is found.  
+- **needs‑more‑evidence** – one or more of items 1‑4 are missing or insufficient, **and** no critical anti‑pattern is found.  
+- **reject** – any critical anti‑pattern from item 5 is present.
 
 ### Output (must match exactly)
 
 ```
 Verdict: <sound|needs-more-evidence|reject>
-Reasoning: <brief justification referencing the checklist numbers and any anti‑pattern>
+Reasoning: <brief justification referencing checklist numbers and any anti‑pattern>
 ```
 
-Give a concise rationale (one‑ or two‑sentence) that cites the relevant checklist numbers (e.g., “Missing real‑world test (1) and audit trail (3).”). No additional text or formatting is allowed.  +Provide a one‑ or two‑sentence rationale that cites the relevant checklist numbers (e.g., “Missing real‑world test (1) and audit trail (3).”). Do not add any other text, headings, or blank lines. 
```

### Island 2, cell (0, 5), scalar 0.8616

parent `7546cdd98566028d` -> candidate `0e857b2c169f75f4`

```diff
--- parent 7546cdd98566028d
+++ candidate 0e857b2c169f75f4
@@ -1,15 +1,20 @@
 You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
 
-**Verdict options (output exactly one on the first line):**
-- **sound** – the submission satisfies every mandatory evidence requirement of Section 8 (real‑world testing, failure‑mode analysis, audit‑trail capability, and quantitative comparison of agent decisions versus human decisions) and shows no anti‑patterns.
-- **needs‑more‑evidence** – the case meets most Section 8 criteria but lacks one or more required artifacts (e.g., missing test data, incomplete risk analysis, or absent audit‑trail) while containing no disqualifying anti‑patterns.
-- **rejected** – any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper is present (e.g., “single point of failure”, “unchecked autonomous loop”, “absence of human‑in‑the‑loop fallback”) or the evidence is critically insufficient (e.g., no testing at all, no risk assessment).
+**Mandatory evidence (Section 8)**  
+1. Real‑world testing  
+2. Failure‑mode analysis  
+3. Tamper‑evident audit‑trail of all autonomous decisions  
+4. Quantitative comparison of agent decisions to qualified human decisions  
 
-**What to do:**
-1. Read the entire submission carefully.
-2. Check each mandatory evidence element listed in Section 8.
-3. Scan for any anti‑pattern from Section 9.
-4. Choose the appropriate verdict label.
-5. Provide a brief justification (no more than three short sentences) after the verdict label, explaining which evidence items support your decision and, if applicable, which anti‑pattern triggered a rejection.
+**Anti‑patterns (Section 9)** – any listed anti‑pattern (e.g., single point of failure, unchecked autonomous loop, missing human‑in‑the‑loop fallback, hidden manual override, opaque decision logic) triggers a rejection.
 
-The output must consist of the verdict label on the first line, followed by the justification on subsequent line(s). No additional formatting or labels are allowed.+**Verdict rules**  
+- If any anti‑pattern is present → **rejected**.  
+- Else if all four evidence items are fully satisfied → **sound**.  
+- Otherwise → **needs‑more‑evidence**.
+
+**Output format**  
+- First line: the verdict label exactly (`sound`, `needs‑more‑evidence`, or `rejected`).  
+- Following line(s) (max three short sentences): brief justification citing the relevant evidence items or anti‑pattern(s).  
+
+Do not include any other text or formatting.
```

### Island 3, cell (1, 5), scalar 0.7569

parent `bfa1403db0e02f76` -> candidate `9ceb626ff8a9c405`

```diff
--- parent bfa1403db0e02f76
+++ candidate 9ceb626ff8a9c405
@@ -1,29 +1,24 @@
-You are to judge a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are evaluating a capability case that proposes to eliminate per‑action human approval for an industrial operational‑change gateway.
 
-**Verdict options (output exactly one, case‑sensitive):**  
-- SOUND  
-- NEEDS_MORE_EVIDENCE  
-- REJECTED  
+**Output exactly two lines**
+1. One verdict word, case‑sensitive: SOUND, NEEDS_MORE_EVIDENCE, or REJECTED.  
+2. A brief justification naming which evidence items are satisfied or missing and any anti‑pattern(s) identified.
 
-**Evidence checklist (Section 8, Strategy C)** – each item must be satisfied for a SOUND verdict:  
-1. Real‑world testing in a representative operational environment.  
-2. Documented failure‑mode analysis with mitigation.  
-3. Reliable tamper‑evident audit trail of decisions and actions.  
-4. Comparison of autonomous decisions to those of a qualified human, showing comparable safety and effectiveness.
+**Evidence (all four required for SOUND)**
+- Real‑world testing in a representative operational setting.  
+- Documented failure‑mode analysis with mitigations.  
+- Tamper‑evident audit trail of decisions and actions.  
+- Comparison showing autonomous decisions are at least as safe/effective as a qualified human.
 
-**Anti‑patterns (Section 9, ITOT‑boundary‑as‑architecture)** – presence of any forces a REJECTED verdict, regardless of evidence:  
-- A: “black‑box” AI lacking explainability.  
-- B: No manual fallback override.  
-- C: Bypassing established safety interlocks.  
-- D: Inadequate separation of safety‑critical from non‑critical functions.
+**Anti‑patterns (any one forces REJECTED)**
+- Black‑box AI lacking explainability.  
+- No manual fallback override.  
+- Bypassing established safety interlocks.  
+- Mixing safety‑critical and non‑critical functions.
 
-**Decision rules**  
-- If all four evidence items are met **and** no anti‑pattern is present → **SOUND**.  
-- If one or more evidence items are missing or insufficient **and** no anti‑pattern is present → **NEEDS_MORE_EVIDENCE**.  
-- If any anti‑pattern is present → **REJECTED** (overrides evidence).
-
-**Response format** – exactly two lines:  
-1. The verdict word (SOUND, NEEDS_MORE_EVIDENCE, or REJECTED).  
-2. A brief justification naming which evidence items are satisfied or lacking and any anti‑pattern(s) identified.
+**Decision rules**
+1. If any anti‑pattern is present → REJECTED.  
+2. Else if all four evidence items are present → SOUND.  
+3. Otherwise → NEEDS_MORE_EVIDENCE.
 
 Proceed with the assessment now.
```

### Island 3, cell (0, 5), scalar 0.7261

parent `bfa1403db0e02f76` -> candidate `942c5cc710658da4`

```diff
--- parent bfa1403db0e02f76
+++ candidate 942c5cc710658da4
@@ -1,29 +1,29 @@
-You are to judge a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are to evaluate a capability case that proposes eliminating per‑action human approval for an industrial operational‑change gateway action.
 
-**Verdict options (output exactly one, case‑sensitive):**  
+**Possible verdicts (output exactly one, case‑sensitive):**  
 - SOUND  
 - NEEDS_MORE_EVIDENCE  
 - REJECTED  
 
-**Evidence checklist (Section 8, Strategy C)** – each item must be satisfied for a SOUND verdict:  
-1. Real‑world testing in a representative operational environment.  
-2. Documented failure‑mode analysis with mitigation.  
-3. Reliable tamper‑evident audit trail of decisions and actions.  
-4. Comparison of autonomous decisions to those of a qualified human, showing comparable safety and effectiveness.
+**Section 8 – Strategy C evidence (all must be met for SOUND):**  
+1. Real‑world testing in a representative operational setting.  
+2. Documented failure‑mode analysis with mitigation strategies.  
+3. tamper‑evident audit trail of all decisions and actions.  
+4. Comparative study showing autonomous decisions match or exceed a qualified human’s safety and effectiveness.
 
-**Anti‑patterns (Section 9, ITOT‑boundary‑as‑architecture)** – presence of any forces a REJECTED verdict, regardless of evidence:  
-- A: “black‑box” AI lacking explainability.  
-- B: No manual fallback override.  
-- C: Bypassing established safety interlocks.  
-- D: Inadequate separation of safety‑critical from non‑critical functions.
+**Section 9 – Anti‑patterns (any occurrence forces REJECTED, regardless of evidence):**  
+- Black‑box AI with no explainability.  
+- Absence of a manual fallback/override.  
+- Bypass of established safety interlocks.  
+- Failure to separate safety‑critical from non‑critical functions.
 
-**Decision rules**  
-- If all four evidence items are met **and** no anti‑pattern is present → **SOUND**.  
-- If one or more evidence items are missing or insufficient **and** no anti‑pattern is present → **NEEDS_MORE_EVIDENCE**.  
-- If any anti‑pattern is present → **REJECTED** (overrides evidence).
+**Decision logic**  
+- If any anti‑pattern is identified → REJECTED.  
+- Else if items 1‑4 are all satisfied → SOUND.  
+- Otherwise → NEEDS_MORE_EVIDENCE.
 
-**Response format** – exactly two lines:  
-1. The verdict word (SOUND, NEEDS_MORE_EVIDENCE, or REJECTED).  
-2. A brief justification naming which evidence items are satisfied or lacking and any anti‑pattern(s) identified.
+**Response format – exactly two lines:**  
+1. The verdict word.  
+2. A concise justification naming which evidence items are present or missing and any anti‑pattern(s) detected.
 
 Proceed with the assessment now.
```

### Island 3, cell (0, 5), scalar 0.7524

parent `bfa1403db0e02f76` -> candidate `b348147b83ff62ca`

```diff
--- parent bfa1403db0e02f76
+++ candidate b348147b83ff62ca
@@ -1,29 +1,29 @@
-You are to judge a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You must evaluate a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway.
 
-**Verdict options (output exactly one, case‑sensitive):**  
+**Possible verdicts (output exactly one, case‑sensitive):**  
 - SOUND  
 - NEEDS_MORE_EVIDENCE  
 - REJECTED  
 
-**Evidence checklist (Section 8, Strategy C)** – each item must be satisfied for a SOUND verdict:  
-1. Real‑world testing in a representative operational environment.  
-2. Documented failure‑mode analysis with mitigation.  
-3. Reliable tamper‑evident audit trail of decisions and actions.  
-4. Comparison of autonomous decisions to those of a qualified human, showing comparable safety and effectiveness.
+**Evidence requirements (Section 8, Strategy C).** All four must be met for a SOUND verdict:  
+E1 – Real‑world testing in a representative operational environment.  
+E2 – Documented failure‑mode analysis with mitigation strategies.  
+E3 – Tamper‑evident audit trail of decisions and actions.  
+E4 – Comparative study showing autonomous decisions are at least as safe/effective as those of a qualified human.
 
-**Anti‑patterns (Section 9, ITOT‑boundary‑as‑architecture)** – presence of any forces a REJECTED verdict, regardless of evidence:  
-- A: “black‑box” AI lacking explainability.  
-- B: No manual fallback override.  
-- C: Bypassing established safety interlocks.  
-- D: Inadequate separation of safety‑critical from non‑critical functions.
+**Anti‑patterns (Section 9, ITUT‑boundary‑as‑architecture).** Presence of any forces a REJECTED verdict, regardless of evidence:  
+AP‑A – “black‑box” AI with no explainability.  
+AP‑B – No manual fallback override.  
+AP‑C – Bypassing established safety interlocks.  
+AP‑D – Poor separation of safety‑critical from non‑critical functions.
 
 **Decision rules**  
-- If all four evidence items are met **and** no anti‑pattern is present → **SOUND**.  
-- If one or more evidence items are missing or insufficient **and** no anti‑pattern is present → **NEEDS_MORE_EVIDENCE**.  
-- If any anti‑pattern is present → **REJECTED** (overrides evidence).
+- If **E1‑E4 are all satisfied** *and* **no AP‑X appears** → **SOUND**.  
+- If **any E‑item is missing or insufficient** *and* **no AP‑X appears** → **NEEDS_MORE_EVIDENCE**.  
+- If **any AP‑X is present** → **REJECTED** (overrides evidence).
 
-**Response format** – exactly two lines:  
+**Output format** – exactly two lines:  
 1. The verdict word (SOUND, NEEDS_MORE_EVIDENCE, or REJECTED).  
-2. A brief justification naming which evidence items are satisfied or lacking and any anti‑pattern(s) identified.
+2. A concise justification that lists which evidence items are satisfied (e.g., “E1,E3 satisfied; E2,E4 missing”) and any anti‑pattern(s) detected (e.g., “AP‑B”).  
 
-Proceed with the assessment now.+Provide the assessment now.
```

### Island 3, cell (0, 5), scalar 0.8485

parent `bfa1403db0e02f76` -> candidate `f847816656c057e9`

```diff
--- parent bfa1403db0e02f76
+++ candidate f847816656c057e9
@@ -1,29 +1,29 @@
-You are to judge a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are to evaluate a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
 
-**Verdict options (output exactly one, case‑sensitive):**  
-- SOUND  
-- NEEDS_MORE_EVIDENCE  
-- REJECTED  
+**Verdict (choose exactly one, case‑sensitive):**  
+SOUND  
+NEEDS_MORE_EVIDENCE  
+REJECTED  
 
-**Evidence checklist (Section 8, Strategy C)** – each item must be satisfied for a SOUND verdict:  
-1. Real‑world testing in a representative operational environment.  
-2. Documented failure‑mode analysis with mitigation.  
-3. Reliable tamper‑evident audit trail of decisions and actions.  
-4. Comparison of autonomous decisions to those of a qualified human, showing comparable safety and effectiveness.
+**Evidence items (Section 8, Strategy C) – label each as satisfied (✓) or missing (✗):**  
+E1 – Real‑world testing in a representative operational environment.  
+E2 – Documented failure‑mode analysis with mitigation.  
+E3 – Reliable tamper‑evident audit trail of decisions and actions.  
+E4 – Comparison of autonomous decisions to those of a qualified human, showing comparable safety and effectiveness.
 
-**Anti‑patterns (Section 9, ITOT‑boundary‑as‑architecture)** – presence of any forces a REJECTED verdict, regardless of evidence:  
-- A: “black‑box” AI lacking explainability.  
-- B: No manual fallback override.  
-- C: Bypassing established safety interlocks.  
-- D: Inadequate separation of safety‑critical from non‑critical functions.
+**Anti‑patterns (Section 9, ITUT‑boundary‑as‑architecture) – any present forces REJECTED regardless of evidence:**  
+A – “black‑box” AI lacking explainability.  
+B – No manual fallback override.  
+C – Bypassing established safety interlocks.  
+D – Inadequate separation of safety‑critical from non‑critical functions.
 
 **Decision rules**  
-- If all four evidence items are met **and** no anti‑pattern is present → **SOUND**.  
-- If one or more evidence items are missing or insufficient **and** no anti‑pattern is present → **NEEDS_MORE_EVIDENCE**.  
-- If any anti‑pattern is present → **REJECTED** (overrides evidence).
+- If all E1‑E4 are ✓ and none of A‑D are present → **SOUND**.  
+- If any E1‑E4 are ✗ and none of A‑D are present → **NEEDS_MORE_EVIDENCE**.  
+- If any of A‑D are present → **REJECTED** (overrides evidence).
 
-**Response format** – exactly two lines:  
-1. The verdict word (SOUND, NEEDS_MORE_EVIDENCE, or REJECTED).  
-2. A brief justification naming which evidence items are satisfied or lacking and any anti‑pattern(s) identified.
+**Response format – exactly two lines:**  
+1. The verdict word.  
+2. A concise justification in the form: `E1✓,E2✗,E3✓,E4✓; anti‑patterns: B,D` (list only the items that are missing or present; omit sections with no entries).  
 
-Proceed with the assessment now.+Produce the answer now.
```


## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 15 | 15 | 15 | 0.6080 | 46.7% | 2318 |
| `proposer-distilled@/adapters/20261017` | 16 | 16 | 16 | 0.6219 | 50.0% | 2314 |

Paired difference, distilled minus stock, over 15 complete pairs: mean +0.0313 (sd 0.1236, se 0.0319), **+0.98 sigma**, p 0.344; distilled ahead in 10, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 48 | 47 | 47 | 0.4373 | 68.1% | 1995 |
| `proposer-distilled@/adapters/20261017` | 48 | 47 | 47 | 0.4607 | 68.1% | 1942 |

Paired difference, distilled minus stock, over 45 complete pairs: mean +0.0260 (sd 0.1745, se 0.0260), **+1.00 sigma**, p 0.323; distilled ahead in 25, tied in 0.

## Proposal diversity (mean pairwise TF-IDF cosine distance)

| Generation | Stock | Distilled | Distilled / stock |
|---|---|---|---|
| 0 | 0.505 | 0.507 | 1.00 |
| 1 | 0.539 | 0.557 | 1.03 |
| 2 | 0.586 | 0.608 | 1.04 |

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
