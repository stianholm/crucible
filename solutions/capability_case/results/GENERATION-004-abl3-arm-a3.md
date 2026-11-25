# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 66.0%
- Aggregate throughput: 73.5 tok/s (206655 completion tokens / 2810.0s)

## Archive

- Island 0: coverage 30.6%, QD score 6.718, unique ancestors 2
- Island 1: coverage 19.4%, QD score 4.061, unique ancestors 3
- Island 2: coverage 30.6%, QD score 6.284, unique ancestors 4
- Island 3: coverage 30.6%, QD score 6.519, unique ancestors 4
- Cells newly claimed this generation: 6

## Quality

- Best scalar this generation: 0.7517
- Median scalar of newly-claimed: 0.6794

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 3123068, 'max_tokens': 3000000, 'elapsed_s_total': 11659.6, 'generation_wall_s': 2810.0}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 2), scalar 0.7517

parent `2ed205cccf5b78cb` -> candidate `ff077e91532f5213`

```diff
--- parent 2ed205cccf5b78cb
+++ candidate ff077e91532f5213
@@ -1,36 +1,36 @@
-You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Choose exactly one of the three outcomes defined in the white‑paper:
+You are to evaluate a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Choose **exactly one** of the three verdicts defined in the white‑paper:
 
-* **sound** – the submission demonstrates, with solid evidence, that all risks are mitigated.
-* **needs‑more‑evidence** – the submission is incomplete or vague on essential points but shows no disqualifying flaw.
-* **rejected** – the submission violates any anti‑pattern from Section 9 or introduces an unacceptable safety/security hazard.
+* **sound** – the case provides convincing, complete evidence that all identified risks are mitigated.  
+* **needs‑more‑evidence** – the case is missing or incomplete on essential points but contains no disqualifying flaw.  
+* **rejected** – the case exhibits any anti‑pattern from Section 9 or introduces an unacceptable safety/security hazard.
 
-**Evaluation checklist**
+### Checklist (all items must be considered)
 
-1. **Real‑world verification** – evidence of controlled field trials or realistic simulation, including quantitative results and failure rates.  
-2. **Failure‑mode & risk analysis** – systematic identification of possible faults (e.g., FMEA, fault trees) together with mitigation strategies.  
-3. **Audit trail** – immutable logging or other mechanisms that allow post‑action inspection of every automated decision.  
-4. **Human‑baseline comparison** – side‑by‑side performance data (accuracy, false‑positive/false‑negative rates, etc.) comparing the automation to qualified human operators.  
-5. **Anti‑pattern screening (Section 9)** – confirm that none of the prohibited patterns appear, such as:
-   - Unbounded autonomy without a fallback or manual override,
+1. **Real‑world verification** – documented controlled field trials or high‑fidelity simulations with quantitative results (e.g., success/failure rates).  
+2. **Failure‑mode & risk analysis** – systematic identification of faults (FMEA, fault trees, hazard analysis) together with concrete mitigation strategies.  
+3. **Auditability** – immutable logging or equivalent that enables post‑action inspection of every automated decision.  
+4. **Human‑baseline comparison** – side‑by‑side performance data (accuracy, false‑positive/false‑negative rates, latency, etc.) comparing the automation to qualified human operators.  
+5. **Anti‑pattern screening (Section 9)** – verify that none of the prohibited patterns appear, such as:
+   - Unbounded autonomy without a manual fallback or emergency stop,
    - Single point of failure in the decision pipeline,
    - Opaque/black‑box decision logic,
    - Missing segregation of duties or revocation capability,
    - Any other listed anti‑pattern.
 
-**Decision rules**
+### Decision logic (apply in order)
 
-* If any item in **5** is present → **rejected**.  
-* Else if any of items **1‑4** is missing or only partially addressed → **needs‑more‑evidence**.  
-* Else (all items **1‑4** fully satisfied and no anti‑pattern) → **sound**.
+1. **If any item in 5 is present → verdict = `rejected`.**  
+2. **Otherwise, if any of items 1‑4 is missing, incomplete, or only partially addressed → verdict = `needs-more-evidence`.**  
+3. **If items 1‑4 are fully satisfied and no anti‑pattern is found → verdict = `sound`.**
 
-**Output format (must be followed exactly)**  
+### Output format (must be followed exactly)
 
 ```
 <verdict>
 <brief rationale>
 ```
 
-- `<verdict>` is one of: `sound`, `needs-more-evidence`, or `rejected` (all lower‑case).  
-- `<brief rationale>` is one or two short sentences citing the checklist items that led to the verdict. No additional text or formatting is allowed.
+* `<verdict>`: `sound`, `needs-more-evidence`, or `rejected` (lower‑case).  
+* `<brief rationale>`: one or two short sentences that cite the checklist items that led to the verdict. No extra text, headings, or formatting are allowed.
 
 Proceed with the assessment now.
```

### Island 0, cell (2, 5), scalar 0.5960

parent `6aff105be4b987bb` -> candidate `22aa4de1cfc11e45`

```diff
--- parent 6aff105be4b987bb
+++ candidate 22aa4de1cfc11e45
@@ -1,31 +1,35 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and, according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, classify the case into one of three outcomes:
+You are to judge a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway. Using Section 8 (Strategy C) and the anti‑patterns of Section 9 of the IT‑OT‑boundary‑as‑architecture whitepaper, decide **exactly one** of the three outcomes:
 
-* **SOUND** – the evidence convincingly demonstrates that the proposed relaxation can be safely implemented.
-* **NEEDS_MORE_EVIDENCE** – the submission contains gaps or insufficient detail that prevents a confident decision.
-* **REJECTED** – the submission exhibits a serious flaw or anti‑pattern that makes the proposal unsafe or non‑compliant.
+* **SOUND** – the submission supplies convincing, complete evidence that the relaxation can be deployed safely.  
+* **NEEDS_MORE_EVIDENCE** – the submission is missing or only partially addressing essential evidence, so a confident decision cannot be made.  
+* **REJECTED** – the submission exhibits a prohibited anti‑pattern or a critical safety/security flaw that makes the proposal unacceptable.
 
-When making your decision, explicitly consider each of the following criteria and note any that are unmet:
+### Evaluation checklist
+For each item mark **PASS** if the evidence fully meets the requirement, otherwise **FAIL**.
 
-1. **Empirical Testing** – Has the team performed realistic, end‑to‑end testing of the automated decision‑making in the intended operational environment? Include load, failure, and recovery scenarios.
-2. **Risk Analysis** – Is there a documented analysis of potential failure modes, their likelihood, and mitigations (e.g., “what‑if” or FMEA style reasoning)?
-3. **Auditability** – Does the solution provide an immutable audit trail (e.g., tamper‑evident logs, traceability to the originating data and decision logic)?
-4. **Human‑Decision Benchmarking** – Are the agent’s decisions compared against a baseline of human decisions, with quantitative or qualitative performance metrics?
-5. **Governance & Compliance** – Does the proposal adhere to relevant regulatory, safety, and IT‑OT governance requirements (e.g., segregation of duties, fallback procedures)?
-6. **Anti‑Pattern Checks (Section 9)** – Verify that none of the following appear:
-   - Unjustified “black‑box” automation without explainability.
-   - Absence of a manual override or emergency stop.
-   - Over‑reliance on a single point of failure.
-   - Insufficient separation between IT and OT control domains.
+1. **Real‑world testing** – end‑to‑end, realistic trials (including load, failure, recovery) with quantitative results.  
+2. **Failure‑mode analysis** – documented systematic analysis (e.g., FMEA, fault trees) with likelihoods and mitigations.  
+3. **Auditability** – immutable, tamper‑evident logs or traceability that can be reviewed after every automated decision.  
+4. **Human‑benchmark comparison** – quantitative/qualitative comparison of automated decisions to expert human decisions.  
+5. **Governance & compliance** – alignment with relevant regulatory, safety, and IT‑OT governance rules (segregation of duties, fallback, etc.).  
+6. **Anti‑pattern check** – confirm none of the Section 9 anti‑patterns appear:
+   - Black‑box automation without explainability  
+   - No manual override or emergency stop  
+   - Single point of failure in the decision pipeline  
+   - Insufficient IT/OT domain separation  
 
-**Output format** (must be followed exactly):
+### Decision rules
+* If any **anti‑pattern check** is **FAIL** → **REJECTED**.  
+* Else if any of items 1‑5 is **FAIL** → **NEEDS_MORE_EVIDENCE**.  
+* Else (all items **PASS**) → **SOUND**.
+
+### Output (exactly this format)
 
 ```
-Verdict: <SOUND | NEEDS_MORE_EVIDENCE | REJECTED>
+Verdict: <SOUND|NEEDS_MORE_EVIDENCE|REJECTED>
 Reasoning:
-- <brief point addressing each criterion, noting satisfied or missing>
-- <additional observations, including any anti‑pattern violations>
+- <criterion>: PASS/FAIL (brief note)
+- <additional comment, e.g., which anti‑pattern caused a rejection or the most critical missing evidence>
 ```
 
-Provide a concise but complete justification for every criterion you reference. If the verdict is **NEEDS_MORE_EVIDENCE**, specify the most critical missing elements. If the verdict is **REJECTED**, highlight the specific anti‑pattern(s) that cause the rejection.
-
-Proceed with the evaluation now.+List each checklist item (or at least those that influenced the verdict) on its own line prefixed with “-”. Keep the reasoning concise but sufficient to show which criteria were satisfied or lacking, and why the final verdict was chosen. Proceed with the evaluation now.
```

### Island 1, cell (1, 5), scalar 0.7444

parent `c1d9615ddd4c16b9` -> candidate `de785b29038fb805`

```diff
--- parent c1d9615ddd4c16b9
+++ candidate de785b29038fb805
@@ -1,33 +1,33 @@
-You are an expert reviewer evaluating a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action.  
+You are an expert reviewer assessing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.  
 
-Assess the submission **against Section 8 (Strategy C, capability‑based opening)** and **the anti‑patterns listed in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+Evaluate the submission **against Section 8 (Strategy C, capability‑based opening)** and **the anti‑patterns listed in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Verdict options (choose one)
-- **sound** – every required evidence item is fully satisfied and no anti‑pattern is present.  
-- **needs‑more‑evidence** – no anti‑pattern is found, but one or more required evidence items are missing, incomplete, or only partially addressed.  
-- **reject** – any anti‑pattern is present or a fatal safety/compliance flaw is identified.
+### Verdict choices (pick one)
+- **sound** – all required evidence items are completely satisfied **and** no anti‑pattern appears.  
+- **needs‑more‑evidence** – no anti‑pattern is present, but one or more evidence items are missing, incomplete, or only partially addressed.  
+- **reject** – any anti‑pattern is found or a fatal safety/compliance flaw exists.
 
-### Required evidence (all must be satisfied for **sound**)
+### Required evidence (must all be met for **sound**)
 
-1. **Empirical testing** – realistic end‑to‑end tests in a production‑like environment with quantified results (success rate, error types, latency, etc.).  
-2. **Risk & failure‑mode analysis** – documented threat model covering probable failure modes and mitigation or fallback for each high‑impact failure.  
-3. **Auditability & traceability** – immutable logs that capture inputs, decisions, outputs, timestamps, and enable a regulator to reconstruct any action sequence.  
-4. **Human‑parity benchmark** – comparison of the system’s decisions to qualified humans on a representative dataset, with metrics (accuracy, false‑positive/negative rates) meeting whitepaper thresholds.  
-5. **Risk‑based justification** – quantitative residual‑risk assessment demonstrating that risk remains within acceptable limits.
+1. **Empirical testing** – end‑to‑end tests in a production‑like environment with quantitative results (success rate, error types, latency, etc.).  
+2. **Risk & failure‑mode analysis** – documented threat model covering probable failure modes with mitigation or fallback for each high‑impact failure.  
+3. **Auditability & traceability** – immutable logs capturing inputs, decisions, outputs, timestamps, enabling full reconstruction of any action.  
+4. **Human‑parity benchmark** – systematic comparison to qualified humans on a representative dataset, meeting the whitepaper’s accuracy / false‑positive / false‑negative thresholds.  
+5. **Risk‑based justification** – quantitative residual‑risk assessment showing risk remains within acceptable limits.
 
 ### Disqualifying anti‑patterns (any occurrence → **reject**)
 
 - Single point of failure without redundancy.  
 - Opaque “black‑box” automation lacking explainability or audit capability.  
 - Bypassing safety interlocks or critical supervisory controls.  
-- Unbounded escalation permitting unlimited changes without external review.  
+- Unbounded escalation allowing unlimited changes without external review.  
 - Unvalidated external data sources feeding the decision engine.  
 - Absence of rollback / safe‑stop mechanism.  
 - Missing continuous monitoring or alerting for anomalous behavior.
 
 ### Decision procedure
-1. **Anti‑pattern scan** – if any anti‑pattern is detected, output **reject** and cite each offending pattern.  
-2. **Evidence check** – if no anti‑pattern, verify the five evidence items:  
+1. **Anti‑pattern scan** – If any anti‑pattern is detected, output **reject** and list each offending pattern.  
+2. **Evidence check** – If no anti‑pattern is found, evaluate the five evidence items:  
    - If *all* are fully satisfied → **sound**.  
    - If one or more are missing or only partially satisfied → **needs‑more‑evidence**, listing every deficient item.
 

```

### Island 2, cell (0, 3), scalar 0.6293

parent `f200095f38152fee` -> candidate `5a3fd5dadf5f18eb`

```diff
--- parent f200095f38152fee
+++ candidate 5a3fd5dadf5f18eb
@@ -1,26 +1,26 @@
-You are a reviewer for a Capability Case that proposes eliminating per‑action human approval for an operational‑change gateway. Using only the material supplied in the case, decide on one of the three outcomes below.
+You are an independent reviewer tasked with judging a Capability Case that asks to drop per‑action human approval for an operational‑change gateway. Examine only the evidence supplied in the case and choose one of the three verdicts below.
 
-**Possible outcomes**
-- **sound** – the submission contains sufficient, verifiable evidence for safe automation.  
-- **needs-more-evidence** – the idea is reasonable but one or more required pieces of evidence are missing or inadequate.  
-- **rejected** – the submission exhibits a disqualifying anti‑pattern or a critical safety/compliance flaw.
+**Verdicts**
+- **sound** – the submission supplies verifiable, complete evidence that the automation can be deployed safely.  
+- **needs-more-evidence** – the concept is plausible but one or more required pieces of proof are missing or insufficient.  
+- **rejected** – the case contains a disqualifying anti‑pattern or a critical safety/compliance flaw.
 
-**Review checklist (apply sequentially; stop as soon as a rule triggers a verdict)**  
+**Checklist (apply in order, stop as soon as a rule forces a verdict)**  
 
-1. **Real‑world validation** – Does the case include pilots, field trials, or stress‑tests performed in conditions that resemble production?  
-2. **Failure‑mode & risk assessment** – Are failure scenarios identified, their impact quantified, and concrete mitigations (e.g., FMEA, hazard analysis) described?  
-3. **Audit trail** – Is there an immutable, traceable log that can reconstruct every autonomous decision after execution?  
-4. **Human‑parity data** – Is there empirical evidence that the autonomous system matches or exceeds the performance of qualified human operators for the same action?  
-5. **Anti‑pattern screening (Section 9)** – Verify that none of the listed anti‑patterns appear (e.g., single point of failure without fallback, missing rollback, hidden manual overrides, opaque AI with no explainability, unchecked privilege escalation, lack of segregation of duties, insufficient monitoring).
+1. **Production‑like testing** – does the case report pilots, field trials, or stress tests that mimic real‑world operation?  
+2. **Failure‑mode & risk analysis** – are failure scenarios identified, their consequences quantified, and concrete mitigations (e.g., FMEA, hazard analysis) described?  
+3. **Auditability** – is there an immutable, reconstructable log or record for every autonomous decision?  
+4. **Human‑parity evidence** – is there quantitative data showing the automated action meets or exceeds the performance of qualified human operators?  
+5. **Anti‑pattern check (Section 9)** – verify that none of the listed anti‑patterns appear (single point of failure without fallback, missing rollback, hidden manual overrides, opaque AI with no explainability, unchecked privilege escalation, lack of segregation of duties, insufficient monitoring, etc.).
 
-**Decision logic**
+**Decision flow**
 - If step 5 fails → **rejected**.  
-- Else if any of steps 1‑4 are absent or insufficient → **needs-more-evidence**.  
+- Else if any of steps 1‑4 are absent or inadequate → **needs-more-evidence**.  
 - Else (all steps 1‑4 satisfied and step 5 clean) → **sound**.
 
-**Required response (exactly two lines)**
+**Response format (exactly two lines)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise justification naming the checklist items that determined the verdict>
+Reasoning: <brief justification naming the checklist items that triggered the verdict>
 ```
-The first line must be the verdict line; the second line must start with “Reasoning: ” and contain only the brief explanation. No additional text is permitted. Apply the checklist rigorously and base the decision solely on the evidence presented in the submission.+The first line must start with “Verdict:”. The second line must start with “Reasoning: ” and contain only the short explanation. No other text is allowed. Base your decision solely on the material provided in the submission.
```

### Island 2, cell (0, 4), scalar 0.7295

parent `f200095f38152fee` -> candidate `3a0a0fadb2fee10e`

```diff
--- parent f200095f38152fee
+++ candidate 3a0a0fadb2fee10e
@@ -1,26 +1,20 @@
-You are a reviewer for a Capability Case that proposes eliminating per‑action human approval for an operational‑change gateway. Using only the material supplied in the case, decide on one of the three outcomes below.
+You are reviewing a Capability Case that proposes removing per‑action human approval for an operational‑change gateway. Using only the evidence presented in the case, choose one verdict: **sound**, **needs-more-evidence**, or **rejected**.
 
-**Possible outcomes**
-- **sound** – the submission contains sufficient, verifiable evidence for safe automation.  
-- **needs-more-evidence** – the idea is reasonable but one or more required pieces of evidence are missing or inadequate.  
-- **rejected** – the submission exhibits a disqualifying anti‑pattern or a critical safety/compliance flaw.
+**Checklist (evaluate in order, stop when a rule applies)**  
+1. **Real‑world testing** – Does the case show pilots, field trials, or stress‑tests in a production‑like environment?  
+2. **Failure‑mode & risk analysis** – Are failure scenarios identified, impacts quantified, and mitigations (e.g., FMEA, hazard analysis) described?  
+3. **Auditability** – Is there an immutable log or other artifact that can fully reconstruct every autonomous decision?  
+4. **Human‑parity evidence** – Is there quantitative data proving the automated action meets or exceeds qualified human performance?  
+5. **Anti‑pattern screening (Section 9)** – Confirm none of the listed anti‑patterns appear (e.g., single‑point‑of‑failure without fallback, missing rollback, hidden manual overrides, opaque AI, unchecked privilege escalation, lack of segregation of duties, insufficient monitoring).
 
-**Review checklist (apply sequentially; stop as soon as a rule triggers a verdict)**  
+**Decision hierarchy**  
+- If step 5 fails → **rejected**.  
+- Else if any of steps 1‑4 are missing or inadequate → **needs-more-evidence**.  
+- Else → **sound**.
 
-1. **Real‑world validation** – Does the case include pilots, field trials, or stress‑tests performed in conditions that resemble production?  
-2. **Failure‑mode & risk assessment** – Are failure scenarios identified, their impact quantified, and concrete mitigations (e.g., FMEA, hazard analysis) described?  
-3. **Audit trail** – Is there an immutable, traceable log that can reconstruct every autonomous decision after execution?  
-4. **Human‑parity data** – Is there empirical evidence that the autonomous system matches or exceeds the performance of qualified human operators for the same action?  
-5. **Anti‑pattern screening (Section 9)** – Verify that none of the listed anti‑patterns appear (e.g., single point of failure without fallback, missing rollback, hidden manual overrides, opaque AI with no explainability, unchecked privilege escalation, lack of segregation of duties, insufficient monitoring).
-
-**Decision logic**
-- If step 5 fails → **rejected**.  
-- Else if any of steps 1‑4 are absent or insufficient → **needs-more-evidence**.  
-- Else (all steps 1‑4 satisfied and step 5 clean) → **sound**.
-
-**Required response (exactly two lines)**
+**Response (exactly two lines)**  
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise justification naming the checklist items that determined the verdict>
+Reasoning: <brief justification naming the checklist items that determined the verdict>
 ```
-The first line must be the verdict line; the second line must start with “Reasoning: ” and contain only the brief explanation. No additional text is permitted. Apply the checklist rigorously and base the decision solely on the evidence presented in the submission.+The first line must start with “Verdict:”. The second line must start with “Reasoning:” and contain only the short explanation. No extra text is allowed. Apply the checklist strictly and base your decision solely on the supplied material.
```

### Island 3, cell (1, 5), scalar 0.6123

parent `66307149c308e964` -> candidate `1fb9a692df71023c`

```diff
--- parent 66307149c308e964
+++ candidate 1fb9a692df71023c
@@ -1,20 +1,19 @@
-You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway action.
+You are evaluating a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway action.
 
-**Task** – Read the submission and produce **exactly two lines**:
+**Output** – exactly two lines, no extra whitespace or headings:
+1. Verdict word alone (`sound`, `needs-more-evidence` or `rejected`) on the first line. Do **not** add punctuation after it.  
+2. A justification on the second line (≤ 3 sentences) that cites the checklist items or anti‑patterns that determined the verdict.
 
-1. The verdict word alone on the first line: `sound`, `needs-more-evidence` or `rejected` (lower‑case, no extra characters).  
-2. A justification on the second line (no more than three sentences) that references the relevant checklist items or any anti‑pattern you identified.
+**Checklist (must be considered)**  
+1. **Real‑world testing** – end‑to‑end trials in a production‑like environment with results or metrics.  
+2. **Failure‑mode & risk analysis** – identified hazards, impacts, mitigations, and fallback/rollback procedures.  
+3. **Auditability** – tamper‑evident logs or provenance enabling reconstruction of the agent’s decision.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison showing the agent meets or exceeds qualified human performance.  
+5. **Anti‑pattern screening (Section 9)** – confirm none of the listed red‑flags appear (e.g., single‑point automated authority, unbounded escalation, missing rollback, opaque logic, over‑broad permissions, lack of monitoring, unclear ownership).
 
-**Checklist (must be evaluated)**  
-1. **Real‑world testing** – end‑to‑end trials in a production‑like environment with results or metrics.  
-2. **Failure‑mode & risk analysis** – identified hazards, impacts, and mitigations or fallback procedures.  
-3. **Auditability** – tamper‑evident logs or provenance that allow reconstruction of the agent’s decision after execution.  
-4. **Human‑parity evidence** – quantitative or qualitative comparison showing the agent matches or exceeds qualified human performance.  
-5. **Anti‑pattern screening (Section 9)** – ensure none of the listed red‑flags appear, including but not limited to: single point of automated authority, unbounded escalation, missing rollback/abort path, opaque decision logic, over‑broad permissions, lack of monitoring or clear ownership.
+**Decision hierarchy**  
+- If any anti‑pattern from item 5 is present → **rejected**.  
+- Else if items 1‑4 are all satisfactorily addressed → **sound**.  
+- Otherwise → **needs-more-evidence**.
 
-**Decision rules**  
-- **sound** – all five checklist items are satisfactorily addressed and no anti‑pattern is present.  
-- **needs-more-evidence** – one or more items are weak or missing, but no anti‑pattern is found.  
-- **rejected** – any anti‑pattern is evident **or** a critical safety/security gap exists, regardless of other items.
-
-Output must be exactly two lines with no headings, labels, or extra whitespace. Do not add punctuation after the verdict word.+Base your reasoning solely on information provided in the submission; do not assume facts not present. Keep the justification concise and reference the relevant checklist items or anti‑patterns. 
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.127 vs base 0.482, 9.7 sigma below
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 19: **kept** — precision 0.980 >= base 0.881
- Lesson 11: **kept** — precision 0.857 vs base 0.937, only 0.6 sigma below

## Held-out check (best-ever candidate)

- Candidate: `5abeae25c893a003` (rotation scalar 0.8548)
- Held-out quality: 0.5583 (passes: 0.5667, 0.5500)
- Held-out scalar: 0.4350 (passes: 0.4422, 0.4278)
- All held-out tasks valid: True
