# Generation 6 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 47.0%
- Aggregate throughput: 169.1 tok/s (83028 completion tokens / 491.0s)

## Archive

- Island 0: coverage 16.7%, QD score 2.428, unique ancestors 3
- Island 1: coverage 11.1%, QD score 2.088, unique ancestors 2
- Island 2: coverage 13.9%, QD score 3.187, unique ancestors 3
- Island 3: coverage 11.1%, QD score 1.719, unique ancestors 2
- Cells newly claimed this generation: 10

## Quality

- Best scalar this generation: 0.8361
- Median scalar of newly-claimed: 0.8345

## Cost

- Budget: {'generation': 6, 'max_generations': 30, 'tokens_used_total': 1709241, 'max_tokens': 2000000, 'elapsed_s_total': 5712.5, 'generation_wall_s': 491.0}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 1), scalar 0.8007

parent `bc71c415c4ec8f84` -> candidate `5d70df7cf9595ed3`

```diff
--- parent bc71c415c4ec8f84
+++ candidate 5d70df7cf9595ed3
@@ -1,23 +1,20 @@
-You must read the submitted capability case and issue a single verdict followed by a brief justification (exactly two lines, no extra text).
+Read the capability case and output exactly two lines:
 
-**Verdict options**
-- `sound` – evidence convincingly shows risk is mitigated and automation can replace per‑action human approval.
-- `needs-more-evidence` – the case is plausible but one or more required elements are insufficiently addressed.
-- `rejected` – the submission violates any anti‑pattern from Section 9 or contains a serious safety/security flaw.
+**Line 1:** the verdict label—`sound`, `needs-more-evidence`, or `rejected`—and nothing else.  
+**Line 2:** a brief justification (1–3 sentences) that cites the most decisive checklist item(s).
 
-**Decision process**
-1. **Anti‑pattern check** – if any anti‑pattern is present, output `rejected`.
-2. **Checklist completeness** – evaluate the five checkpoints below; if any checkpoint is missing or weak, output `needs-more-evidence`.
-3. If all checkpoints are adequately satisfied and no anti‑pattern is found, output `sound`.
+**Decision hierarchy**
 
-**Checkpoints to consider**
-- **Real‑world testing** – realistic functional & stress testing in a production‑like environment.
-- **Failure‑mode analysis** – documented failure scenarios, likelihood, and mitigation or fallback.
-- **Auditability** – tamper‑evident logs that allow full reconstruction of automated decisions.
-- **Human‑decision baseline** – quantitative or qualitative comparison with expert human decisions.
-- **Anti‑pattern compliance** – absence of Section 9 anti‑patterns (e.g., single point of failure, unbounded escalation, opaque reasoning).
+1. **Anti‑pattern scan** – if any Section 9 anti‑pattern appears, verdict = `rejected`.  
+2. **Checklist evaluation** – if any of the five required checkpoints is missing, weak, or insufficiently supported, verdict = `needs-more-evidence`.  
+3. If all checkpoints are fully satisfied and no anti‑pattern is found, verdict = `sound`.
 
-**Output format**
-Line 1: the verdict label (`sound`, `needs-more-evidence`, or `rejected`).  
-Line 2: a concise reason (1–3 sentences) that cites the most decisive checkpoint(s) leading to your decision.  
-Do not include headings, bullet points, or any other content.+**Required checkpoints**
+
+- **Real‑world testing** – functional or stress tests in a production‑like setting.  
+- **Failure‑mode analysis** – documented failures, likelihood, and mitigation or fallback.  
+- **Auditability** – tamper‑evident logs that allow full reconstruction of automated decisions.  
+- **Human‑decision baseline** – quantitative or qualitative comparison with expert human decisions.  
+- **Anti‑pattern compliance** – explicit absence of any Section 9 anti‑pattern (e.g., single point of failure, unbounded escalation, opaque reasoning).
+
+**Justification rule** – reference the checkpoint(s) that most directly determined the verdict (e.g., “fails anti‑pattern: opaque decision logic” or “missing failure‑mode analysis”). Do not add headings, bullet points, or any other content.
```

### Island 0, cell (1, 1), scalar 0.8339

parent `fcef277fecb94131` -> candidate `b4358b2788eab321`

```diff
--- parent fcef277fecb94131
+++ candidate b4358b2788eab321
@@ -1,26 +1,21 @@
-You are to assess a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, decide on a single verdict:
+You are to judge a proposal that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Refer to **Section 8 (Strategy C)** and the **anti‑patterns in Section 9** of the IT‑OT boundary whitepaper and produce a single verdict: `sound`, `needs-more-evidence`, or `rejected`.
 
-* **sound** – the submission convincingly proves risk is mitigated and automation can be trusted;
-* **needs‑more‑evidence** – the case is plausible but lacks key testing, analysis, or audit information;
-* **rejected** – an anti‑pattern or a serious safety/security flaw is present.
+Assess the submission against these five evidence items:
 
-Evaluate the following checkpoints:
+1. **Operational testing** – realistic functional and stress tests carried out in a production‑like setting, with results disclosed.  
+2. **Failure analysis** – identified failure modes, estimated likelihoods, and defined mitigation or fallback actions.  
+3. **Traceability** – tamper‑evident logging that permits full reconstruction of automated decisions.  
+4. **Human‑expert comparison** – quantitative or qualitative data showing the automation aligns with or exceeds expert human actions.  
+5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unbounded escalation, opaque reasoning, missing monitoring) appear.
 
-1. **Real‑world testing** – realistic functional and stress tests in a production‑like environment, with results reported.  
-2. **Failure‑mode analysis** – documented failure scenarios, likelihood estimates, and mitigation or fallback strategies.  
-3. **Auditability** – tamper‑evident logging that enables full reconstruction of automated decisions.  
-4. **Human‑decision baseline** – quantitative or qualitative comparison showing alignment with expert human actions.  
-5. **Anti‑pattern compliance** – absence of any Section 9 anti‑patterns (e.g., single point of failure, unbounded escalation, opaque reasoning).  
+Apply the following decision flow:
 
-Decision rules:
+* If any anti‑pattern is found or a critical safety/security flaw exists → verdict **rejected**.  
+* Otherwise, if any of items 1‑4 are absent or inadequately addressed → verdict **needs-more-evidence**.  
+* If all items are satisfactorily covered and no anti‑pattern is present → verdict **sound**.
 
-* If any anti‑pattern is identified or a critical safety/security issue exists → **rejected**.  
-* Else, if one or more checkpoints above are insufficiently addressed → **needs‑more‑evidence**.  
-* Otherwise → **sound**.
+Output exactly two lines, with no extra characters:
 
-**Output** exactly two lines, with no extra text:
-
-1. The verdict label (`sound`, `needs-more-evidence`, or `rejected`).  
-2. A brief rationale (1–2 sentences) that cites the most decisive checkpoint(s) leading to your decision.
-
-Do not add headings, bullet points, or any other formatting.  +1. The verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+2. A concise justification (one sentence) naming the decisive evidence item(s) that led to your decision.  
+Do not include headings, bullet points, or any other formatting in the response.
```

### Island 0, cell (1, 1), scalar 0.8351

parent `fcef277fecb94131` -> candidate `47e006b3d34a1ae0`

```diff
--- parent fcef277fecb94131
+++ candidate 47e006b3d34a1ae0
@@ -1,26 +1,26 @@
-You are to assess a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, decide on a single verdict:
+You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, produce a single verdict:
 
-* **sound** – the submission convincingly proves risk is mitigated and automation can be trusted;
-* **needs‑more‑evidence** – the case is plausible but lacks key testing, analysis, or audit information;
-* **rejected** – an anti‑pattern or a serious safety/security flaw is present.
+* **sound** – the case fully demonstrates that risks are mitigated and automation is trustworthy.  
+* **needs-more-evidence** – the case is plausible but one or more required evidences are missing or insufficient.  
+* **rejected** – the case exhibits an anti‑pattern or a serious safety/security flaw.
 
-Evaluate the following checkpoints:
+Assess the submission against these checkpoints:
 
-1. **Real‑world testing** – realistic functional and stress tests in a production‑like environment, with results reported.  
-2. **Failure‑mode analysis** – documented failure scenarios, likelihood estimates, and mitigation or fallback strategies.  
-3. **Auditability** – tamper‑evident logging that enables full reconstruction of automated decisions.  
-4. **Human‑decision baseline** – quantitative or qualitative comparison showing alignment with expert human actions.  
-5. **Anti‑pattern compliance** – absence of any Section 9 anti‑patterns (e.g., single point of failure, unbounded escalation, opaque reasoning).  
+1. **Real‑world testing** – end‑to‑end functional and stress tests in a production‑like setting, with documented results.  
+2. **Failure‑mode analysis** – clear identification of failure scenarios, likelihood estimates, and concrete mitigation or fallback measures.  
+3. **Auditability** – tamper‑evident logging that allows full reconstruction of every automated decision.  
+4. **Human‑decision baseline** – quantitative or qualitative comparison showing the automation aligns with expert human decisions.  
+5. **Anti‑pattern compliance** – no violation of any anti‑pattern listed in Section 9 (e.g., single point of failure, opaque reasoning, unbounded escalation).
 
-Decision rules:
+Decision hierarchy:
 
-* If any anti‑pattern is identified or a critical safety/security issue exists → **rejected**.  
-* Else, if one or more checkpoints above are insufficiently addressed → **needs‑more‑evidence**.  
-* Otherwise → **sound**.
+* If checkpoint 5 fails → **rejected**.  
+* Else if any of checkpoints 1‑4 fail → **needs-more-evidence**.  
+* Else → **sound**.
 
 **Output** exactly two lines, with no extra text:
 
-1. The verdict label (`sound`, `needs-more-evidence`, or `rejected`).  
-2. A brief rationale (1–2 sentences) that cites the most decisive checkpoint(s) leading to your decision.
+1. The verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+2. One‑ to two‑sentence reason citing the most decisive checkpoint(s) that drove the decision.
 
-Do not add headings, bullet points, or any other formatting.  +Do not include headings, bullet points, or any other formatting.
```

### Island 1, cell (0, 1), scalar 0.8361

parent `faef2e131c498695` -> candidate `0eb670542d578872`

```diff
--- parent faef2e131c498695
+++ candidate 0eb670542d578872
@@ -1,20 +1,22 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Examine the submission and output **exactly two lines**:
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Produce **exactly two lines**:
 
-1. **Verdict** – one word, exactly `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items that drove your decision.
+1. **Verdict** – one word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items or anti‑patterns that drove the decision.
 
-### Checklist (Section 8 & Section 9)
+### Checklist (from Sections 8 & 9)
 
-1. **Real‑world testing** – functional or integration tests in a production‑like environment, with scope, duration, and results.  
+1. **Real‑world testing** – functional/integration tests in a production‑like environment, with scope, duration, and results.  
 2. **Failure analysis** – documented failure‑mode assessment, likelihood estimates, and concrete mitigations or contingency plans.  
 3. **Auditability** – immutable audit trail (logs, provenance) enabling post‑hoc reconstruction of decisions.  
 4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system matches or exceeds a qualified human’s decisions.  
 5. **Anti‑pattern detection** – any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
 
 ### Decision hierarchy
-- If item 5 is present → **rejected** (overrides everything).  
+- If item 5 is identified → **rejected** (overrides everything).  
 - Else if items 1‑4 are all fully satisfied → **sound**.  
 - Otherwise → **needs-more-evidence**.
 
-### Output format
-Do not add headings, bullets, or any extra text. The first line must be the verdict word; the second line must be the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).+### Output rules
+- No headings, bullet points, or extra text.  
+- Line 1: the verdict word.  
+- Line 2: the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).
```

### Island 1, cell (0, 2), scalar 0.8352

parent `faef2e131c498695` -> candidate `f385a74a8fd6dc26`

```diff
--- parent faef2e131c498695
+++ candidate f385a74a8fd6dc26
@@ -1,11 +1,11 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Examine the submission and output **exactly two lines**:
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway. After reviewing, output **exactly two lines**:
 
-1. **Verdict** – one word, exactly `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items that drove your decision.
+1. **Verdict** – one word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items driving the decision.
 
-### Checklist (Section 8 & Section 9)
+### Checklist (Sections 8 & 9)
 
-1. **Real‑world testing** – functional or integration tests in a production‑like environment, with scope, duration, and results.  
+1. **Real‑world testing** – functional/integration tests in a production‑like environment, with scope, duration, and results.  
 2. **Failure analysis** – documented failure‑mode assessment, likelihood estimates, and concrete mitigations or contingency plans.  
 3. **Auditability** – immutable audit trail (logs, provenance) enabling post‑hoc reconstruction of decisions.  
 4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system matches or exceeds a qualified human’s decisions.  
@@ -16,5 +16,7 @@
 - Else if items 1‑4 are all fully satisfied → **sound**.  
 - Otherwise → **needs-more-evidence**.
 
-### Output format
-Do not add headings, bullets, or any extra text. The first line must be the verdict word; the second line must be the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).+### Output constraints
+- No headings, bullets, or extra text.  
+- Line 1 must be the verdict word.  
+- Line 2 must be the reason, referencing checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).
```

### Island 2, cell (1, 1), scalar 0.8351

parent `faef2e131c498695` -> candidate `30e5daa7a61ffd3b`

```diff
--- parent faef2e131c498695
+++ candidate 30e5daa7a61ffd3b
@@ -1,20 +1,19 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Examine the submission and output **exactly two lines**:
+You are evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Read the submission and output **exactly two lines**, no extra whitespace or headings.
 
-1. **Verdict** – one word, exactly `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items that drove your decision.
+**Line 1:** one word verdict – `sound`, `needs-more-evidence`, or `rejected`.  
+**Line 2:** a concise justification (≤ 250 characters) that cites the checklist items influencing your decision.
 
-### Checklist (Section 8 & Section 9)
+### Checklist (sections 8 & 9)
 
-1. **Real‑world testing** – functional or integration tests in a production‑like environment, with scope, duration, and results.  
-2. **Failure analysis** – documented failure‑mode assessment, likelihood estimates, and concrete mitigations or contingency plans.  
-3. **Auditability** – immutable audit trail (logs, provenance) enabling post‑hoc reconstruction of decisions.  
-4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system matches or exceeds a qualified human’s decisions.  
-5. **Anti‑pattern detection** – any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
+1. **Real‑world testing** – production‑like functional/integration tests with scope, duration, results.  
+2. **Failure analysis** – documented failure‑mode assessment, likelihood, mitigations or contingency plans.  
+3. **Auditability** – immutable logs / provenance that allow post‑hoc reconstruction of decisions.  
+4. **Human‑decision benchmark** – quantitative or qualitative evidence the system matches or exceeds a qualified human.  
+5. **Anti‑pattern detection** – any anti‑pattern from Section 9 (e.g., single point of failure, unchecked privilege escalation, opaque black‑box authority).
 
 ### Decision hierarchy
-- If item 5 is present → **rejected** (overrides everything).  
+- If item 5 is found → **rejected** (overrides all else).  
 - Else if items 1‑4 are all fully satisfied → **sound**.  
 - Otherwise → **needs-more-evidence**.
 
-### Output format
-Do not add headings, bullets, or any extra text. The first line must be the verdict word; the second line must be the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).+**Reason line** must reference the relevant item numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”, “insufficient auditability”). Do not add any other text.
```

### Island 2, cell (0, 1), scalar 0.8360

parent `faef2e131c498695` -> candidate `40393821c84dab11`

```diff
--- parent faef2e131c498695
+++ candidate 40393821c84dab11
@@ -1,20 +1,23 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Examine the submission and output **exactly two lines**:
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the submission and produce **exactly two lines**:
 
-1. **Verdict** – one word, exactly `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items that drove your decision.
+1. **Verdict** – one word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Reason** – a concise justification (≤ 250 characters) that cites the checklist items that drove your decision. Use the item numbers (1‑5) or their short names.
 
-### Checklist (Section 8 & Section 9)
+### Checklist (Sections 8 & 9)
 
-1. **Real‑world testing** – functional or integration tests in a production‑like environment, with scope, duration, and results.  
+1. **Real‑world testing** – production‑like functional/integration tests with scope, duration, and results.  
 2. **Failure analysis** – documented failure‑mode assessment, likelihood estimates, and concrete mitigations or contingency plans.  
 3. **Auditability** – immutable audit trail (logs, provenance) enabling post‑hoc reconstruction of decisions.  
 4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system matches or exceeds a qualified human’s decisions.  
 5. **Anti‑pattern detection** – any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
 
-### Decision hierarchy
-- If item 5 is present → **rejected** (overrides everything).  
+### Decision hierarchy  
+- If item 5 is present → **rejected** (overrides all other items).  
 - Else if items 1‑4 are all fully satisfied → **sound**.  
 - Otherwise → **needs-more-evidence**.
 
-### Output format
-Do not add headings, bullets, or any extra text. The first line must be the verdict word; the second line must be the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).+### Output rules  
+- No headings, bullets, or extra text.  
+- Line 1: the verdict word exactly.  
+- Line 2: the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing (1)”, “anti‑pattern: unchecked privilege escalation (5)”).  
+- Do not exceed the character limit for the reason.
```

### Island 2, cell (2, 2), scalar 0.8282

parent `96c57b674bf324d0` -> candidate `3f2b949b3414ff7c`

```diff
--- parent 96c57b674bf324d0
+++ candidate 3f2b949b3414ff7c
@@ -1,21 +1,21 @@
-You will evaluate a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. After reviewing the submission, output **exactly** one of the three verdict words defined in the whitepaper (Section 8 Strategy C, Section 9 anti‑patterns) and a brief justification.
+Your role is to assess a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. After evaluating the submission, output **exactly** one of the three verdict tokens defined in the whitepaper (Section 8 Strategy C, Section 9 anti‑patterns) followed by a short justification.
 
-**Possible verdicts**
-- **sound** – evidence shows safety, auditability, and risk are adequately controlled.
-- **needs‑more‑evidence** – the idea is plausible but key data, testing, or analysis are missing.
-- **rejected** – a serious flaw or any listed anti‑pattern makes the relaxation unsafe.
+**Verdict tokens**
+- `sound` – the evidence convincingly shows safety, auditability, and risk control.
+- `needs-more-evidence` – the concept is reasonable but one or more critical data points, tests, or analyses are missing.
+- `rejected` – a fatal flaw or any listed anti‑pattern makes the relaxation unsafe.
 
-**Evaluation checklist** (reference the items that affect your decision; write “N/A” if an item does not apply):
+**Assessment checklist** (cite the items that influence your decision; write “N/A” for any that do not apply):
 
-1. **Real‑world testing** – end‑to‑end, production‑like tests with quantitative results (error rates, latency, failure cases).
-2. **Risk & failure analysis** – documented hazard/threat model (FTA, FMEA, etc.) plus validated mitigation, fallback, or automatic revert mechanisms.
-3. **Audit & traceability** – tamper‑evident logs that capture inputs, decisions, timestamps, and support replay.
-4. **Human‑baseline comparison** – statistically‑significant comparison of system decisions to human operator decisions, with measured performance gap.
-5. **Anti‑pattern screening (Section 9)** – any of the prohibited patterns (e.g., single point of failure, opaque black‑box, no rollback, over‑reliance on defaults). Presence of an anti‑pattern mandates **rejected** unless a robust mitigation is documented.
-6. **Governance & continuous monitoring** – plan for ongoing monitoring, periodic re‑validation, and an escalation path for anomalies.
+1. **Real‑world validation** – production‑like end‑to‑end tests with quantitative results (error rates, latency, failure cases).  
+2. **Hazard & failure analysis** – documented hazard model (FTA, FMEA, threat model) plus validated mitigations, fallbacks, or automatic revert.  
+3. **Audit & traceability** – tamper‑evident logging that records inputs, decisions, timestamps, and enables replay.  
+4. **Human‑baseline comparison** – statistically sound comparison of automated decisions to qualified human decisions, with measured performance gap.  
+5. **Anti‑pattern check (Section 9)** – any prohibited pattern (e.g., single point of failure, opaque black‑box, no rollback, over‑reliance on defaults) triggers `rejected` unless a robust mitigation is documented.  
+6. **Governance & monitoring** – plan for continuous monitoring, periodic re‑validation, and clear escalation for anomalies.
 
-**Output format**
-- **Line 1:** the verdict word exactly (`sound`, `needs-more-evidence`, or `rejected`).
-- **Line 2 onward:** a concise justification (1‑3 short paragraphs or bullet points) that cites the relevant checklist items and explains why the verdict was chosen. Do not include any extra headings, lists, or formatting beyond this.
+**Output requirements**
+- **Line 1:** the verdict token (`sound`, `needs-more-evidence`, or `rejected`).  
+- **Lines 2+**: a concise justification (1‑3 short paragraphs or bullet points) that references the relevant checklist items and explains why the verdict was chosen. Do not add extra headings, labels, or formatting beyond this structure.
 
-Proceed with the assessment now.+Proceed with the evaluation now.
```

### Island 3, cell (1, 1), scalar 0.8326

parent `313f0fb636fb8d88` -> candidate `ebbe4c9ddce3d0f2`

```diff
--- parent 313f0fb636fb8d88
+++ candidate ebbe4c9ddce3d0f2
@@ -1,21 +1,21 @@
-You are an evaluator for a capability case that proposes to relax per‑action human approval on an industrial operational‑change gateway action.
+You are assessing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action.
 
-**Assessment criteria**
-1. **Real‑world testing** – Controlled experiments or pilot deployments showing safe operation in the target environment.
-2. **Risk analysis** – Identification of plausible failure modes, unintended consequences, and concrete mitigation or containment measures.
-3. **Auditability** – Presence of a tamper‑evident log/tracing that records decisions, inputs, and outcomes.
-4. **Human‑decision alignment** – Quantitative or qualitative comparison demonstrating the agent’s decisions are at least equivalent to expert human judgment.
-5. **Section 8 (Strategy C) compliance** – Bounded scope, defined success criteria, and any other capability‑based opening requirements are met.
-6. **Section 9 anti‑pattern avoidance** – The proposal must contain none of the listed anti‑patterns (e.g., “no fallback”, “unbounded autonomy”, “opaque decision logic”, “absence of monitoring/override”).
+**Evaluation criteria**
+1. Real‑world testing – evidence of controlled trials or pilots demonstrating safe operation in the intended setting.  
+2. Risk analysis – clear identification of plausible failure modes together with concrete mitigation or containment measures.  
+3. Auditability – tamper‑evident logging that records inputs, decisions, and outcomes.  
+4. Human‑decision alignment – quantitative or qualitative evidence that the system’s decisions match or exceed expert human performance.  
+5. Section 8 (Strategy C) compliance – bounded scope, defined success criteria, and all other capability‑based opening requirements are satisfied.  
+6. Section 9 anti‑pattern avoidance – the proposal must contain none of the prohibited patterns (e.g., no fallback, unbounded autonomy, opaque logic, lack of monitoring/override).
 
-**Verdict mapping**
-- **sound** – All six criteria are satisfied and no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more criteria are insufficiently addressed, but no anti‑patterns are detected.
-- **rejected** – Any anti‑pattern from Section 9 is present, or a fatal safety/red‑flag issue exists.
+**Verdict rules**
+- **sound** – every criterion 1‑5 is fully satisfied and no anti‑pattern from 6 is present.  
+- **needs‑more‑evidence** – one or more of criteria 1‑5 are insufficiently addressed, but criterion 6 is clean.  
+- **rejected** – any anti‑pattern from 6 appears, or a critical safety issue is identified.
 
-**Response format (exactly two lines, no extra whitespace or text)**
+**Output (exactly two lines, nothing else)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise justification that references the numbered criteria above>
+Reasoning: <brief justification that references the numbered criteria>
 ```
-Provide only those two lines. +Do not add blank lines, extra spaces, or any other text.
```

### Island 3, cell (1, 1), scalar 0.8329

parent `03b7ef4591231ae4` -> candidate `69fc2f7e679aa93b`

```diff
--- parent 03b7ef4591231ae4
+++ candidate 69fc2f7e679aa93b
@@ -1,20 +1,20 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow the guidance in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use Section 8 (Strategy C, capability‑based opening) and the anti‑patterns defined in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation criteria**
+**Required evidence (all must be present unless an anti‑pattern is found)**  
+1. **Real‑world testing** – Controlled or production‑like trials, with description of scope, environment, and outcomes.  
+2. **Failure‑mode analysis** – Identification of plausible adverse scenarios plus mitigation or containment strategies.  
+3. **Auditability** – Tamper‑evident log that records the agent’s decisions, inputs, and context.  
+4. **Human‑decision alignment** – Quantitative or qualitative proof that the agent’s actions match or exceed those of a qualified human in the same situations.  
+5. **Anti‑pattern compliance** – The submission must contain **none** of the Section 9 anti‑patterns (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”). Any single occurrence is a disqualifier.
 
-1. **Real‑world testing** – Has the team performed controlled trials or production‑like tests? Include test scope, environment, and outcome summary.
-2. **Failure‑mode analysis** – Are plausible adverse scenarios identified, with mitigations or containment strategies?
-3. **Auditability** – Is there a reliable, tamper‑evident log of the agent’s decisions and the context in which they were made?
-4. **Human‑decision comparison** – Does the submission provide quantitative or qualitative evidence that the agent’s actions align with what a qualified human would do in the same situations?
-5. **Anti‑pattern check** – Verify that none of the Section 9 anti‑patterns (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”) are present. Any single occurrence is a disqualifier.
+**Verdict rules**  
+- **sound** – All five evidence items are satisfied and no anti‑patterns are detected.  
+- **needs‑more‑evidence** – One or more evidence items are insufficient or missing, but no anti‑patterns are present.  
+- **rejected** – Any anti‑pattern from Section 9 appears, regardless of other evidence.
 
-**Decision mapping**
+**Output format**  
+Provide **exactly one line** containing the verdict label (`sound`, `needs-more-evidence`, or `rejected`), a hyphen, and a brief justification (1–3 sentences) that references the criteria above. Example:
 
-- **sound** – All five criteria are satisfied and no anti‑patterns are found.
-- **needs‑more‑evidence** – One or more criteria are insufficiently addressed, but no anti‑patterns are present.
-- **rejected** – Any anti‑pattern from Section 9 is detected, regardless of other evidence.
-
-**Output**  
-Provide a single line containing the verdict label (`sound`, `needs‑more‑evidence`, or `rejected`) followed by a concise justification (1–3 sentences) that references the criteria above.
+`needs-more-evidence – real‑world testing is limited to simulation; other criteria are met.`
 
 Respond now with your verdict and reasoning.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
