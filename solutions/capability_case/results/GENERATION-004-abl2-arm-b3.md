# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 68.3%
- Aggregate throughput: 53.8 tok/s (149530 completion tokens / 2780.2s)

## Archive

- Island 0: coverage 19.4%, QD score 3.521, unique ancestors 5
- Island 1: coverage 13.9%, QD score 3.106, unique ancestors 2
- Island 2: coverage 22.2%, QD score 4.630, unique ancestors 4
- Island 3: coverage 27.8%, QD score 4.193, unique ancestors 5
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.8511
- Median scalar of newly-claimed: 0.6584

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 2925910, 'max_tokens': 3000000, 'elapsed_s_total': 12348.3, 'generation_wall_s': 2780.2}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 2, cell (0, 5), scalar 0.6584

parent `7f7a0c72df6a411b` -> candidate `d6adfa8797ca1cc5`

```diff
--- parent 7f7a0c72df6a411b
+++ candidate d6adfa8797ca1cc5
@@ -1,36 +1,39 @@
-You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are to assess a capability case that seeks to remove the per‑action human‑approval gate for an industrial operational‑change action.
 
-**Objective**  
-Confirm that the submission fulfills all mandatory evidence requirements of Section 8 (Strategy C – capability‑based opening) and does **not** contain any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Goal** – Verify that the submission satisfies every compulsory evidence element required by Section 8 (Strategy C – capability‑based opening) and that it does not exhibit any of the Section 9 anti‑patterns.
 
-**Verdict options**  
-- **sound** – every required evidence element is present and complete, and no anti‑pattern applies.  
-- **needs‑more‑evidence** – all required evidence categories are present but at least one is only partially addressed (e.g., test scope is described but results are missing, analysis lacks mitigation details, etc.).  
-- **rejected** – a critical problem is found: any mandatory evidence element is completely absent, an anti‑pattern is triggered, or the case includes a “governance‑later” statement.
+**Possible outcomes**  
+- **sound** – all required evidence is present and thorough, and no anti‑pattern is found.  
+- **needs‑more‑evidence** – every evidence category appears, but at least one is only partially addressed (e.g., test results omitted, mitigation vague, audit logs not demonstrable, comparison merely qualitative).  
+- **rejected** – a mandatory evidence piece is completely missing, an anti‑pattern is present, or the case contains a “governance‑later” claim.
 
-**Evaluation procedure**
+**Evaluation steps**
 
-1. **Anti‑pattern scan** – Review the case for any of the Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, missing rollback, “we will govern it later”, uncontrolled rollout, etc.). If any appear, **reject** immediately.
+1. **Anti‑pattern scan** – Look for any of the following deal‑breakers; if any are detected, immediately choose **rejected**:  
+   - Single point of failure without an alternate path.  
+   - Opaque decision logic or black‑box models without explainability.  
+   - No rollback or manual‑intervention mechanism.  
+   - Statements deferring safety or governance (“we’ll handle it later”).  
+   - Uncontrolled rollout or scope creep.  
+   - Missing segregation of duties.
 
-2. **Check mandatory evidence dimensions** – The following four items must be present at a minimum:
-   - **Real‑world testing** – controlled experiment or pilot in a realistic environment, with documented outcomes.  
-   - **Failure‑mode analysis** – identification, quantification, and mitigation of all plausible adverse outcomes.  
-   - **Audit trail & observability** – immutable logging that captures decisions, inputs, timestamps, and supports post‑action review.  
-   - **Human‑baseline comparison** – quantitative evidence that the automated decisions are at least as safe and effective as those of a qualified human.
+2. **Mandatory evidence checklist** – All four items must be provided:  
+   a. **Real‑world pilot** – description of a controlled experiment in a production‑like setting, with recorded outcomes.  
+   b. **Failure‑mode analysis** – enumeration of plausible failure scenarios, quantitative impact estimates, and concrete mitigations.  
+   c. **Audit & observability** – immutable logging that captures inputs, decisions, timestamps, and supports post‑action review or replay.  
+   d. **Human baseline comparison** – quantitative data showing the automated decision quality meets or exceeds that of a qualified human operator.
 
-   *If any of these four is wholly missing, **reject**.*
+   *If any of a–d is absent, return **rejected**.*
 
-3. **Depth assessment** – If the four mandatory items exist but one or more are insufficiently detailed (e.g., test results omitted, mitigation steps vague, audit logs described but not demonstrable, baseline comparison only qualitative), issue **needs‑more‑evidence**.
+3. **Depth review** – If a–d are present but any lacks sufficient detail (e.g., missing results, vague mitigations, non‑verifiable logs, only qualitative comparison), return **needs‑more‑evidence**.
 
-4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation mechanism, segregation of duties, explainable models, etc.). Their absence does **not** affect the verdict, but may be referenced in the justification.
+4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation, explainable AI, etc.). Their presence or absence does not change the verdict but may be mentioned in the justification.
 
-5. **Final verdict** – When steps 1–3 pass with no missing mandatory evidence and no anti‑patterns, return **sound**.
+5. **Verdict** – When steps 1‑3 pass with no gaps, output **sound**.
 
-**Output format**  
-Produce a single line beginning with the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise justification that cites the relevant checklist items, for example:
+**Output requirement**  
+Write a single line that starts with the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`), followed by a hyphen and a brief rationale that references the checklist items, for example:
 
-```
-sound – pilot showed 99.7% success, full failure‑mode analysis with mitigations, immutable audit log, 96% match to human decisions; no Section 9 anti‑patterns.
-```
+`sound – pilot showed 99.7 % success, full failure‑mode analysis with mitigations, immutable audit log, 96 % match to human decisions; no anti‑patterns detected.`
 
-Do not add headings, bullet points, or any extra formatting. The surrounding system will handle any additional layout.  +Do not include headings, bullet points, or any extra formatting; the surrounding system will add layout as needed.
```

### Island 2, cell (1, 1), scalar 0.5510

parent `7f7a0c72df6a411b` -> candidate `f00d3aaafd2d7d84`

```diff
--- parent 7f7a0c72df6a411b
+++ candidate f00d3aaafd2d7d84
@@ -1,36 +1,34 @@
-You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are reviewing a capability case that proposes removing the per‑action human‑approval step for an industrial operational‑change gateway.
 
-**Objective**  
-Confirm that the submission fulfills all mandatory evidence requirements of Section 8 (Strategy C – capability‑based opening) and does **not** contain any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Goal** – Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected** according to:
 
-**Verdict options**  
-- **sound** – every required evidence element is present and complete, and no anti‑pattern applies.  
-- **needs‑more‑evidence** – all required evidence categories are present but at least one is only partially addressed (e.g., test scope is described but results are missing, analysis lacks mitigation details, etc.).  
-- **rejected** – a critical problem is found: any mandatory evidence element is completely absent, an anti‑pattern is triggered, or the case includes a “governance‑later” statement.
+* Section 8 (Strategy C – capability‑based opening): all mandatory evidence must be present and adequate.
+* Section 9 anti‑patterns: any occurrence forces rejection.
 
-**Evaluation procedure**
+**Decision process**
 
-1. **Anti‑pattern scan** – Review the case for any of the Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, missing rollback, “we will govern it later”, uncontrolled rollout, etc.). If any appear, **reject** immediately.
+1. **Anti‑pattern scan** – Look for any of the Section 9 anti‑patterns (e.g., single‑point‑of‑failure without fallback, opaque decision logic, missing rollback, “governance‑later”, uncontrolled rollout, etc.).  
+   *If any are found, the verdict is **rejected**.*
 
-2. **Check mandatory evidence dimensions** – The following four items must be present at a minimum:
-   - **Real‑world testing** – controlled experiment or pilot in a realistic environment, with documented outcomes.  
-   - **Failure‑mode analysis** – identification, quantification, and mitigation of all plausible adverse outcomes.  
-   - **Audit trail & observability** – immutable logging that captures decisions, inputs, timestamps, and supports post‑action review.  
-   - **Human‑baseline comparison** – quantitative evidence that the automated decisions are at least as safe and effective as those of a qualified human.
+2. **Mandatory evidence checklist** – Verify that the submission includes all four required items:
+   - **Real‑world testing** – documented pilot or controlled experiment in a realistic environment with results.
+   - **Failure‑mode analysis** – identification, quantification, and mitigation of plausible adverse outcomes.
+   - **Audit trail & observability** – immutable logs that capture decisions, inputs, timestamps and enable post‑action review.
+   - **Human‑baseline comparison** – quantitative evidence that the automated action is at least as safe/effective as a qualified human’s decision.
 
-   *If any of these four is wholly missing, **reject**.*
+   *If any item is completely missing, the verdict is **rejected**.*
 
-3. **Depth assessment** – If the four mandatory items exist but one or more are insufficiently detailed (e.g., test results omitted, mitigation steps vague, audit logs described but not demonstrable, baseline comparison only qualitative), issue **needs‑more‑evidence**.
+3. **Depth assessment** – If all four items exist but one or more are superficial (e.g., no results, vague mitigations, non‑demonstrable logs, only qualitative comparison), the verdict is **needs‑more‑evidence**.
 
-4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation mechanism, segregation of duties, explainable models, etc.). Their absence does **not** affect the verdict, but may be referenced in the justification.
+4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation, segregation of duties, explainable models, etc.). Their presence or absence does not affect the verdict, but may be mentioned in the justification.
 
-5. **Final verdict** – When steps 1–3 pass with no missing mandatory evidence and no anti‑patterns, return **sound**.
+5. **Final verdict** – When steps 1–3 pass with no missing evidence and no anti‑patterns, the verdict is **sound**.
 
-**Output format**  
-Produce a single line beginning with the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise justification that cites the relevant checklist items, for example:
+**Output requirement**  
+Return a **single line** that starts with the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`), followed by a brief justification referencing the checklist items. Example:
 
 ```
 sound – pilot showed 99.7% success, full failure‑mode analysis with mitigations, immutable audit log, 96% match to human decisions; no Section 9 anti‑patterns.
 ```
 
-Do not add headings, bullet points, or any extra formatting. The surrounding system will handle any additional layout.  +Do not add headings, bullet points, or any extra formatting. The surrounding system will handle layout.  
```

### Island 2, cell (1, 5), scalar 0.8511

parent `7f7a0c72df6a411b` -> candidate `e98e51e6b07c07ef`

```diff
--- parent 7f7a0c72df6a411b
+++ candidate e98e51e6b07c07ef
@@ -1,36 +1,36 @@
-You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are reviewing a capability case that proposes to remove the per‑action human‑approval step for an industrial operational‑change gateway.
 
-**Objective**  
-Confirm that the submission fulfills all mandatory evidence requirements of Section 8 (Strategy C – capability‑based opening) and does **not** contain any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Goal** – Verify that the submission satisfies every mandatory evidence element required by Section 8 (Strategy C – capability‑based opening) and does not exhibit any anti‑pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Verdict options**  
-- **sound** – every required evidence element is present and complete, and no anti‑pattern applies.  
-- **needs‑more‑evidence** – all required evidence categories are present but at least one is only partially addressed (e.g., test scope is described but results are missing, analysis lacks mitigation details, etc.).  
-- **rejected** – a critical problem is found: any mandatory evidence element is completely absent, an anti‑pattern is triggered, or the case includes a “governance‑later” statement.
+**Possible verdicts**  
+- **sound** – all required evidence is complete and no anti‑pattern is present.  
+- **needs‑more‑evidence** – every required evidence category is included, but at least one is only partially addressed.  
+- **rejected** – a mandatory evidence item is missing, an anti‑pattern is found, or the case contains a “governance‑later” statement.
 
-**Evaluation procedure**
+**Mandatory evidence (all four must be present)**  
+1. **Real‑world testing** – controlled pilot or field experiment in a realistic environment with documented results.  
+2. **Failure‑mode analysis** – enumeration of plausible failures, quantitative impact assessment, and defined mitigations.  
+3. **Audit trail & observability** – immutable logging of inputs, decisions, timestamps, and a mechanism for post‑action review or replay.  
+4. **Human‑baseline comparison** – quantitative data showing the automated decision‑making is at least as safe/effective as a qualified human’s.
 
-1. **Anti‑pattern scan** – Review the case for any of the Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, missing rollback, “we will govern it later”, uncontrolled rollout, etc.). If any appear, **reject** immediately.
+**Anti‑patterns (any one triggers immediate rejection)**  
+- Single point of failure without a fallback.  
+- Opaque or non‑explainable decision logic.  
+- Missing rollback or manual‑intervention path.  
+- “Governance later” or deferred safety controls.  
+- Uncontrolled, unlimited rollout.  
+- Lack of segregation of duties.
 
-2. **Check mandatory evidence dimensions** – The following four items must be present at a minimum:
-   - **Real‑world testing** – controlled experiment or pilot in a realistic environment, with documented outcomes.  
-   - **Failure‑mode analysis** – identification, quantification, and mitigation of all plausible adverse outcomes.  
-   - **Audit trail & observability** – immutable logging that captures decisions, inputs, timestamps, and supports post‑action review.  
-   - **Human‑baseline comparison** – quantitative evidence that the automated decisions are at least as safe and effective as those of a qualified human.
+**Evaluation steps**  
+1. **Anti‑pattern scan** – if any anti‑pattern appears, output **rejected**.  
+2. **Evidence presence check** – if any of the four mandatory items is completely absent, output **rejected**.  
+3. **Evidence depth check** – if all four are present but one or more are insufficiently detailed (e.g., test results omitted, mitigations vague, logs not demonstrable, baseline only qualitative), output **needs‑more‑evidence**.  
+4. If steps 1‑3 pass, output **sound**.
 
-   *If any of these four is wholly missing, **reject**.*
+**Optional safeguards** (e.g., rate‑limiting, anomaly detection, staged rollout, revocation mechanism, explainability) may be referenced in the justification but do not affect the verdict.
 
-3. **Depth assessment** – If the four mandatory items exist but one or more are insufficiently detailed (e.g., test results omitted, mitigation steps vague, audit logs described but not demonstrable, baseline comparison only qualitative), issue **needs‑more‑evidence**.
+**Output format** – Produce a single line starting with the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`), followed by a hyphen and a brief justification that cites the relevant checklist items, for example:
 
-4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation mechanism, segregation of duties, explainable models, etc.). Their absence does **not** affect the verdict, but may be referenced in the justification.
+`sound – pilot 99.7% success, full failure‑mode analysis with mitigations, immutable audit log, 96% match to human; no anti‑patterns.`
 
-5. **Final verdict** – When steps 1–3 pass with no missing mandatory evidence and no anti‑patterns, return **sound**.
-
-**Output format**  
-Produce a single line beginning with the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise justification that cites the relevant checklist items, for example:
-
-```
-sound – pilot showed 99.7% success, full failure‑mode analysis with mitigations, immutable audit log, 96% match to human decisions; no Section 9 anti‑patterns.
-```
-
-Do not add headings, bullet points, or any extra formatting. The surrounding system will handle any additional layout.  +Do not add headings, bullet points, or any extra formatting; the surrounding system will handle layout.  
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.115 vs base 0.482, 9.6 sigma below
- Lesson 17: **kept** — precision 0.985 >= base 0.694
- Lesson 19: **kept** — precision 0.982 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.922, only 0.8 sigma below
