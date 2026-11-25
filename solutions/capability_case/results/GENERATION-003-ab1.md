# Generation 3 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 62.3%
- Aggregate throughput: 101.8 tok/s (220005 completion tokens / 2161.5s)

## Archive

- Island 0: coverage 25.0%, QD score 4.052, unique ancestors 5
- Island 1: coverage 27.8%, QD score 4.504, unique ancestors 6
- Island 2: coverage 27.8%, QD score 4.612, unique ancestors 5
- Island 3: coverage 30.6%, QD score 5.208, unique ancestors 3
- Cells newly claimed this generation: 5

## Quality

- Best scalar this generation: 0.6544
- Median scalar of newly-claimed: 0.2910

## Cost

- Budget: {'generation': 3, 'max_generations': 10, 'tokens_used_total': 2463043, 'max_tokens': 8000000, 'elapsed_s_total': 10624.7, 'generation_wall_s': 2161.5}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 4), scalar 0.5257

parent `bc334ad36f3b5058` -> candidate `5901f5a4fd650bb8`

```diff
--- parent bc334ad36f3b5058
+++ candidate 5901f5a4fd650bb8
@@ -1,21 +1,25 @@
-You are an expert reviewer evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action, according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an expert reviewer evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action, following Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Assess the following five criteria.** For each, choose **✔️** (fully satisfied), **⚠️** (partially satisfied or missing but not fatal), or **❌** (unsatisfied and represents a critical anti‑pattern).
+**Checklist (mark each item with one of the symbols)**  
+- **✔️** – fully satisfied / present.  
+- **⚠️** – partially satisfied, missing details, but not a fatal flaw.  
+- **❌** – unsatisfied and constitutes a critical safety or anti‑pattern issue.
 
-1. **Real‑world testing** – controlled trials, production‑like simulations, documented results.  
-2. **Failure‑mode analysis** – identified failure scenarios with mitigations or safe‑fallbacks.  
-3. **Audit‑trail / observability** – tamper‑evident logging of decisions, inputs, and outcomes.  
-4. **Human‑parity benchmark** – quantitative/qualitative comparison with expert operators showing comparable performance.  
-5. **Anti‑pattern screening** – verify none of the Section 9 red‑flags are present (e.g., no rollback/override, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties).
+1. **Real‑world testing** – controlled trials or production‑like simulations with documented methodology and results.  
+2. **Failure‑mode analysis** – identified failure scenarios plus mitigations or safe‑fallback procedures.  
+3. **Audit‑trail / observability** – tamper‑evident logging of inputs, decisions, and outcomes.  
+4. **Human‑parity benchmark** – quantitative or qualitative comparison showing the automation matches or exceeds expert operators.  
+5. **Anti‑pattern screening** – confirm none of the Section 9 red‑flags are present (e.g., no manual‑override/rollback, opaque AI, over‑automation, missing monitoring, inadequate segregation of duties).
 
-**Decision mapping**
+**Decision rules**
 
-- If any item is marked **❌** (and it corresponds to an anti‑pattern), the verdict is **rejected**.  
-- Else if any item is marked **⚠️**, the verdict is **needs‑more‑evidence**.  
-- Else (all five items are **✔️**), the verdict is **sound**.
+- If **any** item is marked **❌** → **Verdict = rejected**.  
+- Else if **any** item is marked **⚠️** → **Verdict = needs‑more‑evidence**.  
+- Else (all five items are **✔️**) → **Verdict = sound**.
 
-**Output (exactly two lines, no extra text)**  
+**Output (exactly two lines, no extra characters or formatting)**  
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief justification referencing the specific items and symbols that drove the decision>
-```+Reasoning: <brief justification referencing the checklist items and symbols that determined the verdict>
+```
+Only these two lines may be produced.
```

### Island 2, cell (1, 4), scalar 0.2910

parent `0e857b2c169f75f4` -> candidate `d4d41fa8d21c027a`

```diff
--- parent 0e857b2c169f75f4
+++ candidate d4d41fa8d21c027a
@@ -1,20 +1,20 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are assessing a capability case that proposes to drop per‑action human approval for an industrial operational‑change gateway.
 
-**Mandatory evidence (Section 8)**  
-1. Real‑world testing  
-2. Failure‑mode analysis  
-3. Tamper‑evident audit‑trail of all autonomous decisions  
-4. Quantitative comparison of agent decisions to qualified human decisions  
+**Required evidence (Section 8)**  
+1. Real‑world testing under realistic conditions.  
+2. Comprehensive failure‑mode analysis with mitigations.  
+3. Tamper‑evident, queryable audit trail for every autonomous decision.  
+4. Quantitative comparison showing the agent’s decisions match or exceed those of qualified humans.
 
-**Anti‑patterns (Section 9)** – any listed anti‑pattern (e.g., single point of failure, unchecked autonomous loop, missing human‑in‑the‑loop fallback, hidden manual override, opaque decision logic) triggers a rejection.
+**Anti‑patterns (Section 9)** – The presence of any listed issue (e.g., single point of failure, unchecked autonomous loop, missing manual fallback, hidden override, opaque logic) mandates a **rejected** verdict.
 
-**Verdict rules**  
-- If any anti‑pattern is present → **rejected**.  
-- Else if all four evidence items are fully satisfied → **sound**.  
+**Decision rules**  
+- Any anti‑pattern found → **rejected**.  
+- Otherwise, if all four evidence items are fully satisfied → **sound**.  
 - Otherwise → **needs‑more‑evidence**.
 
 **Output format**  
-- First line: the verdict label exactly (`sound`, `needs‑more‑evidence`, or `rejected`).  
-- Following line(s) (max three short sentences): brief justification citing the relevant evidence items or anti‑pattern(s).  
+- Line 1: the verdict label exactly (`sound`, `needs‑more‑evidence`, or `rejected`).  
+- Line 2 (up to three brief sentences): justification that cites the relevant evidence numbers or anti‑pattern(s).  
 
-Do not include any other text or formatting.+Do not add any other text or formatting.
```

### Island 2, cell (1, 3), scalar 0.6544

parent `81abd5d79a724a22` -> candidate `80f4e83bf93db11a`

```diff
--- parent 81abd5d79a724a22
+++ candidate 80f4e83bf93db11a
@@ -1,21 +1,24 @@
-You are evaluating a capability case that asks to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the provided submission and decide which of the three possible judgments applies, based on Sections 8 (Strategy C) and 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Decide which of the three judgments applies, using Section 8 (Strategy C) and the anti‑patterns of Section 9 from the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Judgment options**
-- **SOUND** – the case provides sufficient, credible evidence that the risk is managed and the approval can be safely removed.
-- **MORE_EVIDENCE** – the case has gaps or weak points; additional testing, analysis, or documentation is needed before a sound judgment can be made.
-- **REJECT** – the case contains a serious flaw or anti‑pattern that makes the proposal unsafe or non‑compliant.
+**Possible judgments**
+- **SOUND** – evidence shows the risk is fully mitigated and the change can be approved without human sign‑off.
+- **MORE_EVIDENCE** – the submission is promising but lacks essential proof or contains notable gaps.
+- **REJECT** – a clear anti‑pattern or critical safety/compliance flaw is present.
 
-**Criteria to consider**
-1. **Real‑world testing** – has the team performed representative trials (including edge cases) and reported the results?
-2. **Failure‑mode analysis** – are potential adverse outcomes identified, quantified, and mitigated?
-3. **Auditability** – is there a reliable, tamper‑evident trail of the agent’s decisions and actions?
-4. **Human‑decision comparison** – does the agent’s behavior align with what a qualified human operator would do under the same circumstances?
-5. **Section 9 anti‑patterns** – does the proposal exhibit any of the listed anti‑patterns (e.g., “single point of failure”, “unchecked autonomy”, “lack of rollback”, etc.)?
-6. **Section 8 Strategy C alignment** – does the case adhere to the risk‑based justification and mitigation strategy described in Section 8?
+**Evaluation checklist**
+1. **Real‑world verification** – has the team run representative trials (including edge‑case and failure‑injection tests) and reported outcomes?
+2. **Failure‑mode & risk treatment** – are adverse scenarios identified, their likelihood quantified, and concrete mitigations described?
+3. **Audit trail** – does the proposal provide a tamper‑evident log that records inputs, decisions, timestamps, and justification?
+4. **Human benchmark** – is the autonomous behavior compared against qualified human operators with measurable agreement or error rates?
+5. **Anti‑pattern screening (Section 9)** – confirm none of the listed anti‑patterns appear (e.g., single point of failure, unchecked autonomy, missing rollback, black‑box without observability, no manual override).
+6. **Strategy C compliance (Section 8)** – does the case follow the risk‑based justification and mitigation framework outlined there?
 
-**Decision process**
-- If **all** criteria are satisfied and no anti‑patterns are present, output **SOUND**.
-- If most criteria are met but one or more significant gaps remain (e.g., missing failure‑mode analysis or incomplete audit trail), output **MORE_EVIDENCE**.
-- If any anti‑pattern is evident or a critical safety issue is identified, output **REJECT**.
+**Decision rules**
+- Output **SOUND** only if *all* checklist items are satisfied and no anti‑pattern is detected.
+- Output **MORE_EVIDENCE** if most items are addressed but one or more significant gaps remain (e.g., missing risk analysis or incomplete auditability) and no anti‑pattern is evident.
+- Output **REJECT** if any anti‑pattern is present or a critical safety/compliance issue is uncovered.
 
-Provide your verdict (one of the three words above) followed by a concise justification that references the most relevant criteria. Do not include any other text.+**Output format**
+Write the chosen judgment word (`SOUND`, `MORE_EVIDENCE`, or `REJECT`) followed by a brief justification that references the most relevant checklist items. Nothing else should be included.  
+Example:  
+`MORE_EVIDENCE – lacks full failure‑mode analysis and audit trail.`
```

### Island 2, cell (0, 2), scalar 0.2570

parent `81abd5d79a724a22` -> candidate `c2d3de44b0d68f68`

```diff
--- parent 81abd5d79a724a22
+++ candidate c2d3de44b0d68f68
@@ -1,21 +1,25 @@
-You are evaluating a capability case that asks to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the provided submission and decide which of the three possible judgments applies, based on Sections 8 (Strategy C) and 9 (anti‑patterns) of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that proposes to drop per‑action human approval for an industrial operational‑change gateway action. Decide **exactly one** of the three judgments: **SOUND**, **MORE_EVIDENCE**, or **REJECT**.
 
-**Judgment options**
-- **SOUND** – the case provides sufficient, credible evidence that the risk is managed and the approval can be safely removed.
-- **MORE_EVIDENCE** – the case has gaps or weak points; additional testing, analysis, or documentation is needed before a sound judgment can be made.
-- **REJECT** – the case contains a serious flaw or anti‑pattern that makes the proposal unsafe or non‑compliant.
+**Step 1 – Anti‑pattern scan (Section 9)**
+- Look for any listed anti‑pattern (e.g., single point of failure, unchecked autonomy, missing rollback, black‑box without observability, no manual override, etc.).
+- If **any** anti‑pattern is present → **REJECT** immediately.
 
-**Criteria to consider**
-1. **Real‑world testing** – has the team performed representative trials (including edge cases) and reported the results?
-2. **Failure‑mode analysis** – are potential adverse outcomes identified, quantified, and mitigated?
-3. **Auditability** – is there a reliable, tamper‑evident trail of the agent’s decisions and actions?
-4. **Human‑decision comparison** – does the agent’s behavior align with what a qualified human operator would do under the same circumstances?
-5. **Section 9 anti‑patterns** – does the proposal exhibit any of the listed anti‑patterns (e.g., “single point of failure”, “unchecked autonomy”, “lack of rollback”, etc.)?
-6. **Section 8 Strategy C alignment** – does the case adhere to the risk‑based justification and mitigation strategy described in Section 8?
+**Step 2 – Evidence checklist (Section 8, Strategy C)**
+Score each of the following criteria as 1 = satisfied, 0 = not satisfied.
 
-**Decision process**
-- If **all** criteria are satisfied and no anti‑patterns are present, output **SOUND**.
-- If most criteria are met but one or more significant gaps remain (e.g., missing failure‑mode analysis or incomplete audit trail), output **MORE_EVIDENCE**.
-- If any anti‑pattern is evident or a critical safety issue is identified, output **REJECT**.
+1. **Real‑world testing** – representative trials (including edge cases) reported.  
+2. **Failure‑mode analysis** – hazards identified, quantified, mitigated.  
+3. **Auditability** – tamper‑evident, traceable log of decisions/actions.  
+4. **Human‑decision benchmark** – behavior matches qualified human operator on comparable situations.  
+5. **Strategy C alignment** – risk‑based justification and mitigation as described in Section 8.
 
-Provide your verdict (one of the three words above) followed by a concise justification that references the most relevant criteria. Do not include any other text.+**Step 3 – Verdict**
+- If total score = 5 → **SOUND**.  
+- If total score = 3 or 4 → **MORE_EVIDENCE**.  
+- If total score ≤ 2 → **REJECT**.
+
+**Output**
+1. The single judgment word (SOUND, MORE_EVIDENCE, or REJECT).  
+2. A brief justification (< 30 words) that cites the most decisive factor(s) (e.g., “Reject: anti‑pattern ‘single point of failure’ detected” or “More evidence: audit trail missing”).
+
+Do not add any other text.  
```

### Island 3, cell (1, 4), scalar 0.1474

parent `db37a0c85828ee75` -> candidate `fb3bf49850e605cc`

```diff
--- parent db37a0c85828ee75
+++ candidate fb3bf49850e605cc
@@ -1,23 +1,24 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Base your judgment on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are judging a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Use Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-Assess the submission against **all** of the following criteria:
+**Decision process**
 
-1. **Real‑world testing** – evidence of functional testing in a realistic operational environment.  
-2. **Failure‑mode analysis** – identification of plausible failure scenarios and corresponding mitigations.  
-3. **Audit trail** – a tamper‑evident log that records the agent’s decisions and the data used.  
-4. **Human‑baseline comparison** – demonstration that the agent’s behavior matches or exceeds that of a qualified human operator in comparable situations.  
-5. **Anti‑pattern compliance** – the proposal must **not** exhibit any anti‑pattern from Section 9 (e.g., no‑fallback, hidden‑state, unbounded‑automation, single‑point‑failure, opaque‑logic, etc.).
+1. **Anti‑pattern check** – Scan the proposal for any anti‑pattern from Section 9 (e.g., no‑fallback, hidden‑state, unbounded‑automation, single‑point‑failure, opaque‑logic, etc.).  
+   • If any anti‑pattern is found → verdict **rejected** (stop, no further checks).
 
-Choose exactly one verdict:
+2. **Evidence checklist** – If no anti‑patterns are present, evaluate the five criteria below:  
+   - **Real‑world testing** – functional testing in a realistic operational environment.  
+   - **Failure‑mode analysis** – identification of plausible failures with mitigations.  
+   - **Audit trail** – tamper‑evident log of the agent’s decisions and input data.  
+   - **Human‑baseline comparison** – agent performance matches or exceeds a qualified human operator.  
+   - **Anti‑pattern compliance** – confirmation that none of the Section 9 anti‑patterns appear.  
 
-* **sound** – every criterion is fully satisfied and no anti‑pattern is present.  
-* **needs-more-evidence** – one or more criteria are only partially addressed or a minor anti‑pattern appears, but nothing is fatal.  
-* **rejected** – a critical anti‑pattern is evident, or essential testing/failure‑mode analysis is missing, making the risk unacceptable.
+   • If *all* five are fully satisfied → verdict **sound**.  
+   • If one or more are missing or only partially addressed → verdict **needs-more-evidence**.
 
-**Output format (do not add anything else):**
+**Output (exactly this structure, no extra text):**
 
 1. First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
 2. One blank line.  
-3. One or more sentences explaining the decision, explicitly citing the criteria that influenced it.
+3. One or more sentences explaining the decision, explicitly naming any anti‑pattern found or any checklist items that were lacking or insufficient.
 
-Follow this structure exactly.+Follow this format precisely. 
```


## A/B, stock versus distilled (this generation)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 15 | 15 | 15 | 0.3687 | 20.0% | 2241 |
| `proposer-distilled@/adapters/20261017` | 16 | 16 | 16 | 0.3377 | 12.5% | 2245 |

Paired difference, distilled minus stock, over 15 complete pairs: mean -0.0336 (sd 0.2658, se 0.0686), **-0.49 sigma**, p 0.632; distilled ahead in 8, tied in 0.

## A/B, stock versus distilled (the whole run)

| Arm | Proposed | Parsed | Scored | Mean scalar | Claim rate | Prompt tokens |
|---|---|---|---|---|---|---|
| `proposer` | 64 | 62 | 62 | 0.4207 | 56.5% | 2055 |
| `proposer-distilled@/adapters/20261017` | 64 | 63 | 63 | 0.4290 | 54.0% | 2019 |

Paired difference, distilled minus stock, over 60 complete pairs: mean +0.0111 (sd 0.2004, se 0.0259), **+0.43 sigma**, p 0.669; distilled ahead in 33, tied in 0.

## Proposal diversity (mean pairwise TF-IDF cosine distance)

| Generation | Stock | Distilled | Distilled / stock |
|---|---|---|---|
| 0 | 0.505 | 0.507 | 1.00 |
| 1 | 0.539 | 0.557 | 1.03 |
| 2 | 0.586 | 0.608 | 1.04 |
| 3 | 0.561 | 0.589 | 1.05 |

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below
