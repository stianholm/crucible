# Generation 3 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 52.1%
- Aggregate throughput: 59.1 tok/s (61935 completion tokens / 1047.1s)

## Archive

- Island 0: coverage 19.4%, QD score 4.143, unique ancestors 2
- Island 1: coverage 27.8%, QD score 4.163, unique ancestors 4
- Island 2: coverage 11.1%, QD score 2.430, unique ancestors 2
- Island 3: coverage 11.1%, QD score 2.928, unique ancestors 2
- Cells newly claimed this generation: 9

## Quality

- Best scalar this generation: 0.8577
- Median scalar of newly-claimed: 0.6120

## Cost

- Budget: {'generation': 3, 'max_generations': 10, 'tokens_used_total': 906324, 'max_tokens': 5000000, 'elapsed_s_total': 3883.9, 'generation_wall_s': 1047.1}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 4), scalar 0.8577

parent `7182282bc5022a9e` -> candidate `753f3f82016cf250`

```diff
--- parent 7182282bc5022a9e
+++ candidate 753f3f82016cf250
@@ -1,34 +1,26 @@
-You are tasked with judging a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Your assessment must follow **Section 8 (Strategy C – capability‑based opening)** and avoid any **Section 9 anti‑patterns** from the ITOT‑boundary‑as‑architecture whitepaper.
+You are to evaluate a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Apply **Section 8 (Strategy C – capability‑based opening)** and reject any case that exhibits an **anti‑pattern from Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Evaluation Framework
+### Required evidence (all must be present)
+- **Real‑world validation** – end‑to‑end testing in a production‑like environment (including fault injection or field trial results).  
+- **Failure‑mode & mitigation analysis** – identified failure modes with likelihood, severity, and concrete countermeasures.  
+- **Auditability** – tamper‑evident logs capturing decisions, inputs, timestamps, and outcomes, reviewable by an independent party.  
+- **Human‑equivalence benchmark** – quantitative or qualitative proof that the autonomous action is at least as safe/effective as a qualified human operator.
 
-1. **Evidence Requirements** – Confirm that the submission includes **all** of the following:
-   - **Real‑world validation** – End‑to‑end testing in a production‑like environment (including fault injection or field trials).
-   - **Failure‑mode & mitigation analysis** – Identification of possible failures, their likelihood/severity, and concrete countermeasures.
-   - **Auditability** – Tamper‑evident logging of decisions, inputs, timestamps, and outcomes that can be independently reviewed.
-   - **Human‑equivalence benchmark** – Direct comparison (quantitative or qualitative) showing the autonomous action is at least as safe/effective as a qualified human operator.
+### Anti‑pattern disqualifiers (any one triggers REJECTED)
+- No defined rollback, safe‑state, or fallback procedure.  
+- Use of an opaque “black‑box” AI component lacking explainability/observability.  
+- Absence of independent verification or validation.  
+- Capability to bypass mandatory safety interlocks or other hard constraints.  
+- Any other pattern explicitly prohibited in Section 9.
 
-2. **Anti‑Pattern Check** – Scan for any of the listed red‑flags. The presence of **any** anti‑pattern automatically results in **REJECTED**:
-   - No defined rollback or safe‑state fallback.
-   - Use of opaque “black‑box” AI without explainability/observability.
-   - Absence of independent verification or validation.
-   - Capability to bypass mandatory safety interlocks.
-   - Unbounded escalation or missing revocation mechanisms.
-   - Any other pattern expressly prohibited in Section 9.
+### Verdict rules
+- **SOUND** – every evidence item is satisfied **and** no anti‑patterns are found.  
+- **NEEDS_MORE_EVIDENCE** – one or more evidence items are missing or insufficient, **and** no anti‑patterns are present.  
+- **REJECTED** – any anti‑pattern is detected, regardless of evidence completeness.
 
-### Verdict Logic
-
-- **SOUND** – Every evidence item in (1) is satisfied **and** no anti‑patterns from (2) are found.
-- **NEEDS_MORE_EVIDENCE** – One or more items in (1) are missing or insufficient, **and** no anti‑patterns are present.
-- **REJECTED** – Any anti‑pattern from (2) is detected, regardless of evidence completeness.
-
-### Output Specification
-
-Produce **exactly** the following format (no extra text):
-
+### Output format (exactly, no extra text)
 ```
-Verdict: <SOUND | NEEDS_MORE_EVIDENCE | REJECTED>
-Reasoning: <brief explanation citing the specific evidence items satisfied/absent and/or the anti‑pattern(s) that triggered the decision>
+Verdict: <SOUND|NEEDS_MORE_EVIDENCE|REJECTED>
+Reasoning: <concise explanation citing the specific evidence items satisfied/absent and/or the anti‑pattern(s) that led to the decision>
 ```
-
-The reasoning should be concise (one to three sentences) and reference the relevant checklist point(s) or anti‑pattern(s) that guided your judgment.+The reasoning should be one‑ or two‑sentence and reference the relevant checklist points or anti‑patterns.
```

### Island 0, cell (1, 4), scalar 0.1020

parent `2a3cb845d4a90dfc` -> candidate `b33ce3b7b8551fe4`

```diff
--- parent 2a3cb845d4a90dfc
+++ candidate b33ce3b7b8551fe4
@@ -1,25 +1,32 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that proposes eliminating per‑action human approval for an industrial operational‑change gateway. Base your assessment on **Section 8 (Strategy C – capability‑based opening)** and **Section 9 (anti‑patterns)** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Assessment steps**
+### Evaluation checklist
 
-1. **Core evidence checklist** – Verify that the submission provides:
-   - **Real‑world testing** of the automation under realistic conditions.
-   - **Failure‑mode analysis** that identifies what could go wrong and mitigation measures.
-   - **Audit‑trail mechanism** that records decisions, inputs, and outcomes.
-   - **Human‑equivalence comparison** showing how the agent’s decisions match or improve upon those of a human operator.
+1. **Mandatory evidence** – the submission must contain all of the following:
+   - **Real‑world validation** – end‑to‑end testing in a production‑like environment (including fault injection or field trial results).
+   - **Failure‑mode & mitigation analysis** – a systematic list of possible failures together with concrete mitigation or containment actions.
+   - **Auditable trail** – tamper‑evident logging of every automated decision, its inputs, timestamps, and outcomes.
+   - **Human‑equivalence benchmark** – quantitative or qualitative comparison showing the automated action is at least as safe/effective as a qualified human operator.
 
-2. **Anti‑pattern screening** – Look for any of the following red‑flags (if any are present, the case must be **REJECTED**):
-   - Absence of a rollback or safe‑state procedure.
-   - Reliance on “black‑box” AI without explainability or observability.
-   - Lack of independent verification or validation.
-   - Any indication that the system could bypass critical safety interlocks.
+2. **Anti‑pattern screening** – if any of these disqualifiers appear, the case is **REJECTED** regardless of other evidence:
+   - No defined rollback, safe‑state, or fallback procedure.
+   - Use of an opaque “black‑box” AI component without explainability, observability, or monitoring.
+   - Absence of independent verification/validation (e.g., third‑party review, peer audit).
+   - Capability to bypass mandatory safety interlocks or other hard constraints.
+   - Unbounded escalation or missing revocation mechanisms.
+   - Any other pattern explicitly prohibited in Section 9.
 
-3. **Verdict determination**
-   - If **all** core evidence items are present **and** no anti‑patterns are detected, label the case **SOUND**.
-   - If one or more core evidence items are missing or insufficient, but no anti‑patterns appear, label it **NEEDS_MORE_EVIDENCE**.
-   - If any anti‑pattern is found, label it **REJECTED**.
+### Verdict rules
 
-**Output**  
-State the verdict (`SOUND`, `NEEDS_MORE_EVIDENCE`, or `REJECTED`) followed by a concise justification that references the specific criteria or anti‑patterns that guided your decision.
+- **SOUND** – every mandatory evidence item is present **and** no anti‑patterns are found.
+- **NEEDS_MORE_EVIDENCE** – one or more mandatory items are missing or insufficient, **and** no anti‑patterns are present.
+- **REJECTED** – any anti‑pattern is detected.
 
-Respond with your verdict and reasoning.+### Output format (exactly)
+
+```
+Verdict: <SOUND | NEEDS_MORE_EVIDENCE | REJECTED>
+Reasoning: <brief statement referencing the specific evidence items satisfied/absent and/or the anti‑pattern(s) that determined the verdict>
+```
+
+Provide only the two lines above; do not add any other text.
```

### Island 1, cell (0, 2), scalar 0.3605

parent `112a9df19e383d20` -> candidate `bdb937fb3068930f`

```diff
--- parent 112a9df19e383d20
+++ candidate bdb937fb3068930f
@@ -1,26 +1,28 @@
-You are tasked with judging a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Examine the submitted scenario and assess it against the requirements from Section 8 (Strategy C, capability‑based opening) and the anti‑pattern list in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to evaluate a proposal that removes the per‑action human‑approval step for an industrial operational‑change gateway. Base your judgment on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence (all must be present for a “sound” result)**  
-1. **Operational testing** – documented pilots, simulations, or field‑trials that demonstrate the automated decision works safely in realistic conditions.  
-2. **Hazard analysis** – clear identification of failure modes, their impacts, and defined mitigations or safe‑state fall‑backs.  
-3. **Traceable logging** – tamper‑evident record of every decision, inputs, timestamps, and responsible entities.  
-4. **Human‑performance benchmark** – quantitative or qualitative comparison showing the automation meets or exceeds qualified human decision accuracy (e.g., concordance rate, false‑positive/negative limits).  
-5. **Capability limits** – explicit scope, confidence thresholds, and a revocation/override mechanism as required by Section 8.
+**Step 1 – Look for disqualifying anti‑patterns (any one ⇒ verdict = rejected)**
+- No immediate manual‑override or safe‑state fallback.  
+- Decision logic is opaque/black‑box with no explainability.  
+- Unlimited escalation authority or unrestricted action domain.  
+- Absence of continuous monitoring or performance metrics.  
+- Any other anti‑pattern described in Section 9 that appears in the submission.
 
-**Disqualifying anti‑patterns (any one forces “rejected”)**  
-- No immediate manual override or safe‑state fallback.  
-- Opaque/black‑box decision logic with no explainability.  
-- Unlimited escalation of authority or unbounded action domain.  
-- Missing continuous monitoring or performance metrics.  
-- Any other anti‑pattern enumerated in Section 9 that appears in the submission.
+If you find any, output **rejected** with a short reason.
 
-**Decision categories**  
-- **sound** – every evidence item 1‑5 is satisfied and none of the anti‑patterns appear.  
-- **needs-more-evidence** – one or more evidence items are absent or weak, but no disqualifying anti‑pattern is found.  
-- **rejected** – any anti‑pattern is present, or the risk justification is fundamentally inadequate.
+**Step 2 – Check the five required evidence items (all must be satisfied for “sound”)**
+1. **Operational validation** – pilots, simulations, or field trials proving the automation works safely in realistic conditions.  
+2. **Hazard / failure‑mode analysis** – identified faults, impacts, and defined mitigations or fallback procedures.  
+3. **Audit‑ready logging** – tamper‑evident records of each decision, inputs, timestamps, and responsible entities.  
+4. **Human‑performance comparison** – quantitative or qualitative data showing the automation meets or exceeds qualified human decision accuracy.  
+5. **Capability limits & controls** – explicit scope, confidence thresholds, and a revocation/override mechanism as required by Section 8.
 
-**Output**  
-Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (one or two sentences) that cites the most decisive evidence point(s) or anti‑pattern(s). Do not add any other text or formatting.
+If every item in Step 2 is adequately addressed and no anti‑pattern was found, output **sound**.
+
+**Step 3 – Otherwise**  
+If no anti‑pattern exists but one or more evidence items are missing or weak, output **needs-more-evidence**.
+
+**Output format**  
+Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by one‑to‑two sentences that cite the most decisive evidence point(s) or anti‑pattern(s). Do not add any other text or formatting.
 
 Example:  
-`sound – real‑world pilots and a full audit log are provided, and the fallback override is clearly defined.`+`sound – pilots and a full audit log are provided, and a manual override is clearly defined.`
```

### Island 1, cell (1, 2), scalar 0.4115

parent `2194be9c14e4f7f1` -> candidate `9ce42ee484d37ef0`

```diff
--- parent 2194be9c14e4f7f1
+++ candidate 9ce42ee484d37ef0
@@ -1,32 +1,31 @@
-You will assess a proposal that seeks to remove the per‑action human‑approval
-step for an operational‑change gateway in an industrial environment. Your
-judgment must follow the guidance in Section 8 (Strategy C, capability‑based
-opening) and the anti‑pattern checklist in Section 9 of the ITOT‑boundary‑as‑architecture
-whitepaper.
+You are to evaluate a proposal that wants to eliminate the per‑action human‑approval step for an operational‑change gateway in an industrial setting. Your assessment must follow the rules in **Section 8 (Strategy C, capability‑based opening)** and the anti‑pattern list in **Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper.
 
-Read the submission carefully and decide which of the three outcomes is
-appropriate:
+### Decision procedure
+1. **Search for disqualifying anti‑patterns** (any one triggers an automatic **Rejected**).  
+   - No fallback to human control or safe‑state.  
+   - Opaque/black‑box decision logic without explainability.  
+   - Unlimited escalation or unrestricted action domain.  
+   - Lack of continuous monitoring or performance metrics.  
+   - Any other anti‑pattern explicitly enumerated in Section 9 that appears in the submission.
 
-* **Sound** – The team supplies concrete test results, a complete failure‑mode
-  analysis, an auditable logging solution, and quantitative evidence that the
-  automated decisions are at least as reliable as human decisions. No
-  anti‑patterns from Section 9 are present.
+2. **If no anti‑pattern is found, verify the required evidence** for a **Sound** judgment. All items must be present and satisfactory:  
+   - **Real‑world validation** – pilots, simulations, or field trials demonstrating the automation works under realistic conditions.  
+   - **Failure‑mode & risk analysis** – identification of possible faults, their impacts, and mitigations or fallback strategies.  
+   - **Auditability** – tamper‑evident logs that record inputs, decisions, and rationale for post‑incident review.  
+   - **Human‑parity data** – quantitative or qualitative evidence that the automated decisions are at least as reliable as those of qualified humans.  
+   - **Capability‑based controls** – clear definition of scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-* **Needs more evidence** – The proposal includes some relevant material but
-  is missing one or more key elements (e.g., real‑world testing, thorough
-  risk assessment, audit trail, or sufficient human‑vs‑agent performance data).
-  Any identified anti‑patterns are acknowledged but not fully mitigated.
+3. **Determine the verdict**  
+   - If an anti‑pattern is detected → **Rejected**.  
+   - Else if **all** evidence items are satisfied → **Sound**.  
+   - Otherwise → **Needs more evidence**.
 
-* **Rejected** – The submission exhibits a serious violation of the
-  anti‑pattern list (e.g., uncontrolled escalation, hidden manual overrides,
-  lack of fallback, or any safety/security‑critical gap). The evidence does
-  not convincingly ensure safe operation.
+### Output format
+Provide exactly the two lines below, replacing the placeholders with your result and a brief justification (2‑4 sentences) that cites the most decisive checklist item(s) or anti‑pattern(s):
 
-After choosing the verdict, provide a brief justification (2‑4 sentences)
-explaining which criteria were met or lacking and why the selected outcome
-follows.
+```
+Verdict: <Sound|Needs more evidence|Rejected>
+Reasoning: <concise explanation>
+```
 
-Respond exactly in this format:
-
-Verdict: <Sound|Needs more evidence|Rejected>  
-Reasoning: <your concise explanation>+Do not add any other text.
```

### Island 1, cell (0, 4), scalar 0.3598

parent `d37dc06e0e8842b5` -> candidate `794afc7cb05b37e3`

```diff
--- parent d37dc06e0e8842b5
+++ candidate 794afc7cb05b37e3
@@ -1,28 +1,29 @@
-You are evaluating a proposal that seeks to remove per‑action human approval for an operational‑change gateway in an industrial system. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are reviewing a capability case that proposes to waive per‑action human approval for an operational‑change gateway. Use **Section 8 (Strategy C, capability‑based opening)** and the **anti‑patterns from Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper to reach one of three judgments: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Required evidence (must all be satisfied for a “sound” judgment)**
-1. **Real‑world validation** – pilots, simulations, or field trials that demonstrate the automated decision works under realistic conditions.  
-2. **Failure‑mode analysis** – explicit list of possible faults, their impact, and mitigation or safe‑state fallback.  
-3. **Auditable trail** – tamper‑evident logging of inputs, decisions, and rationale that can be inspected after the fact.  
-4. **Human‑parity data** – quantitative or qualitative comparison showing the agent’s performance matches or exceeds that of a qualified human (e.g., accuracy, false‑positive/negative rates).  
-5. **Capability‑based controls** – defined scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
+### 1. Disqualifying anti‑patterns (any single occurrence → **rejected**)
+- No fallback to human control or safe‑state.  
+- Opaque/black‑box decision logic without explainability.  
+- Unlimited escalation or unrestricted action domain.  
+- Absence of continuous monitoring or performance metrics.  
+- Any other anti‑pattern listed in Section 9 that appears in the submission.
 
-**Disqualifying anti‑patterns (any one triggers an automatic “rejected”)**
-- No fallback to human control or safe‑state.  
-- Opaque/black‑box decision logic with no explainability.  
-- Unlimited escalation or unrestricted action domain.  
-- Lack of continuous monitoring or performance metrics.  
-- Any other anti‑pattern explicitly listed in Section 9 that appears in the submission.
+### 2. Required evidence for a **sound** judgment (all must be satisfied)
+1. **Real‑world validation** – pilots, simulations, or field trials showing the automation works under realistic conditions.  
+2. **Failure‑mode & risk analysis** – identified faults, their impacts, and mitigations or safe‑state fallbacks.  
+3. **Auditable trail** – tamper‑evident logs of inputs, decisions, and rationales.  
+4. **Human‑parity data** – quantitative/qualitative comparison demonstrating performance equal to or better than a qualified human.  
+5. **Capability‑based controls** – clearly defined scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-**Decision logic**
-- **Rejected**: any anti‑pattern is present, or the risk analysis is fundamentally inadequate.  
-- **Sound**: all five evidence items are present *and* no anti‑patterns are detected.  
-- **Needs‑more‑evidence**: at least one evidence item is missing or weak, but no anti‑pattern is found.
+### 3. Decision flow
+- **Step A:** Scan the submission for any anti‑pattern from §1. If found, output **rejected**.  
+- **Step B:** If no anti‑pattern, check the five evidence items from §2.  
+  - If **all** are present and adequate → **sound**.  
+  - If at least one is missing or insufficient → **needs‑more‑evidence**.
 
-**Output format**
-Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by a single short justification (one or two sentences) that cites the most decisive evidence or anti‑pattern.
+### 4. Output format
+Produce a single line: the verdict word (`sound`, `needs‑more‑evidence`, or `rejected`) followed by a brief justification (one‑to‑two sentences) that cites the most decisive evidence item or anti‑pattern.
 
-Example:  
-`sound – pilot testing demonstrated 99 % success and a tamper‑evident audit log is provided.`
+**Example:**  
+`sound – pilot testing showed 99 % success and includes a tamper‑evident audit log.`
 
-Proceed to read the submission and apply the above rules.+Read the submission, apply the above rules, and respond accordingly.
```

### Island 2, cell (0, 4), scalar 0.6154

parent `6e586d006c113d22` -> candidate `d2f16a8137e6c2c5`

```diff
--- parent 6e586d006c113d22
+++ candidate d2f16a8137e6c2c5
@@ -1,53 +1,25 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
+You are evaluating a capability case that proposes to drop per‑action human approval for an industrial operational‑change gateway. After reviewing the supplied evidence, output **exactly two lines**:
 
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
-2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
+1. **Verdict:** `sound`, `needs-more-evidence`, or `rejected`  
+2. **Reasoning:** a concise (1‑2 sentence) explanation that references the most decisive checklist item(s) by number.
 
-Do not add headings, tables, or any other text.
+Do not include any other text, headings, or formatting.
 
-**Checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns):**
+**Checklist (Section 8 Strategy C & Section 9 anti‑patterns)**  
+1. Real‑world testing – documented end‑to‑end, production‑like tests (scope, frequency, results).  
+2. Failure analysis – identified failure modes, their likelihood, and mitigation measures.  
+3. Auditability – immutable log for each autonomous decision (timestamp, inputs, outcome).  
+4. Human‑decision benchmark – quantitative comparison with expert human decisions.  
+5. Anti‑pattern screening – ensure none of the following appear:  
+   – Unbounded autonomy without escalation or manual override.  
+   – Missing “kill‑switch” or fallback.  
+   – Opaque ML models lacking explainability.  
+   – Inadequate logging for forensics.  
+   – Claims of “fail‑safe” without proof.
 
-1. **Real‑world testing** – end‑to‑end, production‑like tests with scope, frequency, and results documented.  
-2. **Failure analysis** – identified failure modes, likelihood, and mitigation strategies.  
-3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
-4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
-5. **Anti‑pattern screening** – ensure none of the following appear:
-   - Unbounded autonomy without escalation or manual override.  
-   - Missing “kill‑switch” or fallback.  
-   - Opaque ML models without explainability.  
-   - Inadequate logging for forensics.  
-   - Claims of “fail‑safe” without proof.
-
-**Decision rules**
-
-- If any anti‑pattern is present → `rejected`.  
-- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
+**Decision hierarchy**  
+- If any item in #5 is present → `rejected`.  
+- Else if any of items 1‑4 is missing or only partially addressed → `needs-more-evidence`.  
 - Else (all items satisfied) → `sound`.
 
-Produce the verdict line first, then the reasoning line.
-<candidate>
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
-
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
-2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
-
-Do not add headings, tables, or any other text.
-
-**Checklist (from Section 8 Strategy C and Section 9 anti‑patterns):**
-1. **Real‑world testing** – documented end‑to‑end, production‑like tests (scope, frequency, results).  
-2. **Failure analysis** – identified failure modes, their likelihood, and mitigation strategies.  
-3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
-4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
-5. **Anti‑pattern screening** – ensure none of the following appear:
-   - Unbounded autonomy without escalation or manual override.  
-   - Missing “kill‑switch” or fallback.  
-   - Opaque ML models without explainability.  
-   - Inadequate logging for forensics.  
-   - Claims of “fail‑safe” without demonstrable proof.
-
-**Decision rules**
-- If any anti‑pattern is present → `rejected`.  
-- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
-- Else (all items satisfied) → `sound`.
-
-Output the verdict line first, then the reasoning line.+Provide the verdict line first, then the reasoning line.  
```

### Island 2, cell (0, 4), scalar 0.6157

parent `6e586d006c113d22` -> candidate `8818f99d6040c338`

```diff
--- parent 6e586d006c113d22
+++ candidate 8818f99d6040c338
@@ -1,53 +1,25 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
+You are evaluating a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. After reading the supplied evidence, output **exactly two lines**:
 
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
-2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
+1. **Verdict:** `sound`, `needs-more-evidence`, or `rejected` (prefixed with “Verdict: ”)  
+2. **Reasoning:** a brief sentence (1‑2 sentences) that cites the checklist item(s) that most strongly drive the decision (e.g., “fails item 3 – audit log missing”).
 
-Do not add headings, tables, or any other text.
+Do not include any other text, headings, or tables.
 
-**Checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns):**
-
-1. **Real‑world testing** – end‑to‑end, production‑like tests with scope, frequency, and results documented.  
-2. **Failure analysis** – identified failure modes, likelihood, and mitigation strategies.  
-3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
-4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
-5. **Anti‑pattern screening** – ensure none of the following appear:
+**Checklist (from Section 8 Strategy C and Section 9 anti‑patterns)**  
+1. Real‑world testing – documented end‑to‑end, production‑like trials (scope, frequency, results).  
+2. Failure analysis – identified failure modes, their likelihood, and mitigation plans.  
+3. Auditability – immutable audit record for every autonomous decision (timestamp, inputs, outcome).  
+4. Human‑decision benchmark – quantitative comparison to expert human decisions.  
+5. Anti‑pattern screening – ensure none of the following appear:  
    - Unbounded autonomy without escalation or manual override.  
-   - Missing “kill‑switch” or fallback.  
-   - Opaque ML models without explainability.  
+   - No “kill‑switch” or fallback.  
+   - Opaque ML models lacking explainability.  
    - Inadequate logging for forensics.  
    - Claims of “fail‑safe” without proof.
 
-**Decision rules**
+**Decision hierarchy**  
+- If any anti‑pattern (item 5) is present → verdict **rejected**.  
+- Else if any of items 1‑4 is missing or only partially addressed → verdict **needs-more-evidence**.  
+- Else (all items satisfied) → verdict **sound**.
 
-- If any anti‑pattern is present → `rejected`.  
-- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
-- Else (all items satisfied) → `sound`.
-
-Produce the verdict line first, then the reasoning line.
-<candidate>
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
-
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
-2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
-
-Do not add headings, tables, or any other text.
-
-**Checklist (from Section 8 Strategy C and Section 9 anti‑patterns):**
-1. **Real‑world testing** – documented end‑to‑end, production‑like tests (scope, frequency, results).  
-2. **Failure analysis** – identified failure modes, their likelihood, and mitigation strategies.  
-3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
-4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
-5. **Anti‑pattern screening** – ensure none of the following appear:
-   - Unbounded autonomy without escalation or manual override.  
-   - Missing “kill‑switch” or fallback.  
-   - Opaque ML models without explainability.  
-   - Inadequate logging for forensics.  
-   - Claims of “fail‑safe” without demonstrable proof.
-
-**Decision rules**
-- If any anti‑pattern is present → `rejected`.  
-- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
-- Else (all items satisfied) → `sound`.
-
-Output the verdict line first, then the reasoning line.+Follow the order: first line “Verdict: …”, second line “Reasoning: …”.
```

### Island 3, cell (0, 5), scalar 0.8572

parent `0f2a55eb9910123d` -> candidate `c1faa78ea857db24`

```diff
--- parent 0f2a55eb9910123d
+++ candidate c1faa78ea857db24
@@ -1,26 +1,22 @@
-You are reviewing a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Assess the supplied evidence against the criteria of **Section 8 (Strategy C – capability‑based opening)** and verify that none of the **Section 9 anti‑patterns** apply.
+You are evaluating a proposal that wants to drop the per‑action human‑approval step for an industrial operational‑change gateway.  
+Judge the submission by checking the six evidence categories below **and** confirming that none of the Section 9 anti‑patterns appear.
 
-**Possible verdicts**
-- **sound** – every required piece of evidence is present and the design respects the strategy while avoiding anti‑patterns.
-- **needs-more-evidence** – the case is plausible but one or more required items are missing or only partially demonstrated; no fatal anti‑pattern is found.
-- **rejected** – a disqualifying anti‑pattern is detected or a critical evidence item is completely absent.
+**Evidence categories (all must be satisfied for a “sound” judgment)**  
+1️⃣ Real‑world validation – functional tests, pilots or high‑fidelity simulations that demonstrate correct behavior in normal and edge cases.  
+2️⃣ Failure‑mode & mitigation – list of possible failures, mitigations, and an escalation/fallback plan.  
+3️⃣ Audit trail – logging that records every automated decision with enough detail for later reconstruction.  
+4️⃣ Human‑equivalence – quantitative or qualitative comparison showing the automation is at least as safe/effective as a trained human operator.  
+5️⃣ Section 8 compliance – explicit reference to the capability‑based opening criteria (risk thresholds, fallback mechanisms, etc.).  
+6️⃣ No Section 9 anti‑patterns – confirmation that none of the listed anti‑patterns (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”) are present.
 
-**Evidence items (all must be satisfied for a “sound” judgment)**
-1. **Real‑world validation** – functional tests, pilots or high‑fidelity simulations that prove the automation works under normal and edge conditions.  
-2. **Failure‑mode & mitigation** – clear enumeration of possible failures, associated mitigations, and an escalation/fallback plan.  
-3. **Audit trail** – logging that captures each automated decision with enough detail to reconstruct the event later.  
-4. **Human‑equivalence** – quantitative or qualitative comparison showing the automation is at least as safe/effective as a trained human operator.  
-5. **Section 8 compliance** – explicit reference to the capability‑based opening criteria (risk thresholds, fallback mechanisms, etc.).  
-6. **No Section 9 anti‑patterns** – confirmation that none of the listed anti‑patterns (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”) are present.
+**Decision rules**  
+- **Reject** immediately if any anti‑pattern is found **or** if any of items 1, 2, 3 are completely missing.  
+- If the submission passes the reject test and all six items are fully met → **sound**.  
+- If it passes the reject test but one or more items are only partially addressed → **needs‑more‑evidence**.
 
-**Decision logic**
-- If items 1‑6 are fully met and no anti‑pattern appears → **sound**.  
-- If most items are addressed but one or more are missing or only partially shown, and no anti‑pattern is triggered → **needs-more-evidence**.  
-- If any anti‑pattern is present, or if any critical item (1, 2, 3) is wholly absent → **rejected**.
-
-**Output (exactly two lines)**
+**Required output (exactly two lines)**  
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise, point‑by‑point reference to the numbered items above>
-```
-Place the verdict on the first line and a brief rationale on the second line. Do not add any other text or formatting.+Reasoning: <brief point‑by‑point reference to the numbered items above>
+```  
+Place the verdict on the first line and a concise rationale on the second line. Do not add any other text or formatting.
```

### Island 3, cell (0, 4), scalar 0.6120

parent `0f2a55eb9910123d` -> candidate `2e3c919946664f4e`

```diff
--- parent 0f2a55eb9910123d
+++ candidate 2e3c919946664f4e
@@ -1,26 +1,21 @@
-You are reviewing a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Assess the supplied evidence against the criteria of **Section 8 (Strategy C – capability‑based opening)** and verify that none of the **Section 9 anti‑patterns** apply.
+You are evaluating a proposal that wants to drop the per‑action human‑approval requirement for an industrial operational‑change gateway. Your judgment must be consistent with **Section 8 (Strategy C – capability‑based opening)** and must confirm that none of the **Section 9 anti‑patterns** are present.
 
-**Possible verdicts**
-- **sound** – every required piece of evidence is present and the design respects the strategy while avoiding anti‑patterns.
-- **needs-more-evidence** – the case is plausible but one or more required items are missing or only partially demonstrated; no fatal anti‑pattern is found.
-- **rejected** – a disqualifying anti‑pattern is detected or a critical evidence item is completely absent.
+**Required evidence (all must be satisfied for a “sound” verdict)**
+1. **Real‑world validation** – functional tests, pilots or high‑fidelity simulations showing correct behavior in normal and edge cases.  
+2. **Failure‑mode analysis & mitigation** – identified failure modes, mitigations, and a concrete escalation/fallback plan.  
+3. **Audit trail** – immutable logs that record every automated decision with sufficient detail for later reconstruction.  
+4. **Human‑equivalence** – quantitative or qualitative proof that the automation is at least as safe/effective as a trained human operator.  
+5. **Section 8 compliance** – explicit reference to the capability‑based opening criteria (risk thresholds, fallback mechanisms, etc.).  
+6. **No Section 9 anti‑patterns** – confirmation that the design avoids all listed anti‑patterns (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”).
 
-**Evidence items (all must be satisfied for a “sound” judgment)**
-1. **Real‑world validation** – functional tests, pilots or high‑fidelity simulations that prove the automation works under normal and edge conditions.  
-2. **Failure‑mode & mitigation** – clear enumeration of possible failures, associated mitigations, and an escalation/fallback plan.  
-3. **Audit trail** – logging that captures each automated decision with enough detail to reconstruct the event later.  
-4. **Human‑equivalence** – quantitative or qualitative comparison showing the automation is at least as safe/effective as a trained human operator.  
-5. **Section 8 compliance** – explicit reference to the capability‑based opening criteria (risk thresholds, fallback mechanisms, etc.).  
-6. **No Section 9 anti‑patterns** – confirmation that none of the listed anti‑patterns (e.g., “no‑fallback”, “black‑box control”, “unbounded authority”) are present.
-
-**Decision logic**
-- If items 1‑6 are fully met and no anti‑pattern appears → **sound**.  
-- If most items are addressed but one or more are missing or only partially shown, and no anti‑pattern is triggered → **needs-more-evidence**.  
-- If any anti‑pattern is present, or if any critical item (1, 2, 3) is wholly absent → **rejected**.
+**Decision rubric**
+- **sound** – items 1‑6 are fully met and no anti‑pattern is found.  
+- **needs‑more‑evidence** – most items are addressed but one or more are missing or only partially demonstrated; no anti‑pattern is triggered.  
+- **rejected** – any anti‑pattern is present, or any critical item (1, 2, 3) is completely absent.
 
 **Output (exactly two lines)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise, point‑by‑point reference to the numbered items above>
+Reasoning: <concise reference to the numbered items above>
 ```
 Place the verdict on the first line and a brief rationale on the second line. Do not add any other text or formatting.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
