# Generation 1 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 74.6%
- Aggregate throughput: 92.8 tok/s (184150 completion tokens / 1984.9s)

## Archive

- Island 0: coverage 13.9%, QD score 1.958, unique ancestors 3
- Island 1: coverage 11.1%, QD score 1.938, unique ancestors 2
- Island 2: coverage 16.7%, QD score 2.327, unique ancestors 5
- Island 3: coverage 16.7%, QD score 2.594, unique ancestors 4
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.6294
- Median scalar of newly-claimed: 0.5245

## Cost

- Budget: {'generation': 1, 'max_generations': 30, 'tokens_used_total': 1168707, 'max_tokens': 3000000, 'elapsed_s_total': 4300.2, 'generation_wall_s': 1984.9}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 4), scalar 0.5389

parent `da4ba008393d23f1` -> candidate `c672b91b08de7e05`

```diff
--- parent da4ba008393d23f1
+++ candidate c672b91b08de7e05
@@ -1,22 +1,22 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Evaluate the submission against the criteria set out in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns enumerated in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are assessing a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Judge the submission by checking it against the requirements of Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the IT/OT‑boundary‑as‑architecture whitepaper.
 
-Assess the following five elements:
+Evaluate the case on the following five points:
 
-1. **Real‑world testing** – evidence of live or high‑fidelity simulated trials of the automated decision‑making.
-2. **Failure‑mode analysis** – identification of possible ways the automation could go wrong and concrete mitigation or fallback measures.
-3. **Audit trail** – an immutable record that logs each automated decision, its inputs, and outcomes.
-4. **Human‑baseline comparison** – quantitative or qualitative comparison showing that the agent’s decisions meet or exceed human performance (e.g., error rates, response times).
-5. **Anti‑pattern compliance** – ensure none of the Section 9 anti‑patterns (such as single point of failure, unbounded automation, lack of rollback, opaque logic, etc.) are present.
+1. **Real‑world or high‑fidelity testing** – Does the submission include live runs or realistic simulations that demonstrate safe automated decision‑making?
+2. **Failure‑mode analysis** – Are plausible failure modes identified and are concrete mitigation or fallback mechanisms described?
+3. **Auditability** – Is there an immutable, tamper‑evident log of each automated decision together with its inputs and outcomes?
+4. **Human baseline comparison** – Is there quantitative or qualitative evidence that the automation meets or exceeds human performance (e.g., error rates, response times)?
+5. **Anti‑pattern check** – Verify that none of the Section 9 anti‑patterns (single point of failure, unchecked automation, missing rollback, opaque logic, etc.) are present.
 
-Choose exactly one of the three allowed verdicts:
+Select **exactly one** verdict:
 
-- **sound** – the case provides credible evidence for all five elements and contains no anti‑pattern.
-- **needs‑more‑evidence** – one or more elements are weak or missing, but no fatal anti‑pattern is found.
-- **rejected** – a serious anti‑pattern or fundamental flaw makes the relaxation unsafe.
+* **sound** – all five points are convincingly satisfied and no anti‑pattern is found.  
+* **needs‑more‑evidence** – at least one point is weak or missing, but no fatal anti‑pattern appears.  
+* **rejected** – a serious anti‑pattern or fundamental safety flaw is identified.
 
-After the verdict, give a concise rationale (maximum three sentences) that cites the specific criteria influencing your decision.
+After the verdict, provide a brief rationale (no more than three sentences) that cites the specific criteria influencing your decision.
 
-Respond in this exact format:
+Output must follow this exact layout:
 
-Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation>+Verdict: <sound|needs-more-evidence|rejected>  
+Reasoning: <your concise explanation>
```

### Island 0, cell (1, 5), scalar 0.3455

parent `da4ba008393d23f1` -> candidate `9905d37fcb4dcd39`

```diff
--- parent da4ba008393d23f1
+++ candidate 9905d37fcb4dcd39
@@ -1,20 +1,20 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Evaluate the submission against the criteria set out in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns enumerated in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are assessing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Judge the submission against Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-Assess the following five elements:
+Evaluate the following five required evidence items:
 
-1. **Real‑world testing** – evidence of live or high‑fidelity simulated trials of the automated decision‑making.
-2. **Failure‑mode analysis** – identification of possible ways the automation could go wrong and concrete mitigation or fallback measures.
-3. **Audit trail** – an immutable record that logs each automated decision, its inputs, and outcomes.
-4. **Human‑baseline comparison** – quantitative or qualitative comparison showing that the agent’s decisions meet or exceed human performance (e.g., error rates, response times).
-5. **Anti‑pattern compliance** – ensure none of the Section 9 anti‑patterns (such as single point of failure, unbounded automation, lack of rollback, opaque logic, etc.) are present.
+1. **Real‑world or high‑fidelity testing** – documented live or simulated trials of the automated decision‑making.
+2. **Failure‑mode analysis** – identified failure vectors together with concrete mitigation or fallback measures.
+3. **Audit trail** – an immutable, tamper‑evident record of each automated decision, its inputs, and outcomes.
+4. **Human‑baseline comparison** – quantitative or qualitative evidence that the automation matches or exceeds human performance.
+5. **Anti‑pattern compliance** – verification that none of the Section 9 anti‑patterns (e.g., single point of failure, unbounded automation, lack of rollback, opaque logic, etc.) are present.
 
-Choose exactly one of the three allowed verdicts:
+Select exactly one of the three verdicts:
 
-- **sound** – the case provides credible evidence for all five elements and contains no anti‑pattern.
-- **needs‑more‑evidence** – one or more elements are weak or missing, but no fatal anti‑pattern is found.
+- **sound** – all five items are convincingly addressed and no anti‑pattern is found.
+- **needs-more-evidence** – one or more items are weak or missing, but no fatal anti‑pattern is present.
 - **rejected** – a serious anti‑pattern or fundamental flaw makes the relaxation unsafe.
 
-After the verdict, give a concise rationale (maximum three sentences) that cites the specific criteria influencing your decision.
+After the verdict, provide a concise rationale (no more than three sentences) that cites the specific item(s) influencing your decision.
 
 Respond in this exact format:
 

```

### Island 1, cell (0, 5), scalar 0.5275

parent `c2a9a9052af9eb27` -> candidate `fb475c3839db3a12`

```diff
--- parent c2a9a9052af9eb27
+++ candidate fb475c3839db3a12
@@ -1,40 +1,26 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.  
-Your task is to read the submitted material and output **one of three verdicts** – **sound**, **needs‑more‑evidence**, or **rejected** – followed by a concise justification.
+You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. After reviewing the submission, output **exactly** one of the three verdicts—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification.
 
-### Decision framework
+#### Evaluation rubric
 
-1. **Evidence of real‑world testing**  
-   - Has the team executed end‑to‑end tests in a production‑like environment?  
-   - Are test results documented, reproducible, and cover normal as well as edge cases?
+| Area | What to look for |
+|------|------------------|
+| **1. Real‑world validation** | Pilots, staged roll‑outs, or high‑fidelity simulations that mimic production; quantitative results for normal and edge conditions. |
+| **2. Failure‑mode and mitigation** | Catalog of plausible failures (per Section 9), with defined fallback, safe‑state, or recovery actions for each. |
+| **3. Traceability** | Immutable, tamper‑evident logs or cryptographic receipts that let an auditor reconstruct the decision chain. |
+| **4. Human‑parity evidence** | Direct comparison to expert human decisions; metrics such as precision/recall, false‑positive/negative rates meeting the thresholds of Section 8 (Strategy C). |
+| **5. Anti‑pattern compliance** | Absence of any listed anti‑patterns: black‑box only reasoning, missing manual override, single point of failure without redundancy, unbounded autonomy, or lack of safety monitoring. |
 
-2. **Risk & failure analysis**  
-   - Is there a systematic identification of plausible failure modes (Section 9 anti‑patterns)?  
-   - Are mitigations, fall‑back procedures, or safe‑state actions described for each risk?
+#### Verdict rules
 
-3. **Auditability & traceability**  
-   - Does the proposal include an immutable audit trail (e.g., tamper‑evident logs, cryptographic signing)?  
-   - Can a regulator or operator reconstruct the decision path after the fact?
+* **rejected** – any anti‑pattern from #5 is present **or** a fatal safety gap (e.g., no mitigation for a high‑impact failure).  
+* **sound** – every item in columns 1‑4 is fully satisfied with quantitative evidence and no anti‑patterns are found.  
+* **needs‑more‑evidence** – no anti‑patterns, but at least one of the items 1‑4 is weak, missing, or only superficially addressed.
 
-4. **Human‑parity or superiority validation**  
-   - Are there comparative studies showing the agent’s decisions match or exceed human performance on a representative set of scenarios?  
-   - Are performance metrics (precision, recall, false‑positive/negative rates) provided and meet the thresholds defined in Section 8 (Strategy C)?
-
-5. **Compliance with anti‑patterns (Section 9)**  
-   - No reliance on “black‑box only” justification.  
-   - No omission of a clearly defined exit/override mechanism.  
-   - No evidence of “single point of failure” without redundancy.
-
-### Verdict criteria
-
-- **sound** – All five categories above are satisfied with sufficient depth and quantitative support.  
-- **needs‑more‑evidence** – The submission is generally reasonable but at least one critical element (e.g., testing breadth, risk mitigation, audit trail, or human‑parity data) is missing, weak, or only superficially addressed.  
-- **rejected** – A fatal flaw is present: serious safety risk without mitigation, violation of an anti‑pattern, or complete lack of testing/auditability.
-
-### Output format
+#### Required output
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation referencing the criteria above>
+Reasoning: <concise reference to the rubric items that led to the decision>
 ```
 
-Provide the verdict on the first line exactly as shown, then a single‑sentence or short‑paragraph justification on the second line. Do not include any extra sections or commentary.+Place the verdict on the first line exactly as shown, then a single sentence or short paragraph on the second line that cites the relevant rubric sections. Do not add any other text.
```

### Island 1, cell (1, 5), scalar 0.5057

parent `c2a9a9052af9eb27` -> candidate `d146b69015c0fa21`

```diff
--- parent c2a9a9052af9eb27
+++ candidate d146b69015c0fa21
@@ -1,40 +1,22 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.  
-Your task is to read the submitted material and output **one of three verdicts** – **sound**, **needs‑more‑evidence**, or **rejected** – followed by a concise justification.
+You are to assess a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. After reviewing the submitted evidence, output **exactly** one of the three verdicts – **sound**, **needs‑more‑evidence**, or **rejected** – followed by a brief justification.
 
-### Decision framework
+#### Evaluation checklist  
+For each item, note whether the submission **meets**, **partially meets**, or **fails** the requirement.
 
-1. **Evidence of real‑world testing**  
-   - Has the team executed end‑to‑end tests in a production‑like environment?  
-   - Are test results documented, reproducible, and cover normal as well as edge cases?
+1. **Production‑like testing** – end‑to‑end trials in an environment that mirrors real operations, with documented results for normal and edge cases.  
+2. **Failure‑mode & mitigation analysis** – systematic list of plausible failures (per Section 9 anti‑patterns) together with fallback actions, safe‑state procedures, or redundancy.  
+3. **Audit & traceability** – immutable, tamper‑evident logs (e.g., signed records) that allow reconstruction of the decision path.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison showing the agent’s decisions equal or exceed expert human performance on a representative scenario set, with metrics (precision, recall, false‑positive/negative rates) meeting Section 8 thresholds.  
+5. **Anti‑pattern compliance** – verify the absence of any Section 9 anti‑patterns (black‑box‑only justification, missing manual override, single point of failure, unbounded autonomy, lack of safety monitoring, etc.).
 
-2. **Risk & failure analysis**  
-   - Is there a systematic identification of plausible failure modes (Section 9 anti‑patterns)?  
-   - Are mitigations, fall‑back procedures, or safe‑state actions described for each risk?
+#### Decision rules
+- **Reject** if any anti‑pattern from item 5 is present **or** if a fatal safety flaw is evident.  
+- **Sound** if all five items are satisfied with sufficient depth and quantitative support.  
+- **Needs‑more‑evidence** if the case is overall acceptable but one or more of items 1‑4 are missing, weak, or only superficially addressed, and no anti‑patterns are detected.
 
-3. **Auditability & traceability**  
-   - Does the proposal include an immutable audit trail (e.g., tamper‑evident logs, cryptographic signing)?  
-   - Can a regulator or operator reconstruct the decision path after the fact?
-
-4. **Human‑parity or superiority validation**  
-   - Are there comparative studies showing the agent’s decisions match or exceed human performance on a representative set of scenarios?  
-   - Are performance metrics (precision, recall, false‑positive/negative rates) provided and meet the thresholds defined in Section 8 (Strategy C)?
-
-5. **Compliance with anti‑patterns (Section 9)**  
-   - No reliance on “black‑box only” justification.  
-   - No omission of a clearly defined exit/override mechanism.  
-   - No evidence of “single point of failure” without redundancy.
-
-### Verdict criteria
-
-- **sound** – All five categories above are satisfied with sufficient depth and quantitative support.  
-- **needs‑more‑evidence** – The submission is generally reasonable but at least one critical element (e.g., testing breadth, risk mitigation, audit trail, or human‑parity data) is missing, weak, or only superficially addressed.  
-- **rejected** – A fatal flaw is present: serious safety risk without mitigation, violation of an anti‑pattern, or complete lack of testing/auditability.
-
-### Output format
-
+#### Required output
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation referencing the criteria above>
+Reasoning: <concise explanation citing the checklist items that drove the decision>
 ```
-
-Provide the verdict on the first line exactly as shown, then a single‑sentence or short‑paragraph justification on the second line. Do not include any extra sections or commentary.+Place the verdict on the first line exactly as shown, then a single sentence or short paragraph on the second line. Do not add any other sections, headings, or commentary.
```

### Island 2, cell (0, 5), scalar 0.3412

parent `b65fbc6601292569` -> candidate `2ed2409d3a2f9a44`

```diff
--- parent b65fbc6601292569
+++ candidate 2ed2409d3a2f9a44
@@ -1,32 +1,16 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and issue a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a concise rationale (1‑2 sentences) that explains the decision.
-
-### Decision criteria
-1. **Sound** – The submission demonstrates **all** of the following:
-   - **Real‑world testing**: concrete test results (e.g., pilot runs, simulations) that show the automated decision works reliably under realistic conditions.
-   - **Risk analysis**: a thorough identification of failure modes, their likelihood, and mitigations.
-   - **Auditability**: a clear, immutable audit trail for every automated decision, covering inputs, outputs, and timestamps.
-   - **Human‑benchmark comparison**: quantitative or qualitative evidence that the automated decisions match or exceed the quality of a human operator in comparable scenarios.
-
-2. **Needs‑more‑evidence** – The submission is missing **one or more** of the items above, but there is no indication of a fundamental flaw. Typical gaps include:
-   - Limited or synthetic test data.
-   - Incomplete risk assessment or missing mitigation details.
-   - No defined audit‑log mechanism or insufficient logging depth.
-   - Lack of direct comparison to human performance.
-
-   Indicate which specific element(s) are lacking.
-
-3. **Rejected** – The submission contains a **serious red‑flag** that violates the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, such as:
-   - Proposing to remove human oversight for safety‑critical or irreversible actions.
-   - Absence of any testing or reliance solely on theoretical arguments.
-   - Evidence of potential conflict of interest, opaque decision logic, or inability to roll back decisions.
-   - Any indication that the system could bypass established security or compliance controls.
-
-   State the primary anti‑pattern that leads to rejection.
-
-### Output format
-Provide exactly two lines:
+You are reviewing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Read the supplied evidence and output **exactly two lines**:
 
 1. **Verdict:** `<sound|needs-more-evidence|rejected>`
-2. **Reasoning:** `<brief justification>`
+2. **Reasoning:** `<concise justification>`
 
-Do not include any additional text, headings, or formatting.+### How to decide
+
+| Verdict | Must be true |
+|---------|--------------|
+| **sound** | The submission **fully satisfies** all four mandatory evidence groups: <br>• **Real‑world testing** – documented pilot or simulation results that prove reliable automated decisions.<br>• **Risk analysis** – identified failure modes, likelihoods, and concrete mitigations.<br>• **Auditability** – immutable log of inputs, outputs, timestamps for every decision.<br>• **Human‑benchmark** – quantitative or qualitative comparison showing the automation meets or exceeds human performance. |
+| **needs-more-evidence** | At least one of the four groups above is **partially or not addressed**, but no critical anti‑pattern is present. List the missing or weak element(s) in the reasoning (e.g., “Missing: real‑world testing, audit log”). |
+| **rejected** | The submission contains a **serious anti‑pattern** from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper (e.g., removal of oversight for safety‑critical actions, no testing, opaque decision logic, no rollback, security bypass). State the primary anti‑pattern in the reasoning (e.g., “Red‑flag: removal of human oversight for irreversible action”). |
+
+### Output rules
+- **Only** the two lines described above; no headings, bullet points, or extra whitespace.
+- The reasoning line must be a single sentence that either enumerates missing items (for *needs‑more‑evidence*) or names the anti‑pattern (for *rejected*), or simply states why the case is sound.
```

### Island 3, cell (0, 5), scalar 0.6294

parent `c80cc76b4c1b31a6` -> candidate `35f1adc2d569ac01`

```diff
--- parent c80cc76b4c1b31a6
+++ candidate 35f1adc2d569ac01
@@ -1,38 +1,25 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and issue a single verdict—**sound**, **needs-more-evidence**, or **rejected**—plus a concise justification.
+You are tasked with judging a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Review the supplied evidence and emit **one** of the three verdicts – **sound**, **needs‑more‑evidence**, or **rejected** – together with a short rationale.
 
-**Assessment checklist**
+### Evaluation framework
+| # | Criterion | What to look for |
+|---|-----------|------------------|
+| 1 | **Live‑environment testing** | Demonstrated functional runs in a production‑like setting, with quantitative outcomes (success rate, failure modes, sample size). |
+| 2 | **Failure‑mode & mitigation analysis** | Identification of realistic failure scenarios **and** concrete mitigations or fallback procedures for each. |
+| 3 | **Audit trail** | Tamper‑evident logging of inputs, decisions, timestamps, and outcomes that can be inspected after the fact. |
+| 4 | **Human‑baseline comparison** | Benchmarks against qualified human operators, including accuracy, false‑positive/negative rates, or equivalent qualitative evidence. |
+| 5 | **Anti‑pattern compliance (Section 9)** | Absence of any listed anti‑patterns (e.g., single point of failure, unbounded autonomy, opaque reasoning, missing manual override). |
 
-1. **Real‑world testing**  
-   - Has the team conducted functional tests in a production‑like environment?  
-   - Are test results quantified (e.g., success rate, failure modes, sample size)?
+### Verdict rules
+- **rejected** – any anti‑pattern is present **or** a critical risk has no mitigation.  
+- **sound** – all five criteria are satisfied to a degree that a reasonable reviewer would consider the risk mitigated.  
+- **needs‑more‑evidence** – one or more criteria are partially addressed or missing, but no anti‑pattern or unmitigated critical risk is found.
 
-2. **Risk & failure‑mode analysis**  
-   - Does the submission identify plausible failure scenarios?  
-   - Are mitigations or fallback procedures described for each identified risk?
-
-3. **Auditability & traceability**  
-   - Is there a logged audit trail that records the agent’s decisions, inputs, and outcomes?  
-   - Can the trail be inspected post‑hoc to verify correct behavior?
-
-4. **Human‑decision baseline comparison**  
-   - Does the team benchmark the agent’s actions against decisions a qualified human would make?  
-   - Are performance metrics (e.g., accuracy, false‑positive/negative rates) reported?
-
-5. **Compliance with anti‑patterns (Section 9 of the whitepaper)**  
-   - Verify that none of the listed anti‑patterns (e.g., “single point of failure”, “unbounded autonomy”, “opaque reasoning”) are present.  
-   - If any anti‑pattern is detected, the case must be **rejected**.
-
-**Verdict mapping**
-
-- **sound** – All checklist items are satisfactorily addressed and no anti‑patterns are present.  
-- **needs-more-evidence** – One or more checklist items are incomplete or weak, but no critical red‑flag or anti‑pattern is found.  
-- **rejected** – Any anti‑pattern is present, or a critical risk is unmitigated.
-
-**Output format** (do not alter external template)
-
+### Output (do not modify the surrounding template)
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation referencing the checklist items>
+Reasoning: <brief statement that cites the specific checklist items that drove the decision>
 ```
+- Place the verdict on the first line.  
+- Follow with a single line of reasoning, explicitly referencing the numbered criteria (e.g., “Missing audit trail (criterion 3)” or “All criteria met, no anti‑patterns detected”).  
 
-Provide the verdict first, then the reasoning on a new line. Ensure the reasoning directly ties back to the criteria above.+Make your rationale concise and directly tied to the framework above.
```

### Island 3, cell (1, 5), scalar 0.5245

parent `c80cc76b4c1b31a6` -> candidate `172bf780d2645838`

```diff
--- parent c80cc76b4c1b31a6
+++ candidate 172bf780d2645838
@@ -1,38 +1,46 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and issue a single verdict—**sound**, **needs-more-evidence**, or **rejected**—plus a concise justification.
+You are tasked with reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence supplied and issue a single verdict – **sound**, **needs-more-evidence**, or **rejected** – followed by a brief justification.
 
-**Assessment checklist**
+**Decision framework**
 
-1. **Real‑world testing**  
-   - Has the team conducted functional tests in a production‑like environment?  
-   - Are test results quantified (e.g., success rate, failure modes, sample size)?
+1. **Real‑world validation**  
+   - Does the submission show repeatable testing in a production‑representative environment?  
+   - Are outcomes expressed with concrete numbers (e.g., “99 % success over 1 000 runs, 2 % failure on edge case X”)?
 
-2. **Risk & failure‑mode analysis**  
-   - Does the submission identify plausible failure scenarios?  
-   - Are mitigations or fallback procedures described for each identified risk?
+2. **Failure‑mode & mitigation**  
+   - Are plausible failure scenarios enumerated?  
+   - For each scenario, is a specific mitigation or fallback (e.g., automatic revert to human control, safe‑shutdown) described and its effectiveness quantified?
 
-3. **Auditability & traceability**  
-   - Is there a logged audit trail that records the agent’s decisions, inputs, and outcomes?  
-   - Can the trail be inspected post‑hoc to verify correct behavior?
+3. **Audit trail**  
+   - Is there a tamper‑evident log that captures inputs, decisions, timestamps, and results?  
+   - Can an auditor reconstruct the decision path after the fact?
 
-4. **Human‑decision baseline comparison**  
-   - Does the team benchmark the agent’s actions against decisions a qualified human would make?  
-   - Are performance metrics (e.g., accuracy, false‑positive/negative rates) reported?
+4. **Human‑baseline comparison**  
+   - Does the case provide a direct comparison between the automated action and a qualified human operator (accuracy, false‑positive/negative rates, decision latency)?  
+   - Are the comparison results favorable or at least comparable?
 
-5. **Compliance with anti‑patterns (Section 9 of the whitepaper)**  
-   - Verify that none of the listed anti‑patterns (e.g., “single point of failure”, “unbounded autonomy”, “opaque reasoning”) are present.  
-   - If any anti‑pattern is detected, the case must be **rejected**.
+5. **Anti‑pattern compliance (Section 9)**  
+   - Check for any listed anti‑patterns such as:  
+     * single point of failure,  
+     * unbounded autonomy,  
+     * opaque/black‑box reasoning,  
+     * lack of manual override,  
+     * insufficient monitoring.  
+   - Presence of any anti‑pattern is an automatic **rejected**.
 
-**Verdict mapping**
+6. **Governance & ongoing oversight** *(optional but strengthens the case)*  
+   - Is there a defined process for continuous monitoring, periodic review, and re‑instating human approval if metrics degrade?
 
-- **sound** – All checklist items are satisfactorily addressed and no anti‑patterns are present.  
-- **needs-more-evidence** – One or more checklist items are incomplete or weak, but no critical red‑flag or anti‑pattern is found.  
-- **rejected** – Any anti‑pattern is present, or a critical risk is unmitigated.
+**Verdict rules**
 
-**Output format** (do not alter external template)
+- **sound** – Every mandatory item (1‑5) is fully satisfied, no anti‑patterns are found, and any optional governance is at least outlined.  
+- **needs-more-evidence** – One or more mandatory items are partially addressed or missing, but no anti‑pattern appears.  
+- **rejected** – Any anti‑pattern is present, or a critical risk (e.g., no mitigation for a high‑impact failure mode) is unaddressed.
+
+**Output format** (must match the surrounding template)
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation referencing the checklist items>
+Reasoning: <concise explanation that cites the specific checklist items]
 ```
 
-Provide the verdict first, then the reasoning on a new line. Ensure the reasoning directly ties back to the criteria above.+Place the verdict on the first line, then the reasoning on a new line, directly referencing the items above. Do not add any other sections or formatting.
```


## Lesson retirement (dry run)

- Lesson 11: **kept** — never injected
- Lesson 15: **RETIRED** — precision 0.173 vs base 0.482, 6.2 sigma below
- Lesson 19: **kept** — precision 0.982 >= base 0.881
- Lesson 17: **kept** — precision 0.973 >= base 0.688
