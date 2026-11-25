# Generation 5 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 30
- Prefix cache hit rate: 60.8%
- Aggregate throughput: 90.2 tok/s (218557 completion tokens / 2422.4s)

## Archive

- Island 0: coverage 25.0%, QD score 4.658, unique ancestors 4
- Island 1: coverage 30.6%, QD score 5.502, unique ancestors 7
- Island 2: coverage 30.6%, QD score 5.690, unique ancestors 6
- Island 3: coverage 30.6%, QD score 6.090, unique ancestors 4
- Cells newly claimed this generation: 8

## Quality

- Best scalar this generation: 0.7490
- Median scalar of newly-claimed: 0.6374

## Cost

- Budget: {'generation': 5, 'max_generations': 10, 'tokens_used_total': 3694679, 'max_tokens': 8000000, 'elapsed_s_total': 15380.6, 'generation_wall_s': 2422.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 3), scalar 0.5546

parent `bc99371ad5110cf1` -> candidate `d6a46b243c7195e8`

```diff
--- parent bc99371ad5110cf1
+++ candidate d6a46b243c7195e8
@@ -1,24 +1,29 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Your task is to decide whether the case is **Sound**, **Needs More Evidence**, or **Rejected**, in line with Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. judge it as **Sound**, **Needs More Evidence**, or **Rejected** according to Section 8 (Strategy C) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Checklist**
 
-1. **Empirical validation** – Has the team performed realistic end‑to‑end testing (including failure injections) that demonstrates the agent behaves safely under normal and degraded conditions?
-2. **Risk analysis** – Is there a documented assessment of possible failure modes, their likelihood, and impact, with mitigation strategies for each?
-3. **Auditability** – Does the solution provide a tamper‑evident log or other traceability mechanism that records the agent’s decisions and the context in which they were made?
-4. **Human‑equivalence benchmark** – Has the agent’s decision‑making been compared against expert human operators on a representative set of scenarios, showing comparable or better outcomes?
-5. **Compliance with anti‑patterns (Section 9)** – Verify that none of the following red‑flags are present:
-   - Relying on a single point of failure without redundancy.
-   - Absence of a revert/override capability for the operator.
-   - Over‑generalizing results from a narrow test suite.
-   - Ignoring post‑deployment monitoring or anomaly detection.
-   - Insufficient separation between control‑plane and data‑plane functions.
+1. **Real‑world testing** – End‑to‑end trials (including fault injection) that show safe behaviour in normal and degraded modes.  
+2. **Failure‑mode analysis** – Documented list of possible failures, their likelihood, impact, and mitigations or safe‑fallbacks.  
+3. **Auditability** – Tamper‑evident logging or equivalent that records decisions, inputs, and context for post‑hoc review.  
+4. **Human‑parity evidence** – Comparison with expert operators on a representative scenario set demonstrating equal or better outcomes.  
+5. **Anti‑pattern screening (Section 9)** – Ensure none of the following appear:
+   - Single point of failure without redundancy.  
+   - No operator revert/override capability.  
+   - Over‑generalising from a narrow test suite.  
+   - Lack of monitoring or anomaly detection after deployment.  
+   - Insufficient separation of control‑plane and data‑plane functions.
 
-**Decision criteria**
+**Decision rules**
 
-- **Sound** – All checklist items are satisfied, and no anti‑pattern applies. The evidence collectively demonstrates that removing per‑action human approval will not compromise safety, security, or compliance.
-- **Needs More Evidence** – The case meets most items but has one or more gaps (e.g., missing risk analysis, incomplete audit trail, limited testing scope) that could be addressed with additional data or clarification.
-- **Rejected** – One or more anti‑patterns are evident, or a critical safety or security risk is identified that is not mitigated, making the proposal untenable.
+- **Sound** – All five checklist items are satisfied and no anti‑pattern is present.  
+- **Needs More Evidence** – One or more items are partially addressed or missing, but no fatal anti‑pattern is found.  
+- **Rejected** – Any anti‑pattern is evident or a critical safety/security risk is unmitigated.
 
-**Output requirement**
+**Output**
 
-Provide your verdict (**Sound**, **Needs More Evidence**, or **Rejected**) followed by a concise justification that references the specific checklist items or anti‑patterns that led to your decision. Do not include any other text.
+Produce exactly two lines:
+
+1. The verdict (`Sound`, `Needs More Evidence`, or `Rejected`).  
+2. A brief justification that cites the specific checklist item(s) or anti‑pattern(s) that drove the decision.
+
+Do not include any other text.
```

### Island 0, cell (0, 5), scalar 0.7008

parent `9be2aa3fb481730f` -> candidate `4138e1a55b2ff7ab`

```diff
--- parent 9be2aa3fb481730f
+++ candidate 4138e1a55b2ff7ab
@@ -1,25 +1,24 @@
-You are an expert reviewer assessing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Your evaluation must follow Section 8 (Strategy C, capability‑based opening) and ensure none of the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper are present.
+You are an expert reviewer assessing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Your assessment must follow Section 8 (Strategy C, capability‑based opening) and must ensure that none of the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper appear.
 
-**Evaluation checklist (mark each item with a single symbol):**  
+**Checklist (mark each item with exactly one symbol):**  
 - **✔️** – fully satisfied  
 - **⚠️** – partially satisfied / missing but not fatal  
 - **❌** – unsatisfied and represents a critical anti‑pattern  
 
-1. **Real‑world testing** – controlled trials or production‑like simulations with documented results.  
-2. **Failure‑mode analysis** – identified failure scenarios, their impacts, and mitigations or safe fall‑backs.  
-3. **Audit‑trail / observability** – tamper‑evident logging of decisions, inputs, and outcomes.  
-4. **Human‑parity benchmark** – quantitative or qualitative comparison showing performance comparable to expert operators.  
-5. **Anti‑pattern screening** – confirm that none of the Section 9 red‑flags (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties) are present.
+1️⃣ Real‑world testing – controlled trials or production‑like simulations with documented scope and results.  
+2️⃣ Failure‑mode analysis – identified failure scenarios, impacts, and mitigations or safe fall‑backs.  
+3️⃣ Audit‑trail / observability – tamper‑evident logging of inputs, decisions, and outcomes.  
+4️⃣ Human‑parity benchmark – quantitative or qualitative evidence that automation matches or exceeds expert operators.  
+5️⃣ Anti‑pattern screening – confirm that none of the Section 9 red‑flags (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties) are present.
 
-**Decision rules**
+**Decision logic**  
+- If any item is marked **❌**, output **rejected**.  
+- Else if any item is marked **⚠️**, output **needs‑more‑evidence**.  
+- Else (all five items are **✔️**), output **sound**.
 
-- If any item is marked **❌**, the verdict is **rejected**.  
-- Otherwise, if any item is marked **⚠️**, the verdict is **needs‑more‑evidence**.  
-- If all five items are **✔️**, the verdict is **sound**.
-
-**Output (exactly two lines, no extra text)**  
+**Output format (exactly two lines, no extra text or formatting):**  
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief justification referencing the checklist items and symbols that determined the verdict>
+Reasoning: <brief justification that cites the checklist items and the symbols you assigned, e.g., "Item 2 ⚠️ (partial failure‑mode analysis) → needs‑more‑evidence">
 ```
```

### Island 0, cell (0, 5), scalar 0.7405

parent `9be2aa3fb481730f` -> candidate `72e2eec8cdd8e397`

```diff
--- parent 9be2aa3fb481730f
+++ candidate 72e2eec8cdd8e397
@@ -1,25 +1,30 @@
-You are an expert reviewer assessing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Your evaluation must follow Section 8 (Strategy C, capability‑based opening) and ensure none of the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper are present.
+You are an expert reviewer deciding whether a capability case can waive per‑action human approval for an industrial operational‑change gateway action. Follow Section 8 (Strategy C, capability‑based opening) and ensure none of the Section 9 anti‑patterns appear.
 
-**Evaluation checklist (mark each item with a single symbol):**  
-- **✔️** – fully satisfied  
-- **⚠️** – partially satisfied / missing but not fatal  
-- **❌** – unsatisfied and represents a critical anti‑pattern  
+**Evidence items (must be fully satisfied for a “sound” verdict):**
+1. Real‑world testing – documented controlled trials or production‑like simulations.  
+2. Failure‑mode analysis – identified failures with mitigations or safe fall‑backs.  
+3. Audit‑trail / observability – tamper‑evident logging of inputs, decisions, outcomes.  
+4. Human‑parity benchmark – quantitative or qualitative proof of performance comparable to expert operators.
 
-1. **Real‑world testing** – controlled trials or production‑like simulations with documented results.  
-2. **Failure‑mode analysis** – identified failure scenarios, their impacts, and mitigations or safe fall‑backs.  
-3. **Audit‑trail / observability** – tamper‑evident logging of decisions, inputs, and outcomes.  
-4. **Human‑parity benchmark** – quantitative or qualitative comparison showing performance comparable to expert operators.  
-5. **Anti‑pattern screening** – confirm that none of the Section 9 red‑flags (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties) are present.
+**Anti‑patterns (any presence forces a “rejected” verdict):**  
+A. No manual rollback/override.  
+B. Opaque or black‑box AI without explainability.  
+C. Over‑automation lacking safety case.  
+D. Missing runtime monitoring or alerts.  
+E. Inadequate segregation of duties.
+
+**Mark each item:**
+- Evidence: **S** = satisfied, **P** = partially satisfied, **N** = not satisfied.  
+- Anti‑patterns: **Y** = present, **N** = absent.
 
 **Decision rules**
+- If any anti‑pattern is **Y**, verdict = **rejected**.  
+- Else if any evidence item is **N**, verdict = **rejected** (critical gap).  
+- Else if any evidence item is **P**, verdict = **needs‑more‑evidence**.  
+- Else all evidence items are **S**, verdict = **sound**.
 
-- If any item is marked **❌**, the verdict is **rejected**.  
-- Otherwise, if any item is marked **⚠️**, the verdict is **needs‑more‑evidence**.  
-- If all five items are **✔️**, the verdict is **sound**.
-
-**Output (exactly two lines, no extra text)**  
-
+**Output (exactly two lines, no extra text)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief justification referencing the checklist items and symbols that determined the verdict>
+Reasoning: <brief justification citing the specific evidence letters (1‑4) and anti‑pattern letters (A‑E) with their marks that led to the verdict>
 ```
```

### Island 1, cell (1, 5), scalar 0.7490

parent `912078cca66bf895` -> candidate `ef22049c50aaac35`

```diff
--- parent 912078cca66bf895
+++ candidate ef22049c50aaac35
@@ -1,31 +1,33 @@
-You are tasked with judging a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway. After reviewing the submitted material, choose exactly one of the three outcomes defined in the white‑paper (Section 8):
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway. After reviewing the submitted material, select **exactly one** verdict from the three defined in the white‑paper (Section 8):
 
-* **sound**
-* **needs-more-evidence**
-* **rejected**
+- **sound**
+- **needs-more-evidence**
+- **rejected**
 
-#### Evidence that must be present for a **sound** decision  
+### Required evidence for a **sound** verdict  
+All four items must be **clearly documented and sufficient**:
 
-1. **Operational testing** – concrete results from pilots, simulations, or field trials that prove the automation can carry out the action safely without a human operator.  
-2. **Failure‑mode & mitigation plan** – a clear enumeration of plausible failure scenarios together with specific mitigations or fallback procedures.  
-3. **Auditable record** – immutable, tamper‑evident logs or provenance data that capture the inputs, decision logic, and outcomes of each automated execution.  
-4. **Human‑performance benchmark** – quantitative (or well‑justified qualitative) comparison showing the automation meets or exceeds the performance of a qualified human under identical conditions.  
+1. **Operational testing** – results from pilots, simulations, or field trials that demonstrate safe autonomous execution.  
+2. **Failure‑mode & mitigation** – identified failure scenarios together with concrete mitigation or fallback procedures.  
+3. **Auditable record** – immutable, tamper‑evident logs or provenance data capturing inputs, decision logic, and outcomes for each execution.  
+4. **Human‑performance benchmark** – quantitative (or well‑justified qualitative) comparison showing the automation meets or exceeds a qualified human’s performance under identical conditions.
 
-#### Anti‑patterns that automatically trigger **rejected**  
+### Anti‑patterns that force a **rejected** verdict  
+If any of the following is present, the case is automatically **rejected** (Section 9):
 
 - Black‑box logic with no observability or diagnostics.  
-- Claims of “zero risk” because the action is rare.  
+- Claim of “zero risk” because the action is rare.  
 - Deployment of an untested AI in a safety‑critical role.  
-- Lack of a manual override or rapid rollback capability.  
-- Any other pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+- Absence of a manual override or rapid rollback capability.  
+- Any other anti‑pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-#### Decision hierarchy  
-1. If **any** anti‑pattern is detected → verdict **rejected**.  
-2. Otherwise, if **any** of the four evidence items is missing, insufficient, or vague → verdict **needs-more-evidence**.  
-3. If all four evidence items are fully satisfied and no anti‑patterns appear → verdict **sound**.
+### Decision hierarchy  
+1. **Reject** if any anti‑pattern is detected.  
+2. Otherwise, **needs-more-evidence** if any required evidence item is missing, incomplete, or vague.  
+3. Otherwise, **sound**.
 
-#### Output format (must be obeyed exactly)  
+### Output format (must be obeyed exactly)  
 - **Line 1:** the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
-- **Line 2:** a concise rationale (1–2 sentences) that references the specific evidence items or anti‑patterns influencing the decision.  
+- **Line 2:** a concise rationale (1–2 sentences) that references the specific evidence items or anti‑patterns influencing the decision. No extra lines, headings, or prose.
 
 Proceed with the evaluation.
```

### Island 1, cell (0, 5), scalar 0.6549

parent `912078cca66bf895` -> candidate `46a49203528b34eb`

```diff
--- parent 912078cca66bf895
+++ candidate 46a49203528b34eb
@@ -1,31 +1,33 @@
-You are tasked with judging a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway. After reviewing the submitted material, choose exactly one of the three outcomes defined in the white‑paper (Section 8):
+You are evaluating a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway. Select **exactly one** verdict defined in Section 8 of the white‑paper:
 
-* **sound**
-* **needs-more-evidence**
-* **rejected**
+- **sound**
+- **needs-more-evidence**
+- **rejected**
 
-#### Evidence that must be present for a **sound** decision  
+**Evidence that must be demonstrably provided for a “sound” verdict**
 
-1. **Operational testing** – concrete results from pilots, simulations, or field trials that prove the automation can carry out the action safely without a human operator.  
-2. **Failure‑mode & mitigation plan** – a clear enumeration of plausible failure scenarios together with specific mitigations or fallback procedures.  
-3. **Auditable record** – immutable, tamper‑evident logs or provenance data that capture the inputs, decision logic, and outcomes of each automated execution.  
-4. **Human‑performance benchmark** – quantitative (or well‑justified qualitative) comparison showing the automation meets or exceeds the performance of a qualified human under identical conditions.  
+1. **Real‑world validation** – pilots, simulations, or field trials showing the automation can perform the action safely.  
+2. **Failure‑mode analysis** – a catalog of plausible failure scenarios together with concrete mitigation or fallback steps.  
+3. **Auditable trace** – immutable, tamper‑evident logs or provenance records that capture inputs, decision logic, and outcomes for every run.  
+4. **Human‑performance comparison** – quantitative (or well‑justified qualitative) data showing the automation meets or exceeds a qualified human’s performance under the same conditions.  
 
-#### Anti‑patterns that automatically trigger **rejected**  
+**Anti‑patterns that force an automatic “rejected” verdict (Section 9)**  
 
-- Black‑box logic with no observability or diagnostics.  
+- Opaque or black‑box logic with no observability.  
 - Claims of “zero risk” because the action is rare.  
 - Deployment of an untested AI in a safety‑critical role.  
-- Lack of a manual override or rapid rollback capability.  
+- Absence of a manual override or rapid rollback mechanism.  
 - Any other pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-#### Decision hierarchy  
-1. If **any** anti‑pattern is detected → verdict **rejected**.  
+**Decision hierarchy**
+
+1. If **any** anti‑pattern is present → verdict **rejected**.  
 2. Otherwise, if **any** of the four evidence items is missing, insufficient, or vague → verdict **needs-more-evidence**.  
 3. If all four evidence items are fully satisfied and no anti‑patterns appear → verdict **sound**.
 
-#### Output format (must be obeyed exactly)  
+**Output format (must be followed exactly)**  
+
 - **Line 1:** the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
-- **Line 2:** a concise rationale (1–2 sentences) that references the specific evidence items or anti‑patterns influencing the decision.  
+- **Line 2:** a brief rationale (one sentence) that cites the specific evidence item(s) or anti‑pattern(s) that determined the decision.  
 
 Proceed with the evaluation.
```

### Island 2, cell (1, 5), scalar 0.3535

parent `0e857b2c169f75f4` -> candidate `b89f90cc78f4951b`

```diff
--- parent 0e857b2c169f75f4
+++ candidate b89f90cc78f4951b
@@ -1,20 +1,21 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are to decide whether a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway meets the criteria of Section 8 and avoids the anti‑patterns of Section 9.
 
-**Mandatory evidence (Section 8)**  
-1. Real‑world testing  
-2. Failure‑mode analysis  
-3. Tamper‑evident audit‑trail of all autonomous decisions  
-4. Quantitative comparison of agent decisions to qualified human decisions  
+**Evidence that must be supplied (Section 8)**  
+- **Real‑world trial** – documented testing in production‑like conditions covering normal and edge cases.  
+- **Failure‑mode study** – systematic analysis of possible failures, their probabilities, and mitigation measures.  
+- **Tamper‑evident audit log** – immutable record of every autonomous decision for post‑hoc review.  
+- **Human‑level benchmark** – quantitative comparison of the system’s decisions to those of qualified operators.
 
-**Anti‑patterns (Section 9)** – any listed anti‑pattern (e.g., single point of failure, unchecked autonomous loop, missing human‑in‑the‑loop fallback, hidden manual override, opaque decision logic) triggers a rejection.
+**Disqualifying anti‑patterns (Section 9)**  
+The presence of any listed anti‑pattern (e.g., single point of failure, unchecked autonomous loop, missing rollback, opaque decision logic, hidden manual override) mandates a **rejected** verdict.
 
-**Verdict rules**  
-- If any anti‑pattern is present → **rejected**.  
-- Else if all four evidence items are fully satisfied → **sound**.  
-- Otherwise → **needs‑more‑evidence**.
+**Verdict algorithm**  
+1. If any anti‑pattern is detected → **rejected**.  
+2. Else if all four evidence items are fully satisfied → **sound**.  
+3. Otherwise → **needs‑more‑evidence**.
 
 **Output format**  
-- First line: the verdict label exactly (`sound`, `needs‑more‑evidence`, or `rejected`).  
-- Following line(s) (max three short sentences): brief justification citing the relevant evidence items or anti‑pattern(s).  
+- Line 1: the verdict label exactly (`sound`, `needs‑more‑evidence`, or `rejected`).  
+- Lines 2‑4 (up to three short sentences): concise justification referencing the satisfied evidence items or the anti‑pattern(s) that led to the decision.  
 
 Do not include any other text or formatting.
```

### Island 2, cell (1, 4), scalar 0.6199

parent `0e857b2c169f75f4` -> candidate `5ddba71b2cb88868`

```diff
--- parent 0e857b2c169f75f4
+++ candidate 5ddba71b2cb88868
@@ -1,20 +1,20 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are judging a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway.
 
-**Mandatory evidence (Section 8)**  
-1. Real‑world testing  
-2. Failure‑mode analysis  
-3. Tamper‑evident audit‑trail of all autonomous decisions  
-4. Quantitative comparison of agent decisions to qualified human decisions  
+**Evidence required (Section 8)**  
+- Real‑world testing  
+- Failure‑mode analysis  
+- Tamper‑evident audit trail of autonomous decisions  
+- Quantitative comparison with qualified human decisions  
 
-**Anti‑patterns (Section 9)** – any listed anti‑pattern (e.g., single point of failure, unchecked autonomous loop, missing human‑in‑the‑loop fallback, hidden manual override, opaque decision logic) triggers a rejection.
+**Anti‑patterns (Section 9)** – any occurrence of the listed patterns (e.g., single point of failure, unchecked autonomous loop, missing human‑in‑the‑loop fallback, hidden manual override, opaque decision logic) forces a **rejected** verdict.
 
-**Verdict rules**  
-- If any anti‑pattern is present → **rejected**.  
-- Else if all four evidence items are fully satisfied → **sound**.  
-- Otherwise → **needs‑more‑evidence**.
+**Decision flow**
+1. Detect an anti‑pattern → verdict **rejected**.  
+2. Otherwise, if **all four** evidence items are present and satisfactory → verdict **sound**.  
+3. In all other cases → verdict **needs‑more‑evidence**.
 
-**Output format**  
-- First line: the verdict label exactly (`sound`, `needs‑more‑evidence`, or `rejected`).  
-- Following line(s) (max three short sentences): brief justification citing the relevant evidence items or anti‑pattern(s).  
+**Output**  
+- First line: exactly one of `sound`, `needs‑more‑evidence`, or `rejected`.  
+- Subsequent line(s) (up to three brief sentences): justification that cites the relevant evidence items or anti‑pattern(s).  
 
-Do not include any other text or formatting.+Do not add any other text or formatting.
```

### Island 3, cell (1, 4), scalar 0.5812

parent `e9319fb259bfa0c1` -> candidate `29ffb76c21a2fef5`

```diff
--- parent e9319fb259bfa0c1
+++ candidate 29ffb76c21a2fef5
@@ -1,25 +1,29 @@
-You are reviewing a capability case that requests relaxation of the per‑action human‑approval requirement for an industrial operational‑change gateway action. Examine the submitted evidence and decide whether the case meets the standards of Section 8 (Strategy C, capability‑based opening) and does not trigger any anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Apply Section 8 (Strategy C, capability‑based opening) and the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Decision options (choose exactly one):**
-- **sound** – the evidence convincingly supports safe removal of human approval.
-- **needs-more-evidence** – the case is plausible but lacks critical data or analysis.
-- **rejected** – a serious deficiency or an anti‑pattern is present that makes the proposal unsafe.
+**Step 1 – Anti‑pattern scan**  
+If the proposal exhibits any anti‑pattern listed in Section 9 (e.g., single point of failure, unbounded authority, opaque logic, insufficient monitoring, etc.), the verdict is **rejected** and you stop.
 
-**Evaluation checklist (all items must be satisfied for a “sound” verdict):**
-1. **Real‑world testing** – documented tests in a representative environment, with results showing reliable autonomous behavior.
-2. **Failure‑mode analysis** – explicit identification of plausible failure scenarios, their impact, and mitigations.
-3. **Auditability** – a tamper‑evident log or trace that can reconstruct the agent’s decision after the fact.
-4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the agent’s actions are at least as safe and effective as a human operator would be.
-5. **Risk alignment** – the residual risk after mitigation is within the thresholds defined in Section 8.
-6. **Absence of Section 9 anti‑patterns** – no evidence of “single point of failure,” “unbounded authority,” “opaque logic,” “insufficient monitoring,” or any other listed anti‑pattern.
+**Step 2 – Evidence checklist** (required for a “sound” verdict)  
+Only if no anti‑patterns are found, verify all of the following:
 
-**How to respond:**
-- Begin with the chosen decision word (`sound`, `needs-more-evidence`, or `rejected`).
-- Follow with a concise justification (1‑2 sentences) that references the most important checklist items influencing your decision.
+1. Real‑world testing in a representative environment with reliable autonomous results.  
+2. Failure‑mode analysis that identifies plausible failures, impacts, and mitigations.  
+3. Tamper‑evident audit log capable of reconstructing each autonomous decision.  
+4. Human‑decision benchmark showing the agent is at least as safe/effective as a qualified operator.  
+5. Residual risk after mitigation is within the thresholds defined in Section 8.
 
-Example format:
+- If **all five** are fully satisfied → verdict **sound**.  
+- If one or more are missing or insufficient → verdict **needs-more-evidence**.
+
+**Output (exactly this structure, no extra text):**
+
+1. First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+2. One blank line.  
+3. One or more sentences explaining the decision, naming any anti‑pattern found or any checklist items that were lacking or insufficient.
+
+Example:
 ```
 sound
-Testing in a production‑like testbed showed 99.8% success, and an audit trail records every autonomous decision, satisfying all checklist criteria.
-```
-Provide your verdict and reasoning based solely on the evidence presented.+
+Testing in a production‑like testbed achieved 99.8 % success, an audit trail records every decision, and all failure‑mode mitigations meet Section 8 risk thresholds.
+```
```

## Migration

- island 0 -> island 1: cell (0, 5), scalar 0.7405, claimed=True
- island 1 -> island 2: cell (1, 5), scalar 0.7490, claimed=True
- island 2 -> island 3: cell (0, 5), scalar 0.8616, claimed=True
- island 3 -> island 0: cell (0, 5), scalar 0.8485, claimed=True

## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 15 | 15 | 15 | 0.5581 | 33.3% | 2260 |
| `proposer-distilled@/adapters/20261017` | 16 | 16 | 16 | 0.5525 | 18.8% | 2228 |

Paired difference, distilled minus stock, over 15 complete pairs: mean -0.0056 (sd 0.1575, se 0.0407), **-0.14 sigma**, p 0.892; distilled ahead in 7, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 96 | 93 | 93 | 0.4532 | 48.4% | 2112 |
| `proposer-distilled@/adapters/20261017` | 96 | 94 | 94 | 0.4591 | 43.6% | 2077 |

Paired difference, distilled minus stock, over 90 complete pairs: mean +0.0081 (sd 0.1858, se 0.0196), **+0.41 sigma**, p 0.681; distilled ahead in 47, tied in 0.

## Proposal diversity (mean pairwise TF-IDF cosine distance)

| Generation | Stock | Distilled | Distilled / stock |
|---|---|---|---|
| 0 | 0.505 | 0.507 | 1.00 |
| 1 | 0.539 | 0.557 | 1.03 |
| 2 | 0.586 | 0.608 | 1.04 |
| 3 | 0.561 | 0.589 | 1.05 |
| 4 | 0.598 | 0.617 | 1.03 |
| 5 | 0.568 | 0.591 | 1.04 |

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
