# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 69.6%
- Aggregate throughput: 111.9 tok/s (235859 completion tokens / 2108.4s)

## Archive

- Island 0: coverage 16.7%, QD score 3.630, unique ancestors 2
- Island 1: coverage 11.1%, QD score 2.049, unique ancestors 2
- Island 2: coverage 11.1%, QD score 2.286, unique ancestors 3
- Island 3: coverage 16.7%, QD score 4.108, unique ancestors 2
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.8524
- Median scalar of newly-claimed: 0.7497

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 3297930, 'max_tokens': 3000000, 'elapsed_s_total': 10120.7, 'generation_wall_s': 2108.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (0, 4), scalar 0.3605

parent `b52b002d4310bbbb` -> candidate `e75fe0406f9ed4c2`

```diff
--- parent b52b002d4310bbbb
+++ candidate e75fe0406f9ed4c2
@@ -1,28 +1,43 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow these steps and produce **only** the required output format (verdict and reasoning) as defined by the surrounding template.
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow the checklist **exactly** and output **only** the two required lines (verdict and reasoning) as defined by the surrounding template.
 
-**Evaluation steps**
+**Step 1 – Anti‑pattern screening (any match ⇒ REJECTED)**  
+Check the submission for any of the following anti‑patterns from Section 9:
 
-1. **Evidence of Real‑World Testing** – Check whether the submission includes concrete test results (e.g., pilot runs, simulations, field trials) that demonstrate the system works reliably under realistic conditions.
+- No manual override or safe‑state fallback.  
+- Opaque “black‑box only” logic (no explainability or traceability).  
+- Unbounded authority or runaway automation.  
+- Lack of rollback / irreversible actions.  
+- Removal of approval for regulatory‑ or safety‑critical actions.  
+- “Govern later” – governance, rollback, or monitoring not defined up‑front.
 
-2. **Risk‑Analysis** – Look for a documented analysis of potential failure modes, including worst‑case scenarios, impact assessments, and mitigation strategies.
+If any anti‑pattern is present, return **rejected** and cite the specific issue(s).
 
-3. **Auditability** – Verify that the proposal describes an immutable audit trail (e.g., logs, provenance metadata) that can be reviewed after each automated decision.
+**Step 2 – Mandatory evidence (absence ⇒ REJECTED)**  
+All three items must be present with concrete, verifiable data; otherwise the case is rejected.
 
-4. **Human‑Decision Benchmarking** – Confirm that the team has compared the automated agent’s decisions against a representative set of human decisions and quantified the agreement or error rates.
+1. **Real‑world testing** – includes pilot, sandbox, staged rollout, field trial, or similar evidence showing correct behavior under realistic load and failure conditions.  
+2. **Failure‑mode & risk analysis** – a documented enumeration of possible failures, their impact, and defined mitigation or safe‑state fallback procedures.  
+3. **Audit‑trail / observability** – immutable logs, provenance metadata, or other mechanisms that allow post‑hoc review of each automated decision.
 
-5. **Compliance with Anti‑Patterns (Section 9)** – Ensure the case does **not** contain any of the listed anti‑patterns (e.g., “black‑box only”, “no rollback”, “unbounded authority”, “absence of monitoring”).
+**Step 3 – Additional evidence (partial or missing ⇒ NEEDS‑MORE‑EVIDENCE)**  
+If the mandatory evidence is satisfied and no anti‑pattern was found, evaluate these two items:
 
-**Verdict criteria**
+4. **Human‑decision benchmarking** – quantitative or qualitative comparison of the automated decisions to those a qualified human would make, with error‑rate or agreement metrics.  
+5. **Governance & boundedness (Section 8)** – demonstrates the capability is bounded, reversible, quickly disableable, and stays within the organization’s risk tolerance.
 
-- **sound** – All five categories above are satisfied with concrete, verifiable evidence; no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more categories are partially addressed or missing, but no fatal anti‑pattern is found.
-- **rejected** – A serious anti‑pattern is present, or the evidence is fundamentally inadequate (e.g., no testing, no audit trail, or the risk analysis shows unacceptable danger).
+If both items are fully satisfied, the case is **sound**. If one or both are only partially addressed or missing, issue **needs‑more‑evidence** and reference the lacking item(s).
 
-**Output format**
+**Verdict hierarchy**
+
+- **rejected** – any anti‑pattern present *or* any mandatory evidence item completely absent.  
+- **needs‑more‑evidence** – no anti‑patterns, all mandatory evidence present, but at least one of the additional items is incomplete.  
+- **sound** – no anti‑patterns, all five items fully satisfied with concrete evidence.
+
+**Output format (must be followed exactly)**
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the relevant criteria>
+Reasoning: <concise explanation referencing the checklist items and/or anti‑pattern(s)>
 ```
 
-Provide the verdict on the first line and a brief, focussed reasoning on the second line. Do not add any additional commentary or sections.+Place the verdict on the first line and the reasoning on the second line. Do not add any other text, headings, or bullet points.
```

### Island 2, cell (0, 5), scalar 0.8524

parent `eac46ed259e320b2` -> candidate `8276e46de733fd0a`

```diff
--- parent eac46ed259e320b2
+++ candidate 8276e46de733fd0a
@@ -1,38 +1,36 @@
-You are assessing a capability case that proposes to relax or eliminate per‑action human approval for an industrial operational‑change gateway action.
+You are reviewing a capability case that seeks to remove or relax per‑action human approval for an industrial operational‑change gateway.
 
-**Goal:** Assign one of three verdicts – **Sound**, **Needs‑More‑Evidence**, or **Rejected** – by applying the checklist from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑Boundary‑as‑Architecture whitepaper.
+**Task:** Choose one verdict – **Sound**, **Needs‑More‑Evidence**, or **Rejected** – by applying the criteria from Section 8 (Strategy C) and the anti‑patterns from Section 9 of the ITOT‑Boundary‑as‑Architecture whitepaper.
 
-### Mandatory evidence dimensions  
-All four items **must be present**; if any is completely missing the case is **Rejected**.
+### Required evidence (all four must be present)
+- **Real‑world testing:** end‑to‑end trials in a production‑like setting; include scope, frequency, reproducibility.  
+- **Failure‑mode analysis:** enumerate safety/reliability/security failure modes, their likelihood, impact, and mitigations.  
+- **Auditability & traceability:** tamper‑evident log capturing decision source, timestamps, and justification.  
+- **Human‑baseline comparison:** quantitative benchmark showing the automated decision meets or exceeds qualified human performance.
 
-1. **Real‑world testing** – end‑to‑end tests in a production‑like environment; describe scope, frequency, and reproducibility.  
-2. **Failure‑mode analysis** – list possible safety, reliability, or security failures, their likelihood, impact, and mitigation.  
-3. **Auditability & traceability** – tamper‑evident log that records decision source, timestamps, and justification.  
-4. **Human‑baseline comparison** – quantitative benchmark showing the automated decision matches or exceeds qualified human performance.
-
-### Anti‑pattern check (Section 9)  
-If any of the following is found, the verdict is **Rejected** (overrides all other checks):
-
+### Disqualifying anti‑patterns (any one → **Rejected**)
 - Single point of failure without redundancy.  
 - Unbounded escalation with no fallback.  
 - Insufficient observability or logging.  
-- Missing rollback or safe‑stop mechanism.  
-- Decision‑transparency gaps preventing post‑hoc review.  
-- “Govern later” posture (governance or safeguards deferred to future phases).
+- Missing rollback / safe‑stop mechanism.  
+- Gaps in decision‑transparency that hinder post‑hoc review.  
+- “Govern later” stance (deferring safeguards to future phases).
 
-### Decision hierarchy
-1. **Anti‑pattern detected** → **Rejected**.  
-2. **Any mandatory evidence dimension absent** → **Rejected**.  
-3. **All dimensions present** but one or more contain **critical gaps** (e.g., limited test coverage, incomplete failure analysis, partial audit data, weak baseline comparison) → **Needs‑More‑Evidence**.  
+### Verdict decision flow
+1. Detect any anti‑pattern → **Rejected**.  
+2. Any required evidence item completely missing → **Rejected**.  
+3. All items present but one or more contain critical gaps (e.g., limited test coverage, incomplete failure analysis, partial audit data, weak baseline) → **Needs‑More‑Evidence**.  
 4. Otherwise → **Sound**.
 
-### Output format (must be reproduced exactly)
+### Output (must match exactly)
 
 ```
 Verdict: <Sound|Needs-More-Evidence|Rejected>
-Reasoning: <concise bullet‑pointed justification referencing the checklist items above>
+Reasoning:
+- <bullet point explaining the decisive factor(s)>
+- <additional bullet if needed>
 ```
 
-- Use one bullet (`-`) per line after **Reasoning:**.  
+- Use one dash (`-`) per line after **Reasoning:**.  
 - List only the factors that directly determined the verdict (e.g., “Missing real‑world testing”, “Anti‑pattern: single point of failure”).  
-- Do not add any other headings, prose, or decorative text.  +- No extra headings, prose, or decorative text.
```

### Island 3, cell (1, 5), scalar 0.7497

parent `e9123678cb2f570d` -> candidate `0851c75c8fc0b3c7`

```diff
--- parent e9123678cb2f570d
+++ candidate 0851c75c8fc0b3c7
@@ -1,17 +1,29 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the information supplied in the scenario, assign the case to one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using the scenario, assign **exactly one** verdict from the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-Base your decision on the following checklist derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9:
+### Mandatory evidence (all must be fully satisfied)
 
-1. **Empirical validation** – has the team performed realistic end‑to‑end testing in the intended environment?  
-2. **Risk and failure analysis** – are plausible failure modes identified and mitigations described?  
-3. **Auditability** – is there a verifiable log or trace that can be inspected after each automated decision?  
-4. **Human‑equivalence comparison** – does the submission provide data showing that the automated agent’s outcomes match or exceed those of a qualified human operator?  
-5. **Anti‑pattern screening** – does the proposal exhibit any of the disallowed patterns (e.g., “no‑fallback”, “opaque‑logic”, “single‑point‑automation”) described in Section 9?
+1. **Real‑world testing** – documented end‑to‑end tests performed in the target environment, covering normal operation, edge cases, and stress conditions, with results shown.  
+2. **Failure‑mode analysis** – a list of plausible failure modes, their likelihood/impact, and concrete mitigation or fallback procedures.  
+3. **Audit trail** – a tamper‑evident log or trace that records every automated decision, its inputs, and outcomes, and that can be inspected after the fact.  
+4. **Human‑equivalence data** – quantitative or qualitative evidence that the automated action’s outcomes match or exceed those of a qualified human operator.
 
-- If the case satisfies **all five** items, output **sound**.  
-- If one or more items are missing or insufficiently substantiated, output **needs‑more‑evidence**.  
-- If any anti‑pattern is present or a critical safety gap is evident, output **rejected**.
+### Anti‑patterns (any occurrence ⇒ immediate **rejected**)
 
-Your response must consist of exactly two lines:
-1. The verdict word (sound, needs‑more‑evidence, or rejected).  
-2. A concise justification (one‑to‑two sentences) referencing the relevant checklist items that led to your decision.+- **no‑fallback** – no manual override, emergency stop, or rollback.  
+- **opaque‑logic** – reliance on black‑box models without explainability.  
+- **single‑point‑automation** – a single point of failure with no redundancy.  
+- **we_will_govern_it_later** – governance, responsibility, or compliance not defined up‑front.  
+- Any other pattern listed in Section 9 of the whitepaper.
+
+### Decision hierarchy
+
+1. **Reject** – if any anti‑pattern is present **or** any mandatory evidence item is completely missing.  
+2. **Needs‑more‑evidence** – if all mandatory items are present but at least one is only partially substantiated (e.g., tests described but results absent, risk analysis lacking concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient). No anti‑pattern detected.  
+3. **Sound** – if every mandatory item is fully satisfied and no anti‑pattern appears.
+
+### Output (exactly two lines)
+
+1. The verdict word: `sound`, `needs‑more‑evidence`, or `rejected`.  
+2. One‑to‑two sentences citing the specific checklist items or anti‑patterns that led to your decision.
+
+Do not add any other text.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.127 vs base 0.482, 9.7 sigma below
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 19: **kept** — precision 0.980 >= base 0.881
- Lesson 11: **kept** — precision 0.857 vs base 0.937, only 0.6 sigma below

## Held-out check (best-ever candidate)

- Candidate: `0b1a8ebd10cfae2c` (rotation scalar 0.8544)
- Held-out quality: 0.8985 (passes: 0.9125, 0.8845)
- Held-out scalar: 0.7757 (passes: 0.7842, 0.7672)
- All held-out tasks valid: True
