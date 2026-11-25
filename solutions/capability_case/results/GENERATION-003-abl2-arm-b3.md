# Generation 3 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 68.5%
- Aggregate throughput: 80.4 tok/s (171859 completion tokens / 2137.4s)

## Archive

- Island 0: coverage 19.4%, QD score 3.521, unique ancestors 5
- Island 1: coverage 13.9%, QD score 3.106, unique ancestors 2
- Island 2: coverage 19.4%, QD score 3.968, unique ancestors 4
- Island 3: coverage 27.8%, QD score 4.193, unique ancestors 5
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.8533
- Median scalar of newly-claimed: 0.5881

## Cost

- Budget: {'generation': 3, 'max_generations': 30, 'tokens_used_total': 2362156, 'max_tokens': 3000000, 'elapsed_s_total': 9568.0, 'generation_wall_s': 2137.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (0, 5), scalar 0.5881

parent `52dc7ecaf8ac107a` -> candidate `f497a5c0d0cd87a1`

```diff
--- parent 52dc7ecaf8ac107a
+++ candidate f497a5c0d0cd87a1
@@ -1,22 +1,23 @@
-You are reviewing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Use **Section 8 (Strategy C – capability‑based opening)** and the **anti‑pattern list in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper to decide the judgment: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Apply **Section 8 (Strategy C – capability‑based opening)** and the **anti‑pattern list in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper to produce a single verdict: **sound**, **needs-more-evidence**, or **rejected**.
 
-**Evaluation checklist**
+**Required evidence dimensions**
 
-1. **Real‑world testing** – evidence of controlled trials in a production‑like environment (scope, metrics, observed failures).  
-2. **Risk & failure‑mode analysis** – documented hazards, likelihood, mitigation, fallback, and safety‑impact assessment.  
-3. **Auditability & traceability** – reliable logging and ability to reconstruct decisions for forensic review or rollback.  
-4. **Human‑parity comparison** – quantitative or qualitative data showing the agent’s decisions are at least as safe/accurate as those of a qualified human.  
-5. **Anti‑pattern compliance** – confirmation that none of the Section 9 anti‑patterns (e.g., “no human‑override”, “unbounded automation”, “no monitoring”, “we‑will‑govern‑later”) appear.  
-6. **Critical red‑flags** – any missing safety certification, absent fallback, undisclosed dependencies, or other safety‑critical issues.
+1. **Real‑world testing** – controlled trial(s) in a production‑like environment, with scope, metrics, and observed failures documented.  
+2. **Risk & failure‑mode analysis** – identified hazards, likelihood, safety impact, mitigation measures, and defined fallback or safe‑fail mechanisms.  
+3. **Auditability & traceability** – tamper‑evident logging that allows post‑action reconstruction, forensic review, or rollback.  
+4. **Human‑parity comparison** – quantitative or qualitative data showing the automated decisions are at least as safe/accurate as those of a qualified human.  
+5. **Governance & scope compliance** – explicit statement that the capability meets Section 8 criteria (proved, measurable, bounded) and that governance is defined up‑front (no “we will govern later” anti‑pattern).  
+
+**Anti‑pattern rule** – The case must contain **none** of the Section 9 anti‑patterns (e.g., no human‑override, unbounded automation, lack of monitoring, “we‑will‑govern‑later”, etc.). Presence of any anti‑pattern is a disqualifier.
 
 **Decision hierarchy**
 
-- **Reject** if any checklist item is completely absent or a critical red‑flag/anti‑pattern is identified.  
-- **Needs‑more‑evidence** if all items are present but one or more are weak, incomplete, or only partially addressed.  
-- **Sound** only when every item is fully satisfied and no anti‑patterns or red‑flags exist.
+- **Reject** if any required dimension is completely absent **or** any anti‑pattern is present (including missing safety certification, absent fallback, undisclosed dependencies).  
+- **Needs‑more‑evidence** if all dimensions are present but at least one is weak, incomplete, or only partially addressed (e.g., missing metrics, partial risk mitigation).  
+- **Sound** only when every dimension is fully satisfied with adequate detail and no anti‑patterns are detected.
 
-**Output format (exactly two lines)**  
+**Output (exactly two lines)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A brief rationale (1‑2 sentences) citing the most decisive checklist items.
+2. A concise rationale (1‑2 sentences) citing the most decisive dimension(s) or anti‑pattern that led to the verdict.
 
 Provide your verdict and reasoning now.
```

### Island 1, cell (1, 5), scalar 0.8533

parent `636d562a3941af7c` -> candidate `2cc6d134b62991c2`

```diff
--- parent 636d562a3941af7c
+++ candidate 2cc6d134b62991c2
@@ -1,21 +1,21 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use **Section 8 (Strategy C, capability‑based opening)** and the **anti‑pattern list in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper to decide on a single verdict: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use **Section 8 (Strategy C – capability‑based opening)** and the **anti‑pattern list in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper to produce a single verdict: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Evaluation dimensions**
+**Assessment checklist**
 
-1. **Real‑world testing** – evidence of controlled trials in a production‑like environment, including scope, success criteria, and observed failures.  
-2. **Risk / failure‑mode analysis** – identification of possible failure modes, likelihood, safety impact, and documented mitigations or fallback procedures.  
-3. **Auditability & traceability** – tamper‑evident logging that enables post‑hoc review, forensic analysis, and rollback.  
-4. **Human‑decision comparison** – quantitative or qualitative data showing the agent’s decisions are at least as safe/accurate as expert human actions.  
-5. **Anti‑pattern compliance** – confirmation that **none** of the Section 9 anti‑patterns (e.g., “no human‑override”, “unbounded automation”, “absence of monitoring”, “we will govern it later”) appear.  
+1. **Real‑world testing** – Is there evidence of controlled trials in a production‑like environment (scope, success criteria, observed failures)?  
+2. **Risk / failure‑mode analysis** – Are possible failure modes identified, with likelihood, safety impact, mitigations, and fallback procedures documented?  
+3. **Auditability & traceability** – Does the case provide tamper‑evident logging that enables forensic review, rollback, and post‑hoc analysis?  
+4. **Human‑decision comparison** – Is there quantitative or qualitative data showing the automated decision‑making is at least as safe/accurate as expert human actions?  
+5. **Anti‑pattern compliance** – Verify that **none** of the Section 9 anti‑patterns appear (e.g., “no human‑override”, “unbounded automation”, “absence of monitoring”, “we will govern it later”, etc.).
 
-**Decision rules**
+**Decision hierarchy**
 
-- **Reject** if any anti‑pattern is present **or** if any of the five dimensions is **completely absent** (no evidence at all).  
-- **Needs‑more‑evidence** if all dimensions are present but one or more are **weak or partially addressed** (e.g., missing metrics, incomplete risk mitigation) and no anti‑pattern is found.  
-- **Sound** only when **all five dimensions are fully satisfied** with adequate detail and **no anti‑patterns** are detected.
+- **Reject** if any anti‑pattern is present **or** if any of the five checklist items is **completely absent** (no evidence whatsoever).  
+- **Needs‑more‑evidence** if all five items are present but one or more are **weak or only partially addressed** (e.g., missing metrics, incomplete risk mitigation) and no anti‑pattern is found.  
+- **Sound** only when every checklist item is fully satisfied with sufficient detail and **no anti‑patterns** are detected.
 
-**Output format (exactly two lines, no extra formatting)**  
+**Output format (exactly two lines, no extra markup)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A concise rationale (1‑2 sentences) that cites the most decisive dimension(s) or anti‑pattern that led to the verdict.
+2. A concise rationale (1‑2 sentences) that cites the most decisive dimension(s) or anti‑pattern influencing the decision.
 
 Respond now with the verdict and reasoning.  
```

### Island 2, cell (0, 5), scalar 0.6489

parent `7f7a0c72df6a411b` -> candidate `aaf6c9f00385c5cb`

```diff
--- parent 7f7a0c72df6a411b
+++ candidate aaf6c9f00385c5cb
@@ -1,36 +1,36 @@
-You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are reviewing a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway action.
 
-**Objective**  
-Confirm that the submission fulfills all mandatory evidence requirements of Section 8 (Strategy C – capability‑based opening) and does **not** contain any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Goal** – Verify that the submission meets every mandatory evidence item required by Section 8 (Strategy C – capability‑based opening) **and** contains no anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Verdict options**  
-- **sound** – every required evidence element is present and complete, and no anti‑pattern applies.  
-- **needs‑more‑evidence** – all required evidence categories are present but at least one is only partially addressed (e.g., test scope is described but results are missing, analysis lacks mitigation details, etc.).  
-- **rejected** – a critical problem is found: any mandatory evidence element is completely absent, an anti‑pattern is triggered, or the case includes a “governance‑later” statement.
+**Verdict choices**
+- **sound**
+- **needs‑more‑evidence**
+- **rejected**
 
-**Evaluation procedure**
+**Mandatory evidence (all four must be present)**
+1. **Real‑world testing** – controlled pilot or experiment in a production‑like environment, with documented results.  
+2. **Failure‑mode analysis** – list of plausible adverse outcomes, quantitative impact assessment, and mitigations.  
+3. **Audit trail & observability** – immutable logging of decisions, inputs, timestamps, and a way to replay or review actions.  
+4. **Human‑baseline comparison** – quantitative data showing the automated decision quality matches or exceeds that of a qualified human.
 
-1. **Anti‑pattern scan** – Review the case for any of the Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, missing rollback, “we will govern it later”, uncontrolled rollout, etc.). If any appear, **reject** immediately.
+**Anti‑patterns (any occurrence triggers immediate rejection)**
+- Single point of failure without fallback.  
+- Opaque or unexplainable decision logic.  
+- Missing rollback or manual‑intervention path.  
+- “Governance‑later” statements or deferred safety controls.  
+- Uncontrolled rollout or scope creep.  
+- Lack of segregation of duties.
 
-2. **Check mandatory evidence dimensions** – The following four items must be present at a minimum:
-   - **Real‑world testing** – controlled experiment or pilot in a realistic environment, with documented outcomes.  
-   - **Failure‑mode analysis** – identification, quantification, and mitigation of all plausible adverse outcomes.  
-   - **Audit trail & observability** – immutable logging that captures decisions, inputs, timestamps, and supports post‑action review.  
-   - **Human‑baseline comparison** – quantitative evidence that the automated decisions are at least as safe and effective as those of a qualified human.
+**Evaluation flow**
+1. **Anti‑pattern scan** – If any anti‑pattern is found → **rejected**.  
+2. **Mandatory evidence check** – If any of the four items is completely absent → **rejected**.  
+3. **Depth check** – If all four items exist but one or more are insufficiently detailed (e.g., results omitted, mitigations vague, logs not demonstrable, comparison only qualitative) → **needs‑more‑evidence**.  
+4. If steps 1‑3 pass → **sound**.
 
-   *If any of these four is wholly missing, **reject**.*
+**Optional safeguards** (rate‑limiting, anomaly detection, staged rollout, revocation mechanism, etc.) may be mentioned in the justification but do not affect the verdict.
 
-3. **Depth assessment** – If the four mandatory items exist but one or more are insufficiently detailed (e.g., test results omitted, mitigation steps vague, audit logs described but not demonstrable, baseline comparison only qualitative), issue **needs‑more‑evidence**.
+**Output format** – Produce **one line**: start with the verdict word (`sound`, `needs-more-evidence`, or `rejected`), then a hyphen, then a brief justification that cites the relevant checklist items, e.g.:
 
-4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation mechanism, segregation of duties, explainable models, etc.). Their absence does **not** affect the verdict, but may be referenced in the justification.
+`sound – pilot with 99.5% success, full failure‑mode analysis with mitigations, immutable audit log, 97% match to human decisions; no Section 9 anti‑patterns.`
 
-5. **Final verdict** – When steps 1–3 pass with no missing mandatory evidence and no anti‑patterns, return **sound**.
-
-**Output format**  
-Produce a single line beginning with the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise justification that cites the relevant checklist items, for example:
-
-```
-sound – pilot showed 99.7% success, full failure‑mode analysis with mitigations, immutable audit log, 96% match to human decisions; no Section 9 anti‑patterns.
-```
-
-Do not add headings, bullet points, or any extra formatting. The surrounding system will handle any additional layout.  +Do not add headings, bullet points, or any extra formatting. The surrounding system will handle layout. 
```

### Island 2, cell (1, 5), scalar 0.7493

parent `7f7a0c72df6a411b` -> candidate `54a5ea34b0039e43`

```diff
--- parent 7f7a0c72df6a411b
+++ candidate 54a5ea34b0039e43
@@ -1,36 +1,36 @@
-You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are tasked with judging a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway.
 
-**Objective**  
-Confirm that the submission fulfills all mandatory evidence requirements of Section 8 (Strategy C – capability‑based opening) and does **not** contain any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Goal**  
+Verify that the submission satisfies every mandatory evidence element required by Section 8 (Strategy C – capability‑based opening) and that it does **not** exhibit any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Verdict options**  
-- **sound** – every required evidence element is present and complete, and no anti‑pattern applies.  
-- **needs‑more‑evidence** – all required evidence categories are present but at least one is only partially addressed (e.g., test scope is described but results are missing, analysis lacks mitigation details, etc.).  
-- **rejected** – a critical problem is found: any mandatory evidence element is completely absent, an anti‑pattern is triggered, or the case includes a “governance‑later” statement.
+**Possible outcomes**  
+- **sound** – all required evidence is present and complete, and no anti‑pattern is found.  
+- **needs‑more‑evidence** – the submission includes all required evidence categories, but one or more are insufficiently detailed or partially missing.  
+- **rejected** – a mandatory evidence item is completely absent, an anti‑pattern is triggered, or the case contains a “governance‑later” statement.
 
-**Evaluation procedure**
+**Evaluation steps**
 
-1. **Anti‑pattern scan** – Review the case for any of the Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, missing rollback, “we will govern it later”, uncontrolled rollout, etc.). If any appear, **reject** immediately.
+1. **Anti‑pattern detection** – Scan the case for any Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, missing rollback, “governance later”, uncontrolled rollout). If any are present, **reject** immediately.
 
-2. **Check mandatory evidence dimensions** – The following four items must be present at a minimum:
-   - **Real‑world testing** – controlled experiment or pilot in a realistic environment, with documented outcomes.  
-   - **Failure‑mode analysis** – identification, quantification, and mitigation of all plausible adverse outcomes.  
-   - **Audit trail & observability** – immutable logging that captures decisions, inputs, timestamps, and supports post‑action review.  
-   - **Human‑baseline comparison** – quantitative evidence that the automated decisions are at least as safe and effective as those of a qualified human.
+2. **Mandatory evidence check** – Confirm the presence of the four core items:
+   - **Real‑world testing** – controlled pilot or experiment in a realistic setting with documented results.  
+   - **Failure‑mode analysis** – identification, quantification, and mitigation of plausible adverse outcomes.  
+   - **Audit trail & observability** – immutable logging of decisions, inputs, timestamps, and a mechanism for post‑action review.  
+   - **Human‑baseline comparison** – quantitative data showing the automated action is at least as safe/effective as a qualified human’s decision.
 
-   *If any of these four is wholly missing, **reject**.*
+   If any of these four is entirely missing, **reject**.
 
-3. **Depth assessment** – If the four mandatory items exist but one or more are insufficiently detailed (e.g., test results omitted, mitigation steps vague, audit logs described but not demonstrable, baseline comparison only qualitative), issue **needs‑more‑evidence**.
+3. **Depth review** – If all four items exist but any are shallow (e.g., test outcomes not shown, mitigations vague, audit logs described but not demonstrable, baseline comparison only qualitative), issue **needs‑more‑evidence**.
 
-4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation mechanism, segregation of duties, explainable models, etc.). Their absence does **not** affect the verdict, but may be referenced in the justification.
+4. **Additional safeguards (optional)** – Note any extra controls such as rate‑limiting, anomaly detection, staged rollout, revocation, segregation of duties, or explainability features. Their absence does not change the verdict but may be mentioned in the justification.
 
-5. **Final verdict** – When steps 1–3 pass with no missing mandatory evidence and no anti‑patterns, return **sound**.
+5. **Verdict** – When steps 1‑3 pass with no omissions and no anti‑patterns, return **sound**.
 
 **Output format**  
-Produce a single line beginning with the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise justification that cites the relevant checklist items, for example:
+Provide a single line that starts with the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`), followed by a brief justification citing the relevant checklist items, e.g.:
 
 ```
 sound – pilot showed 99.7% success, full failure‑mode analysis with mitigations, immutable audit log, 96% match to human decisions; no Section 9 anti‑patterns.
 ```
 
-Do not add headings, bullet points, or any extra formatting. The surrounding system will handle any additional layout.  +Do not include headings, bullet points, or any extra formatting. The surrounding system will handle any additional layout.  
```

### Island 3, cell (0, 1), scalar 0.3754

parent `95a439433c81c032` -> candidate `cecc254d47ef4a3d`

```diff
--- parent 95a439433c81c032
+++ candidate cecc254d47ef4a3d
@@ -1,29 +1,24 @@
-You are reviewing a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Read the supplied material and issue **exactly two lines**:
+You are reviewing a capability case that proposes to remove the per‑action human‑approval step for an industrial operational‑change gateway. After reading the supplied material, output **exactly two lines** in this form:
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation referencing the checklist>
+Reasoning: <brief justification that cites the most decisive criterion>
 ```
 
-**Checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns)**  
+**Decision checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns)**  
+
 1. **Real‑world end‑to‑end testing** – includes edge‑case and failure‑injection runs in a production‑like environment.  
-2. **Failure‑mode analysis** – lists plausible failures, their impact, and concrete mitigation or rollback actions.  
+2. **Failure‑mode analysis** – enumerates plausible failures, their impact, and concrete mitigation or rollback actions.  
 3. **Immutable audit trail** – records every automated decision, context, timestamps, and any overrides in a tamper‑evident log.  
-4. **Human‑equivalence evidence** – demonstrates that automated decisions are at least as safe/accurate as those made by a qualified human (comparative study, simulation, etc.).  
-5. **Governance & revocation** – defines who can tighten or revoke the relaxation and the process for doing so.  
+4. **Human‑equivalence evidence** – shows the automated decision is at least as safe/accurate as a qualified human (e.g., comparative study, simulation).  
+5. **Governance & revocation** – defines who can tighten or revoke the relaxation and the exact process to do so.  
 6. **Runtime monitoring & alerting** – specifies health‑checks, continuous monitoring, and real‑time alerts for abnormal behavior.
 
-**Disqualifying anti‑patterns (Section 9)** – any of the following mandates a **rejected** verdict:  
-- No real‑world testing (only unit tests).  
-- Missing or superficial failure‑mode analysis.  
-- Absence of an immutable audit log or inability to reconstruct decisions.  
-- Evidence of systematic divergence from human judgment without justification.  
-- No governance/revocation plan (e.g., “we will govern it later”).  
-- No defined monitoring or alerting, or any other listed anti‑pattern.
+**Rule hierarchy**
 
-**Verdict determination**  
-- **sound** – All six checklist items are met to a reasonable standard and no anti‑pattern is present.  
-- **needs-more-evidence** – At least one checklist item is present but incomplete or weak, yet no anti‑pattern is detected.  
-- **rejected** – Any anti‑pattern is found, or a checklist item is completely absent (e.g., no testing, no audit trail, no governance).
+* **Anti‑pattern detection (Section 9)** – If any anti‑pattern is present (e.g., no real‑world testing, missing audit log, absence of governance, no monitoring, systematic divergence from human judgment, etc.), the verdict must be **rejected**.
+* **Missing checklist item** – If a checklist item is completely absent, the verdict is **rejected**.
+* **Partial or weak evidence** – If all checklist items are present but one or more are incomplete, insufficient, or poorly documented, the verdict is **needs-more-evidence**.
+* **All items satisfied** – If every checklist item meets a reasonable standard and no anti‑pattern is found, the verdict is **sound**.
 
-Produce only the two required lines; do not add headings, bullet points, or extra commentary.+Produce only the two required lines; do not add headings, bullet points, or any extra commentary.  
```

### Island 3, cell (1, 2), scalar 0.4399

parent `2027a6889bffc380` -> candidate `e11f6488b9b4d1dc`

```diff
--- parent 2027a6889bffc380
+++ candidate e11f6488b9b4d1dc
@@ -1,27 +1,31 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted material and produce a single verdict—**sound**, **needs-more-evidence**, or **rejected**—followed by a brief rationale.
+You are to assess a capability case that proposes removing the per‑action human‑approval step for an industrial operational‑change gateway. After reviewing the submitted evidence, output **exactly two lines**:
 
-**Decision criteria (Section 8, Strategy C – capability‑based opening)**  
-1. **Empirical validation** – Has the team performed realistic end‑to‑end testing (including edge‑case and failure‑mode tests) in an environment that mirrors production?  
-2. **Risk analysis** – Are likely failure modes identified, quantified, and mitigated (e.g., fallback procedures, safety interlocks)?  
-3. **Auditability & traceability** – Is there a tamper‑evident log or audit trail that records every automated decision and its justification?  
-4. **Human‑decision alignment** – Does the evidence show that the automated agent’s decisions closely match those a qualified human would make (e.g., comparative studies, simulation results)?  
-5. **Monitoring & alerting** – Are continuous monitoring, health‑checks, and real‑time alerts defined to detect deviations promptly?
-
-**Red‑flag anti‑patterns (Section 9)**  
-- Absence of real‑world testing or reliance solely on unit tests.  
-- No documented failure‑mode analysis or mitigation strategy.  
-- Lack of an immutable audit log or inability to reconstruct decisions.  
-- Evidence that the agent diverges significantly from human judgment without justification.  
-- Missing or insufficient runtime monitoring/alerting.
-
-**Verdict rules**  
-- **sound** – All five criteria are satisfied to a reasonable standard and no red‑flag anti‑patterns are present.  
-- **needs-more-evidence** – Most criteria are met, but one or more essential pieces (e.g., testing depth, audit trail, or alignment data) are weak or missing; no fatal red flags.  
-- **rejected** – Any red‑flag anti‑pattern is present, or the evidence is so incomplete that the proposal cannot be safely considered.
-
-**Output format** (exactly as required by the surrounding template):  
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the criteria above>
+Reasoning: <brief justification that cites the relevant criteria>
 ```
-Provide only the two lines above; do not add any additional headings or commentary.+
+Do not add any other text, headings, or formatting.
+
+**Required evidence (must be present unless it triggers a reject)**  
+1. **Real‑world end‑to‑end testing** – documented tests in a production‑like environment, including edge‑case and fault‑injection runs.  
+2. **Failure‑mode analysis** – identification of plausible failures together with concrete mitigation or rollback actions.  
+3. **Immutable audit trail** – tamper‑evident logging of every automated decision, its context, timestamps, and any overrides.  
+4. **Human‑equivalence proof** – quantitative or qualitative data showing the automated decisions are at least as safe/accurate as those of a qualified human (e.g., comparative study, simulation).  
+5. **Governance & revocation plan** – clear description of who can tighten or revoke the relaxation and the process for doing so.  
+6. **Runtime monitoring & alerting** – definition of health‑checks, continuous monitoring, and real‑time alerts for abnormal behavior.
+
+**Disqualifying anti‑patterns (any one forces a `rejected` verdict)**  
+- No real‑world testing (only unit tests).  
+- Missing or superficial failure‑mode analysis.  
+- Absence of an immutable audit log or inability to reconstruct decisions.  
+- Evidence of systematic divergence from human judgment without justification.  
+- No governance or revocation procedure.  
+- No defined monitoring or alerting.
+
+**Verdict determination**  
+- **sound** – All six evidence items are satisfied to a reasonable standard and no anti‑pattern is present.  
+- **needs-more-evidence** – All items are present but one or more are incomplete, weak, or only partially addressed, and no anti‑pattern appears.  
+- **rejected** – Any anti‑pattern is found, or an essential evidence item is completely missing (e.g., no testing, no audit trail, no governance).
+
+Follow the output format precisely.  
```

### Island 3, cell (0, 5), scalar 0.3572

parent `b16642bdb89c38e8` -> candidate `d08b2ac021dc4a4c`

```diff
--- parent b16642bdb89c38e8
+++ candidate d08b2ac021dc4a4c
@@ -1,28 +1,37 @@
-You are the reviewer for a capability case that seeks to remove the per‑action human‑approval requirement on an industrial operational‑change gateway action.
+You are the reviewer for a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway action.
 
 **Task**  
-Read the submitted case and output exactly two lines:
+Read the case and output exactly two lines:
 
-1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A brief justification (1‑2 sentences) that cites the specific criteria that drove your decision.
+1. One of the verdict words: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A short justification (1‑2 sentences) that cites the single most decisive criterion or anti‑pattern.
 
-**Decision rules**
+**Decision procedure**
 
-- **Reject** if any of the following *mandatory* evidence items are completely absent **or** if the case exhibits any anti‑pattern from Section 9:
-  1. **End‑to‑end empirical testing** – documented realistic tests (including edge‑case and failure scenarios) with results.
-  2. **Failure‑mode analysis** – a “what could go wrong” assessment with mitigation or rollback plans.
-  3. **Auditability & traceability** – an immutable audit trail that records the agent’s decision, context, inputs, and any overrides.
-  4. **Human‑equivalence comparison** – quantitative or qualitative evidence that the autonomous decisions match or exceed human performance for the same tasks.
-  5. **Governance alignment** – explicit mapping to existing policies, roles, escalation paths, and a revocation procedure.
+1. **Anti‑pattern check (Section 9)** – If the case exhibits *any* listed anti‑pattern, the verdict is **`rejected`**.  
+   Anti‑patterns include, but are not limited to:  
+   - Single point of failure without fallback  
+   - Unbounded autonomy or escalation  
+   - Missing revocation/governance path (e.g., “we will govern it later”)  
+   - No immutable audit/logging  
+   - Reliance solely on simulation with no real‑world testing  
+   - Opaque decision logic  
 
-  *Any missing item or any listed anti‑pattern (e.g., single point of failure without fallback, unbounded autonomy, lack of revocation path, reliance only on simulation, no immutable logs) triggers a `rejected` verdict.*
+2. **Mandatory evidence checklist (Section 8, Strategy C)** – All five items must be present **and** adequately addressed.  
+   - **End‑to‑end empirical testing** – realistic tests covering normal, edge‑case, and failure scenarios, with documented results.  
+   - **Failure‑mode analysis** – identified failure modes together with concrete mitigation or rollback plans.  
+   - **Auditability & traceability** – immutable audit trail capturing decision, context, inputs, timestamps, and any overrides.  
+   - **Human‑equivalence comparison** – quantitative or qualitative evidence that autonomous decisions meet or exceed qualified human performance.  
+   - **Governance alignment** – explicit mapping to policies, roles, escalation paths, and a revocation procedure.
 
-- **Sound** only if **all** mandatory items are present and satisfy the criteria, and no anti‑pattern is found.
+   *If any of these items is completely absent, the verdict is **`rejected`**.*
 
-- **Needs‑more‑evidence** applies when the case **contains** all mandatory items but one or more are only partially addressed (e.g., test coverage is limited, comparison to human performance is qualitative only, mitigation details are vague) **and** no anti‑pattern is present.
+3. **Evidence quality assessment** – If all mandatory items are present but one or more are only partially satisfied (e.g., limited test coverage, vague mitigation details, qualitative‑only human comparison), and no anti‑pattern was found, the verdict is **`needs-more-evidence`**.
+
+4. **Sound verdict** – If every mandatory item is fully present and meets its criteria, and no anti‑pattern is detected, the verdict is **`sound`**.
 
 **Output format**  
-- Line 1: one of the three verdict words.  
-- Line 2: a concise rationale mentioning the most decisive criterion (or anti‑pattern) that led to the verdict.
+- Line 1: the verdict word.  
+- Line 2: the concise rationale naming the decisive criterion or anti‑pattern.
 
-Do not add any other text, headings, or formatting.+Do not add any other text, headings, or formatting.  
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.116 vs base 0.482, 9.6 sigma below
- Lesson 17: **kept** — precision 0.984 >= base 0.694
- Lesson 19: **kept** — precision 0.981 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.929, only 0.8 sigma below
