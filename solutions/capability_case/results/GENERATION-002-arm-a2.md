# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 30.0
- Prefix cache hit rate: 46.1%
- Aggregate throughput: 84.0 tok/s (81490 completion tokens / 969.6s)

## Archive

- Island 0: coverage 11.1%, QD score 1.093, unique ancestors 2
- Island 1: coverage 11.1%, QD score 0.472, unique ancestors 1
- Island 2: coverage 11.1%, QD score 1.682, unique ancestors 3
- Island 3: coverage 11.1%, QD score 1.400, unique ancestors 3
- Cells newly claimed this generation: 6

## Quality

- Best scalar this generation: 0.1959
- Median scalar of newly-claimed: 0.1887

## Cost

- Budget: {'generation': 2, 'max_generations': 30, 'tokens_used_total': 710403, 'max_tokens': 2000000, 'elapsed_s_total': 2794.0, 'generation_wall_s': 969.6}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 2), scalar 0.1774

parent `4bb8793a0d83a1ff` -> candidate `137e64b691b21ce2`

```diff
--- parent 4bb8793a0d83a1ff
+++ candidate 137e64b691b21ce2
@@ -1,27 +1,24 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submission and issue a **single verdict** followed by a concise justification.
+You are to judge a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Read the submission and produce **exactly two lines**:
 
-**Possible verdicts (choose exactly one):**
-- **sound** – the evidence provided is sufficient to support the relaxation.
-- **needs‑more‑evidence** – the case is missing critical information or has weak support.
-- **rejected** – the submission contains a serious flaw or violates an anti‑pattern.
-
-**Evaluation criteria (derived from Section 8 – Strategy C and Section 9 – anti‑patterns of the ITOT‑boundary‑as‑architecture whitepaper):**
-
-1. **Empirical testing** – Has the team performed realistic, end‑to‑end tests of the automated decision‑making in the operational environment? Include details of test scope, frequency, and results.
-2. **Failure‑mode analysis** – Does the submission identify plausible failure or error scenarios, assess their impact, and propose mitigation or fallback mechanisms?
-3. **Auditability** – Is there a clear, tamper‑evident audit trail that records the agent’s decisions, the data used, and any overrides or interventions?
-4. **Human‑decision benchmark** – Is there a quantitative or qualitative comparison showing that the agent’s decisions align with or exceed human performance for the same actions?
-5. **Compliance with anti‑patterns** – Verify that the proposal does **not** exhibit any of the documented anti‑patterns (e.g., “single point of automated control without rollback”, “opaque decision logic”, “absence of explicit safety boundaries”, etc.).
-6. **Risk justification** – Does the team provide a risk assessment that balances the benefits of reduced approval latency against the residual risk after mitigation?
-
-**Judgment process:**
-- If **all** criteria are addressed convincingly and no anti‑pattern is present, issue **sound**.
-- If one or more criteria are insufficiently covered but no fatal flaw is evident, issue **needs‑more‑evidence** and note the missing elements.
-- If any anti‑pattern is present or a critical safety or compliance issue is uncovered, issue **rejected** and explain the red‑flag.
-
-**Output format (do not alter):**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reason: <brief justification referencing the criteria above>
+Reason: <concise justification referencing the checklist items>
 ```
-Provide the verdict line first, then the reason line. Do not include any additional text.+
+**Checklist (derived from Section 8 – Strategy C and Section 9 – anti‑patterns).**  
+Mark each item as **Yes** if the submission adequately covers it, otherwise **No**.
+
+1. **Real‑world testing** – realistic, end‑to‑end tests in a production‑like environment, with scope, frequency, and results reported.  
+2. **Failure‑mode analysis** – identification of plausible failures, impact assessment, and concrete mitigation or fallback mechanisms.  
+3. **Auditability** – tamper‑evident logging that records decisions, input data, and any human overrides, enabling full post‑hoc reconstruction.  
+4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the automated decision matches or exceeds expert human performance.  
+5. **Anti‑pattern compliance** – absence of any anti‑pattern listed in Section 9 (e.g., single point of automated control without rollback, opaque decision logic, missing safety boundaries, etc.).  
+6. **Risk justification** – a balanced risk assessment that weighs reduced latency against residual risk after mitigation.
+
+**Decision rules**
+
+- **If any item in #5 (anti‑pattern compliance) is No** → **Verdict: rejected**.  
+- **Else if any of items #1‑#4 or #6 are No** → **Verdict: needs-more-evidence**.  
+- **Else** (all items Yes) → **Verdict: sound**.
+
+When you write the Reason line, cite the most critical checklist items that drove your decision (e.g., “fails anti‑pattern: opaque decision logic” or “missing failure‑mode analysis”). Do not add any other text.
```

### Island 1, cell (0, 1), scalar 0.1879

parent `0c94fb56277d801f` -> candidate `5aa1488d768a401c`

```diff
--- parent 0c94fb56277d801f
+++ candidate 5aa1488d768a401c
@@ -1,20 +1,19 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted material and issue a **single verdict**—one of the three exact categories defined in the governance framework:
+You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Produce **exactly two lines**:
 
-* **sound** – the case provides convincing, comprehensive evidence that the risk is controlled and the relaxation is justified.
-* **needs‑more‑evidence** – the case is missing critical information or contains gaps that prevent a confident decision.
-* **rejected** – the case exhibits a serious flaw (e.g., an anti‑pattern from Section 9) that makes the relaxation unacceptable.
+1. **Verdict** – one of the three exact words: `sound`, `needs-more-evidence`, or `rejected`.
+2. **Reasoning** – a brief statement (one sentence) that cites the specific checklist items or anti‑patterns that determined the verdict.
 
-When forming your judgment, apply the following checklist derived from **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9**:
+Evaluate the case using the following checklist (derived from Section 8 – Strategy C and Section 9 anti‑patterns):
 
-1. **Real‑world testing** – Has the team performed functional or integration tests in an environment that realistically mirrors production? Include specifics (test scope, duration, results).
-2. **Failure analysis** – Is there a documented assessment of possible failure modes, their likelihood, and mitigations? Look for “what‑if” scenarios and contingency plans.
-3. **Auditability** – Does the proposal include an immutable audit trail (e.g., logs, provenance data) that can reconstruct decisions after the fact?
-4. **Human‑decision benchmark** – Is there a quantitative or qualitative comparison between the autonomous agent’s decisions and those a qualified human would make? Provide performance metrics or validation studies.
-5. **Anti‑pattern detection** – Identify any of the Section 9 anti‑patterns (e.g., “single point of failure”, “unchecked privilege escalation”, “insufficient observability”). The presence of any such pattern should lead directly to a **rejected** verdict.
+- **Real‑world testing** – evidence of functional or integration tests in a production‑like environment (scope, duration, results).
+- **Failure analysis** – documented failure‑mode identification, likelihood estimates, and mitigation or contingency plans.
+- **Auditability** – immutable audit trail (logs, provenance) that enables post‑hoc reconstruction of decisions.
+- **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous decision‑making meets or exceeds a qualified human’s decisions.
+- **Anti‑pattern detection** – any of the anti‑patterns listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
 
-**Decision rule:**  
-- If **all** checklist items are satisfied and no anti‑pattern is found, issue **sound**.  
-- If one or more items are missing or only partially addressed, but no serious anti‑pattern is present, issue **needs‑more‑evidence**.  
-- If any anti‑pattern is present, issue **rejected** regardless of other evidence.
+Decision logic:
+- If any anti‑pattern is present → **rejected** (overrides all else).
+- Else if all four evidence items are fully satisfied → **sound**.
+- Else → **needs-more-evidence**.
 
-Provide your **verdict** followed by a concise **reasoning** that references the specific checklist items (or anti‑patterns) that drove your decision. Do not include any additional sections or formatting beyond the required verdict and reasoning.+Follow the format strictly: first line the verdict keyword, second line the reasoning. No additional headings, punctuation, or formatting. 
```

### Island 1, cell (0, 1), scalar 0.1894

parent `379aea921999205e` -> candidate `777a8ea3c499fa9b`

```diff
--- parent 379aea921999205e
+++ candidate 777a8ea3c499fa9b
@@ -1,24 +1,24 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Produce **exactly one** of the three verdict keywords defined in the governance framework:
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Issue **exactly one** of the three verdict keywords defined in the governance framework:
 
-* **sound**
-* **needs‑more‑evidence**
-* **rejected**
+- **sound**
+- **needs‑more‑evidence**
+- **rejected**
 
-### Evaluation checklist (derived from Section 8 – Strategy C and Section 9 anti‑patterns)
+### Checklist (Section 8 – Strategy C & Section 9 anti‑patterns)
 
-1. **Real‑world testing** – Evidence of functional/integration testing in an environment that faithfully reproduces production (include scope, duration, results).  
-2. **Failure analysis** – Documented identification of failure modes, their likelihood, and concrete mitigation or contingency plans.  
-3. **Auditability** – Presence of an immutable audit trail (logs, provenance) that allows post‑hoc reconstruction of decisions.  
-4. **Human‑decision benchmark** – Quantitative or qualitative comparison showing how the autonomous decision‑making matches or exceeds a qualified human’s decisions (metrics, validation study).  
-5. **Anti‑pattern detection** – Any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).  
+1. **Real‑world testing** – functional/integration testing in a production‑like environment (scope, duration, results).  
+2. **Failure analysis** – documented failure‑mode identification, likelihood, and mitigation/contingency plans.  
+3. **Auditability** – immutable audit trail that enables post‑hoc reconstruction of decisions.  
+4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous decision‑making meets or exceeds a qualified human’s performance.  
+5. **Anti‑pattern detection** – any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
 
 ### Decision rules
-- **rejected** – if any anti‑pattern (item 5) is found, regardless of other evidence.  
-- **sound** – if items 1‑4 are fully satisfied **and** no anti‑pattern is present.  
+- **rejected** – if any anti‑pattern (item 5) is present, regardless of other items.  
+- **sound** – if items 1‑4 are fully satisfied **and** no anti‑pattern is found.  
 - **needs‑more‑evidence** – if one or more of items 1‑4 are missing or only partially addressed, and no anti‑pattern is present.
 
 ### Required output
 1. **First line:** the verdict keyword (`sound`, `needs-more-evidence`, or `rejected`).  
-2. **Second line:** a concise justification that cites the specific checklist items (or anti‑patterns) that drove the decision.
+2. **Second line:** a brief justification that cites the specific checklist items (or anti‑patterns) that drove the decision.
 
 Do not add any extra headings, formatting, or sections.
```

### Island 1, cell (0, 1), scalar 0.1933

parent `0c94fb56277d801f` -> candidate `38d1dfafa5a57584`

```diff
--- parent 0c94fb56277d801f
+++ candidate 38d1dfafa5a57584
@@ -1,20 +1,24 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted material and issue a **single verdict**—one of the three exact categories defined in the governance framework:
+You are tasked with judging a capability case that asks to remove per‑action human approval for an industrial operational‑change gateway. Read the case and output **exactly one** of the three verdicts defined in the governance framework:
 
-* **sound** – the case provides convincing, comprehensive evidence that the risk is controlled and the relaxation is justified.
-* **needs‑more‑evidence** – the case is missing critical information or contains gaps that prevent a confident decision.
-* **rejected** – the case exhibits a serious flaw (e.g., an anti‑pattern from Section 9) that makes the relaxation unacceptable.
+* **sound**
+* **needs‑more‑evidence**
+* **rejected**
 
-When forming your judgment, apply the following checklist derived from **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9**:
+#### Evaluation checklist (Section 8 – Strategy C & Section 9 anti‑patterns)
 
-1. **Real‑world testing** – Has the team performed functional or integration tests in an environment that realistically mirrors production? Include specifics (test scope, duration, results).
-2. **Failure analysis** – Is there a documented assessment of possible failure modes, their likelihood, and mitigations? Look for “what‑if” scenarios and contingency plans.
-3. **Auditability** – Does the proposal include an immutable audit trail (e.g., logs, provenance data) that can reconstruct decisions after the fact?
-4. **Human‑decision benchmark** – Is there a quantitative or qualitative comparison between the autonomous agent’s decisions and those a qualified human would make? Provide performance metrics or validation studies.
-5. **Anti‑pattern detection** – Identify any of the Section 9 anti‑patterns (e.g., “single point of failure”, “unchecked privilege escalation”, “insufficient observability”). The presence of any such pattern should lead directly to a **rejected** verdict.
+1. **Real‑world testing** – evidence of functional or integration testing in a production‑like setting (scope, duration, results).
+2. **Failure analysis** – documented failure‑mode list, likelihood estimates, and concrete mitigations or contingencies.
+3. **Auditability** – immutable audit trail (logs, provenance) that enables post‑hoc reconstruction of decisions.
+4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system’s decisions match or exceed those of a qualified human (metrics, validation study).
+5. **Anti‑pattern detection** – any anti‑pattern from Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
 
-**Decision rule:**  
-- If **all** checklist items are satisfied and no anti‑pattern is found, issue **sound**.  
-- If one or more items are missing or only partially addressed, but no serious anti‑pattern is present, issue **needs‑more‑evidence**.  
-- If any anti‑pattern is present, issue **rejected** regardless of other evidence.
+#### Decision logic
+- If any anti‑pattern (item 5) is present → **rejected** (overrides everything else).  
+- Else if items 1‑4 are all fully satisfied → **sound**.  
+- Else → **needs‑more‑evidence**.
 
-Provide your **verdict** followed by a concise **reasoning** that references the specific checklist items (or anti‑patterns) that drove your decision. Do not include any additional sections or formatting beyond the required verdict and reasoning.+#### Output format
+1. **First line:** the verdict keyword (`sound`, `needs-more-evidence`, or `rejected`).  
+2. **Second line:** a brief justification that cites the checklist items (or anti‑patterns) that led to your decision.
+
+Do not add headings, extra sentences, or any other formatting. Only the two lines described above. 
```

### Island 1, cell (0, 1), scalar 0.1959

parent `0c94fb56277d801f` -> candidate `16246e8205de236c`

```diff
--- parent 0c94fb56277d801f
+++ candidate 16246e8205de236c
@@ -1,20 +1,19 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted material and issue a **single verdict**—one of the three exact categories defined in the governance framework:
+You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Respond with **exactly two lines**:
 
-* **sound** – the case provides convincing, comprehensive evidence that the risk is controlled and the relaxation is justified.
-* **needs‑more‑evidence** – the case is missing critical information or contains gaps that prevent a confident decision.
-* **rejected** – the case exhibits a serious flaw (e.g., an anti‑pattern from Section 9) that makes the relaxation unacceptable.
+1. **Verdict** – one word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Reason** – a brief justification that cites the specific checklist items that led to your decision.
 
-When forming your judgment, apply the following checklist derived from **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9**:
+Use this checklist (derived from Section 8, Strategy C and the anti‑patterns of Section 9):
 
-1. **Real‑world testing** – Has the team performed functional or integration tests in an environment that realistically mirrors production? Include specifics (test scope, duration, results).
-2. **Failure analysis** – Is there a documented assessment of possible failure modes, their likelihood, and mitigations? Look for “what‑if” scenarios and contingency plans.
-3. **Auditability** – Does the proposal include an immutable audit trail (e.g., logs, provenance data) that can reconstruct decisions after the fact?
-4. **Human‑decision benchmark** – Is there a quantitative or qualitative comparison between the autonomous agent’s decisions and those a qualified human would make? Provide performance metrics or validation studies.
-5. **Anti‑pattern detection** – Identify any of the Section 9 anti‑patterns (e.g., “single point of failure”, “unchecked privilege escalation”, “insufficient observability”). The presence of any such pattern should lead directly to a **rejected** verdict.
+- **Test** – shows functional/integration testing in a production‑like environment, with scope, duration, and results.  
+- **Failure** – provides a documented failure‑mode analysis, likelihood estimates, and mitigation or contingency plans.  
+- **Audit** – includes an immutable audit trail (logs, provenance) that can reconstruct every decision.  
+- **Benchmark** – offers a quantitative or qualitative comparison between the autonomous decision and a qualified human’s decision.  
+- **Anti‑pattern** – any pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
 
-**Decision rule:**  
-- If **all** checklist items are satisfied and no anti‑pattern is found, issue **sound**.  
-- If one or more items are missing or only partially addressed, but no serious anti‑pattern is present, issue **needs‑more‑evidence**.  
-- If any anti‑pattern is present, issue **rejected** regardless of other evidence.
+**Decision rules:**  
+- If any anti‑pattern is present → `rejected` (overrides everything).  
+- If no anti‑pattern and **all** items Test, Failure, Audit, and Benchmark are fully satisfied → `sound`.  
+- If no anti‑pattern but one or more of those four items are missing or incomplete → `needs-more-evidence`.
 
-Provide your **verdict** followed by a concise **reasoning** that references the specific checklist items (or anti‑patterns) that drove your decision. Do not include any additional sections or formatting beyond the required verdict and reasoning.+Do not add headings, bullet points, or any additional text beyond the two required lines. 
```

### Island 2, cell (2, 1), scalar 0.1778

parent `295716d798eeaaf0` -> candidate `a5378d2d495bc797`

```diff
--- parent 295716d798eeaaf0
+++ candidate a5378d2d495bc797
@@ -1,36 +1,21 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submission and produce a **verdict**—one of the three categories defined in the whitepaper (Section 8 Strategy C and Section 9 anti‑patterns)—followed by a concise **justification**.
+You are asked to judge a capability case that seeks to remove the per‑action human approval requirement for an industrial operational‑change gateway. Read the submission and output **one** of the three verdict words defined in the whitepaper (Section 8 Strategy C, Section 9 anti‑patterns), then give a short justification.
 
-**Verdict options**
-- **sound** – the case provides sufficient, high‑quality evidence that the risk of removing human approval is mitigated.
-- **needs‑more‑evidence** – the case is plausible but missing critical data, testing, or analysis; it cannot yet be approved.
-- **rejected** – the case exhibits a serious flaw or matches an anti‑pattern that makes the proposed relaxation unsafe.
+**Verdict choices**
+- **sound** – the evidence convincingly shows that safety, auditability, and risk are controlled.
+- **needs‑more‑evidence** – the proposal is plausible but lacks key data, testing, or analysis.
+- **rejected** – a serious flaw or a listed anti‑pattern makes the relaxation unsafe.
 
-**Evaluation checklist** (address each relevant item in your reasoning; you may note “not applicable” when appropriate):
+**Decision‑making checklist** (reference the items that influence your verdict; mark “N/A” if an item does not apply):
 
-1. **Empirical testing**
-   - Has the team performed realistic, end‑to‑end tests of the automated decision‑making under production‑like conditions?
-   - Are test results quantified (e.g., false‑positive/false‑negative rates, latency, failure modes)?
+1. **Real‑world testing** – Are end‑to‑end, production‑like tests reported? Are results quantified (error rates, latency, failure cases)?
+2. **Risk & failure analysis** – Is there a documented hazard or threat model (FTA, FMEA, etc.)? Are mitigation, fallback, or automatic revert mechanisms described and validated?
+3. **Audit & traceability** – Does the design produce a tamper‑evident log that captures inputs, decisions, timestamps, and can be replayed?
+4. **Human‑baseline comparison** – Are the system’s decisions compared against a statistically significant sample of human operator decisions? Is the performance gap measured and justified?
+5. **Anti‑pattern screening (Section 9)** – Does the submission contain any prohibited patterns (e.g., single point of failure, opaque black‑box, no rollback, over‑reliance on defaults)? If so, the verdict must be **rejected** unless a robust mitigation is documented.
+6. **Governance & continuous monitoring** – Is there a plan for ongoing monitoring, periodic re‑validation, and an escalation path for anomalies?
 
-2. **Risk & failure analysis**
-   - Is there a documented hazard analysis (FTA/FMEA, threat modeling, etc.) covering likely failure modes?
-   - Are mitigation or fallback strategies (e.g., automatic revert, manual override) described and validated?
+**Output format**
+- **Line 1:** the verdict word exactly (`sound`, `needs-more-evidence`, or `rejected`).
+- **Subsequent lines:** a concise justification (1‑3 short paragraphs or bullet points) that cites the relevant checklist items and explains why the verdict was chosen. Do not add any extra commentary or formatting beyond this.
 
-3. **Auditability & traceability**
-   - Does the solution generate a tamper‑evident audit log that records inputs, decisions, and timestamps?
-   - Can the log be inspected post‑hoc to reconstruct the decision path?
-
-4. **Human‑baseline comparison**
-   - Are the agent’s decisions compared against a statistically significant sample of human operator decisions?
-   - Is the performance gap quantified and justified as acceptable?
-
-5. **Alignment with anti‑patterns (Section 9)**
-   - Identify any of the listed anti‑patterns (e.g., “single point of failure”, “opaque black‑box decision”, “absence of rollback”, “over‑reliance on defaults”). If any are present, the verdict must be **rejected** unless a convincing mitigation is documented.
-
-6. **Governance & continuous monitoring**
-   - Is there a plan for ongoing monitoring, periodic re‑validation, and an explicit escalation path if anomalies arise?
-
-**Output requirements**
-- Begin with the single‑word verdict (**sound**, **needs‑more‑evidence**, or **rejected**).
-- Follow with a brief, structured reasoning section (e.g., bullet points or short paragraphs) that references the checklist items above and explains why the verdict was chosen.
-
-Do not include any additional commentary beyond the verdict and its justification.+Proceed with the assessment now.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
