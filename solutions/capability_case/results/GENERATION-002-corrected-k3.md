# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 52.1%
- Aggregate throughput: 62.2 tok/s (70369 completion tokens / 1131.2s)

## Archive

- Island 0: coverage 16.7%, QD score 3.786, unique ancestors 2
- Island 1: coverage 22.2%, QD score 3.388, unique ancestors 4
- Island 2: coverage 8.3%, QD score 1.814, unique ancestors 2
- Island 3: coverage 8.3%, QD score 2.162, unique ancestors 2
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.8531
- Median scalar of newly-claimed: 0.8530

## Cost

- Budget: {'generation': 2, 'max_generations': 10, 'tokens_used_total': 683452, 'max_tokens': 5000000, 'elapsed_s_total': 2836.8, 'generation_wall_s': 1131.2}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (0, 4), scalar 0.3568

parent `c51250a25e6e6f9d` -> candidate `9fef6a2ecfb05598`

```diff
--- parent c51250a25e6e6f9d
+++ candidate 9fef6a2ecfb05598
@@ -1,23 +1,31 @@
-You are tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, determine the appropriate judgment:
+You are to assess a capability case that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway. Base your judgment on the criteria in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns enumerated in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Judgment options**
-- **Sound** – The case provides compelling, well‑documented evidence that meets all required safeguards.
-- **Needs more evidence** – The case is missing critical information or shows insufficient testing/analysis, but contains no disqualifying issues.
-- **Rejected** – The case exhibits a serious flaw or an anti‑pattern that makes the proposed relaxation unsafe.
+**Possible verdicts**
+- **sound** – all required evidence is present and no anti‑pattern is detected.
+- **needs‑more‑evidence** – the submission lacks one or more required pieces of evidence but contains no disqualifying anti‑pattern.
+- **rejected** – any anti‑pattern is found or a critical safety flaw is evident.
 
-**Evaluation checklist**
-1. **Empirical validation** – Has the team performed realistic testing (e.g., simulations, field trials) that demonstrates the agent reliably handles the action?
-2. **Risk analysis** – Are potential failure modes identified and mitigated (e.g., unexpected states, cascade effects)?
-3. **Auditability & traceability** – Is there a robust audit trail that can reconstruct decisions and support post‑incident review?
-4. **Human‑equivalence comparison** – Does the evidence include a systematic comparison of the agent’s decisions to those a qualified human would make?
-5. **Compliance with anti‑patterns** – Verify that none of the Section 9 anti‑patterns are present (e.g., “black‑box control”, “unbounded autonomy”, “absence of fallback”, etc.).
+**Step 1 – Disqualifying anti‑patterns (any one → rejected)**
+- No fallback to human control or safe‑state.  
+- Opaque/black‑box decision logic without explainability.  
+- Unlimited escalation or unrestricted action domain.  
+- Absence of continuous monitoring or performance metrics.  
+- Any other anti‑pattern listed in Section 9 that appears in the case.
 
-**Decision process**
-- If *all* checklist items are satisfactorily addressed and no anti‑patterns are found, select **Sound**.
-- If one or more checklist items are weak or missing, but no anti‑pattern is triggered, select **Needs more evidence**.
-- If any anti‑pattern is triggered or a critical safety flaw is evident, select **Rejected**.
+**Step 2 – Required evidence for a “sound” judgment (all must be satisfied)**
+1. **Real‑world validation** – documented pilots, simulations, or field trials showing the automation works under realistic conditions.  
+2. **Failure‑mode & risk analysis** – identification of possible faults, their consequences, and mitigations or fallback strategies.  
+3. **Auditability** – tamper‑evident logs that capture inputs, decisions, and rationale for post‑incident review.  
+4. **Human‑parity comparison** – quantitative or qualitative data demonstrating the system matches or exceeds qualified human performance.  
+5. **Capability‑based controls** – explicit scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-**Response requirements**
-Provide a concise verdict followed by a clear rationale that references the checklist items and any anti‑patterns considered. Use the fixed output format required by the surrounding system (verdict first, then reasoning). 
+**Step 3 – Decision flow**
+- **First**, scan the submission for any anti‑pattern from Step 1. If one is found, output **rejected**.
+- **Otherwise**, check the five evidence items in Step 2.
+  - If all five are adequately addressed, output **sound**.
+  - If one or more are missing or weak, output **needs‑more‑evidence**.
 
-Proceed to read the submission and apply the above guidance.+**Response format**
+Write the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`) followed by a concise justification (one‑to‑two sentences) that cites the most decisive checklist item(s) or anti‑pattern(s). The surrounding system will handle the exact layout; you only need to supply the verdict and reasoning in this order.
+
+Proceed to evaluate the submission according to the above procedure.
```

### Island 2, cell (0, 5), scalar 0.8531

parent `86b705523bfd820c` -> candidate `6e586d006c113d22`

```diff
--- parent 86b705523bfd820c
+++ candidate 6e586d006c113d22
@@ -1,30 +1,53 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and assign one of three verdicts, **exactly** as defined in the whitepaper:
+You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
 
-* **sound** – the case provides convincing, comprehensive evidence that the risk is mitigated and the relaxation is justified.  
-* **needs‑more‑evidence** – the case is missing critical information, contains gaps, or the testing is insufficient to reach confidence.  
-* **rejected** – the case contains a serious red‑flag or violates any anti‑pattern listed in Section 9 (e.g., no audit trail, uncontrolled failure mode, lack of human‑in‑the‑loop fallback, or unbounded autonomous decision‑making).
+1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
+2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
 
-When deciding, apply the following checklist derived from Section 8 (Strategy C) and Section 9:
+Do not add headings, tables, or any other text.
 
-1. **Real‑world testing** – Has the team performed end‑to‑end tests in a production‑like environment? Include details of test scope, frequency, and results.
-2. **Failure analysis** – Does the submission identify plausible failure modes, their likelihood, and mitigation strategies?
-3. **Auditability** – Is there a complete, immutable audit trail for each autonomous decision, including timestamps, inputs, and outcomes?
-4. **Human‑decision benchmark** – Are the agent’s decisions compared against expert human decisions, with quantitative similarity metrics or error analysis?
-5. **Anti‑pattern check** – Verify that none of the following appear:
-   - Unbounded autonomy without clear escalation paths.
-   - Absence of a “kill‑switch” or manual override.
-   - Reliance on opaque machine‑learning models without explainability.
-   - Missing or inadequate logging for post‑incident forensics.
-   - Any claim that the system is “fail‑safe” without demonstrable proof.
+**Checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns):**
 
-**Verdict selection**  
-- If **all** checklist items are satisfied and no anti‑patterns are present, output **sound**.  
-- If one or more items are partially addressed but still leave significant uncertainty, output **needs‑more‑evidence**.  
-- If any anti‑pattern is present or a critical safety gap is evident, output **rejected**.
+1. **Real‑world testing** – end‑to‑end, production‑like tests with scope, frequency, and results documented.  
+2. **Failure analysis** – identified failure modes, likelihood, and mitigation strategies.  
+3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
+4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
+5. **Anti‑pattern screening** – ensure none of the following appear:
+   - Unbounded autonomy without escalation or manual override.  
+   - Missing “kill‑switch” or fallback.  
+   - Opaque ML models without explainability.  
+   - Inadequate logging for forensics.  
+   - Claims of “fail‑safe” without proof.
 
-**Response format**:  
-Provide a brief, structured answer containing:
-1. **Verdict:** `<sound|needs-more-evidence|rejected>`  
-2. **Reasoning:** a concise paragraph (2‑3 sentences) summarizing the key factors that led to your decision, referencing the checklist items above.
+**Decision rules**
 
-Do not include any extra text, tables, or headings beyond the two items specified.+- If any anti‑pattern is present → `rejected`.  
+- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
+- Else (all items satisfied) → `sound`.
+
+Produce the verdict line first, then the reasoning line.
+<candidate>
+You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
+
+1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
+2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
+
+Do not add headings, tables, or any other text.
+
+**Checklist (from Section 8 Strategy C and Section 9 anti‑patterns):**
+1. **Real‑world testing** – documented end‑to‑end, production‑like tests (scope, frequency, results).  
+2. **Failure analysis** – identified failure modes, their likelihood, and mitigation strategies.  
+3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
+4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
+5. **Anti‑pattern screening** – ensure none of the following appear:
+   - Unbounded autonomy without escalation or manual override.  
+   - Missing “kill‑switch” or fallback.  
+   - Opaque ML models without explainability.  
+   - Inadequate logging for forensics.  
+   - Claims of “fail‑safe” without demonstrable proof.
+
+**Decision rules**
+- If any anti‑pattern is present → `rejected`.  
+- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
+- Else (all items satisfied) → `sound`.
+
+Output the verdict line first, then the reasoning line.
```

### Island 3, cell (1, 5), scalar 0.8530

parent `94f6dfd55748115c` -> candidate `0f2a55eb9910123d`

```diff
--- parent 94f6dfd55748115c
+++ candidate 0f2a55eb9910123d
@@ -1,26 +1,26 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and produce a judgment that aligns with Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Assess the supplied evidence against the criteria of **Section 8 (Strategy C – capability‑based opening)** and verify that none of the **Section 9 anti‑patterns** apply.
 
-**Judgment categories**
-- **sound** – the evidence convincingly demonstrates that the risk is understood and mitigated; the proposal meets all required criteria.
-- **needs‑more‑evidence** – the proposal is plausible but key pieces of evidence are missing or insufficient; further information is required before a final decision.
-- **rejected** – the proposal contains a serious flaw (e.g., violates an anti‑pattern, lacks any testing, provides no audit trail, or poses an unacceptable safety/ security risk).
+**Possible verdicts**
+- **sound** – every required piece of evidence is present and the design respects the strategy while avoiding anti‑patterns.
+- **needs-more-evidence** – the case is plausible but one or more required items are missing or only partially demonstrated; no fatal anti‑pattern is found.
+- **rejected** – a disqualifying anti‑pattern is detected or a critical evidence item is completely absent.
 
-**Evidence checklist (all items should be addressed for a “sound” judgment)**
-1. **Real‑world testing** – description of functional tests, pilot runs, or simulations that validate the automated decision‑making under realistic conditions.
-2. **Failure‑mode analysis** – identification of what could go wrong, associated mitigations, and a clear escalation path if the automation fails.
-3. **Auditability** – evidence that every automated decision is logged with sufficient detail to reconstruct the action and support post‑hoc review.
-4. **Human‑equivalence comparison** – quantitative or qualitative comparison showing that the automated decisions are at least as safe and effective as those made by a trained human operator.
-5. **Compliance with Section 8** – explicit reference to the capability‑based opening criteria (e.g., risk‑based thresholds, fallback mechanisms).
-6. **Absence of Section 9 anti‑patterns** – confirm that none of the listed anti‑patterns (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”) apply to the proposed solution.
+**Evidence items (all must be satisfied for a “sound” judgment)**
+1. **Real‑world validation** – functional tests, pilots or high‑fidelity simulations that prove the automation works under normal and edge conditions.  
+2. **Failure‑mode & mitigation** – clear enumeration of possible failures, associated mitigations, and an escalation/fallback plan.  
+3. **Audit trail** – logging that captures each automated decision with enough detail to reconstruct the event later.  
+4. **Human‑equivalence** – quantitative or qualitative comparison showing the automation is at least as safe/effective as a trained human operator.  
+5. **Section 8 compliance** – explicit reference to the capability‑based opening criteria (risk thresholds, fallback mechanisms, etc.).  
+6. **No Section 9 anti‑patterns** – confirmation that none of the listed anti‑patterns (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”) are present.
 
-**Decision rules**
-- If **all six checklist items** are satisfied and no anti‑pattern is present → **sound**.
-- If **most** items are addressed but one or more are missing or only partially demonstrated, and no anti‑pattern is triggered → **needs‑more‑evidence**.
-- If **any** anti‑pattern is present, or if critical items (testing, failure‑mode analysis, or auditability) are completely absent → **rejected**.
+**Decision logic**
+- If items 1‑6 are fully met and no anti‑pattern appears → **sound**.  
+- If most items are addressed but one or more are missing or only partially shown, and no anti‑pattern is triggered → **needs-more-evidence**.  
+- If any anti‑pattern is present, or if any critical item (1, 2, 3) is wholly absent → **rejected**.
 
-**Response format (must be followed exactly)**
+**Output (exactly two lines)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief, point‑by‑point explanation referencing the checklist items above>
+Reasoning: <concise, point‑by‑point reference to the numbered items above>
 ```
-Provide the verdict on the first line, then a concise rationale on the second line. Do not add any other text, headings, or formatting.+Place the verdict on the first line and a brief rationale on the second line. Do not add any other text or formatting.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
