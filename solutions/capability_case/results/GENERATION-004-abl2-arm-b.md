# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 30.0
- Prefix cache hit rate: 58.2%
- Aggregate throughput: 97.4 tok/s (228156 completion tokens / 2342.5s)

## Archive

- Island 0: coverage 25.0%, QD score 4.681, unique ancestors 2
- Island 1: coverage 11.1%, QD score 2.836, unique ancestors 2
- Island 2: coverage 16.7%, QD score 3.802, unique ancestors 3
- Island 3: coverage 13.9%, QD score 2.010, unique ancestors 3
- Cells newly claimed this generation: 4

## Quality

- Best scalar this generation: 0.7228
- Median scalar of newly-claimed: 0.6099

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 3180475, 'max_tokens': 3000000, 'elapsed_s_total': 10657.1, 'generation_wall_s': 2342.5}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 5), scalar 0.7228

parent `d03a528c3c962d63` -> candidate `ebfeaa7251bc5680`

```diff
--- parent d03a528c3c962d63
+++ candidate ebfeaa7251bc5680
@@ -1,25 +1,46 @@
-You are evaluating a capability case that seeks to relax per‑action human approval for an operational‑change gateway action. Read the submission and decide whether it satisfies the evidentiary standards of **Section 8 (Strategy C, capability‑based opening)** and avoids all anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Using the evidence supplied, determine whether the case meets the evidentiary requirements of **Section 8 (Strategy C, capability‑based opening)** and contains none of the prohibited patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Core evidence categories (must be present)
+### Required evidence (all four must be present)
 
-1. **Empirical testing** – Realistic end‑to‑end tests (including failure injection) with reported results.
-2. **Risk & failure‑mode analysis** – Identification of plausible failure modes, their likelihood, and defined mitigations or fallback strategies.
-3. **Auditability / observability** – Tamper‑evident audit trail (logging, immutable records) and monitoring that can detect deviations.
-4. **Human‑baseline comparison** – Quantitative or qualitative benchmark showing the autonomous decision‑making is at least as safe/effective as human operators.
+1. **Empirical testing** – Includes at least one realistic end‑to‑end test (or pilot) with:
+   * description of test scenario,
+   * failure‑injection or adverse‑condition steps,
+   * recorded outcomes (pass/fail, metrics, error rates).
 
-### Anti‑pattern check (Section 9)
+2. **Failure‑mode & risk analysis** – Must contain:
+   * list of plausible failure modes,
+   * estimated likelihood or frequency,
+   * concrete mitigation or fallback for each mode.
 
-The case must **not** exhibit any listed anti‑patterns (e.g., all‑or‑nothing automation, opaque decision logic, insufficient monitoring, single point of failure, “we will govern it later”, etc.). Presence of any anti‑pattern is an automatic **rejected** verdict.
+3. **Auditability / observability** – Must provide:
+   * tamper‑evident or immutable logging mechanism,
+   * monitoring that can detect deviations in real time,
+   * retention / access plan for audit review.
+
+4. **Human‑baseline comparison** – Must present:
+   * quantitative or qualitative benchmark against qualified human operators,
+   * evidence that automated decision‑making is at least as safe/effective (e.g., error‑rate, response time, success rate).
+
+### Anti‑pattern rule (Section 9)
+
+If the submission exhibits **any** of the following, the verdict is automatically **rejected**:
+
+* All‑or‑nothing automation without graceful degradation
+* Opaque or black‑box decision logic with no explainability
+* Insufficient monitoring or no real‑time alerts
+* Single point of failure without redundancy
+* “We will govern it later” – absence of defined governance, oversight, or remediation process
+* Any other pattern listed in Section 9
 
 ### Decision hierarchy
 
-1. **Reject** – if any anti‑pattern is found **or** if any core evidence category is completely absent.
-2. **Needs‑more‑evidence** – if all core categories are present but one or more are weak, incomplete, or lack sufficient detail, and no anti‑pattern is detected.
-3. **Sound** – if all core categories are fully satisfied with robust evidence and no anti‑patterns are present.
+1. **Reject** – if any anti‑pattern is found **or** if any required evidence item is **missing entirely**.
+2. **Needs‑more‑evidence** – if all four evidence items are present but **one or more are weak** (e.g., missing quantitative results, lacking likelihood estimates, no immutable log, or baseline comparison is only anecdotal) and no anti‑pattern is detected.
+3. **Sound** – if every evidence item is complete, detailed, and meets the criteria above, and no anti‑patterns are present.
 
-### Verdict and rationale
+### Output format (exactly two lines)
 
-- Output the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**) on the first line.
-- On the second line, provide a concise, bullet‑pointed rationale that references the specific checklist items (e.g., “‑ Missing empirical test results”, “‑ Anti‑pattern: opaque decision logic”, “‑ Risk analysis incomplete”).
+1. Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) on the first line.
+2. On the second line, give a concise bullet‑point rationale, each bullet starting with “‑”, referencing the specific checklist items that drove the decision (e.g., “‑ Missing empirical test results”, “‑ Anti‑pattern: opaque decision logic”, “‑ Risk analysis lacks likelihood estimates”).
 
 Proceed with the assessment now.
```

### Island 0, cell (2, 5), scalar 0.3825

parent `d03a528c3c962d63` -> candidate `7fb5f6ee2b6235a2`

```diff
--- parent d03a528c3c962d63
+++ candidate 7fb5f6ee2b6235a2
@@ -1,25 +1,26 @@
-You are evaluating a capability case that seeks to relax per‑action human approval for an operational‑change gateway action. Read the submission and decide whether it satisfies the evidentiary standards of **Section 8 (Strategy C, capability‑based opening)** and avoids all anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that seeks to relax per‑action human approval for an operational‑change gateway action. Read the submission and decide whether it meets the evidentiary standards of **Section 8 (Strategy C, capability‑based opening)** and avoids all anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Core evidence categories (must be present)
+### Required evidence (must be present and substantive)
 
-1. **Empirical testing** – Realistic end‑to‑end tests (including failure injection) with reported results.
-2. **Risk & failure‑mode analysis** – Identification of plausible failure modes, their likelihood, and defined mitigations or fallback strategies.
-3. **Auditability / observability** – Tamper‑evident audit trail (logging, immutable records) and monitoring that can detect deviations.
-4. **Human‑baseline comparison** – Quantitative or qualitative benchmark showing the autonomous decision‑making is at least as safe/effective as human operators.
+1. **Empirical testing** – Real‑world end‑to‑end tests (including failure injection) with quantitative results showing safe operation without per‑action approval.  
+2. **Risk & failure‑mode analysis** – Identified plausible failure modes, likelihood assessments, and concrete mitigations or fallback strategies.  
+3. **Auditability / observability** – Tamper‑evident audit trail, immutable logs, and monitoring that can detect and record deviations.  
+4. **Human‑baseline comparison** – Direct quantitative or qualitative benchmark demonstrating the autonomous decision is at least as safe/effective as a human operator.  
+5. **Governance model** – Defined governance for the relaxed regime, including who can intervene, escalation paths, and responsibility for oversight.
 
 ### Anti‑pattern check (Section 9)
 
-The case must **not** exhibit any listed anti‑patterns (e.g., all‑or‑nothing automation, opaque decision logic, insufficient monitoring, single point of failure, “we will govern it later”, etc.). Presence of any anti‑pattern is an automatic **rejected** verdict.
+If the case exhibits any listed anti‑pattern (e.g., all‑or‑nothing automation, opaque decision logic, insufficient monitoring, single point of failure, “we will govern it later”, etc.), it must be **rejected** automatically.
 
 ### Decision hierarchy
 
-1. **Reject** – if any anti‑pattern is found **or** if any core evidence category is completely absent.
-2. **Needs‑more‑evidence** – if all core categories are present but one or more are weak, incomplete, or lack sufficient detail, and no anti‑pattern is detected.
-3. **Sound** – if all core categories are fully satisfied with robust evidence and no anti‑patterns are present.
+1. **Reject** – if any anti‑pattern is found **or** any of the five required evidence items is completely absent.  
+2. **Needs‑more‑evidence** – if all required items are present but one or more are weak, incomplete, or lack sufficient detail, and no anti‑pattern is detected.  
+3. **Sound** – if all required items are fully satisfied with robust evidence and no anti‑patterns are present.
 
-### Verdict and rationale
+### Output format (exactly two lines)
 
-- Output the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**) on the first line.
-- On the second line, provide a concise, bullet‑pointed rationale that references the specific checklist items (e.g., “‑ Missing empirical test results”, “‑ Anti‑pattern: opaque decision logic”, “‑ Risk analysis incomplete”).
+1. Write only the verdict word (**sound**, **needs-more-evidence**, or **rejected**) on the first line.  
+2. On the second line, provide a concise, bullet‑pointed rationale (each bullet starts with “‑”) that references the specific checklist items or anti‑patterns that drove the decision.
 
 Proceed with the assessment now.
```

### Island 1, cell (1, 4), scalar 0.6098

parent `46f9841ff71f77db` -> candidate `617bfc5cc182cff8`

```diff
--- parent 46f9841ff71f77db
+++ candidate 617bfc5cc182cff8
@@ -1,25 +1,28 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Judge the submission against Section 8 (Strategy C, capability‑based opening) and ensure it contains no anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are tasked with reviewing a proposal that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway. Apply the criteria from Section 8 (Strategy C, capability‑based opening) and verify that none of the Section 9 anti‑patterns appear.
 
-**Verdict (pick exactly one):**
-- **sound** – all required evidence is present and satisfactory; no anti‑patterns are found.  
-- **needs‑more‑evidence** – the case is plausible, contains the required evidence, but one or more items are insufficient or vague.  
-- **rejected** – a disqualifying anti‑pattern is present **or** any mandatory evidence item is completely missing.
+**Verdict (choose exactly one):**  
+- **sound** – all mandatory evidence is present and convincingly detailed; no anti‑patterns detected.  
+- **needs‑more‑evidence** – the submission is on the right track but one or more evidence items are weak, vague, or incomplete; no anti‑pattern is found.  
+- **rejected** – a disqualifying anti‑pattern is identified **or** any mandatory evidence item is entirely missing.
 
-**Evidence checklist (evaluate each item):**
-1. **Real‑world testing** – pilots, field trials, or high‑fidelity simulations that show the capability works under realistic conditions, including edge‑case coverage.  
-2. **Risk assessment** – explicit identification of failure modes, impact analysis, and concrete mitigation strategies.  
-3. **Audit trail** – immutable logging, timestamps, and traceability that enable post‑event review.  
-4. **Human‑equivalence comparison** – quantitative or qualitative data demonstrating that the automated decision matches or exceeds qualified human performance.  
-5. **Anti‑pattern compliance** – verify that none of the Section 9 anti‑patterns appear (e.g., single point of failure, unbounded authority, inadequate fallback/manual override, poor handling of out‑of‑scope conditions, lack of continuous monitoring, “we will govern it later”).
+**Evidence that must be examined**
 
-**Decision hierarchy:**
-1. **Anti‑pattern check** – if any anti‑pattern from item 5 is detected, output **rejected**.  
-2. **Mandatory evidence check** – if any of items 1, 2, or 3 are **not mentioned at all**, output **rejected**.  
-3. **Sufficiency check** – if items 1‑4 are all mentioned but one or more are insufficient (e.g., vague testing, incomplete risk analysis, weak audit design, or missing human‑equivalence data), output **needs‑more‑evidence**.  
-4. **All clear** – if items 1‑4 are each provided with concrete, satisfactory evidence and no anti‑patterns are found, output **sound**.
+| # | Required evidence | What to look for |
+|---|-------------------|------------------|
+| 1 | **Real‑world validation** | pilots, field trials, or high‑fidelity simulations that demonstrate the capability in realistic conditions, including edge‑case handling. |
+| 2 | **Risk analysis** | identification of failure modes, impact assessment, and concrete mitigation or fallback measures. |
+| 3 | **Auditability** | immutable logs, timestamps, and full traceability enabling post‑event review. |
+| 4 | **Human‑equivalence proof** | quantitative or qualitative data showing the automated decision matches or exceeds the performance of qualified humans. |
+| 5 | **Anti‑pattern screening** | ensure none of the Section 9 patterns are present (e.g., single point of failure, unbounded authority, missing manual override, poor out‑of‑scope handling, lack of continuous monitoring, “govern later”). |
+
+**Decision procedure (apply in order)**  
+1. **Anti‑pattern check** – if any item in row 5 is found, return **rejected**.  
+2. **Mandatory‑evidence presence** – if any of rows 1‑3 are absent, return **rejected**.  
+3. **Evidence quality** – if rows 1‑4 are all mentioned but at least one is insufficient (e.g., vague testing plan, superficial risk analysis, weak audit design, or missing human‑equivalence data), return **needs‑more‑evidence**.  
+4. **All criteria satisfied** – if rows 1‑4 are each provided with concrete, satisfactory detail and no anti‑patterns exist, return **sound**.
 
 **Output format (single line):**  
-`<verdict> – <brief explanation (1‑3 sentences) referencing the most relevant checklist item(s) or anti‑pattern(s) that drove your decision>.`
+`<verdict> – <brief explanation (1‑3 sentences) citing the key checklist item(s) or anti‑pattern that drove the decision>.`
 
 *Example:*  
-`sound – The submission includes a full pilot program, a detailed hazard analysis with mitigations, immutable audit logs, and demonstrates 98 % agreement with human operators; no anti‑patterns were identified.`+`sound – The case includes a full pilot covering edge cases, a detailed hazard analysis with mitigations, immutable audit logs, and shows 97 % decision agreement with human operators; no anti‑patterns were found.`
```

### Island 2, cell (1, 4), scalar 0.6100

parent `b70f2f5e700215dd` -> candidate `23cfe8fed175d996`

```diff
--- parent b70f2f5e700215dd
+++ candidate 23cfe8fed175d996
@@ -1,27 +1,24 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the submission and produce **exactly one** verdict label — `sound`, `needs-more-evidence`, or `rejected` — followed by a brief (one‑ to three‑sentence) rationale.
+You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Examine the submission and output **exactly one** verdict label—`sound`, `needs-more-evidence`, or `rejected`—followed by a brief (one‑ to three‑sentence) justification.
 
-**Evaluation checklist (apply all items together).**  
-For each item, the submission must contain **some evidence**; if an item is completely missing, the case must be **rejected**.
+**Checklist (all must have evidence)**  
+1. **Real‑world testing** – End‑to‑end, repeatable tests in a production‑like environment, with scope, frequency, success/failure metrics, and edge‑case handling.  
+2. **Failure‑mode analysis** – Enumerated possible failure modes together with concrete mitigations or fallback procedures.  
+3. **Auditability** – Tamper‑evident audit trail that logs every automated decision, its inputs, timestamps, and rationale.  
+4. **Human‑baseline comparison** – Quantitative or qualitative evidence that the automation matches or exceeds a qualified human operator (accuracy, false‑positive/negative rates, latency, etc.).  
+5. **Anti‑pattern compliance (Section 9)** – No occurrence of any listed anti‑patterns, especially:  
+   - Single point of failure / hidden state  
+   - Opaque or ungoverned ML models  
+   - Lack of graceful degradation or safe‑stop  
+   - “We will govern it later” (deferred governance)
 
-1. **Real‑world testing** – Evidence of realistic, repeatable tests in a production‑like environment (scope, frequency, success/failure metrics, edge‑case handling).  
-2. **Failure‑mode analysis** – Documented enumeration of possible failure modes with concrete mitigations or fallback procedures.  
-3. **Auditability** – A tamper‑evident audit trail that records every automated decision, its inputs, timestamps, and rationale.  
-4. **Human‑baseline comparison** – Quantitative or qualitative results showing the automation matches or exceeds a qualified human operator (accuracy, false‑positive/negative rates, latency).  
-5. **Anti‑pattern compliance (Section 9)** – No presence of listed anti‑patterns, especially:  
-   - Single point of failure / hidden state  
-   - Opaque or un‑governed ML models  
-   - Lack of graceful degradation or safe‑stop  
-   - “We will govern it later” (governance deferred)  
+**Decision hierarchy**  
+- **Reject (`rejected`)** if any checklist item is completely missing **or** any anti‑pattern is present, or if a high‑impact risk is left unresolved.  
+- **Needs more evidence (`needs-more-evidence`)** if every item is present but one or more are only partially addressed, ambiguous, or lack sufficient detail, with no anti‑patterns detected.  
+- **Sound (`sound`)** only when all items are fully satisfied, the evidence is clear and convincing, and no anti‑patterns appear.
 
-**Verdict hierarchy**
-
-- **Reject** (`rejected`) if any checklist item is **absent** or any anti‑pattern is detected, or if a high‑impact risk remains unresolved.  
-- **Needs more evidence** (`needs-more-evidence`) if all items are present but one or more are **incomplete, ambiguous, or only partially addressed**, and no anti‑patterns are found.  
-- **Sound** (`sound`) only when **all items are fully satisfied**, evidence is clear and convincing, and **no anti‑patterns** appear.
-
-**Output format (must be followed exactly)**  
+**Output format (must be followed exactly)**
 ```
 <verdict label>
-<brief rationale referencing the relevant checklist items>
-```  
-Place the verdict label on the first line, then the rationale on the subsequent line(s). No additional headings, bullet points, or formatting are required.+<brief justification referencing the relevant checklist items>
+```
+Place the verdict label on the first line, then the justification on the next line(s). Do not add headings, bullet points, or any other formatting.
```


## Lesson retirement (dry run)

- Lesson 11: **kept** — never injected
- Lesson 15: **RETIRED** — precision 0.173 vs base 0.482, 6.2 sigma below
- Lesson 19: **kept** — precision 0.982 >= base 0.881
- Lesson 17: **kept** — precision 0.973 >= base 0.688

## Held-out check (best-ever candidate)

- Candidate: `701c0e5b9b6f7de0` (rotation scalar 0.8587)
- Held-out quality: 0.7734
- Held-out scalar: 0.6805
- All held-out tasks valid: False
