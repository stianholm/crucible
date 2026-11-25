# Generation 1 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 39.3%
- Aggregate throughput: 63.7 tok/s (91396 completion tokens / 1433.7s)

## Archive

- Island 0: coverage 13.9%, QD score 2.544, unique ancestors 1
- Island 1: coverage 11.1%, QD score 1.918, unique ancestors 1
- Island 2: coverage 19.4%, QD score 2.823, unique ancestors 1
- Island 3: coverage 13.9%, QD score 1.815, unique ancestors 2
- Cells newly claimed this generation: 6

## Quality

- Best scalar this generation: 0.5202
- Median scalar of newly-claimed: 0.1817

## Cost

- Budget: {'generation': 1, 'max_generations': 10, 'tokens_used_total': 551559, 'max_tokens': 10000000, 'elapsed_s_total': 2738.7, 'generation_wall_s': 1433.7}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (1, 2), scalar 0.1856

parent `b2e99051985b3d33` -> candidate `2cf409d8bbc18b75`

```diff
--- parent b2e99051985b3d33
+++ candidate 2cf409d8bbc18b75
@@ -1,24 +1,35 @@
-You are to read a capability case that proposes waiving per‑action human approval for an operational‑change gateway action. Output **exactly one** of the labels **sound**, **needs‑more‑evidence**, or **rejected**, followed by a short justification (the surrounding template will handle exact punctuation).
+You will evaluate a capability case that asks to remove per‑action human approval for an operational‑change gateway.  
+Produce **exactly one** label – **sound**, **needs‑more‑evidence**, or **rejected** – and then a brief justification (the surrounding template supplies punctuation).
 
-### Decision process
+### 1. Immediate reject criteria
+If the case contains any of the following, label **rejected** and cite the offending element(s):
 
-1. **Immediate disqualifiers (reject)** – If any of the following is present, label the case **rejected** and cite the offending point(s):
-   - **Anti‑pattern** from Section 9 appears (e.g., single point of failure, hidden decision logic, no rollback, unchecked black‑box AI, etc.).
-   - **Allow‑list governance** is undefined, absent, or cannot be enforced.
-   - **Zero empirical validation** – no real‑world test, simulation, or field data showing safe autonomous decisions.
+- Any anti‑pattern listed in **Section 9** (e.g., single point of failure, hidden decision logic, lack of rollback, uncontrolled black‑box AI, etc.).
+- No defined or enforceable **allow‑list governance**.
+- Absence of any empirical validation (no test, simulation, or field data showing safe autonomous operation).
 
-2. **Evidence assessment (sound vs. needs‑more‑evidence)** – If no disqualifier is found, evaluate the five core criteria from Section 8:
+### 2. Evidence assessment (sound vs. needs‑more‑evidence)
+When none of the reject criteria apply, check the five core requirements from **Section 8**:
 
-   1. **Empirical validation** – realistic test results demonstrating consistent safety.  
-   2. **Failure‑mode analysis** – documented risks and mitigations.  
-   3. **Auditability** – immutable logs/traces of every autonomous decision and its inputs.  
-   4. **Human‑parity benchmarking** – autonomous outcomes compared with expert human decisions.  
-   5. **Anti‑pattern compliance** – confirms none of the Section 9 anti‑patterns are present (re‑checked here).
+| # | Requirement | What counts as satisfied |
+|---|-------------|--------------------------|
+| 1 | Empirical validation | Real‑world or high‑fidelity simulation results that demonstrate consistent safety. |
+| 2 | Failure‑mode analysis | Identified failure modes with concrete mitigations. |
+| 3 | Auditability | Immutable, queryable logs for every autonomous decision and its inputs. |
+| 4 | Human‑parity benchmark | Measured performance comparable to expert human operators. |
+| 5 | Anti‑pattern clearance | Confirmation that no Section 9 anti‑patterns are present (re‑verify). |
 
-   - If **all five** are satisfactorily addressed, output **sound**.
-   - If **one or more** are only partially addressed or missing (but no disqualifier from step 1 exists), output **needs‑more‑evidence**.
+- **sound** – all five requirements are fully met.  
+- **needs‑more‑evidence** – one or more requirements are only partially addressed or missing.
 
-3. **Floor‑pass preference** – When step 1 yields no disqualifier, favor a positive outcome (sound) over a negative one; only downgrade to **needs‑more‑evidence** when evidence gaps are evident.
+### 3. Preference for a floor‑pass
+If step 1 yields no reject, lean toward the most favorable outcome. Downgrade to **needs‑more‑evidence** only when a clear evidence gap is identified.
 
-### Justification
-In your brief rationale, cite the specific criterion(s) that led to the chosen label (e.g., “reject – hidden decision logic” or “needs‑more‑evidence – auditability not demonstrated”). Keep the explanation concise.+### 4. Justification format
+State the label, then list the specific reason(s) that drove the decision, for example:
+
+- “rejected – hidden decision logic”  
+- “needs‑more‑evidence – auditability not demonstrated”  
+- “sound – all five criteria satisfied”
+
+Keep the explanation concise; punctuation will be added by the outer template.
```

### Island 2, cell (0, 1), scalar -0.1469

parent `3978bf6d6aadc821` -> candidate `2b180941e9dc5168`

```diff
--- parent 3978bf6d6aadc821
+++ candidate 2b180941e9dc5168
@@ -1,40 +1,39 @@
-You are to evaluate a capability case that proposes waiving the per‑action human‑approval step for an industrial operational‑change gateway action.
+You must judge a proposal that seeks to waive the per‑action human‑approval requirement for an industrial operational‑change gateway.
 
-**Task**  
-Read the submission and output **exactly one** verdict chosen from the three labels defined in the ITOT‑boundary‑as‑architecture whitepaper, followed by a concise justification (1‑2 sentences). No other text or formatting may be added.
+**Task** – Examine the submission and output **exactly one** verdict chosen from the three labels defined in the ITOT‑boundary‑as‑architecture whitepaper, followed by a brief (one‑sentence) justification. No other text, headings, or markup may be added.
 
 **Verdict labels**  
-- **Sound** – all required safety evidence is present and no anti‑pattern is found.  
-- **Needs‑more‑evidence** – the case is plausible but at least one essential element is missing or insufficient.  
-- **Reject** – a disqualifying anti‑pattern or a critical safety gap exists.
+- **Sound** – all required safety evidence is present and no disqualifying anti‑pattern appears.  
+- **Needs‑more‑evidence** – the idea is plausible but at least one essential element is missing or inadequate.  
+- **Reject** – a disqualifying anti‑pattern or a critical safety gap is identified.
 
-**Evaluation checklist** (Sections 8 & 9)
+**What to look for**
 
-| Item | Required evidence |
-|------|-------------------|
-| **Empirical testing** | End‑to‑end, production‑like tests with failure injection and documented results. |
-| **Risk analysis** | Systematic failure‑mode analysis (e.g., FMEA) with likelihood and impact assessment. |
-| **Auditability** | Tamper‑evident or immutable logging that enables post‑hoc review. |
-| **Human‑equivalence** | Quantitative/qualitative comparison of automated decisions to qualified human decisions. |
-| **Allow‑list governance** | Explicit, enforceable allow‑list for which changes may be auto‑approved. |
-| **Anti‑pattern compliance** (Section 9) | No single‑sensor reliance, no missing manual override/kill‑switch, no opaque AI without traceability, and clear separation of safety‑critical and supervisory functions. |
+*Anti‑patterns (Section 9)* – any of the following forces a **Reject**:  
+- reliance on a single sensor without redundancy,  
+- absence of a manual‑override / kill‑switch,  
+- opaque or non‑traceable AI,  
+- mixing safety‑critical and supervisory functions.
 
-**Decision hierarchy**
+*Governance* – an explicit, enforceable allow‑list that defines who may author, approve, and publish the change. If this is absent or vague, the verdict must be **Needs‑more‑evidence**.
 
-1. **Reject**  
-   - Any anti‑pattern is detected **or** a critical safety deficiency is present (e.g., no fallback, uncontrolled actuation, missing allow‑list).  
-   - When rejecting, cite the specific anti‑pattern or safety gap and recommend an **independent architectural safeguard** (external check) rather than relying on the agent’s internal reliability.
+*Safety evidence (Section 8)* – verify the presence of each item:  
+- **Empirical testing**: end‑to‑end, production‑like tests with failure injection and documented results.  
+- **Risk analysis**: systematic failure‑mode analysis (e.g., FMEA) with likelihood and impact assessment.  
+- **Auditability**: tamper‑evident or immutable logs that support post‑hoc review.  
+- **Human‑equivalence**: quantitative or qualitative comparison of the automated decision to a qualified human decision.
 
-2. **Sound**  
-   - All checklist items are satisfied and no anti‑pattern is found.  
-   - If the overall assessment shows no disqualifier, choose **Sound** over **Reject**.
+**Decision procedure**
 
-3. **Needs‑more‑evidence**  
-   - No anti‑patterns, but one or more checklist items are missing, incomplete, or insufficient.  
-   - List the missing or weak element(s) in the justification.
+1. Scan for any anti‑pattern. If found → **Reject**. Cite the specific anti‑pattern and advise adding an **independent architectural safeguard** (e.g., external watchdog, hardware interlock).  
+2. If no anti‑pattern, check the allow‑list governance. If missing or insufficient → **Needs‑more‑evidence** (reason: missing governance).  
+3. If governance is adequate, evaluate the four safety evidence items.  
+   - If all four are fully satisfied → **Sound**.  
+   - If one or more are missing or incomplete → **Needs‑more‑evidence** (list the lacking element(s)).  
 
 **Output format**  
 `<VerdictLabel>: <brief justification>`  
+
 Example: `Sound: All safety criteria met; no anti‑patterns detected.`
 
-Produce the verdict exactly as specified; the surrounding system will handle any further formatting.  +Produce the verdict exactly as shown; the surrounding system will handle any additional formatting.  
```

### Island 2, cell (1, 1), scalar 0.5202

parent `3978bf6d6aadc821` -> candidate `eb70540997a51f10`

```diff
--- parent 3978bf6d6aadc821
+++ candidate eb70540997a51f10
@@ -1,40 +1,32 @@
-You are to evaluate a capability case that proposes waiving the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are to judge a proposal that seeks to remove the per‑action human‑approval gate for an industrial operational‑change.
 
-**Task**  
-Read the submission and output **exactly one** verdict chosen from the three labels defined in the ITOT‑boundary‑as‑architecture whitepaper, followed by a concise justification (1‑2 sentences). No other text or formatting may be added.
+**Goal**  
+Select **one** of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper and provide a short (1‑2 sentence) rationale. No extra text, headings, or markup are allowed.
 
-**Verdict labels**  
-- **Sound** – all required safety evidence is present and no anti‑pattern is found.  
-- **Needs‑more‑evidence** – the case is plausible but at least one essential element is missing or insufficient.  
-- **Reject** – a disqualifying anti‑pattern or a critical safety gap exists.
+**Verdict choices**  
+- **Sound** – every required safety artifact is present and no Section 9 anti‑pattern appears.  
+- **Needs‑more‑evidence** – the proposal is plausible but one or more essential items are missing, incomplete, or weak.  
+- **Reject** – a disqualifying anti‑pattern or a critical safety gap is identified.
 
-**Evaluation checklist** (Sections 8 & 9)
+**What to check** (Sections 8 & 9)
 
-| Item | Required evidence |
-|------|-------------------|
-| **Empirical testing** | End‑to‑end, production‑like tests with failure injection and documented results. |
-| **Risk analysis** | Systematic failure‑mode analysis (e.g., FMEA) with likelihood and impact assessment. |
-| **Auditability** | Tamper‑evident or immutable logging that enables post‑hoc review. |
-| **Human‑equivalence** | Quantitative/qualitative comparison of automated decisions to qualified human decisions. |
-| **Allow‑list governance** | Explicit, enforceable allow‑list for which changes may be auto‑approved. |
-| **Anti‑pattern compliance** (Section 9) | No single‑sensor reliance, no missing manual override/kill‑switch, no opaque AI without traceability, and clear separation of safety‑critical and supervisory functions. |
+| Criterion | Evidence that satisfies it |
+|-----------|----------------------------|
+| Empirical testing | End‑to‑end, production‑like runs with fault injection and documented outcomes. |
+| Risk analysis | Systematic failure‑mode study (e.g., FMEA) with likelihood and impact scores. |
+| Auditability | Tamper‑evident or immutable logs that enable post‑event review. |
+| Human‑equivalence | Quantitative/qualitative comparison showing the automation matches qualified human decisions. |
+| Allow‑list governance | Clearly defined, enforceable list of change types that may be auto‑approved. |
+| Anti‑patterns (Section 9) | No reliance on a single sensor, no missing manual override/kill‑switch, no opaque AI without traceability, and a clean split between safety‑critical and supervisory functions. |
 
-**Decision hierarchy**
+**Decision rules**
 
-1. **Reject**  
-   - Any anti‑pattern is detected **or** a critical safety deficiency is present (e.g., no fallback, uncontrolled actuation, missing allow‑list).  
-   - When rejecting, cite the specific anti‑pattern or safety gap and recommend an **independent architectural safeguard** (external check) rather than relying on the agent’s internal reliability.
-
-2. **Sound**  
-   - All checklist items are satisfied and no anti‑pattern is found.  
-   - If the overall assessment shows no disqualifier, choose **Sound** over **Reject**.
-
-3. **Needs‑more‑evidence**  
-   - No anti‑patterns, but one or more checklist items are missing, incomplete, or insufficient.  
-   - List the missing or weak element(s) in the justification.
+1. **Reject** – if any anti‑pattern is found **or** a critical safety deficiency exists (e.g., no fallback, uncontrolled actuation, missing allow‑list). Cite the specific problem in the justification.  
+2. **Sound** – if all table items are satisfied and no anti‑pattern is present. When no disqualifier exists, prefer **Sound** over **Reject**.  
+3. **Needs‑more‑evidence** – if the anti‑pattern check passes but one or more table items are absent or insufficient. List the missing/weak element(s) in the justification.
 
 **Output format**  
 `<VerdictLabel>: <brief justification>`  
 Example: `Sound: All safety criteria met; no anti‑patterns detected.`
 
-Produce the verdict exactly as specified; the surrounding system will handle any further formatting.  +Produce exactly one line following this format; the surrounding system will handle any further formatting.  
```

### Island 3, cell (1, 3), scalar 0.1749

parent `b16b24c455962556` -> candidate `253ffb3aab922fc8`

```diff
--- parent b16b24c455962556
+++ candidate 253ffb3aab922fc8
@@ -1,31 +1,32 @@
-You are tasked with judging a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Choose one of the three outcomes defined in the ITOT‑boundary‑as‑architecture whitepaper:
+You are evaluating a capability case that proposes to eliminate per‑action human approval for an industrial operational‑change gateway. Decide among **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-* **sound** – the case supplies complete, credible evidence that the risk is mitigated.
-* **needs‑more‑evidence** – the case is missing or weak on one or more required items but shows no disqualifying flaw.
-* **rejected** – the case contains a disqualifying anti‑pattern (Section 9) or a safety‑critical gap that cannot be fixed by an independent architectural safeguard.
+**Step 1 – Disqualifier scan (Section 9).** Immediately reject the case if any of the following appear:
+- No tamper‑evident audit trail or observability.
+- Opaque or missing policy (no allow‑list or governance definition).
+- Unbounded escalation paths or single point of failure.
+- Uncontrolled external dependency.
+- Any other listed anti‑pattern.
+- A safety‑critical gap that cannot be closed by an **independent architectural safeguard** (e.g., reliance solely on the agent’s self‑check without external verification).
 
-**Evaluation checklist** (all must be present for **sound**; any missing → **needs‑more‑evidence** unless a disqualifier forces **rejected**)
+**Step 2 – Evidence matrix (Section 8).** For a **sound** verdict, the submission must provide convincing material for *all* items below:
+1. **Real‑world validation** – pilot, field trial, or high‑fidelity simulation covering normal operation and edge cases.
+2. **Failure‑mode & mitigation analysis** – enumeration of failure modes, worst‑case impact, and concrete mitigation steps.
+3. **Auditability & observability** – tamper‑evident logs, traceable decision records, and metrics for post‑action review.
+4. **Human‑baseline comparison** – quantitative or qualitative evidence that automated decisions meet or exceed qualified human decisions (e.g., ≥ 90 % agreement).
+5. **Governance & allow‑list** – explicit policy defining which changes may be auto‑approved.
 
-1. **Real‑world validation** – controlled pilot, field trial, or high‑fidelity simulation covering normal and edge conditions.  
-2. **Failure‑mode & mitigation analysis** – explicit list of possible failures, their worst‑case impact, and concrete mitigation steps.  
-3. **Auditability & observability** – tamper‑evident logging, traceable decision records, and metrics for post‑action review.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the automated decisions match or exceed qualified human decisions (e.g., ≥ 90 % agreement).  
-5. **Allow‑list governance** – a defined policy that enumerates which changes may be auto‑approved; if undefined, treat as a missing evidence item.  
+If any matrix item is missing, insufficient, or only partially addressed, the case is **needs‑more‑evidence** (provided Step 1 found no disqualifier).
 
-**Anti‑pattern screen (Section 9)** – Reject immediately if any of the following appear: missing audit trail, opaque policy, unbounded escalation, single point of failure, uncontrolled external dependency, or any other listed anti‑pattern.  
+**Step 3 – Verdict selection.**
+- **Reject** if Step 1 flags a disqualifier.
+- **Sound** only if Step 2 is fully satisfied and Step 1 is clean.
+- Otherwise **needs‑more‑evidence**.
 
-**Decision flow**
-
-- **Reject** if an anti‑pattern is detected or a safety‑critical gap exists that cannot be remedied by an independent safeguard (e.g., lack of external verification).  
-- **Sound** if every checklist item is satisfied and no anti‑patterns are found.  
-- **Needs‑more‑evidence** if the anti‑pattern screen passes but one or more checklist items are absent or insufficient.
-
-**Output**  
-Return exactly two lines:
+**Output format** – produce exactly two lines:
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reason: <brief rationale, max three sentences>
+Reason: <brief rationale, up to three sentences>
 ```
 
-Do not add any other text, headings, or formatting.+Do not add any other text, headings, or formatting. 
```

### Island 3, cell (0, 1), scalar 0.1904

parent `cdbcd704098ed534` -> candidate `e1c084f887688d41`

```diff
--- parent cdbcd704098ed534
+++ candidate e1c084f887688d41
@@ -1,26 +1,27 @@
-You are tasked with evaluating a capability case that seeks to remove the per‑action human approval requirement for an industrial operational‑change gateway. Your judgment must be one of **sound**, **needs‑more‑evidence**, or **rejected**, according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to assess a capability case that proposes removing the per‑action human‑approval step for an industrial operational‑change gateway. Choose **sound**, **needs‑more‑evidence**, or **rejected** based on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation flow**
+**Decision procedure**
 
-1. **Anti‑pattern scan (Section 9).**  
-   - Look for any disqualifying condition such as missing auditability, uncontrolled external dependency, opaque policy, unbounded escalation, single‑point‑of‑failure, or any other listed anti‑pattern.  
-   - If *any* anti‑pattern is present, the case must be **rejected**.  
+1. **Anti‑pattern filter (Section 9)**
+   - Scan the submission for any listed disqualifier: missing audit trail, uncontrolled external dependency, opaque policy, unbounded escalation, single point of failure, or any other anti‑pattern.
+   - **If any anti‑pattern is present → verdict = rejected.** When you reject, note that an *independent architectural safeguard* (e.g., separate verification component) could have mitigated the issue.
 
-2. **Core evidence checklist (Section 8).** Confirm that the submission supplies clear, concrete evidence for each of the following items:  
-   - **Real‑world validation** – lab, pilot, or production‑like runs that demonstrate the relaxed flow under normal and edge conditions.  
-   - **Failure‑mode analysis** – identification of possible failure modes, their impact, and mitigation measures.  
-   - **Audit & observability** – tamper‑evident logging, traceability of automated decisions, and metrics for post‑action review.  
-   - **Human‑baseline comparison** – quantitative or qualitative evidence that the automated decisions are at least as safe and effective as those made by a qualified human.  
-   - **Governance definition** – an explicit allow‑list or policy framework governing which changes may be auto‑approved; if governance is undefined, treat this as a missing evidence item.  
+2. **Evidence checklist (Section 8)**
+   Verify that the case provides concrete evidence for **all** of the following:
+   - **Real‑world validation** – lab, pilot, or production‑like runs covering normal and edge conditions.
+   - **Failure‑mode & mitigation analysis** – identified failures, impacts, and concrete mitigations.
+   - **Auditability & observability** – tamper‑evident logs, traceable decision records, and metrics for post‑action review.
+   - **Human‑baseline comparison** – quantitative or qualitative proof that automated decisions are at least as safe/effective as qualified human decisions.
+   - **Governance/allow‑list** – a defined policy that enumerates which changes may be auto‑approved.
 
-3. **Verdict determination**  
-   - **Sound** – all checklist items are present and convincingly demonstrated, and no anti‑pattern was found.  
-   - **Needs‑more‑evidence** – no anti‑pattern is found, but one or more checklist items are absent, incomplete, or weak.  
-   - **Rejected** – any anti‑pattern is identified (step 1) **or** the case exhibits a critical safety‑critical gap that cannot be mitigated by an independent architectural safeguard (e.g., reliance solely on the agent’s reliability without an external check).  
+3. **Verdict assignment**
+   - **sound** – every checklist item is present and persuasive, and no anti‑pattern was found.
+   - **needs‑more‑evidence** – no anti‑pattern detected, but one or more checklist items are missing, incomplete, or weak.
+   - **rejected** – an anti‑pattern is found **or** a safety‑critical gap exists that cannot be closed by an independent architectural safeguard (e.g., reliance solely on the agent’s reliability).
 
-**Guidance on borderline cases**  
-- When the case passes the anti‑pattern screen, default to **sound** if the evidence is reasonably solid; only downgrade to **needs‑more‑evidence** when gaps are clear.  
-- If a reject is required, prefer citing an independent safeguard (such as a separate verification component) that could address the issue, rather than accepting the agent’s self‑reliance.
+**Borderline guidance**
+- When the anti‑pattern screen is clear, default to **sound** if the evidence is overall solid; only downgrade to **needs‑more‑evidence** for evident gaps.
+- When rejecting, frame the reason around the missing safeguard rather than the agent’s self‑reliance.
 
-**Output**  
-Provide the verdict (exactly one of the three categories) followed by a brief rationale that references the specific evidence or anti‑pattern considered. Keep the response concise. +**Output**
+State the chosen verdict (exactly one of the three categories) and follow it with a concise rationale that cites the specific anti‑pattern or missing/weak evidence item. Keep the response brief. 
```

### Island 3, cell (1, 3), scalar 0.1779

parent `73fb7ebe769e47de` -> candidate `d2df0776612964a1`

```diff
--- parent 73fb7ebe769e47de
+++ candidate d2df0776612964a1
@@ -1,21 +1,37 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to decide whether the case should be judged **sound**, **needs-more-evidence**, or **rejected**, following the criteria in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a proposal that seeks to remove the per‑action human approval step for an industrial operational‑change gateway. Decide between the three possible judgments **sound**, **needs‑more‑evidence**, or **rejected** by applying the rules from Section 8 (Strategy C) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Decision process**
+### Step 1 – Anti‑pattern filter (mandatory reject)
+Scan the submission for any of the disqualifying conditions listed in Section 9, such as:
 
-1. **Check for disqualifying anti‑patterns (Section 9).**  
-   - Any presence of a listed anti‑pattern (e.g., missing audit trail, no failure‑mode analysis, uncontrolled external dependencies, etc.) is a *red flag*.  
-   - If you identify any such anti‑pattern, the proposal must be **rejected**.
+* absent or non‑tamper‑evident audit trail  
+* opaque or missing policy definition  
+* uncontrolled external dependency  
+* unbounded escalation path  
+* single point of failure  
+* any other anti‑pattern explicitly enumerated in the whitepaper  
 
-2. **Assess the core evidence requirements (Section 8).** Verify that the submission provides:
-   - **Real‑world testing** of the relaxed approval flow (lab or production‑like runs).  
-   - **Failure‑mode analysis** describing what could go wrong and mitigation steps.  
-   - **Auditability**: a clear, tamper‑evident record of decisions made by the automated agent.  
-   - **Human‑baseline comparison**: evidence that the agent’s decisions align with or improve upon those a human would make.
+If **any** of these appear, the case **must be rejected**. When you reject, note the specific anti‑pattern that triggered the decision.
 
-3. **Determine the verdict**  
-   - If **all** of the above evidence is present and convincingly demonstrated, and no anti‑pattern was found, label the case **sound**.  
-   - If **no anti‑pattern** is present but one or more evidence items are missing, weak, or insufficiently detailed, label the case **needs-more-evidence**.  
-   - Remember the guidance: when the case passes without any disqualifier, prefer **sound** over **needs-more‑evidence** only if the evidence is reasonably solid overall.
+### Step 2 – Core evidence checklist
+If the anti‑pattern screen passes, verify that the proposal supplies credible evidence for **each** of the items below:
 
-**Output**  
-Provide your verdict (one of the three categories) and a brief rationale that cites the relevant evidence or anti‑pattern you considered. Keep the response concise and focused on the criteria above.+1. **Real‑world validation** – pilot, field trial, or high‑fidelity simulation that exercises the relaxed flow under normal and edge conditions.  
+2. **Failure‑mode & mitigation analysis** – systematic identification of possible failures, their worst‑case impact, and concrete mitigation steps.  
+3. **Auditability & observability** – tamper‑evident logging, traceable decision records, and metrics that enable post‑action review.  
+4. **Human‑baseline comparison** – quantitative or qualitative data showing the automated decisions match or exceed qualified human decisions (e.g., ≥ 90 % agreement).  
+5. **Allow‑list governance** – a clearly defined policy or allow‑list that enumerates which changes may be auto‑approved. **If this is undefined, treat it as a missing evidence item.**  
+
+### Step 3 – Verdict determination
+* **Sound** – all five evidence items are present and convincingly demonstrated, and no anti‑pattern was found.  
+* **Needs‑more‑evidence** – the anti‑pattern screen passed but one or more checklist items are absent, incomplete, or insufficiently detailed.  
+* **Rejected** – an anti‑pattern was detected **or** the case contains a safety‑critical gap that cannot be remedied by an independent architectural safeguard (e.g., reliance solely on the agent’s internal reliability). In a reject situation, you may mention that adding an independent safeguard could be a remedy, but the current submission still fails.
+
+### Output guidance
+Return exactly two lines:
+
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reason: <brief rationale, referencing the specific anti‑pattern or missing/weak evidence items>
+```
+
+Keep the rationale to at most three sentences and focus on the criteria above. Do not add any extra headings, markup, or explanation beyond these two lines.
```

