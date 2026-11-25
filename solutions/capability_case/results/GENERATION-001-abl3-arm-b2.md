# Generation 1 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 69.9%
- Aggregate throughput: 105.6 tok/s (216021 completion tokens / 2045.8s)

## Archive

- Island 0: coverage 13.9%, QD score 2.620, unique ancestors 2
- Island 1: coverage 11.1%, QD score 2.009, unique ancestors 2
- Island 2: coverage 11.1%, QD score 1.784, unique ancestors 3
- Island 3: coverage 11.1%, QD score 2.687, unique ancestors 3
- Cells newly claimed this generation: 13

## Quality

- Best scalar this generation: 0.7517
- Median scalar of newly-claimed: 0.5099

## Cost

- Budget: {'generation': 1, 'max_generations': 30, 'tokens_used_total': 1268503, 'max_tokens': 3000000, 'elapsed_s_total': 4098.8, 'generation_wall_s': 2045.8}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 3), scalar 0.7517

parent `be7b0923dff22971` -> candidate `526e93f2fd288e5b`

```diff
--- parent be7b0923dff22971
+++ candidate 526e93f2fd288e5b
@@ -1,25 +1,31 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change action. Read the submission and produce a single judgment using one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are reviewing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and output **exactly** one of the three labels below, followed by a brief justification (1‑3 sentences).
 
 **Labels**
-- **sound** – the case supplies convincing, concrete evidence that the change can be safely automated.
-- **needs-more-evidence** – the case is plausible but lacks one or more critical pieces of information.
-- **rejected** – the case contains a fundamental flaw or a clear violation of the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+- **sound** – the case provides complete, concrete evidence that the automated action is safe and meets all mandatory requirements.
+- **needs‑more‑evidence** – the case is mostly convincing but one or more non‑critical requirements are insufficiently addressed.
+- **rejected** – the case contains a disqualifying flaw, an anti‑pattern from Section 9, or is missing any *critical* evidence element.
 
-**Decision criteria (derived from Section 8, Strategy C and Section 9)**  
-1. **Real‑world testing** – has the team conducted realistic pilots or simulations that demonstrate correct behavior under normal and edge‑case conditions?  
-2. **Risk & failure‑mode analysis** – is there a documented assessment of possible failures, their likelihood, and mitigation strategies?  
-3. **Audit trail** – does the proposal include an immutable log or other mechanism that can reconstruct the agent’s decisions after the fact?  
-4. **Human‑equivalence comparison** – are the agent’s decisions benchmarked against expert human judgments, with quantitative or qualitative results?  
-5. **Anti‑pattern compliance** – does the proposal avoid prohibited patterns such as “single point of failure without fallback”, “unbounded escalation of authority”, or “absence of manual override”?
+**Mandatory evidence (must be present; their total absence forces a **rejected** verdict)**
+1. **Real‑world testing** – documented pilots or high‑fidelity simulations showing correct behavior under normal and edge‑case conditions, with success/failure metrics.  
+2. **Failure‑mode analysis** – a systematic assessment of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
+3. **Auditability** – an immutable log or provenance mechanism that records every automated decision and can be inspected after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against qualified human operators.
 
-**Rule for picking a label**
-- If **all** criteria are met (or any missing item is demonstrably insignificant), label **sound**.  
-- If one or more criteria are insufficiently addressed but no show‑stopper is present, label **needs-more-evidence**.  
-- If any anti‑pattern is present or a critical safety/security gap exists, label **rejected**.
+**Anti‑pattern check (any presence → **rejected**)**
+- Single point of failure without redundancy.  
+- Unbounded escalation of authority.  
+- Absence of a manual override or rollback (“we will govern it later”).  
+- Use of undocumented/proprietary data sources.  
+- Claims of “zero‑risk” without quantitative support.  
 
-**Output format (do not change):**
+**Decision logic**
+- **Reject** if any anti‑pattern is detected **or** if any mandatory evidence item (1‑4) is completely missing.  
+- **Needs‑more‑evidence** if all mandatory items are present but one or more are only partially addressed (e.g., missing metrics, incomplete mitigation details) and no anti‑pattern exists.  
+- **Sound** if every mandatory item is fully satisfied (or any minor omission is demonstrably insignificant) and no anti‑pattern is found.
+
+**Output format (must be followed exactly):**
 ```
 <label>
 <reasoning>
 ```
-Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line.+Replace `<label>` with `sound`, `needs‑more‑evidence`, or `rejected`. Provide the reasoning on the next line (1‑3 sentences). 
```

### Island 0, cell (1, 2), scalar 0.3625

parent `be7b0923dff22971` -> candidate `0969dff43295388e`

```diff
--- parent be7b0923dff22971
+++ candidate 0969dff43295388e
@@ -1,25 +1,34 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change action. Read the submission and produce a single judgment using one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are reviewing a capability case that asks to waive per‑action human approval for an industrial operational‑change gateway action. Read the supplied evidence and output a single verdict followed by a brief justification (1‑3 sentences).
 
-**Labels**
-- **sound** – the case supplies convincing, concrete evidence that the change can be safely automated.
-- **needs-more-evidence** – the case is plausible but lacks one or more critical pieces of information.
-- **rejected** – the case contains a fundamental flaw or a clear violation of the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Verdict options**
+- **sound** – all required evidence is present, convincing, and no anti‑pattern is detected.  
+- **needs-more-evidence** – the case is plausible but one or more required pieces of evidence are insufficiently addressed, yet no disqualifying anti‑pattern exists.  
+- **rejected** – a mandatory evidence element is completely missing **or** any anti‑pattern from Section 9 is present.
 
-**Decision criteria (derived from Section 8, Strategy C and Section 9)**  
-1. **Real‑world testing** – has the team conducted realistic pilots or simulations that demonstrate correct behavior under normal and edge‑case conditions?  
-2. **Risk & failure‑mode analysis** – is there a documented assessment of possible failures, their likelihood, and mitigation strategies?  
-3. **Audit trail** – does the proposal include an immutable log or other mechanism that can reconstruct the agent’s decisions after the fact?  
-4. **Human‑equivalence comparison** – are the agent’s decisions benchmarked against expert human judgments, with quantitative or qualitative results?  
-5. **Anti‑pattern compliance** – does the proposal avoid prohibited patterns such as “single point of failure without fallback”, “unbounded escalation of authority”, or “absence of manual override”?
+**Mandatory evidence checklist**  
+1. **Real‑world testing** – documented pilot or high‑fidelity simulation with success/failure metrics.  
+2. **Failure‑mode analysis** – systematic identification of possible failures, their likelihood, and concrete mitigation or rollback steps.  
+3. **Auditability** – immutable log or provenance record that captures every automated decision and can be inspected after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against qualified human operators.  
+5. **Governance & fallback** – explicit definition of who can intervene, how a manual override or safe‑state entry is performed, and a clear rollback procedure.  
 
-**Rule for picking a label**
-- If **all** criteria are met (or any missing item is demonstrably insignificant), label **sound**.  
-- If one or more criteria are insufficiently addressed but no show‑stopper is present, label **needs-more-evidence**.  
-- If any anti‑pattern is present or a critical safety/security gap exists, label **rejected**.
+**Anti‑pattern check (Section 9)** – reject immediately if any of the following appear:
+- “single point of failure without redundancy”  
+- “unbounded escalation of authority”  
+- “absence of manual override or rollback”  
+- “we will govern it later” or any statement that governance is postponed  
+- “zero‑risk” claim without quantitative evidence  
+- Use of undocumented or proprietary data sources  
 
-**Output format (do not change):**
+**Decision process**
+- If any checklist item **is completely absent** (no test results, no failure analysis, no audit log, no human comparison, or no governance), **reject**.  
+- If any anti‑pattern is found, **reject**.  
+- If all items are present but one or more are only partially addressed (e.g., missing metrics, vague mitigation), **needs‑more‑evidence**.  
+- If every item is fully satisfied and no anti‑pattern is present, **sound**.
+
+**Output format (must be followed exactly)**
 ```
-<label>
+<verdict>
 <reasoning>
 ```
-Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line.+Replace `<verdict>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line. Do not add any other text.
```

### Island 0, cell (1, 5), scalar 0.5099

parent `be7b0923dff22971` -> candidate `2986e18e574372fe`

```diff
--- parent be7b0923dff22971
+++ candidate 2986e18e574372fe
@@ -1,25 +1,33 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change action. Read the submission and produce a single judgment using one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and produce a single judgment using one of the three labels below, followed by a brief justification (1‑3 sentences).
 
 **Labels**
 - **sound** – the case supplies convincing, concrete evidence that the change can be safely automated.
-- **needs-more-evidence** – the case is plausible but lacks one or more critical pieces of information.
-- **rejected** – the case contains a fundamental flaw or a clear violation of the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+- **needs-more-evidence** – the case is plausible but leaves one or more non‑critical gaps.
+- **rejected** – the case contains a fundamental flaw, an anti‑pattern from Section 9, or is missing any *critical* evidence required for a safe decision.
 
-**Decision criteria (derived from Section 8, Strategy C and Section 9)**  
-1. **Real‑world testing** – has the team conducted realistic pilots or simulations that demonstrate correct behavior under normal and edge‑case conditions?  
-2. **Risk & failure‑mode analysis** – is there a documented assessment of possible failures, their likelihood, and mitigation strategies?  
-3. **Audit trail** – does the proposal include an immutable log or other mechanism that can reconstruct the agent’s decisions after the fact?  
-4. **Human‑equivalence comparison** – are the agent’s decisions benchmarked against expert human judgments, with quantitative or qualitative results?  
-5. **Anti‑pattern compliance** – does the proposal avoid prohibited patterns such as “single point of failure without fallback”, “unbounded escalation of authority”, or “absence of manual override”?
+**Critical evidence (must be present for any positive verdict)**
+1. **Real‑world testing** – documented pilots or high‑fidelity simulations with success/failure metrics covering normal and edge‑case conditions.  
+2. **Failure‑mode analysis** – systematic identification of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
+3. **Audit trail** – an immutable log or provenance mechanism that records every automated decision and can be reviewed after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against expert human performance.  
 
-**Rule for picking a label**
-- If **all** criteria are met (or any missing item is demonstrably insignificant), label **sound**.  
-- If one or more criteria are insufficiently addressed but no show‑stopper is present, label **needs-more-evidence**.  
-- If any anti‑pattern is present or a critical safety/security gap exists, label **rejected**.
+**Anti‑pattern check (any presence forces **rejected**)**
+- Single point of failure without redundant fallback.  
+- Unbounded escalation of authority.  
+- Absence of manual override or emergency stop.  
+- Governance “to be defined later” or any statement that oversight will be added after deployment.  
+- Claims of “zero‑risk” without quantitative justification.  
+- Use of undocumented or proprietary data sources.
 
-**Output format (do not change):**
+**Decision workflow**
+1. Scan for any anti‑pattern listed above. If found → **rejected**.  
+2. Verify that all four critical evidence items are present. If any are completely missing → **rejected**.  
+3. If all critical evidence is present and no anti‑patterns are found → **sound**.  
+4. If the case passes steps 1‑3 but some non‑critical details are weak or incomplete (e.g., limited test coverage, partial audit detail) → **needs-more-evidence**.
+
+**Output format (must be followed exactly):**
 ```
 <label>
 <reasoning>
 ```
-Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line.+Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line.  
```

### Island 0, cell (0, 5), scalar 0.3504

parent `be7b0923dff22971` -> candidate `ae2f1586c4fcf94f`

```diff
--- parent be7b0923dff22971
+++ candidate ae2f1586c4fcf94f
@@ -1,25 +1,34 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change action. Read the submission and produce a single judgment using one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are reviewing a capability case that proposes waiving per‑action human approval for an industrial operational‑change gateway action. Read the submission and output a single judgment using one of the three labels below, followed by a brief justification (1‑3 sentences).
 
 **Labels**
-- **sound** – the case supplies convincing, concrete evidence that the change can be safely automated.
-- **needs-more-evidence** – the case is plausible but lacks one or more critical pieces of information.
-- **rejected** – the case contains a fundamental flaw or a clear violation of the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+- **sound** – the case supplies complete, convincing evidence that the change can be safely automated.
+- **needs-more-evidence** – the case is largely complete but one or more evidence items are only partially addressed or lack sufficient detail.
+- **rejected** – the case contains a disqualifying anti‑pattern or is missing an entire required evidence category.
 
-**Decision criteria (derived from Section 8, Strategy C and Section 9)**  
-1. **Real‑world testing** – has the team conducted realistic pilots or simulations that demonstrate correct behavior under normal and edge‑case conditions?  
-2. **Risk & failure‑mode analysis** – is there a documented assessment of possible failures, their likelihood, and mitigation strategies?  
-3. **Audit trail** – does the proposal include an immutable log or other mechanism that can reconstruct the agent’s decisions after the fact?  
-4. **Human‑equivalence comparison** – are the agent’s decisions benchmarked against expert human judgments, with quantitative or qualitative results?  
-5. **Anti‑pattern compliance** – does the proposal avoid prohibited patterns such as “single point of failure without fallback”, “unbounded escalation of authority”, or “absence of manual override”?
+**Required evidence categories (all must be present)**
+1. **Real‑world testing** – documented pilots or high‑fidelity simulations showing correct behavior in normal and edge‑case conditions, with success/failure metrics.  
+2. **Failure‑mode analysis** – systematic assessment of possible failures, their likelihood, and explicit mitigation or rollback procedures.  
+3. **Auditability** – an immutable log or provenance mechanism that records every automated decision and can be reviewed by a human after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against expert human judgments.  
+5. **Governance & compliance** – explicit governance process for the relaxation and confirmation that the proposal complies with Section 8 (Strategy C) and does **not** exhibit any anti‑pattern from Section 9.
 
-**Rule for picking a label**
-- If **all** criteria are met (or any missing item is demonstrably insignificant), label **sound**.  
-- If one or more criteria are insufficiently addressed but no show‑stopper is present, label **needs-more-evidence**.  
-- If any anti‑pattern is present or a critical safety/security gap exists, label **rejected**.
+**Anti‑patterns that force a “rejected” verdict (any occurrence triggers rejection)**
+- Single point of failure without fallback.  
+- Unbounded escalation of authority.  
+- Absence of manual override or emergency stop.  
+- Use of undocumented or proprietary data sources.  
+- Claims of “zero‑risk” without quantitative justification.  
+- “We will govern it later” – governance omitted or postponed.  
 
-**Output format (do not change):**
+**Decision workflow**
+1. Scan for any anti‑pattern. If found, label **rejected**.  
+2. Verify that each of the five evidence categories is present. If any entire category is missing, label **rejected**.  
+3. If all categories are present but one or more are only partially addressed or lack sufficient detail, label **needs-more-evidence**.  
+4. If all categories are fully satisfied and no anti‑patterns are detected, label **sound**.
+
+**Output format (must be followed exactly):**
 ```
 <label>
 <reasoning>
 ```
-Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line.+Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line. 
```

### Island 1, cell (0, 5), scalar 0.4856

parent `b52b002d4310bbbb` -> candidate `08b6e62d51558cfe`

```diff
--- parent b52b002d4310bbbb
+++ candidate 08b6e62d51558cfe
@@ -1,28 +1,32 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow these steps and produce **only** the required output format (verdict and reasoning) as defined by the surrounding template.
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow the steps below and output **exactly** the required two‑line format (verdict line, then a single reasoning line).
 
-**Evaluation steps**
+**Decision hierarchy**
 
-1. **Evidence of Real‑World Testing** – Check whether the submission includes concrete test results (e.g., pilot runs, simulations, field trials) that demonstrate the system works reliably under realistic conditions.
+1. **Anti‑pattern check (must‑reject)** – Scan the submission for any of the disqualifying anti‑patterns listed in Section 9 (e.g., missing manual override, opaque “black‑box‑only” logic, unbounded authority, lack of rollback, regulatory‑critical actions without safeguards, “we will govern it later”, or any statement that governance is undefined).  
+   *If any anti‑pattern is present, the verdict is **rejected** and you stop.*
 
-2. **Risk‑Analysis** – Look for a documented analysis of potential failure modes, including worst‑case scenarios, impact assessments, and mitigation strategies.
+2. **Mandatory evidence categories** – The following five categories are required for a **sound** decision. Each must contain **concrete, verifiable evidence** (e.g., data, artifacts, documented procedures).  
+   - **Real‑world testing** – pilot runs, staged roll‑outs, or realistic simulations with measurable results.  
+   - **Risk & failure‑mode analysis** – exhaustive list of failure modes, likelihoods, impact assessments, and mitigation or safe‑state fallback procedures.  
+   - **Audit‑trail / observability** – immutable logs, provenance metadata, and a defined retention/inspection process.  
+   - **Human‑decision benchmarking** – quantitative comparison of the automated decisions to qualified human decisions, with error‑rate or agreement metrics.  
+   - **Governance & monitoring** – explicit governance model (who can enable/disable, rollback procedures), continuous monitoring metrics, and a process for updating or reverting the capability.
 
-3. **Auditability** – Verify that the proposal describes an immutable audit trail (e.g., logs, provenance metadata) that can be reviewed after each automated decision.
+   *If **any** of these categories is **completely absent**, the verdict is **rejected**.*
 
-4. **Human‑Decision Benchmarking** – Confirm that the team has compared the automated agent’s decisions against a representative set of human decisions and quantified the agreement or error rates.
+   *If all categories are present but one or more are only **partially** addressed (e.g., missing quantitative results, vague mitigation, or incomplete logging), the verdict is **needs‑more‑evidence**.*
 
-5. **Compliance with Anti‑Patterns (Section 9)** – Ensure the case does **not** contain any of the listed anti‑patterns (e.g., “black‑box only”, “no rollback”, “unbounded authority”, “absence of monitoring”).
+3. **Sound verdict** – Only when **all five mandatory categories are fully satisfied** and **no anti‑patterns** were found, the verdict is **sound**.
 
-**Verdict criteria**
-
-- **sound** – All five categories above are satisfied with concrete, verifiable evidence; no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more categories are partially addressed or missing, but no fatal anti‑pattern is found.
-- **rejected** – A serious anti‑pattern is present, or the evidence is fundamentally inadequate (e.g., no testing, no audit trail, or the risk analysis shows unacceptable danger).
-
-**Output format**
+**Output format (must be followed exactly)**
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the relevant criteria>
+Reasoning: <concise explanation referencing the specific criteria or anti‑pattern that determined the verdict>
 ```
 
-Provide the verdict on the first line and a brief, focussed reasoning on the second line. Do not add any additional commentary or sections.+- The first line must start with `Verdict:` followed by the lowercase verdict word.  
+- The second line must start with `Reasoning:` and contain a single sentence that cites the relevant checklist item(s) (e.g., “Missing real‑world testing” or “Anti‑pattern: no manual override”).  
+- No extra lines, bullet points, or commentary are allowed.
+
+Proceed to read the submission, apply the hierarchy above, and produce the two‑line output.
```

### Island 1, cell (0, 4), scalar 0.3501

parent `b52b002d4310bbbb` -> candidate `6fa39be94b0c72cd`

```diff
--- parent b52b002d4310bbbb
+++ candidate 6fa39be94b0c72cd
@@ -1,28 +1,42 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow these steps and produce **only** the required output format (verdict and reasoning) as defined by the surrounding template.
+You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow the decision process below **exactly** and produce **only** the two‑line output (verdict line then reasoning line) required by the surrounding template.
 
-**Evaluation steps**
+### Decision process
 
-1. **Evidence of Real‑World Testing** – Check whether the submission includes concrete test results (e.g., pilot runs, simulations, field trials) that demonstrate the system works reliably under realistic conditions.
+1. **Anti‑pattern screen (Section 9) – immediate reject**  
+   Scan the submission for any of the following disqualifying anti‑patterns. If **any** is found, the verdict is **rejected** and you must cite the specific anti‑pattern(s) in the reasoning.  
+   - No manual override / safe‑state fallback.  
+   - “Black‑box only” – no explainability or traceability.  
+   - Unbounded authority or recursion that can amplify errors.  
+   - Absence of monitoring or audit capability (including the “we will govern it later” pattern).  
+   - Proposal to remove approval for actions that are regulatory or safety‑critical.  
+   - Any other anti‑pattern listed in Section 9.
 
-2. **Risk‑Analysis** – Look for a documented analysis of potential failure modes, including worst‑case scenarios, impact assessments, and mitigation strategies.
+2. **Evidence checklist (Section 8) – determine completeness**  
+   For each of the five evidence items, the submission must contain **concrete, verifiable** information (e.g., data, diagrams, documented processes).  
+   1. **Real‑world testing** – pilot runs, staged roll‑outs, or simulations with results showing correct behavior under realistic load and failure conditions.  
+   2. **Risk & failure‑mode analysis** – explicit enumeration of failure modes, impact assessment, and defined mitigation or fallback procedures.  
+   3. **Audit‑trail / observability** – immutable logs, provenance metadata, and a retention policy that enables post‑hoc review.  
+   4. **Human‑decision benchmarking** – quantitative comparison of the automated decisions to those of qualified humans, with error‑rate or agreement metrics.  
+   5. **Capability bounds (Section 8 criteria)** – evidence that the automation is bounded, reversible, and can be disabled quickly; includes governance / override processes.
 
-3. **Auditability** – Verify that the proposal describes an immutable audit trail (e.g., logs, provenance metadata) that can be reviewed after each automated decision.
+   *If any item is **completely absent** (no evidence at all), the verdict is **rejected**.*  
+   *If all items are present and meet the concrete‑evidence standard, the verdict is **sound**.*  
+   *If the submission contains evidence for the items but one or more are only partially addressed (e.g., vague description, missing data), the verdict is **needs‑more‑evidence**.*
 
-4. **Human‑Decision Benchmarking** – Confirm that the team has compared the automated agent’s decisions against a representative set of human decisions and quantified the agreement or error rates.
+3. **Combine results**  
+   - **Rejected**: any anti‑pattern found **or** any evidence item completely missing.  
+   - **Sound**: no anti‑patterns and all five evidence items fully satisfied.  
+   - **Needs‑more‑evidence**: no anti‑patterns, no completely missing evidence, but at least one item only partially satisfied.
 
-5. **Compliance with Anti‑Patterns (Section 9)** – Ensure the case does **not** contain any of the listed anti‑patterns (e.g., “black‑box only”, “no rollback”, “unbounded authority”, “absence of monitoring”).
-
-**Verdict criteria**
-
-- **sound** – All five categories above are satisfied with concrete, verifiable evidence; no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more categories are partially addressed or missing, but no fatal anti‑pattern is found.
-- **rejected** – A serious anti‑pattern is present, or the evidence is fundamentally inadequate (e.g., no testing, no audit trail, or the risk analysis shows unacceptable danger).
-
-**Output format**
+### Output format (must be followed exactly)
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the relevant criteria>
+Reasoning: <concise explanation that cites the relevant checklist items or anti‑patterns>
 ```
 
-Provide the verdict on the first line and a brief, focussed reasoning on the second line. Do not add any additional commentary or sections.+- Place the verdict on the first line, using the exact lowercase word.
+- Provide a single sentence on the second line that references the specific criteria that drove the decision (e.g., “Missing real‑world test results and presence of a black‑box only anti‑pattern”).  
+- Do **not** add any additional lines, bullet points, or commentary.
+
+Proceed with the evaluation now.
```

### Island 1, cell (0, 5), scalar 0.5622

parent `b52b002d4310bbbb` -> candidate `b1a218624fff768d`

```diff
--- parent b52b002d4310bbbb
+++ candidate b1a218624fff768d
@@ -1,28 +1,33 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow these steps and produce **only** the required output format (verdict and reasoning) as defined by the surrounding template.
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow the checklist below and then output **exactly** the required two‑line format (verdict line, reasoning line). Do not add any extra text.
 
-**Evaluation steps**
+**Checklist (all items must be considered)**  
 
-1. **Evidence of Real‑World Testing** – Check whether the submission includes concrete test results (e.g., pilot runs, simulations, field trials) that demonstrate the system works reliably under realistic conditions.
+1. **Real‑world testing** – Does the submission contain concrete test results (pilot, sandbox, staged rollout, or field trial) that show the system works reliably under realistic load and failure conditions?  
+2. **Risk & failure‑mode analysis** – Is there a documented analysis of possible failure modes, their impact, and mitigation or safe‑state fallback procedures?  
+3. **Auditability / observability** – Are immutable logs, provenance metadata, or other audit trails described that allow post‑hoc review of every automated decision?  
+4. **Human‑decision benchmarking** – Does the team compare the automated decisions to a representative set of human decisions and provide quantitative agreement or error‑rate evidence?  
+5. **Governance & boundedness (Section 8)** – Is the capability bounded, reversible, and quickly disable‑able? Does it stay within the organization’s risk tolerance?  
 
-2. **Risk‑Analysis** – Look for a documented analysis of potential failure modes, including worst‑case scenarios, impact assessments, and mitigation strategies.
+**Anti‑patterns (Section 9) – any single occurrence forces **REJECTED** regardless of other evidence**  
 
-3. **Auditability** – Verify that the proposal describes an immutable audit trail (e.g., logs, provenance metadata) that can be reviewed after each automated decision.
+- No manual override or safe‑state fallback.  
+- Opaque “black‑box only” decision logic with no explainability.  
+- Unbounded authority or runaway automation.  
+- Lack of rollback / irreversible actions.  
+- Removal of approval for regulatory‑ or safety‑critical actions.  
+- “We will govern it later” – governance not defined up front.
 
-4. **Human‑Decision Benchmarking** – Confirm that the team has compared the automated agent’s decisions against a representative set of human decisions and quantified the agreement or error rates.
+**Verdict determination**
 
-5. **Compliance with Anti‑Patterns (Section 9)** – Ensure the case does **not** contain any of the listed anti‑patterns (e.g., “black‑box only”, “no rollback”, “unbounded authority”, “absence of monitoring”).
+- **sound** – All five checklist items are fully satisfied with concrete, verifiable evidence **and** no anti‑patterns are present.  
+- **needs-more-evidence** – No anti‑patterns are found, but one or more checklist items are only partially addressed or missing *non‑critical* evidence (e.g., missing detailed benchmark numbers but a qualitative comparison exists).  
+- **rejected** – Any anti‑pattern is present **or** any *critical* checklist item (testing, risk analysis, or auditability) is completely absent.
 
-**Verdict criteria**
-
-- **sound** – All five categories above are satisfied with concrete, verifiable evidence; no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more categories are partially addressed or missing, but no fatal anti‑pattern is found.
-- **rejected** – A serious anti‑pattern is present, or the evidence is fundamentally inadequate (e.g., no testing, no audit trail, or the risk analysis shows unacceptable danger).
-
-**Output format**
+**Output format (must be exactly as shown)**  
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the relevant criteria>
+Reasoning: <concise explanation referencing the relevant checklist items or anti‑pattern(s)>
 ```
 
-Provide the verdict on the first line and a brief, focussed reasoning on the second line. Do not add any additional commentary or sections.+Place the verdict on the first line and a brief, single‑sentence reasoning on the second line. No additional lines, bullets, or commentary are allowed.
```

### Island 1, cell (0, 4), scalar 0.3581

parent `b52b002d4310bbbb` -> candidate `b24f10ec6f13e27e`

```diff
--- parent b52b002d4310bbbb
+++ candidate b24f10ec6f13e27e
@@ -1,28 +1,38 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow these steps and produce **only** the required output format (verdict and reasoning) as defined by the surrounding template.
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow the hierarchy below and output **only** the required two‑line format (verdict and reasoning) as defined by the surrounding template.
 
-**Evaluation steps**
+**Decision hierarchy**
 
-1. **Evidence of Real‑World Testing** – Check whether the submission includes concrete test results (e.g., pilot runs, simulations, field trials) that demonstrate the system works reliably under realistic conditions.
+1. **Anti‑pattern check (immediate REJECT)** – Scan the submission for any of the following disqualifying items (including any wording that matches these concepts):
+   - Absence of a manual override or safe‑state fallback.  
+   - Opaque/black‑box decision logic with no explainability or auditability.  
+   - “We will govern it later”, “governance to be defined later”, or any lack of upfront governance for the relaxation.  
+   - Unbounded authority, runaway automation, hidden privilege escalation, or lack of rollback.  
+   - Proposal to eliminate approval for actions that are safety‑critical or regulatory‑controlled.  
+   If any anti‑pattern is present, output **rejected** and cite the specific anti‑pattern(s). No further checks are performed.
 
-2. **Risk‑Analysis** – Look for a documented analysis of potential failure modes, including worst‑case scenarios, impact assessments, and mitigation strategies.
+2. **Evidence categories** – For each of the five required evidence dimensions, determine whether the submission:
+   - **Provides concrete, verifiable evidence** (e.g., data, logs, test reports). → consider the category *satisfied*.
+   - **Contains some discussion but lacks sufficient detail or proof** → consider the category *partial*.
+   - **Mentions nothing at all** → consider the category *absent*.
 
-3. **Auditability** – Verify that the proposal describes an immutable audit trail (e.g., logs, provenance metadata) that can be reviewed after each automated decision.
+   The five dimensions are:
+   1. **Real‑world testing** – pilot runs, simulations, staged roll‑outs, and results showing reliable behavior under realistic load and failure conditions.
+   2. **Risk & failure‑mode analysis** – enumeration of plausible failures, impact assessments, and concrete mitigation or fallback strategies.
+   3. **Auditability / observability** – immutable logs, provenance metadata, and a defined process for post‑hoc review.
+   4. **Human‑decision benchmarking** – quantitative or qualitative comparison of the automated decisions to qualified human decisions, with error‑rate thresholds demonstrated.
+   5. **Governance & boundedness (Section 8 criteria)** – explicit statement of how the capability is bounded, reversible, and can be disabled quickly; governance model defined up front.
 
-4. **Human‑Decision Benchmarking** – Confirm that the team has compared the automated agent’s decisions against a representative set of human decisions and quantified the agreement or error rates.
+3. **Verdict determination**
+   - **sound** – All five dimensions are *satisfied* (no partial or absent items) and no anti‑pattern was found.
+   - **rejected** – Any dimension is *absent* (no mention at all) **or** an anti‑pattern was detected in step 1.
+   - **needs‑more‑evidence** – At least one dimension is *partial* (some evidence but not fully convincing) and none are *absent*; also no anti‑pattern is present.
 
-5. **Compliance with Anti‑Patterns (Section 9)** – Ensure the case does **not** contain any of the listed anti‑patterns (e.g., “black‑box only”, “no rollback”, “unbounded authority”, “absence of monitoring”).
-
-**Verdict criteria**
-
-- **sound** – All five categories above are satisfied with concrete, verifiable evidence; no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more categories are partially addressed or missing, but no fatal anti‑pattern is found.
-- **rejected** – A serious anti‑pattern is present, or the evidence is fundamentally inadequate (e.g., no testing, no audit trail, or the risk analysis shows unacceptable danger).
-
-**Output format**
+**Output format (exactly two lines)**
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the relevant criteria>
+Reasoning: <concise explanation referencing the relevant categories or anti‑patterns>
 ```
 
-Provide the verdict on the first line and a brief, focussed reasoning on the second line. Do not add any additional commentary or sections.+- Place the verdict on the first line, using the exact lowercase words shown.
+- On the second line give a brief, single‑sentence rationale that cites the key category (or anti‑pattern) that drove the decision. Do not add any extra commentary, bullet points, or sections.
```

### Island 2, cell (1, 5), scalar 0.6354

parent `38c87c0b57ae33e9` -> candidate `ec0af192a0af70d0`

```diff
--- parent 38c87c0b57ae33e9
+++ candidate ec0af192a0af70d0
@@ -1,31 +1,34 @@
-You are tasked with evaluating a capability case that proposes to relax or remove per‑action human approval for an industrial operational‑change gateway action.  
+You are evaluating a capability case that proposes to relax or remove per‑action human approval for an industrial operational‑change gateway action.
 
-**Goal:** Decide whether the case is **Sound**, **Needs‑More‑Evidence**, or **Rejected** according to the criteria in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑Boundary‑as‑Architecture whitepaper.
+**Goal:** Classify the case as **Sound**, **Needs‑More‑Evidence**, or **Rejected** using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑Boundary‑as‑Architecture whitepaper.
 
-**Evaluation checklist (must consider all items):**
+**Mandatory evidence dimensions** (all must be addressed to avoid automatic rejection):
+1. **Real‑world testing** – realistic, end‑to‑end tests in a production‑like environment; include scope, frequency, and reproducibility.
+2. **Failure‑mode analysis** – identification, likelihood, impact, and mitigation of safety, reliability, and security failures.
+3. **Auditability & traceability** – tamper‑evident audit log recording decision source, timestamps, and justification.
+4. **Human‑baseline comparison** – quantitative benchmark showing the autonomous decision‑making matches or exceeds qualified human performance.
 
-1. **Empirical testing** – Has the team performed realistic, end‑to‑end tests in a production‑like environment? Include details on test scope, frequency, and reproducibility.  
-2. **Failure‑mode analysis** – Are potential adverse outcomes identified, quantified, and mitigated (e.g., safety incidents, cascading faults, cyber‑security breaches)?  
-3. **Auditability & traceability** – Is there a robust audit trail that records who/what made each decision, timestamps, and justification data?  
-4. **Human‑baseline comparison** – Does the submission provide a systematic comparison between the autonomous agent’s decisions and those a qualified human operator would make (e.g., statistical performance metrics, error‑type breakdown)?  
-5. **Compliance with anti‑patterns (Section 9)** – Verify that none of the following disqualifying patterns are present:
-   - **Over‑reliance on a single point of failure**  
-   - **Unbounded escalation without fallback**  
-   - **Insufficient observability or logging**  
-   - **Lack of explicit rollback or safe‑stop mechanisms**  
-   - **Decision transparency gaps that prevent post‑hoc review**  
+**Anti‑pattern check (Section 9).** If any of the following is present, the case must be **Rejected**:
+- Single point of failure without redundancy.  
+- Unbounded escalation with no fallback.  
+- Insufficient observability or logging.  
+- Missing rollback or safe‑stop mechanism.  
+- Decision‑transparency gaps preventing post‑hoc review.  
+- “Govern later” posture (e.g., governance or safeguards deferred to future phases).
 
-**Decision rules**
+**Decision hierarchy**
+1. If any anti‑pattern is detected → **Rejected**.  
+2. Else, if any **mandatory evidence dimension** is completely absent → **Rejected**.  
+3. Else, if all dimensions are present but one or more contain critical gaps (e.g., limited test coverage, incomplete failure analysis, partial audit data, weak baseline comparison) → **Needs‑More‑Evidence**.  
+4. Else → **Sound**.
 
-- **Sound** – All checklist items are addressed satisfactorily, evidence is quantitative or strongly qualitative, and no anti‑patterns are detected.  
-- **Needs‑More‑Evidence** – Most items are covered but one or more critical gaps remain (e.g., missing failure‑mode analysis, incomplete audit trail, or limited testing). The case could become Sound once those gaps are filled.  
-- **Rejected** – Any anti‑pattern is present, or there is a fundamental flaw such as no testing, no fallback, or evidence of unsafe behavior that cannot be mitigated.
-
-**Output format** (must be followed exactly):
+**Output format** (must be reproduced exactly):
 
 ```
 Verdict: <Sound|Needs-More-Evidence|Rejected>
-Reasoning: <concise justification referencing the checklist items above>
+Reasoning: <concise bullet‑pointed justification referencing the checklist items above>
 ```
 
-Provide a clear, bullet‑point or short‑sentence explanation that ties your verdict to specific checklist failures or successes. Do not add any extra sections or decorative text.  +- Provide one bullet (`-`) per line in the Reasoning section.  
+- Cite only the decisive factors that led to your verdict (e.g., missing test results, specific anti‑pattern name, incomplete audit trail).  
+- Do not add any extra headings, prose, or decorative text.  
```

### Island 2, cell (0, 5), scalar 0.3502

parent `3195d910cd5067bb` -> candidate `152aebc6d6e7c3eb`

```diff
--- parent 3195d910cd5067bb
+++ candidate 152aebc6d6e7c3eb
@@ -1,20 +1,37 @@
-You will evaluate a proposal that seeks to drop per‑action human approval for an industrial operational‑change action. Follow these steps:
+You will evaluate a proposal that seeks to drop per‑action human approval for an industrial operational‑change gateway action. Follow the steps below and produce **exactly** the required output.
 
-1. **Read the entire submission carefully.**  
-2. **Assess the following criteria:**  
-   - **Empirical validation** – Has the team performed realistic tests or pilots that demonstrate the system works reliably under expected conditions?  
-   - **Risk analysis** – Are potential failure modes identified, quantified, and mitigated?  
-   - **Traceability** – Is there a verifiable audit log that records decisions, inputs, and outcomes?  
-   - **Human‑parity comparison** – Does the proposal include a systematic comparison showing the automated decisions match or exceed what a qualified human would do?  
-   - **Governance safeguards** – Are there fallback mechanisms (e.g., emergency stop, manual override) and clear escalation paths?
+### Evaluation steps
+1. **Read the entire submission.**  
+2. **Assess each of the five evidence dimensions** (all must be addressed):
+   - **Real‑world testing** – evidence of functional, integration and safety tests performed in environments that faithfully emulate production.
+   - **Failure‑mode analysis** – identification of possible failure modes, their likelihood, and concrete mitigations (e.g., safe‑stop, fallback to human control).
+   - **Auditability & traceability** – a tamper‑evident audit log that records decisions, inputs, timestamps and any operator overrides.
+   - **Human‑baseline comparison** – systematic benchmarking that shows the automated decisions are at least equivalent to those of a qualified human operator.
+   - **Governance safeguards** – clear escalation paths, emergency‑stop procedures, and rollback mechanisms.
 
-3. **Classify the proposal** based on the assessment:  
-   - **Sound** – All criteria are met with sufficient detail and evidence; no unresolved high‑impact risks remain.  
-   - **Needs‑more‑evidence** – Most criteria are addressed, but one or more areas lack concrete data, analysis, or controls, and the deficiency does not constitute an immediate safety or security danger.  
-   - **Rejected** – At least one criterion reveals a critical flaw (e.g., missing audit trail, unmitigated high‑severity risk, no testing under realistic conditions) that makes the relaxation of human approval unacceptable.
+3. **Check for anti‑patterns** from Section 9 (e.g., unbounded autonomy, lack of observability, absent rollback, over‑reliance on a single point of failure). The presence of any anti‑pattern is a **critical flaw**.
 
-4. **Output** exactly two sections:  
-   - **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`.  
-   - **Reasoning:** a concise justification referencing the specific criteria that led to your decision.
+### Decision rules
+- **Sound** – All five dimensions are satisfied with sufficient quantitative or qualitative evidence **and** no anti‑patterns are found.
+- **Needs‑more‑evidence** – All dimensions are present, but one or more lack concrete data, analysis, or controls **and** no critical anti‑pattern is present. The missing information does not create an immediate safety or security danger.
+- **Rejected** – Any of the following occurs:
+  * One or more **critical dimensions** (testing, failure‑mode analysis, auditability) are completely absent or insufficient.
+  * Any anti‑pattern from Section 9 is detected.
+  * A flaw creates an unmitigated high‑severity risk.
 
-Do not add any additional text or formatting beyond these two sections.+### Output format
+Produce **exactly** two sections, with no extra headings or prose:
+
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning:
+- <concise bullet referencing the decisive criteria or anti‑pattern>
+- <additional bullet if needed>
+```
+
+- Use a single hyphen (`-`) per bullet line.
+- Keep the reasoning focused on the factors that led to your verdict.
+- If the verdict is **needs-more-evidence**, list the missing or weak elements.
+- If the verdict is **rejected**, list the specific anti‑pattern(s) or critical missing dimension(s).
+
+Do not add any other text.
```

### Island 3, cell (0, 5), scalar 0.6110

parent `92affb1c98229566` -> candidate `44194b293b1b8880`

```diff
--- parent 92affb1c98229566
+++ candidate 44194b293b1b8880
@@ -1,28 +1,33 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to judge the case according to the criteria in **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Apply the criteria from **Section 8 (Strategy C, capability‑based opening)** and the disqualifying patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Decision procedure**
 
-1. **Evidence of real‑world testing** – Has the team conducted live or high‑fidelity simulated runs that cover normal, edge‑case, and failure scenarios?
-2. **Risk analysis** – Does the submission identify plausible failure modes, their likelihood, and potential impact, and propose mitigations?
-3. **Auditability** – Is there a verifiable, tamper‑evident audit trail for each automated decision, including timestamps, inputs, and outcomes?
-4. **Human‑decision benchmark** – Are the agent’s decisions compared against a baseline of human operator decisions, with quantitative or qualitative results showing comparable or superior performance?
-5. **Compliance with anti‑patterns (Section 9)** – Verify that the case does **not** exhibit any of the following disqualifying patterns:
-   - *Over‑reliance on black‑box models without explainability*
-   - *Absence of fallback or manual override mechanisms*
-   - *Insufficient monitoring of post‑deployment behavior*
-   - *Unclear ownership of responsibility for erroneous actions*
-   - *Lack of documented change‑control or versioning for the capability*
+1. **Anti‑pattern check (Section 9).** Scan the submission for any of the following. If even one is present, the verdict is **rejected** and you must cite the offending pattern.
+   - Opaque “black‑box” models without explainability  
+   - No manual override or emergency‑stop fallback  
+   - Lack of monitoring or post‑deployment observability  
+   - Undefined responsibility/ownership for erroneous actions  
+   - Missing or ad‑hoc change‑control/versioning  
 
-**Verdict categories**
+2. **Mandatory evidence categories (Section 8).** All four must be addressed; evaluate their depth.
+   - **Real‑world testing:** documented live or high‑fidelity simulated runs covering normal, edge‑case, and failure conditions.  
+   - **Failure‑mode / risk analysis:** identification of plausible failures, their likelihood, impact, and concrete mitigations or recovery steps.  
+   - **Auditability:** tamper‑evident log or trace that records each automated decision, inputs, timestamps, and outcomes.  
+   - **Human‑decision benchmark:** quantitative or qualitative comparison showing the automated decision equals or exceeds expert human performance.
 
-- **sound** – All checklist items are satisfied at a level that reasonably demonstrates the capability can operate safely without per‑action human approval.
-- **needs‑more‑evidence** – One or more checklist items are partially addressed or missing, but no deal‑breaking anti‑pattern is present. The case requires additional data, testing, or clarification before a sound judgment can be made.
-- **rejected** – The submission exhibits a Section 9 anti‑pattern or contains a critical gap (e.g., no audit trail, no fallback, or a high‑impact risk with no mitigation) that makes relaxing human approval unsafe.
+   *If any category is completely absent* → **rejected** (critical gap).  
+   *If a category is present but only partially documented or insufficiently detailed* → **needs‑more‑evidence**.
 
-**Response format**
+3. **Verdict assignment.**
+   - **sound** – No anti‑patterns detected and all four evidence categories are fully satisfied.  
+   - **needs‑more‑evidence** – No anti‑patterns, but at least one evidence category is only partially addressed.  
+   - **rejected** – Any anti‑pattern detected or any evidence category entirely missing.
 
-Provide:
-1. The chosen verdict term exactly as listed above.
-2. A concise justification (1‑3 sentences) referencing the specific checklist items or anti‑patterns that led to your decision.
+**Output requirements**
 
-Do not include any additional headings, lists, or extraneous text; only the verdict and the brief reasoning.+Produce exactly two lines:
+
+1. The verdict word (`sound`, `needs‑more‑evidence`, or `rejected`).  
+2. A concise justification (1‑3 short sentences) that references the specific anti‑pattern or evidence items that determined the verdict.
+
+Do not include headings, lists, or any extra text.
```

### Island 3, cell (0, 5), scalar 0.6390

parent `e9123678cb2f570d` -> candidate `cef00096f642d5c3`

```diff
--- parent e9123678cb2f570d
+++ candidate cef00096f642d5c3
@@ -1,17 +1,17 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the information supplied in the scenario, assign the case to one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor deciding whether a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action meets the standards of the ITOT‑boundary‑as‑architecture whitepaper (Section 8 Strategy C and Section 9 anti‑patterns). Using the scenario details, evaluate the case against the following checklist:
 
-Base your decision on the following checklist derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9:
+1. **Real‑world validation** – Has the team performed end‑to‑end testing in the actual target environment (including normal, edge‑case, and failure scenarios)?  
+2. **Risk & failure‑mode analysis** – Are plausible failure modes identified, with likelihood, impact, and concrete mitigations or fallback procedures documented?  
+3. **Auditability** – Is there a tamper‑evident, traceable log that records every automated decision, its inputs, timestamps, and outcomes?  
+4. **Human‑parity evidence** – Does the submission provide quantitative or qualitative comparison showing the automated decisions match or exceed those of a qualified human operator?  
+5. **Anti‑pattern compliance** – Does the proposal avoid all disqualifying patterns from Section 9 (e.g., no‑fallback, opaque black‑box logic, single‑point automation, missing governance, undocumented ownership)?
 
-1. **Empirical validation** – has the team performed realistic end‑to‑end testing in the intended environment?  
-2. **Risk and failure analysis** – are plausible failure modes identified and mitigations described?  
-3. **Auditability** – is there a verifiable log or trace that can be inspected after each automated decision?  
-4. **Human‑equivalence comparison** – does the submission provide data showing that the automated agent’s outcomes match or exceed those of a qualified human operator?  
-5. **Anti‑pattern screening** – does the proposal exhibit any of the disallowed patterns (e.g., “no‑fallback”, “opaque‑logic”, “single‑point‑automation”) described in Section 9?
+**Decision rules**
 
-- If the case satisfies **all five** items, output **sound**.  
-- If one or more items are missing or insufficiently substantiated, output **needs‑more‑evidence**.  
-- If any anti‑pattern is present or a critical safety gap is evident, output **rejected**.
+- **rejected** – If any anti‑pattern is present, **or** if any of items 1‑4 is completely missing (no evidence at all) or a critical safety gap (e.g., no audit trail, no fallback) is identified.  
+- **needs‑more‑evidence** – If all five items are present but one or more (1‑4) are only partially addressed or lack sufficient detail, and no anti‑pattern is detected.  
+- **sound** – Only when all five items are fully satisfied with robust supporting evidence and no anti‑patterns.
 
-Your response must consist of exactly two lines:
-1. The verdict word (sound, needs‑more‑evidence, or rejected).  
-2. A concise justification (one‑to‑two sentences) referencing the relevant checklist items that led to your decision.+Your response must be exactly two lines:
+1. The verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+2. A brief justification (one‑to‑two sentences) citing the specific checklist items that determined the verdict.
```

### Island 3, cell (0, 5), scalar 0.7240

parent `e9123678cb2f570d` -> candidate `07fbb7b40854648b`

```diff
--- parent e9123678cb2f570d
+++ candidate 07fbb7b40854648b
@@ -1,17 +1,25 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the information supplied in the scenario, assign the case to one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-Base your decision on the following checklist derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9:
+Base your decision on the checklist derived from Section 8 (Strategy C) and the anti‑patterns of Section 9. Treat the first four items as mandatory evidence; if any of them is completely absent, the case must be **rejected**. If all mandatory items are present but one or more are only partially substantiated, return **needs‑more‑evidence**. Only when every mandatory item is fully satisfied **and** no anti‑pattern is detected should you return **sound**.
 
-1. **Empirical validation** – has the team performed realistic end‑to‑end testing in the intended environment?  
-2. **Risk and failure analysis** – are plausible failure modes identified and mitigations described?  
-3. **Auditability** – is there a verifiable log or trace that can be inspected after each automated decision?  
-4. **Human‑equivalence comparison** – does the submission provide data showing that the automated agent’s outcomes match or exceed those of a qualified human operator?  
-5. **Anti‑pattern screening** – does the proposal exhibit any of the disallowed patterns (e.g., “no‑fallback”, “opaque‑logic”, “single‑point‑automation”) described in Section 9?
+**Mandatory evidence (must be present)**
+1. **Empirical validation** – realistic end‑to‑end testing in the intended environment, with documented results.  
+2. **Risk and failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations.  
+3. **Auditability** – a verifiable, tamper‑evident log or trace that can be inspected after each automated decision.  
+4. **Human‑equivalence comparison** – data showing the automated outcomes match or exceed those of a qualified human operator.
 
-- If the case satisfies **all five** items, output **sound**.  
-- If one or more items are missing or insufficiently substantiated, output **needs‑more‑evidence**.  
-- If any anti‑pattern is present or a critical safety gap is evident, output **rejected**.
+**Anti‑pattern screening (any presence ⇒ reject)**
+- “no‑fallback” / absence of manual override or emergency stop.  
+- “opaque‑logic” / reliance on black‑box models without explainability.  
+- “single‑point‑automation” / single point of failure with no redundancy.  
+- “we_will_govern_it_later” / governance or responsibility not defined up‑front.  
+- Any other disallowed pattern listed in Section 9.
 
-Your response must consist of exactly two lines:
-1. The verdict word (sound, needs‑more‑evidence, or rejected).  
-2. A concise justification (one‑to‑two sentences) referencing the relevant checklist items that led to your decision.+**Decision rules**
+- **sound** – all four mandatory evidence items are fully satisfied and no anti‑pattern is found.  
+- **needs‑more‑evidence** – all mandatory items are present but at least one is only partially addressed or lacks sufficient detail, and no anti‑pattern is present.  
+- **rejected** – any mandatory evidence item is completely missing **or** any anti‑pattern is detected.
+
+**Output format** – exactly two lines:
+1. The verdict word (`sound`, `needs‑more‑evidence`, or `rejected`).  
+2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that drove your decision.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.116 vs base 0.482, 9.9 sigma below
- Lesson 19: **kept** — precision 0.987 >= base 0.881
- Lesson 17: **kept** — precision 0.987 >= base 0.694
- Lesson 11: **kept** — precision 0.750 vs base 0.930, only 0.8 sigma below
