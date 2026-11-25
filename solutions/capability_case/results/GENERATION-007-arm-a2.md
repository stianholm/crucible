# Generation 7 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 47.1%
- Aggregate throughput: 78.4 tok/s (82854 completion tokens / 1056.7s)

## Archive

- Island 0: coverage 16.7%, QD score 2.439, unique ancestors 3
- Island 1: coverage 13.9%, QD score 2.267, unique ancestors 2
- Island 2: coverage 13.9%, QD score 3.187, unique ancestors 3
- Island 3: coverage 13.9%, QD score 1.921, unique ancestors 2
- Cells newly claimed this generation: 5

## Quality

- Best scalar this generation: 0.1923
- Median scalar of newly-claimed: 0.1832

## Cost

- Budget: {'generation': 7, 'max_generations': 30, 'tokens_used_total': 1949189, 'max_tokens': 2000000, 'elapsed_s_total': 6769.4, 'generation_wall_s': 1056.7}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 2), scalar 0.1832

parent `47e006b3d34a1ae0` -> candidate `d9d86cd70e02e007`

```diff
--- parent 47e006b3d34a1ae0
+++ candidate d9d86cd70e02e007
@@ -1,26 +1,24 @@
-You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, produce a single verdict:
+You are evaluating a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, decide on a single verdict:
 
-* **sound** – the case fully demonstrates that risks are mitigated and automation is trustworthy.  
-* **needs-more-evidence** – the case is plausible but one or more required evidences are missing or insufficient.  
-* **rejected** – the case exhibits an anti‑pattern or a serious safety/security flaw.
+- **sound** – all required evidence is present and no anti‑pattern is detected.  
+- **needs‑more‑evidence** – the case is plausible but one or more required items are missing or insufficient.  
+- **rejected** – the case exhibits an anti‑pattern or a critical safety/security flaw.
 
-Assess the submission against these checkpoints:
+Assess the submission against these five checkpoints:
 
-1. **Real‑world testing** – end‑to‑end functional and stress tests in a production‑like setting, with documented results.  
-2. **Failure‑mode analysis** – clear identification of failure scenarios, likelihood estimates, and concrete mitigation or fallback measures.  
-3. **Auditability** – tamper‑evident logging that allows full reconstruction of every automated decision.  
+1. **Real‑world testing** – end‑to‑end functional and stress tests in a production‑like environment, with documented results.  
+2. **Failure‑mode analysis** – identified failure scenarios, likelihood estimates, and concrete mitigation or fallback measures.  
+3. **Auditability** – tamper‑evident logs that enable full reconstruction of every automated decision.  
 4. **Human‑decision baseline** – quantitative or qualitative comparison showing the automation aligns with expert human decisions.  
 5. **Anti‑pattern compliance** – no violation of any anti‑pattern listed in Section 9 (e.g., single point of failure, opaque reasoning, unbounded escalation).
 
 Decision hierarchy:
 
-* If checkpoint 5 fails → **rejected**.  
-* Else if any of checkpoints 1‑4 fail → **needs-more-evidence**.  
-* Else → **sound**.
+- If checkpoint 5 is not satisfied → **rejected**.  
+- Else if any of checkpoints 1‑4 are not satisfied → **needs‑more‑evidence**.  
+- Otherwise → **sound**.
 
-**Output** exactly two lines, with no extra text:
+**Output exactly two lines, with no extra text:**
 
 1. The verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
-2. One‑ to two‑sentence reason citing the most decisive checkpoint(s) that drove the decision.
-
-Do not include headings, bullet points, or any other formatting.+2. A one‑sentence reason that cites the most decisive checkpoint(s) (e.g., “fails anti‑pattern: opaque reasoning” or “missing real‑world testing results”).
```

### Island 0, cell (0, 2), scalar 0.1881

parent `47e006b3d34a1ae0` -> candidate `f4cb5c0ebd0db9ab`

```diff
--- parent 47e006b3d34a1ae0
+++ candidate f4cb5c0ebd0db9ab
@@ -1,26 +1,26 @@
-You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, produce a single verdict:
+You are evaluating a capability case that seeks to drop per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C)** and the **anti‑patterns from Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, choose a single verdict:
 
-* **sound** – the case fully demonstrates that risks are mitigated and automation is trustworthy.  
+* **sound** – all required evidence is present and no anti‑patterns are found.  
 * **needs-more-evidence** – the case is plausible but one or more required evidences are missing or insufficient.  
-* **rejected** – the case exhibits an anti‑pattern or a serious safety/security flaw.
+* **rejected** – the case exhibits any listed anti‑pattern or a serious safety/security flaw.
 
-Assess the submission against these checkpoints:
+Check the submission against these criteria:
 
-1. **Real‑world testing** – end‑to‑end functional and stress tests in a production‑like setting, with documented results.  
-2. **Failure‑mode analysis** – clear identification of failure scenarios, likelihood estimates, and concrete mitigation or fallback measures.  
-3. **Auditability** – tamper‑evident logging that allows full reconstruction of every automated decision.  
+1. **Real‑world testing** – documented end‑to‑end functional and stress tests in a production‑like environment.  
+2. **Failure‑mode analysis** – identified failure scenarios, likelihood estimates, and concrete mitigation or fallback measures.  
+3. **Auditability** – tamper‑evident logging that enables full reconstruction of every automated decision.  
 4. **Human‑decision baseline** – quantitative or qualitative comparison showing the automation aligns with expert human decisions.  
 5. **Anti‑pattern compliance** – no violation of any anti‑pattern listed in Section 9 (e.g., single point of failure, opaque reasoning, unbounded escalation).
 
-Decision hierarchy:
+**Decision hierarchy**
 
-* If checkpoint 5 fails → **rejected**.  
-* Else if any of checkpoints 1‑4 fail → **needs-more-evidence**.  
-* Else → **sound**.
+* If criterion 5 is violated → **rejected**.  
+* Else if any of criteria 1‑4 are violated → **needs-more-evidence**.  
+* Otherwise → **sound**.
 
 **Output** exactly two lines, with no extra text:
 
 1. The verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
-2. One‑ to two‑sentence reason citing the most decisive checkpoint(s) that drove the decision.
+2. A brief (one‑to‑two‑sentence) reason that cites the decisive criterion/criteria driving the decision.
 
 Do not include headings, bullet points, or any other formatting.
```

### Island 1, cell (0, 4), scalar 0.1790

parent `0eb670542d578872` -> candidate `74f605c48dc33a41`

```diff
--- parent 0eb670542d578872
+++ candidate 74f605c48dc33a41
@@ -1,22 +1,22 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Produce **exactly two lines**:
+You must assess a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Output **exactly two lines**:
 
-1. **Verdict** – one word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reason** – a brief justification (≤ 250 characters) that cites the checklist items or anti‑patterns that drove the decision.
+1. **Verdict** – a single word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Reason** – a concise justification (≤ 250 characters) that points to the checklist items or anti‑patterns influencing the verdict.
 
-### Checklist (from Sections 8 & 9)
+### Evaluation checklist (Sections 8 & 9)
 
-1. **Real‑world testing** – functional/integration tests in a production‑like environment, with scope, duration, and results.  
-2. **Failure analysis** – documented failure‑mode assessment, likelihood estimates, and concrete mitigations or contingency plans.  
-3. **Auditability** – immutable audit trail (logs, provenance) enabling post‑hoc reconstruction of decisions.  
-4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the autonomous system matches or exceeds a qualified human’s decisions.  
-5. **Anti‑pattern detection** – any anti‑pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, insufficient observability).
+1. **Real‑world testing** – evidence of functional/integration trials in an environment that mirrors production, including scope, duration, and outcomes.  
+2. **Failure‑mode analysis** – documented assessment of possible failures, their likelihood, and concrete mitigation or fallback measures.  
+3. **Auditability** – immutable logging or provenance that allows full reconstruction of the automated decision after the fact.  
+4. **Human‑decision benchmark** – quantitative or qualitative comparison showing the automated system meets or exceeds a qualified human’s decisions.  
+5. **Anti‑pattern detection** – any pattern listed in Section 9 (e.g., single point of failure, unchecked privilege escalation, lack of observability).
 
-### Decision hierarchy
-- If item 5 is identified → **rejected** (overrides everything).  
-- Else if items 1‑4 are all fully satisfied → **sound**.  
+### Decision rules
+- If item 5 is present → **rejected** (this overrides any other evidence).  
+- Else if items 1‑4 are each fully satisfied → **sound**.  
 - Otherwise → **needs-more-evidence**.
 
-### Output rules
-- No headings, bullet points, or extra text.  
-- Line 1: the verdict word.  
-- Line 2: the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).+### Output constraints
+- No headings, bullet points, or additional text.  
+- Line 1 must be the verdict word alone.  
+- Line 2 must be the reason, referencing the relevant checklist numbers or names (e.g., “missing real‑world testing”, “anti‑pattern: unchecked privilege escalation”).  
```

### Island 3, cell (0, 2), scalar 0.1923

parent `69fc2f7e679aa93b` -> candidate `3cf43b15fb35260c`

```diff
--- parent 69fc2f7e679aa93b
+++ candidate 3cf43b15fb35260c
@@ -1,20 +1,22 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use Section 8 (Strategy C, capability‑based opening) and the anti‑patterns defined in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are assessing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Evaluate the submission against the guidance in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence (all must be present unless an anti‑pattern is found)**  
-1. **Real‑world testing** – Controlled or production‑like trials, with description of scope, environment, and outcomes.  
-2. **Failure‑mode analysis** – Identification of plausible adverse scenarios plus mitigation or containment strategies.  
-3. **Auditability** – Tamper‑evident log that records the agent’s decisions, inputs, and context.  
-4. **Human‑decision alignment** – Quantitative or qualitative proof that the agent’s actions match or exceed those of a qualified human in the same situations.  
-5. **Anti‑pattern compliance** – The submission must contain **none** of the Section 9 anti‑patterns (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”). Any single occurrence is a disqualifier.
+**Evidence requirements (must all be present unless a Section 9 anti‑pattern is found)**  
+1. **Real‑world trial** – Description of a controlled or production‑like test, including scope, environment, and results.  
+2. **Failure‑mode study** – List of plausible adverse scenarios together with mitigation or containment actions.  
+3. **Audit trail** – Tamper‑evident logging that records the agent’s decisions, inputs, and context.  
+4. **Human‑alignment proof** – Quantitative or qualitative evidence that the agent’s actions match or exceed those of a qualified human under the same conditions.  
+5. **Anti‑pattern check** – The document must contain **none** of the Section 9 anti‑patterns (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”). Any single occurrence disqualifies the case.
 
-**Verdict rules**  
+**Verdict determination**  
 - **sound** – All five evidence items are satisfied and no anti‑patterns are detected.  
-- **needs‑more‑evidence** – One or more evidence items are insufficient or missing, but no anti‑patterns are present.  
-- **rejected** – Any anti‑pattern from Section 9 appears, regardless of other evidence.
+- **needs‑more‑evidence** – One or more evidence items are missing or insufficient, but no anti‑patterns appear.  
+- **rejected** – Any anti‑pattern from Section 9 is present, irrespective of other evidence.
 
-**Output format**  
-Provide **exactly one line** containing the verdict label (`sound`, `needs-more-evidence`, or `rejected`), a hyphen, and a brief justification (1–3 sentences) that references the criteria above. Example:
+**Response format**  
+Produce **exactly one line** containing:  
 
-`needs-more-evidence – real‑world testing is limited to simulation; other criteria are met.`
+`<verdict> – <brief justification>`  
+
+where `<verdict>` is `sound`, `needs‑more‑evidence`, or `rejected`, and the justification (1–3 sentences) cites the relevant criterion or anti‑pattern by name/number. No extra whitespace or lines are allowed.
 
 Respond now with your verdict and reasoning.
```

### Island 3, cell (1, 3), scalar -0.1262

parent `69fc2f7e679aa93b` -> candidate `e7cb1a425da7fa6b`

```diff
--- parent 69fc2f7e679aa93b
+++ candidate e7cb1a425da7fa6b
@@ -1,20 +1,21 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use Section 8 (Strategy C, capability‑based opening) and the anti‑patterns defined in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Apply **Section 8 (Strategy C – capability‑based opening)** and check for any **Section 9 anti‑patterns** from the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence (all must be present unless an anti‑pattern is found)**  
-1. **Real‑world testing** – Controlled or production‑like trials, with description of scope, environment, and outcomes.  
-2. **Failure‑mode analysis** – Identification of plausible adverse scenarios plus mitigation or containment strategies.  
-3. **Auditability** – Tamper‑evident log that records the agent’s decisions, inputs, and context.  
-4. **Human‑decision alignment** – Quantitative or qualitative proof that the agent’s actions match or exceed those of a qualified human in the same situations.  
-5. **Anti‑pattern compliance** – The submission must contain **none** of the Section 9 anti‑patterns (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”). Any single occurrence is a disqualifier.
+**Evidence checklist (all required unless the case is rejected for an anti‑pattern)**  
+1. **Real‑world testing** – description of controlled or production‑like trials, including scope, environment, and results.  
+2. **Failure‑mode analysis** – list of plausible adverse scenarios with concrete mitigation or containment measures.  
+3. **Auditability** – tamper‑evident log that records the agent’s decisions, inputs, and context.  
+4. **Human‑decision alignment** – quantitative or qualitative evidence that the agent’s actions are at least equivalent to those of a qualified human under the same conditions.  
+5. **Capability‑based opening compliance** – the proposal satisfies the bounded‑scope and success‑criteria requirements of Section 8.
 
-**Verdict rules**  
-- **sound** – All five evidence items are satisfied and no anti‑patterns are detected.  
-- **needs‑more‑evidence** – One or more evidence items are insufficient or missing, but no anti‑patterns are present.  
-- **rejected** – Any anti‑pattern from Section 9 appears, regardless of other evidence.
+**Anti‑pattern rule** – If the submission contains **any** of the Section 9 anti‑patterns (e.g., “unbounded autonomy”, “opaque decision logic”, “no rollback”, “absence of manual override”, “no fallback”, etc.), the verdict must be **rejected**, regardless of the evidence.
 
-**Output format**  
-Provide **exactly one line** containing the verdict label (`sound`, `needs-more-evidence`, or `rejected`), a hyphen, and a brief justification (1–3 sentences) that references the criteria above. Example:
+**Verdict mapping**  
+- **sound** – all five evidence items are fully satisfied and no anti‑patterns are present.  
+- **needs‑more‑evidence** – one or more evidence items are missing or insufficient, with no anti‑patterns detected.  
+- **rejected** – any anti‑pattern is present (or a fatal safety flaw).
+
+**Output** – produce **exactly one line**: `<verdict> – <brief justification (1‑3 sentences) referencing the criteria above>`. Example:
 
 `needs-more-evidence – real‑world testing is limited to simulation; other criteria are met.`
 
-Respond now with your verdict and reasoning.+Give your verdict now.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
