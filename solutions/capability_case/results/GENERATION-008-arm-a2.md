# Generation 8 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 47.4%
- Aggregate throughput: 262.9 tok/s (97163 completion tokens / 369.6s)

## Archive

- Island 0: coverage 16.7%, QD score 2.439, unique ancestors 3
- Island 1: coverage 16.7%, QD score 3.336, unique ancestors 2
- Island 2: coverage 13.9%, QD score 3.187, unique ancestors 3
- Island 3: coverage 13.9%, QD score 1.923, unique ancestors 2
- Cells newly claimed this generation: 4

## Quality

- Best scalar this generation: 0.5173
- Median scalar of newly-claimed: 0.5124

## Cost

- Budget: {'generation': 8, 'max_generations': 30, 'tokens_used_total': 2226725, 'max_tokens': 2000000, 'elapsed_s_total': 7139.2, 'generation_wall_s': 369.6}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (1, 1), scalar 0.5173

parent `0eb670542d578872` -> candidate `b64244a6912e068d`

```diff
--- parent 0eb670542d578872
+++ candidate b64244a6912e068d
@@ -1,22 +1,24 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Produce **exactly two lines**:
+You must judge a capability case that seeks to drop per‑action human approval for an industrial operational‑change gateway. Respond with **exactly two lines** and nothing else:
 
-1. **Verdict** – one word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items or anti‑patterns that drove the decision.
+1. **Verdict** – a single word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist item(s) or anti‑pattern responsible for the decision. Use the item number (1‑5) or its short name (e.g., “anti‑pattern: unchecked privilege escalation”).
 
-### Checklist (from Sections 8 & 9)
+### Checklist (Sections 8 & 9)
 
-1. **Real‑world testing** – functional/integration tests in a production‑like environment, with scope, duration, and results.  
-2. **Failure analysis** – documented failure‑mode assessment, likelihood estimates, and concrete mitigations or contingency plans.  
-3. **Auditability** – immutable audit trail (logs, provenance) enabling post‑hoc reconstruction of decisions.  
-4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system matches or exceeds a qualified human’s decisions.  
+1. **Real‑world testing** – production‑like functional/integration tests with scope, duration, and results.  
+2. **Failure analysis** – documented failure‑mode assessment, likelihood, and concrete mitigations or fallback plans.  
+3. **Auditability** – immutable audit trail enabling full reconstruction of decisions.  
+4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system matches or exceeds a qualified human.  
 5. **Anti‑pattern detection** – any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
 
 ### Decision hierarchy
-- If item 5 is identified → **rejected** (overrides everything).  
-- Else if items 1‑4 are all fully satisfied → **sound**.  
-- Otherwise → **needs-more-evidence**.
 
-### Output rules
-- No headings, bullet points, or extra text.  
-- Line 1: the verdict word.  
-- Line 2: the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).+- **If item 5 is present** → output `rejected`.  
+- **Else if items 1‑4 are all fully satisfied** → output `sound`.  
+- **Otherwise** → output `needs-more-evidence`.
+
+### Output constraints
+
+- No headings, bullet points, or extra text in the answer.  
+- Line 1: the verdict word only.  
+- Line 2: the reason, referencing the relevant checklist number(s) or name(s).
```

### Island 1, cell (1, 0), scalar 0.5171

parent `bc71c415c4ec8f84` -> candidate `fde5a573613fd9d2`

```diff
--- parent bc71c415c4ec8f84
+++ candidate fde5a573613fd9d2
@@ -1,23 +1,23 @@
-You must read the submitted capability case and issue a single verdict followed by a brief justification (exactly two lines, no extra text).
+Read the submitted capability case and produce **exactly two lines**.
 
-**Verdict options**
-- `sound` – evidence convincingly shows risk is mitigated and automation can replace per‑action human approval.
-- `needs-more-evidence` – the case is plausible but one or more required elements are insufficiently addressed.
-- `rejected` – the submission violates any anti‑pattern from Section 9 or contains a serious safety/security flaw.
+**Verdict options (use one word only):**
+- `sound`
+- `needs-more-evidence`
+- `rejected`
 
-**Decision process**
-1. **Anti‑pattern check** – if any anti‑pattern is present, output `rejected`.
-2. **Checklist completeness** – evaluate the five checkpoints below; if any checkpoint is missing or weak, output `needs-more-evidence`.
-3. If all checkpoints are adequately satisfied and no anti‑pattern is found, output `sound`.
-
-**Checkpoints to consider**
-- **Real‑world testing** – realistic functional & stress testing in a production‑like environment.
-- **Failure‑mode analysis** – documented failure scenarios, likelihood, and mitigation or fallback.
-- **Auditability** – tamper‑evident logs that allow full reconstruction of automated decisions.
-- **Human‑decision baseline** – quantitative or qualitative comparison with expert human decisions.
-- **Anti‑pattern compliance** – absence of Section 9 anti‑patterns (e.g., single point of failure, unbounded escalation, opaque reasoning).
+**Decision hierarchy**
+1. **Anti‑pattern detection** – if the case exhibits any anti‑pattern from Section 9, output `rejected`.
+2. **Checklist evaluation** – consider the five items below.  
+   - **Real‑world testing** – functional or stress testing in a production‑like environment.  
+   - **Failure‑mode analysis** – documented failure scenarios, their likelihood, and mitigations or fallback plans.  
+   - **Auditability** – tamper‑evident logs that allow full reconstruction of automated decisions.  
+   - **Human‑decision baseline** – quantitative or qualitative comparison with expert human decisions.  
+   - **Anti‑pattern compliance** – confirmation that none of the Section 9 anti‑patterns are present.  
+   If any of the first four items is missing, incomplete, or weak, output `needs-more-evidence`.
+3. If all five items are satisfied and no anti‑pattern was found, output `sound`.
 
 **Output format**
-Line 1: the verdict label (`sound`, `needs-more-evidence`, or `rejected`).  
-Line 2: a concise reason (1–3 sentences) that cites the most decisive checkpoint(s) leading to your decision.  
-Do not include headings, bullet points, or any other content.+- **Line 1:** the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+- **Line 2:** a concise justification (1–3 sentences, ≤ 250 characters) that cites the decisive checklist item(s) or anti‑pattern(s) that drove your decision.  
+
+Do not include headings, bullet points, or any additional text.  
```

### Island 1, cell (0, 0), scalar 0.4513

parent `9baee6b7d2d6eb3c` -> candidate `a57bd71112126d81`

```diff
--- parent 9baee6b7d2d6eb3c
+++ candidate a57bd71112126d81
@@ -1,24 +1,22 @@
-You are reviewing a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action. Examine the submission and produce **exactly one** verdict from the following categories (spelled exactly as shown):
+You are evaluating a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway. Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected** and give a brief justification.
 
-- **sound**
-- **needs‑more‑evidence**
-- **rejected**
+### Evaluation criteria (Sections 8 & 9)
 
-### Checklist (derived from Section 8 – Strategy C and Section 9 anti‑patterns)
+1. **Real‑world testing** – documented functional/integration tests in a production‑like environment, including scope, duration, and outcomes.  
+2. **Failure‑mode analysis** – identified failure scenarios, estimated likelihoods, and concrete mitigation or fallback measures.  
+3. **Auditability** – immutable logging or provenance that permits a full post‑hoc reconstruction of the automated decision.  
+4. **Human‑decision benchmark** – quantitative or qualitative evidence that the automated decision matches or exceeds that of a qualified human.  
+5. **Anti‑pattern detection** – any pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability). The presence of any anti‑pattern forces a **rejected** verdict.
 
-1. **Real‑world testing** – evidence of functional or integration tests in an environment that mirrors production (include scope, duration, results).
-2. **Failure analysis** – documented failure‑mode assessment with likelihoods and mitigations (what‑if scenarios, contingency plans).
-3. **Auditability** – provision of an immutable audit trail (logs, provenance) that enables post‑hoc reconstruction of decisions.
-4. **Human‑decision benchmark** – quantitative or qualitative comparison of the autonomous system’s decisions to those of a qualified human (performance metrics or validation study).
-5. **Anti‑pattern detection** – presence of any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability). Any occurrence forces a **rejected** verdict.
+### Decision hierarchy
+- If criterion 5 is satisfied → **rejected** (overrides all other evidence).  
+- Else if criteria 1‑4 are each fully satisfied → **sound**.  
+- Otherwise → **needs‑more‑evidence**.
 
-### Decision rule
-- **sound** – all five checklist items are fully satisfied and no anti‑pattern is found.  
-- **needs‑more‑evidence** – one or more of items 1‑4 are missing or only partially addressed, and no anti‑pattern is present.  
-- **rejected** – any anti‑pattern from item 5 is present, regardless of the other items.
+### Required output
+Produce **exactly two lines**:
 
-### Output
-1. **Verdict:** `<verdict>` (one of the three words above).  
-2. **Reasoning:** a brief explanation that cites the specific checklist items (or anti‑patterns) that led to your decision.
+1. Line 1: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+2. Line 2: a concise justification (≤ 250 characters) that cites the specific criteria or anti‑patterns influencing your decision (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).
 
-Do not add any other sections, headings, or formatting.+Do not add any other text, headings, or formatting.
```

### Island 3, cell (1, 2), scalar 0.5077

parent `69fc2f7e679aa93b` -> candidate `be0bef0f65ae3a05`

```diff
--- parent 69fc2f7e679aa93b
+++ candidate be0bef0f65ae3a05
@@ -1,20 +1,22 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use Section 8 (Strategy C, capability‑based opening) and the anti‑patterns defined in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are assessing a capability case that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Apply the criteria from Section 8 (Strategy C – capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence (all must be present unless an anti‑pattern is found)**  
-1. **Real‑world testing** – Controlled or production‑like trials, with description of scope, environment, and outcomes.  
-2. **Failure‑mode analysis** – Identification of plausible adverse scenarios plus mitigation or containment strategies.  
-3. **Auditability** – Tamper‑evident log that records the agent’s decisions, inputs, and context.  
-4. **Human‑decision alignment** – Quantitative or qualitative proof that the agent’s actions match or exceed those of a qualified human in the same situations.  
-5. **Anti‑pattern compliance** – The submission must contain **none** of the Section 9 anti‑patterns (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”). Any single occurrence is a disqualifier.
+**Evidence checklist (all must be present unless a Section 9 anti‑pattern is detected)**  
+1. **Real‑world trial** – Description of a controlled or production‑like test, including scope, environment, and results.  
+2. **Failure‑mode study** – List of credible adverse scenarios together with mitigation or containment plans.  
+3. **Audit trail** – Tamper‑evident logging of the agent’s decisions, inputs, and operating context.  
+4. **Human‑alignment evidence** – Quantitative or qualitative data showing the agent’s actions match or exceed those of a qualified human in comparable situations.  
+5. **Anti‑pattern clearance** – The submission must contain **no** anti‑patterns from Section 9 (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”). A single occurrence invalidates the case.
 
-**Verdict rules**  
-- **sound** – All five evidence items are satisfied and no anti‑patterns are detected.  
-- **needs‑more‑evidence** – One or more evidence items are insufficient or missing, but no anti‑patterns are present.  
-- **rejected** – Any anti‑pattern from Section 9 appears, regardless of other evidence.
+**Verdict determination**  
+- **sound** – Every item in the evidence checklist is satisfied and no anti‑patterns appear.  
+- **needs‑more‑evidence** – One or more checklist items are missing or insufficient, but no anti‑patterns are found.  
+- **rejected** – Any Section 9 anti‑pattern is present, regardless of other evidence.
 
-**Output format**  
-Provide **exactly one line** containing the verdict label (`sound`, `needs-more-evidence`, or `rejected`), a hyphen, and a brief justification (1–3 sentences) that references the criteria above. Example:
+**Response format**  
+Output **exactly one line**:  
 
-`needs-more-evidence – real‑world testing is limited to simulation; other criteria are met.`
+`<verdict> – <brief justification>`  
 
-Respond now with your verdict and reasoning.+where `<verdict>` is `sound`, `needs-more-evidence`, or `rejected`. The justification (1–3 sentences) must cite the relevant criterion or anti‑pattern by name or number. No extra whitespace or additional lines are allowed.
+
+Provide your verdict and reasoning now.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

## Held-out check (best-ever candidate)

- Candidate: `0eb670542d578872` (rotation scalar 0.8361)
- Held-out quality: 0.5682
- Held-out scalar: 0.4205
- All held-out tasks valid: False
