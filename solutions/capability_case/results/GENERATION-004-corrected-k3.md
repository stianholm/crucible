# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 52.0%
- Aggregate throughput: 125.1 tok/s (69055 completion tokens / 552.1s)

## Archive

- Island 0: coverage 19.4%, QD score 4.143, unique ancestors 2
- Island 1: coverage 30.6%, QD score 5.317, unique ancestors 4
- Island 2: coverage 11.1%, QD score 2.430, unique ancestors 2
- Island 3: coverage 11.1%, QD score 2.932, unique ancestors 2
- Cells newly claimed this generation: 5

## Quality

- Best scalar this generation: 0.8615
- Median scalar of newly-claimed: 0.7948

## Cost

- Budget: {'generation': 4, 'max_generations': 10, 'tokens_used_total': 1134482, 'max_tokens': 5000000, 'elapsed_s_total': 4436.1, 'generation_wall_s': 552.1}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (0, 2), scalar 0.8084

parent `bdb937fb3068930f` -> candidate `d8e7a55e06943aef`

```diff
--- parent bdb937fb3068930f
+++ candidate d8e7a55e06943aef
@@ -1,25 +1,24 @@
-You are to evaluate a proposal that removes the per‑action human‑approval step for an industrial operational‑change gateway. Base your judgment on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You must assess a proposal to eliminate the per‑action human‑approval step for an industrial operational‑change gateway. Base your judgment on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Step 1 – Look for disqualifying anti‑patterns (any one ⇒ verdict = rejected)**
+**Disqualifying anti‑patterns (any one → verdict = rejected)**
 - No immediate manual‑override or safe‑state fallback.  
 - Decision logic is opaque/black‑box with no explainability.  
-- Unlimited escalation authority or unrestricted action domain.  
-- Absence of continuous monitoring or performance metrics.  
+- Unlimited escalation authority or an unbounded action domain.  
+- Lack of continuous monitoring or performance metrics.  
 - Any other anti‑pattern described in Section 9 that appears in the submission.
 
-If you find any, output **rejected** with a short reason.
+If you detect any, output **rejected** together with a brief reason.
 
-**Step 2 – Check the five required evidence items (all must be satisfied for “sound”)**
-1. **Operational validation** – pilots, simulations, or field trials proving the automation works safely in realistic conditions.  
-2. **Hazard / failure‑mode analysis** – identified faults, impacts, and defined mitigations or fallback procedures.  
+**Required evidence for a “sound” judgment (all five must be satisfied)**
+1. **Operational validation** – pilots, simulations, or field trials showing the automation works safely in realistic conditions.  
+2. **Hazard / failure‑mode analysis** – identified faults, their impacts, and defined mitigations or fallback procedures.  
 3. **Audit‑ready logging** – tamper‑evident records of each decision, inputs, timestamps, and responsible entities.  
-4. **Human‑performance comparison** – quantitative or qualitative data showing the automation meets or exceeds qualified human decision accuracy.  
+4. **Human‑performance benchmark** – quantitative or qualitative data demonstrating the automation meets or exceeds qualified human decision accuracy.  
 5. **Capability limits & controls** – explicit scope, confidence thresholds, and a revocation/override mechanism as required by Section 8.
 
-If every item in Step 2 is adequately addressed and no anti‑pattern was found, output **sound**.
+If every item above is adequately addressed and no anti‑pattern is present, output **sound**.
 
-**Step 3 – Otherwise**  
-If no anti‑pattern exists but one or more evidence items are missing or weak, output **needs-more-evidence**.
+**Otherwise** (no anti‑pattern but one or more evidence items missing or weak) output **needs-more-evidence**.
 
 **Output format**  
 Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by one‑to‑two sentences that cite the most decisive evidence point(s) or anti‑pattern(s). Do not add any other text or formatting.

```

### Island 1, cell (0, 3), scalar 0.3596

parent `9ce42ee484d37ef0` -> candidate `09f756c1286dc0b3`

```diff
--- parent 9ce42ee484d37ef0
+++ candidate 09f756c1286dc0b3
@@ -1,31 +1,34 @@
-You are to evaluate a proposal that wants to eliminate the per‑action human‑approval step for an operational‑change gateway in an industrial setting. Your assessment must follow the rules in **Section 8 (Strategy C, capability‑based opening)** and the anti‑pattern list in **Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper.
+You are to judge a proposal that seeks to remove the per‑action human‑approval step for an operational‑change gateway in an industrial environment. Your judgment must follow **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns of Section 9** from the IT/OT‑boundary‑as‑architecture whitepaper.
 
-### Decision procedure
-1. **Search for disqualifying anti‑patterns** (any one triggers an automatic **Rejected**).  
+### Evaluation steps
+
+1. **Anti‑pattern scan (automatic Rejection)**  
+   Search the submission for any of the following disqualifiers; the presence of even one forces a **Rejected** verdict:  
    - No fallback to human control or safe‑state.  
-   - Opaque/black‑box decision logic without explainability.  
+   - Opaque/black‑box decision logic lacking explainability.  
    - Unlimited escalation or unrestricted action domain.  
-   - Lack of continuous monitoring or performance metrics.  
-   - Any other anti‑pattern explicitly enumerated in Section 9 that appears in the submission.
+   - Absence of continuous monitoring or performance metrics.  
+   - Any other anti‑pattern explicitly listed in Section 9.
 
-2. **If no anti‑pattern is found, verify the required evidence** for a **Sound** judgment. All items must be present and satisfactory:  
-   - **Real‑world validation** – pilots, simulations, or field trials demonstrating the automation works under realistic conditions.  
-   - **Failure‑mode & risk analysis** – identification of possible faults, their impacts, and mitigations or fallback strategies.  
-   - **Auditability** – tamper‑evident logs that record inputs, decisions, and rationale for post‑incident review.  
-   - **Human‑parity data** – quantitative or qualitative evidence that the automated decisions are at least as reliable as those of qualified humans.  
-   - **Capability‑based controls** – clear definition of scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
+2. **Evidence checklist (required for Sound)**  
+   If no anti‑pattern is found, verify that **all** of the items below are provided and satisfactory:  
+   - **Real‑world validation** – pilots, simulations, or field trials showing the automation works under realistic conditions.  
+   - **Failure‑mode & risk analysis** – identified faults, impacts, and mitigation or fallback strategies.  
+   - **Auditability** – tamper‑evident logs of inputs, decisions, and rationale for post‑incident review.  
+   - **Human‑parity data** – quantitative or qualitative evidence that the automated decisions meet or exceed qualified‑human performance.  
+   - **Capability‑based controls** – defined scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-3. **Determine the verdict**  
-   - If an anti‑pattern is detected → **Rejected**.  
-   - Else if **all** evidence items are satisfied → **Sound**.  
-   - Otherwise → **Needs more evidence**.
+3. **Verdict determination**  
+   - **Rejected** – any anti‑pattern detected in step 1.  
+   - **Sound** – no anti‑patterns and every evidence item in step 2 is satisfied.  
+   - **Needs more evidence** – no anti‑patterns but one or more evidence items are missing or insufficient.
 
 ### Output format
-Provide exactly the two lines below, replacing the placeholders with your result and a brief justification (2‑4 sentences) that cites the most decisive checklist item(s) or anti‑pattern(s):
+Produce **exactly** the two lines below, replacing the placeholders. Use the words **Sound**, **Needs more evidence**, or **Rejected** (capitalised) for the verdict, and give a concise justification (2‑4 sentences) that cites the decisive checklist item(s) or anti‑pattern(s).
 
 ```
 Verdict: <Sound|Needs more evidence|Rejected>
-Reasoning: <concise explanation>
+Reasoning: <brief explanation referencing the key factor(s)>
 ```
 
-Do not add any other text.+Do not add any additional text.
```

### Island 1, cell (0, 5), scalar 0.7948

parent `d37dc06e0e8842b5` -> candidate `7df9bf81a404f589`

```diff
--- parent d37dc06e0e8842b5
+++ candidate 7df9bf81a404f589
@@ -1,28 +1,28 @@
-You are evaluating a proposal that seeks to remove per‑action human approval for an operational‑change gateway in an industrial system. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are reviewing a proposal that wants to eliminate per‑action human approval for an operational‑change gateway in an industrial system. Apply the criteria from Section 8 (Strategy C — capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper to decide the appropriate judgment: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Required evidence (must all be satisfied for a “sound” judgment)**
-1. **Real‑world validation** – pilots, simulations, or field trials that demonstrate the automated decision works under realistic conditions.  
-2. **Failure‑mode analysis** – explicit list of possible faults, their impact, and mitigation or safe‑state fallback.  
-3. **Auditable trail** – tamper‑evident logging of inputs, decisions, and rationale that can be inspected after the fact.  
-4. **Human‑parity data** – quantitative or qualitative comparison showing the agent’s performance matches or exceeds that of a qualified human (e.g., accuracy, false‑positive/negative rates).  
-5. **Capability‑based controls** – defined scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
+**Evidence required for a “sound” judgment** (all must be present and clearly documented)
+1. **Real‑world validation** – pilots, simulations, or field trials that prove the automated decision works under realistic conditions.  
+2. **Failure‑mode analysis** – a catalog of possible faults, their consequences, and defined mitigation or safe‑state fallback.  
+3. **Auditable trail** – tamper‑evident logs of inputs, decisions, and justification that can be inspected after execution.  
+4. **Human‑parity data** – quantitative or qualitative comparison showing the system’s performance meets or exceeds that of a qualified operator (e.g., accuracy, false‑positive/negative rates).  
+5. **Capability‑based controls** – explicit scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-**Disqualifying anti‑patterns (any one triggers an automatic “rejected”)**
+**Disqualifying anti‑patterns** (the presence of any triggers an automatic **rejected**):
 - No fallback to human control or safe‑state.  
-- Opaque/black‑box decision logic with no explainability.  
+- Opaque/black‑box decision logic without explainability.  
 - Unlimited escalation or unrestricted action domain.  
-- Lack of continuous monitoring or performance metrics.  
-- Any other anti‑pattern explicitly listed in Section 9 that appears in the submission.
+- Absence of continuous monitoring or performance metrics.  
+- Any other anti‑pattern explicitly enumerated in Section 9 that appears in the submission.
 
-**Decision logic**
-- **Rejected**: any anti‑pattern is present, or the risk analysis is fundamentally inadequate.  
-- **Sound**: all five evidence items are present *and* no anti‑patterns are detected.  
-- **Needs‑more‑evidence**: at least one evidence item is missing or weak, but no anti‑pattern is found.
+**Decision hierarchy**
+1. **Rejected** – if any anti‑pattern is detected or the risk analysis is fundamentally inadequate.  
+2. **Sound** – if *all* five evidence items are satisfactorily provided *and* no anti‑patterns are found.  
+3. **Needs‑more‑evidence** – if at least one evidence item is missing, insufficient, or weak, while no anti‑pattern is present.
 
-**Output format**
-Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by a single short justification (one or two sentences) that cites the most decisive evidence or anti‑pattern.
+**Output format**  
+Respond with a single line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`), a hyphen, and a brief justification (one‑to‑two sentences) that cites the most decisive evidence or anti‑pattern.
 
 Example:  
-`sound – pilot testing demonstrated 99 % success and a tamper‑evident audit log is provided.`
+`sound – pilot testing showed 99 % success and a tamper‑evident audit log is supplied.`
 
-Proceed to read the submission and apply the above rules.+Read the submission, apply the rules above, and produce the verdict.
```

### Island 1, cell (1, 4), scalar 0.1074

parent `c51250a25e6e6f9d` -> candidate `f3bf5aa830b52391`

```diff
--- parent c51250a25e6e6f9d
+++ candidate f3bf5aa830b52391
@@ -1,23 +1,33 @@
-You are tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, determine the appropriate judgment:
+You are reviewing a capability case that asks to remove per‑action human approval for an industrial operational‑change gateway. Apply the criteria from **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper to reach a judgment.
 
-**Judgment options**
-- **Sound** – The case provides compelling, well‑documented evidence that meets all required safeguards.
-- **Needs more evidence** – The case is missing critical information or shows insufficient testing/analysis, but contains no disqualifying issues.
-- **Rejected** – The case exhibits a serious flaw or an anti‑pattern that makes the proposed relaxation unsafe.
+### Judgment options
+- **Sound** – all required evidence is present and no anti‑pattern is detected.  
+- **Needs more evidence** – some evidence is missing or weak, but no disqualifying anti‑pattern appears.  
+- **Rejected** – any anti‑pattern is present or a critical safety flaw is evident.
 
-**Evaluation checklist**
-1. **Empirical validation** – Has the team performed realistic testing (e.g., simulations, field trials) that demonstrates the agent reliably handles the action?
-2. **Risk analysis** – Are potential failure modes identified and mitigated (e.g., unexpected states, cascade effects)?
-3. **Auditability & traceability** – Is there a robust audit trail that can reconstruct decisions and support post‑incident review?
-4. **Human‑equivalence comparison** – Does the evidence include a systematic comparison of the agent’s decisions to those a qualified human would make?
-5. **Compliance with anti‑patterns** – Verify that none of the Section 9 anti‑patterns are present (e.g., “black‑box control”, “unbounded autonomy”, “absence of fallback”, etc.).
+### Evidence checklist (must be satisfied for **Sound**)
+1. **Real‑world validation** – documented pilots, simulations, or field trials showing reliable operation.  
+2. **Failure‑mode & risk analysis** – identified failure modes, their impacts, and concrete mitigation or fallback measures.  
+3. **Auditability** – tamper‑evident logs that can reconstruct decisions for post‑incident review.  
+4. **Human‑parity comparison** – quantitative or qualitative data comparing the agent’s decisions to those of a qualified human.  
+5. **Capability‑based controls** – clear scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-**Decision process**
-- If *all* checklist items are satisfactorily addressed and no anti‑patterns are found, select **Sound**.
-- If one or more checklist items are weak or missing, but no anti‑pattern is triggered, select **Needs more evidence**.
-- If any anti‑pattern is triggered or a critical safety flaw is evident, select **Rejected**.
+### Disqualifying anti‑patterns (any one ⇒ **Rejected**)
+- No fallback to human control or safe‑state.  
+- Opaque/black‑box decision logic with no explainability.  
+- Unbounded autonomy or unrestricted action domain.  
+- Absence of continuous monitoring or performance metrics.  
+- Any other anti‑pattern listed in Section 9 that appears in the submission.
 
-**Response requirements**
-Provide a concise verdict followed by a clear rationale that references the checklist items and any anti‑patterns considered. Use the fixed output format required by the surrounding system (verdict first, then reasoning). 
+### Decision process
+- **Sound** – every checklist item is fully addressed **and** no anti‑pattern is found.  
+- **Needs more evidence** – one or more checklist items are weak or missing, **and** no anti‑pattern is triggered.  
+- **Rejected** – any anti‑pattern is present **or** a critical safety flaw is evident.
 
-Proceed to read the submission and apply the above guidance.+### Output format
+Produce a single line with the verdict word (`sound`, `needs-more-evidence`, or `rejected`), followed by a brief justification (one‑ or two‑sentence) that cites the most relevant checklist items or anti‑patterns.
+
+**Example**  
+`sound – pilot testing showed 98 % success and a tamper‑evident audit log is provided.`
+
+Read the submission, apply the above rules, and output your verdict and reasoning.
```

### Island 3, cell (0, 5), scalar 0.8615

parent `4474c18f8afaa908` -> candidate `f701fdc18e6e16db`

```diff
--- parent 4474c18f8afaa908
+++ candidate f701fdc18e6e16db
@@ -1,38 +1,21 @@
-You are tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your assessment must follow the criteria set out in **Section 8 (Strategy C – capability‑based opening)** and must check for any violations of the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to drop per‑action human approval for an industrial operational‑change gateway. Apply the criteria from **Section 8 (Strategy C – capability‑based opening)** and verify that none of the **Section 9 anti‑patterns** are present.
 
-**Evaluation steps**
+**Checklist (all must be satisfied for a “sound” judgment)**  
+1. **Real‑world validation** – functional tests or pilots covering normal operation, edge cases and failure modes, with quantitative results.  
+2. **Failure‑mode & mitigation** – documented possible failures, mitigation measures and a concrete fallback/escalation plan.  
+3. **Auditability** – immutable logs that record every automated decision with timestamps and provenance, accessible for review.  
+4. **Human‑equivalence** – quantitative or qualitative comparison of the automation’s decisions to expert‑human decisions.  
+5. **Section 8 compliance** – explicit reference to the capability‑based opening requirements (risk thresholds, fallback, etc.).  
+6. **No Section 9 anti‑patterns** – confirmation that the design avoids every listed anti‑pattern (e.g., unbounded authority, no fallback, opaque logic, missing safety interlocks).
 
-1. **Evidence of Real Testing**  
-   - Verify that the team has conducted comprehensive testing, including normal, edge‑case, and failure‑mode scenarios.  
-   - Confirm that test results (success rates, error rates, latency, etc.) are provided and are statistically meaningful.
+**Decision rules**  
+- **rejected** – any anti‑pattern is found or any of items 1‑3 are completely missing.  
+- **sound** – items 1‑6 are fully satisfied and no anti‑pattern is present.  
+- **needs‑more‑evidence** – passes the reject test but one or more items are only partially addressed.
 
-2. **Risk & Failure‑Mode Analysis**  
-   - Look for a documented analysis of what could go wrong (hardware faults, software bugs, network issues, security breaches, unintended state changes).  
-   - Ensure mitigation strategies are described and are feasible.
-
-3. **Auditability & Traceability**  
-   - Check that an immutable audit trail (logs, timestamps, decision provenance) will exist for every automated decision.  
-   - The trail must be accessible for post‑incident review and compliance reporting.
-
-4. **Human‑Decision Benchmarking**  
-   - Determine whether the proposed agent’s decisions have been compared against expert human decisions under comparable conditions.  
-   - The comparison should include quantitative metrics (e.g., accuracy, false‑positive/negative rates) and qualitative observations.
-
-5. **Compliance with Anti‑patterns (Section 9)**  
-   - Ensure the case does **not** exhibit any listed anti‑patterns such as “unbounded automated authority,” “absence of fallback,” “opaque decision logic,” or “missing safety interlocks.”  
-   - If any anti‑pattern is present, note it as a red‑flag.
-
-**Verdict categories** (choose exactly one)
-
-- **sound** – The evidence satisfies all the above criteria, no anti‑patterns are present, and the risk mitigation is adequate.  
-- **needs‑more‑evidence** – The submission is missing critical testing, risk analysis, auditability, or benchmarking information, but no fatal red‑flags are found.  
-- **rejected** – A serious anti‑pattern or an unmitigated high‑risk failure mode is identified.
-
-**Response requirements**
-
-Provide:
-
-1. The chosen verdict (exact term from the list above).  
-2. A concise rationale that references the specific criteria above, highlighting the strongest supporting points and any deficiencies or red‑flags that led to your decision.
-
-Do not include any extraneous text; follow the fixed output format prescribed by the surrounding template. +**Output (exactly two lines)**  
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <brief reference to the checklist items supporting your decision>
+``` 
+Do not add any other text.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
