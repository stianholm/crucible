# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 68.6%
- Aggregate throughput: 70.3 tok/s (167703 completion tokens / 2386.7s)

## Archive

- Island 0: coverage 19.4%, QD score 3.521, unique ancestors 5
- Island 1: coverage 13.9%, QD score 2.526, unique ancestors 3
- Island 2: coverage 16.7%, QD score 3.191, unique ancestors 4
- Island 3: coverage 25.0%, QD score 3.666, unique ancestors 5
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.8487
- Median scalar of newly-claimed: 0.6614

## Cost

- Budget: {'generation': 2, 'max_generations': 30, 'tokens_used_total': 1776496, 'max_tokens': 3000000, 'elapsed_s_total': 7430.4, 'generation_wall_s': 2386.7}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 2, cell (1, 4), scalar 0.8487

parent `aad223762f7b4c1c` -> candidate `7f7a0c72df6a411b`

```diff
--- parent aad223762f7b4c1c
+++ candidate 7f7a0c72df6a411b
@@ -1,31 +1,36 @@
-You are assessing a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway action.
 
-**Goal**  
-Determine whether the case satisfies the evidence requirements of Section 8 (Strategy C – capability‑based opening) and avoids every anti‑pattern listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+**Objective**  
+Confirm that the submission fulfills all mandatory evidence requirements of Section 8 (Strategy C – capability‑based opening) and does **not** contain any anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Possible verdicts**  
-- **sound** – All mandatory evidence is present, the case meets every Section 8 criterion, and no anti‑pattern is triggered.  
-- **needs‑more‑evidence** – The case is largely complete but one or more *non‑critical* items are missing or insufficient; the missing evidence could be supplied without changing the overall risk posture.  
-- **rejected** – A critical deficiency is found (e.g., missing mandatory evidence, violation of an anti‑pattern, or an explicit “governance‑later” statement) that makes the relaxation unsafe.
+**Verdict options**  
+- **sound** – every required evidence element is present and complete, and no anti‑pattern applies.  
+- **needs‑more‑evidence** – all required evidence categories are present but at least one is only partially addressed (e.g., test scope is described but results are missing, analysis lacks mitigation details, etc.).  
+- **rejected** – a critical problem is found: any mandatory evidence element is completely absent, an anti‑pattern is triggered, or the case includes a “governance‑later” statement.
 
-**Decision hierarchy**  
+**Evaluation procedure**
 
-1. **Check for disqualifying anti‑patterns** – If any anti‑pattern from Section 9 is present, immediately **reject**.  
-2. **Verify mandatory evidence dimensions** – The following items are *required* for any judgment:  
-   - **Real‑world testing** – Controlled experiments or pilot deployments in a realistic environment, with documented results.  
-   - **Failure‑mode analysis** – Identification, quantification, and mitigation of all plausible adverse outcomes.  
-   - **Audit trail & observability** – Immutable logging that records decisions, inputs, timestamps, and supports post‑action review.  
-   - **Human‑baseline comparison** – Quantitative evidence that the automated decisions are at least as safe and effective as those of a qualified human.  
-   If **any** of these is completely absent, **reject**.  
-3. **Assess completeness of the above** – If the mandatory items exist but some are only partially described (e.g., test scope given but results missing, or failure analysis lacks mitigation), issue **needs‑more‑evidence**.  
-4. **Check for additional safeguards** (optional but strengthen the case): rate‑limiting, anomaly detection, staged rollout, explicit revocation mechanism, segregation of duties, explainable models, etc. Their absence does **not** cause rejection, but may affect confidence.  
-5. **Final verdict** – If steps 1‑3 pass with no missing mandatory evidence and no anti‑patterns, return **sound**.
+1. **Anti‑pattern scan** – Review the case for any of the Section 9 anti‑patterns (e.g., single point of failure without fallback, opaque decision logic, missing rollback, “we will govern it later”, uncontrolled rollout, etc.). If any appear, **reject** immediately.
+
+2. **Check mandatory evidence dimensions** – The following four items must be present at a minimum:
+   - **Real‑world testing** – controlled experiment or pilot in a realistic environment, with documented outcomes.  
+   - **Failure‑mode analysis** – identification, quantification, and mitigation of all plausible adverse outcomes.  
+   - **Audit trail & observability** – immutable logging that captures decisions, inputs, timestamps, and supports post‑action review.  
+   - **Human‑baseline comparison** – quantitative evidence that the automated decisions are at least as safe and effective as those of a qualified human.
+
+   *If any of these four is wholly missing, **reject**.*
+
+3. **Depth assessment** – If the four mandatory items exist but one or more are insufficiently detailed (e.g., test results omitted, mitigation steps vague, audit logs described but not demonstrable, baseline comparison only qualitative), issue **needs‑more‑evidence**.
+
+4. **Optional safeguards** – Note any extra controls (rate‑limiting, anomaly detection, staged rollout, revocation mechanism, segregation of duties, explainable models, etc.). Their absence does **not** affect the verdict, but may be referenced in the justification.
+
+5. **Final verdict** – When steps 1–3 pass with no missing mandatory evidence and no anti‑patterns, return **sound**.
 
 **Output format**  
-Return a single line with the verdict followed by a brief justification that cites the relevant checklist items, e.g.:
+Produce a single line beginning with the verdict word (**sound**, **needs‑more‑evidence**, or **rejected**), followed by a concise justification that cites the relevant checklist items, for example:
 
 ```
-sound – full pilot results (99.8% success), complete failure‑mode analysis with safe‑stop, immutable audit log, 97% match to human decisions; no Section 9 anti‑patterns.
+sound – pilot showed 99.7% success, full failure‑mode analysis with mitigations, immutable audit log, 96% match to human decisions; no Section 9 anti‑patterns.
 ```
 
-Use exactly one of the words **sound**, **needs‑more‑evidence**, or **rejected** as the first token. No extra headings or formatting are allowed. The surrounding system will handle any additional layout.  +Do not add headings, bullet points, or any extra formatting. The surrounding system will handle any additional layout.  
```

### Island 3, cell (0, 4), scalar 0.4741

parent `2027a6889bffc380` -> candidate `95a439433c81c032`

```diff
--- parent 2027a6889bffc380
+++ candidate 95a439433c81c032
@@ -1,27 +1,29 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted material and produce a single verdict—**sound**, **needs-more-evidence**, or **rejected**—followed by a brief rationale.
+You are reviewing a capability case that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Read the supplied material and issue **exactly two lines**:
 
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
+Reasoning: <brief explanation referencing the checklist>
 ```
-Provide only the two lines above; do not add any additional headings or commentary.+
+**Checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns)**  
+1. **Real‑world end‑to‑end testing** – includes edge‑case and failure‑injection runs in a production‑like environment.  
+2. **Failure‑mode analysis** – lists plausible failures, their impact, and concrete mitigation or rollback actions.  
+3. **Immutable audit trail** – records every automated decision, context, timestamps, and any overrides in a tamper‑evident log.  
+4. **Human‑equivalence evidence** – demonstrates that automated decisions are at least as safe/accurate as those made by a qualified human (comparative study, simulation, etc.).  
+5. **Governance & revocation** – defines who can tighten or revoke the relaxation and the process for doing so.  
+6. **Runtime monitoring & alerting** – specifies health‑checks, continuous monitoring, and real‑time alerts for abnormal behavior.
+
+**Disqualifying anti‑patterns (Section 9)** – any of the following mandates a **rejected** verdict:  
+- No real‑world testing (only unit tests).  
+- Missing or superficial failure‑mode analysis.  
+- Absence of an immutable audit log or inability to reconstruct decisions.  
+- Evidence of systematic divergence from human judgment without justification.  
+- No governance/revocation plan (e.g., “we will govern it later”).  
+- No defined monitoring or alerting, or any other listed anti‑pattern.
+
+**Verdict determination**  
+- **sound** – All six checklist items are met to a reasonable standard and no anti‑pattern is present.  
+- **needs-more-evidence** – At least one checklist item is present but incomplete or weak, yet no anti‑pattern is detected.  
+- **rejected** – Any anti‑pattern is found, or a checklist item is completely absent (e.g., no testing, no audit trail, no governance).
+
+Produce only the two required lines; do not add headings, bullet points, or extra commentary.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.108 vs base 0.482, 9.7 sigma below
- Lesson 19: **kept** — precision 0.980 >= base 0.881
- Lesson 17: **kept** — precision 0.983 >= base 0.694
- Lesson 11: **kept** — precision 0.750 vs base 0.929, only 0.8 sigma below
