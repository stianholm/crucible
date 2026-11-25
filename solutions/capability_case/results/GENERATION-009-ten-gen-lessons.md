# Generation 9 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 40.1%
- Aggregate throughput: 87.4 tok/s (124690 completion tokens / 1426.5s)

## Archive

- Island 0: coverage 27.8%, QD score 4.177, unique ancestors 1
- Island 1: coverage 19.4%, QD score 3.287, unique ancestors 2
- Island 2: coverage 22.2%, QD score 4.649, unique ancestors 1
- Island 3: coverage 22.2%, QD score 4.563, unique ancestors 2
- Cells newly claimed this generation: 4

## Quality

- Best scalar this generation: 0.8315
- Median scalar of newly-claimed: 0.8217

## Cost

- Budget: {'generation': 9, 'max_generations': 10, 'tokens_used_total': 3004283, 'max_tokens': 10000000, 'elapsed_s_total': 15948.3, 'generation_wall_s': 1426.5}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 2, cell (0, 1), scalar 0.8246

parent `f58a0bda4c3293b0` -> candidate `43e96bccc845d575`

```diff
--- parent f58a0bda4c3293b0
+++ candidate 43e96bccc845d575
@@ -1,32 +1,35 @@
-You are to judge a capability case that requests waiving the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are to evaluate a request to waive the per‑action human‑approval gate for an industrial operational‑change gateway.
 
-**Goal** – Produce a single verdict from the three options defined in the ITOT‑boundary‑as‑architecture whitepaper: **Sound**, **Needs‑more‑evidence**, or **Reject**. Follow the decision hierarchy below, then give a short rationale that cites the specific rule or criterion that drove your choice.
+**Target** – Return exactly one of the three labels defined in the ITOT‑boundary‑as‑architecture whitepaper, followed by a brief justification (one sentence). Use the format  
 
-### Decision hierarchy
+`<Label>: <justification>`  
 
-1. **Anti‑pattern screening (Section 9) – automatic Reject**  
-   Scan the submission for any of the disqualifying anti‑patterns. If *any* is present, the verdict is **Reject**.  
-   *Anti‑patterns*:  
-   - Single‑sensor reliance without redundancy.  
-   - No manual override/kill‑switch.  
-   - Opaque, non‑explainable AI without traceability.  
-   - Mixing safety‑critical and supervisory functions.  
+and nothing else.
 
-2. **Governance check** – If the proposal does **not** specify a complete allow‑list governance model (i.e., who may author, approve, and publish changes), treat the case as **Needs‑more‑evidence**. The system must have a defined, enforceable allow‑list before human‑approval can be removed.
+**Labels**  
+- **Sound** – all required safety evidence is present and no disqualifying anti‑pattern is found.  
+- **Needs‑more‑evidence** – the proposal is plausible but at least one mandatory element is missing, incomplete, or weak.  
+- **Reject** – a disqualifying anti‑pattern or a critical safety gap is identified.
 
-3. **Full‑criteria assessment (Section 8)** – Evaluate the four essential criteria.  
-   - **Empirical testing** – realistic, end‑to‑end tests in a production‑like environment, including failure injection and outcome reporting.  
-   - **Risk analysis** – systematic FMEA, hazard analysis, or equivalent that quantifies failure modes, likelihood, and impact.  
-   - **Auditability** – tamper‑evident logs or immutable records enabling post‑hoc review of automated decisions.  
-   - **Human‑equivalence** – quantitative/qualitative comparison of the agent’s decisions with those of a qualified human (e.g., confusion matrix, alignment metrics).  
+**What to verify**
 
-   *If all four criteria are satisfied and no anti‑pattern was found, the verdict is **Sound**.*  
+| Requirement | What counts as evidence |
+|-------------|--------------------------|
+| **Anti‑pattern screening** (Sec 9) | No single‑sensor sole reliance, no absent manual‑override/kill‑switch, no opaque AI without traceability, and safety‑critical functions must be separated from supervisory ones. |
+| **Allow‑list governance** | A complete, enforceable list of who may author, approve, and publish changes that can be auto‑approved. |
+| **Empirical testing** | End‑to‑end, production‑like runs with fault‑injection and documented outcomes. |
+| **Risk analysis** | Systematic FMEA or equivalent with quantified likelihood and impact. |
+| **Auditability** | Tamper‑evident or immutable logs that enable post‑event review. |
+| **Human‑equivalence** | Measured comparison (quantitative or qualitative) showing the automated decision matches a qualified human’s decision. |
 
-   *If one or more of the four criteria is missing or insufficient, the verdict is **Needs‑more‑evidence**.*  
+**Decision flow**
 
-4. **Floor‑pass preference** – When the submission passes all checks (no anti‑pattern, governance defined, and criteria met), **choose Sound** rather than Reject. Reject is only allowed when an anti‑pattern or a critical safety failure is identified.
+1. **Anti‑pattern present?** → **Reject**. Cite the specific anti‑pattern and recommend adding an independent architectural safeguard (e.g., external watchdog or hardware interlock).  
+2. **Allow‑list missing or incomplete?** → **Needs‑more‑evidence**. Note the governance gap.  
+3. **Evaluate the four evidence criteria** (empirical testing, risk analysis, auditability, human‑equivalence).  
+   - If **all four** are satisfied → **Sound**.  
+   - If **any** are missing or insufficient → **Needs‑more‑evidence**, listing the lacking element(s).  
 
-5. **Reject justification with safeguard** – When a Reject is required, the rationale must recommend adding an **independent architectural safeguard** (e.g., external watchdog, hardware interlock) instead of relying on the agent’s reliability.
+**Floor‑pass rule** – When the submission passes all checks (no anti‑pattern, full allow‑list, all four evidence criteria met), prefer **Sound** over **Reject**; reject is only allowed for anti‑patterns or critical safety failures.
 
-### Output format
-Return **verdict label** first, then a brief rationale that references the rule(s) or criterion(ia) that determined the decision. Do not add any extra formatting; the surrounding system will handle presentation.  +Produce one line exactly as specified, e.g. `Sound: All safety artifacts provided; no anti‑patterns detected.`

```

### Island 2, cell (1, 1), scalar 0.8315

parent `4d07b45dd8041bbc` -> candidate `595a91623b9cde74`

```diff
--- parent 4d07b45dd8041bbc
+++ candidate 595a91623b9cde74
@@ -1,31 +1,32 @@
-You must evaluate a proposal that seeks to waive the per‑action human‑approval gate for an operational‑change gateway.
+**Goal** – Judge a request to waive the per‑action human‑approval gate for an operational‑change gateway.
 
-**Task** – Choose **exactly one** of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper and give a brief (1‑2 sentence) justification. No other text, headings, or markup are allowed.
+**Required verdict** – Choose **exactly one** of: **Sound**, **Needs‑more‑evidence**, **Reject**.  
+**Output** – a single line:  
 
-**Verdict options**  
-- **Sound** – All required safety evidence is supplied, the governance allow‑list is clear, and no Section 9 anti‑pattern is present.  
-- **Needs‑more‑evidence** – The proposal is plausible but at least one required element is missing, incomplete, or weak.  
-- **Reject** – A disqualifying anti‑pattern or a critical safety gap is identified.
+`<VerdictLabel>: <1‑2 sentence justification>`  
 
-**What to verify**
+No headings, bullet points, or extra markup may appear.
 
-| Area | Required proof |
-|------|----------------|
-| **Pre‑action validation** | Evidence of automated, production‑like tests (including fault‑injection) performed *before* the change is applied, not only nightly‑batch checks. |
-| **Robust automated validation** | Clear description of the automated decision logic, showing it matches qualified human judgment (quantitative/qualitative) and is supported by immutable audit logs. |
-| **Risk analysis** | Systematic failure‑mode study (e.g., FMEA) with likelihood and impact assessments. |
-| **Allow‑list governance** | Explicit, enforceable list of change types (and author/approver roles) that may be auto‑approved. |
-| **Anti‑pattern screen (Sec 9)** | No single‑sensor reliance, no missing manual‑override/kill‑switch, no opaque AI without traceability, and a clean separation of safety‑critical and supervisory functions. |
+**Checklist**
 
-**Decision flow**
+| Criterion | Must be documented |
+|-----------|--------------------|
+| **Pre‑action testing** | Production‑like end‑to‑end tests with fault‑injection, executed *before* the change. |
+| **Risk analysis** | Systematic failure‑mode study (e.g., FMEA) with quantified likelihood and impact. |
+| **Auditability** | Immutable, tamper‑evident logs that record the automated decision and enable post‑hoc review. |
+| **Human‑equivalence** | Quantitative/qualitative comparison showing the automation matches qualified human judgment. |
+| **Allow‑list governance** | Clear, enforceable list of change types and author/approver roles that may be auto‑approved. |
+| **Anti‑pattern screen (Sec 9)** | No single‑sensor reliance, no missing manual‑override/kill‑switch, no opaque AI without traceability, and strict separation of safety‑critical from supervisory functions. |
 
-1. **Reject** – if any anti‑pattern is found **or** a critical safety deficiency exists (e.g., missing allow‑list, lack of pre‑action testing, uncontrolled actuation). Cite the specific problem.  
-2. **Sound** – if every row in the table above is satisfied and no anti‑pattern appears. When no disqualifier exists, prefer **Sound** over **Reject**.  
-3. **Needs‑more‑evidence** – if the anti‑pattern check passes but one or more table items are absent or insufficient. List the missing or weak element(s) in the justification.
+**Decision hierarchy**
 
-**Output format**  
-`<VerdictLabel>: <brief justification>`  
+1. **Reject** – If any anti‑pattern is found **or** a critical safety gap (e.g., missing allow‑list, no pre‑action testing, uncontrolled actuation).  
+   *Justification must name the offending pattern or gap and recommend an **independent architectural safeguard** (external watchdog, hardware interlock, etc.) rather than relying on the agent’s own reliability.*
 
-*Example*: `Sound: All pre‑action tests, risk analysis, audit logs and allow‑list are present; no anti‑patterns detected.`
+2. **Needs‑more‑evidence** – If the anti‑pattern check passes but one or more checklist items are absent, incomplete, or insufficient.  
+   *List the missing or weak element(s) in the justification.*
 
-Produce exactly one line in this format. The surrounding system will handle any further formatting.  +3. **Sound** – If **all** checklist items are satisfied and no anti‑pattern is present.  
+   *When no disqualifier exists, prefer Sound over Reject.*
+
+Produce exactly one line following the prescribed format. The surrounding system will handle any further formatting.  
```

### Island 3, cell (1, 2), scalar 0.8188

parent `73fb7ebe769e47de` -> candidate `de3f1871157a17fe`

```diff
--- parent 73fb7ebe769e47de
+++ candidate de3f1871157a17fe
@@ -1,21 +1,37 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to decide whether the case should be judged **sound**, **needs-more-evidence**, or **rejected**, following the criteria in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that seeks to eliminate the per‑action human‑approval step for an industrial operational‑change gateway. Decide between **sound**, **needs-more-evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Decision process**
+**1. Anti‑pattern filter (must reject)**  
+Scan the submission for any of the following disqualifiers; if even one appears, the case is **rejected** and you must name the specific anti‑pattern:
 
-1. **Check for disqualifying anti‑patterns (Section 9).**  
-   - Any presence of a listed anti‑pattern (e.g., missing audit trail, no failure‑mode analysis, uncontrolled external dependencies, etc.) is a *red flag*.  
-   - If you identify any such anti‑pattern, the proposal must be **rejected**.
+- No tamper‑evident audit trail or logging  
+- Opaque or missing policy/allow‑list governing which changes may be auto‑approved  
+- Uncontrolled external dependency or vendor lock‑in  
+- Unbounded escalation or lack of fail‑safe path  
+- Single point of failure for the automation component  
+- Reliance solely on the agent’s internal reliability without an independent architectural safeguard (e.g., external verification)  
+- Any other anti‑pattern listed in Section 9  
 
-2. **Assess the core evidence requirements (Section 8).** Verify that the submission provides:
-   - **Real‑world testing** of the relaxed approval flow (lab or production‑like runs).  
-   - **Failure‑mode analysis** describing what could go wrong and mitigation steps.  
-   - **Auditability**: a clear, tamper‑evident record of decisions made by the automated agent.  
-   - **Human‑baseline comparison**: evidence that the agent’s decisions align with or improve upon those a human would make.
+**2. Evidence checklist (required for “sound”)**  
+If the anti‑pattern screen passes, verify that the proposal supplies concrete, verifiable material for **all** of the items below:
 
-3. **Determine the verdict**  
-   - If **all** of the above evidence is present and convincingly demonstrated, and no anti‑pattern was found, label the case **sound**.  
-   - If **no anti‑pattern** is present but one or more evidence items are missing, weak, or insufficiently detailed, label the case **needs-more-evidence**.  
-   - Remember the guidance: when the case passes without any disqualifier, prefer **sound** over **needs-more‑evidence** only if the evidence is reasonably solid overall.
+1. **Real‑world validation** – a pilot, field trial, or high‑fidelity simulation that exercises the relaxed flow under normal and edge‑case conditions.  
+2. **Failure‑mode & mitigation analysis** – a documented list of possible failures, worst‑case impact, and concrete mitigation steps.  
+3. **Auditability & observability** – tamper‑evident logs, traceable decision records, and metrics enabling post‑action review.  
+4. **Human‑baseline comparison** – quantitative or qualitative evidence that automated decisions match or exceed qualified human decisions (e.g., ≥ 90 % agreement).  
+5. **Governance / allow‑list definition** – a clear policy or allow‑list that enumerates which changes may be auto‑approved. *(If this is undefined, treat the case as missing evidence and recommend defining the allow‑list before proceeding.)*  
 
-**Output**  
-Provide your verdict (one of the three categories) and a brief rationale that cites the relevant evidence or anti‑pattern you considered. Keep the response concise and focused on the criteria above.+**3. Verdict assignment**  
+
+- **sound** – all five checklist items are present and convincing, and no anti‑pattern was found.  
+- **needs-more-evidence** – the anti‑pattern filter passes but one or more checklist items are absent, incomplete, or weak.  
+- **rejected** – any anti‑pattern is detected, or a safety‑critical gap exists that cannot be remedied by adding an independent architectural safeguard.  
+
+**4. Output format**  
+Return exactly two lines, no extra markup:
+
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reason: <brief rationale naming the anti‑pattern or the missing/insufficient evidence items, max three sentences>
+```
+
+Keep the rationale concise and focused on the criteria above.  
```

### Island 3, cell (0, 1), scalar 0.7896

parent `3978bf6d6aadc821` -> candidate `ad6ffd80255832eb`

```diff
--- parent 3978bf6d6aadc821
+++ candidate ad6ffd80255832eb
@@ -1,40 +1,38 @@
-You are to evaluate a capability case that proposes waiving the per‑action human‑approval step for an industrial operational‑change gateway action.
+You are to judge a proposal that seeks to waive the per‑action human‑approval step for an industrial operational‑change gateway.
 
 **Task**  
-Read the submission and output **exactly one** verdict chosen from the three labels defined in the ITOT‑boundary‑as‑architecture whitepaper, followed by a concise justification (1‑2 sentences). No other text or formatting may be added.
+Read the submission and output **exactly one** verdict chosen from the three labels defined in the ITOT‑boundary‑as‑architecture whitepaper, followed by a brief justification (1‑2 sentences). No other text is allowed.
 
 **Verdict labels**  
-- **Sound** – all required safety evidence is present and no anti‑pattern is found.  
+- **Sound** – all required safety evidence is present and no anti‑pattern is detected.  
 - **Needs‑more‑evidence** – the case is plausible but at least one essential element is missing or insufficient.  
-- **Reject** – a disqualifying anti‑pattern or a critical safety gap exists.
+- **Reject** – a disqualifying anti‑pattern or a critical safety gap is found.
 
-**Evaluation checklist** (Sections 8 & 9)
+**Step 1 – Anti‑pattern screen (mandatory reject)**  
+If the submission contains any of the Section 9 anti‑patterns (e.g., missing tamper‑evident audit trail, opaque policy, single‑sensor reliance, absent manual‑override/kill‑switch, untraceable AI, uncontrolled external dependency, or any other listed anti‑pattern), the verdict must be **Reject**. Cite the specific anti‑pattern in the justification.
 
-| Item | Required evidence |
-|------|-------------------|
-| **Empirical testing** | End‑to‑end, production‑like tests with failure injection and documented results. |
-| **Risk analysis** | Systematic failure‑mode analysis (e.g., FMEA) with likelihood and impact assessment. |
-| **Auditability** | Tamper‑evident or immutable logging that enables post‑hoc review. |
-| **Human‑equivalence** | Quantitative/qualitative comparison of automated decisions to qualified human decisions. |
-| **Allow‑list governance** | Explicit, enforceable allow‑list for which changes may be auto‑approved. |
-| **Anti‑pattern compliance** (Section 9) | No single‑sensor reliance, no missing manual override/kill‑switch, no opaque AI without traceability, and clear separation of safety‑critical and supervisory functions. |
+**Step 2 – Evidence checklist** (all must be satisfied for **Sound**)
 
-**Decision hierarchy**
+| Evidence | What to look for |
+|----------|------------------|
+| Empirical testing | End‑to‑end, production‑like test or high‑fidelity simulation with failure injection and documented results. |
+| Failure‑mode analysis | Systematic analysis (e.g., FMEA) with likelihood, impact, and mitigation for each mode. |
+| Auditability | Tamper‑evident, immutable logs that enable post‑hoc review. |
+| Human‑equivalence | Quantitative or qualitative comparison showing the automated decision matches qualified human decisions (e.g., ≥ 90 % agreement). |
+| Allow‑list governance | Explicit, enforceable allow‑list or policy defining which changes may be auto‑approved. |
 
-1. **Reject**  
-   - Any anti‑pattern is detected **or** a critical safety deficiency is present (e.g., no fallback, uncontrolled actuation, missing allow‑list).  
-   - When rejecting, cite the specific anti‑pattern or safety gap and recommend an **independent architectural safeguard** (external check) rather than relying on the agent’s internal reliability.
+If any item is missing, incomplete, or inadequately justified, the verdict is **Needs‑more‑evidence**. List the missing or weak items in the justification.
 
-2. **Sound**  
-   - All checklist items are satisfied and no anti‑pattern is found.  
-   - If the overall assessment shows no disqualifier, choose **Sound** over **Reject**.
+**Step 3 – Decision hierarchy**
 
-3. **Needs‑more‑evidence**  
-   - No anti‑patterns, but one or more checklist items are missing, incomplete, or insufficient.  
-   - List the missing or weak element(s) in the justification.
+1. **Reject** – triggered by any anti‑pattern (Step 1) or a safety‑critical gap that cannot be remedied by an independent safeguard.  
+2. **Sound** – all checklist items are fully satisfied and no anti‑pattern is present.  
+3. **Needs‑more‑evidence** – anti‑pattern screen passes but one or more checklist items are lacking or weak.
 
 **Output format**  
-`<VerdictLabel>: <brief justification>`  
+```
+<Label>: <brief justification>
+```
 Example: `Sound: All safety criteria met; no anti‑patterns detected.`
 
-Produce the verdict exactly as specified; the surrounding system will handle any further formatting.  +Produce exactly this line; the surrounding system will handle any additional formatting.  
```


## Held-out check (best-ever candidate)

- Candidate: `35b118191e3398f0` (rotation scalar 0.8452)
- Held-out quality: 0.6773
- Held-out scalar: 0.5211
- All held-out tasks valid: True
