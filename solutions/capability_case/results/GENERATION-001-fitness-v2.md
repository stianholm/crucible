# Generation 1 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 29
- Prefix cache hit rate: 49.3%
- Aggregate throughput: 74.8 tok/s (72210 completion tokens / 965.4s)

## Archive

- Island 0: coverage 8.3%, QD score 1.057, unique ancestors 2
- Island 1: coverage 5.6%, QD score 0.712, unique ancestors 2
- Island 2: coverage 8.3%, QD score 1.064, unique ancestors 2
- Island 3: coverage 8.3%, QD score 1.061, unique ancestors 2
- Cells newly claimed this generation: 4

## Quality

- Best scalar this generation: 0.3548
- Median scalar of newly-claimed: 0.3515

## Cost

- Budget: {'generation': 1, 'max_generations': 30, 'tokens_used_total': 431299, 'max_tokens': 2000000, 'elapsed_s_total': 1331.1, 'generation_wall_s': 965.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 2), scalar 0.3493

parent `fee6775fe3c13a5e` -> candidate `9036e85f683667ca`

```diff
--- parent fee6775fe3c13a5e
+++ candidate 9036e85f683667ca
@@ -1,25 +1,24 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submission and produce a **single verdict**—one of the three exact tokens **sound**, **needs-more-evidence**, or **rejected**—followed by a brief justification.
+You are reviewing a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Read the submission and output **exactly two lines**:
 
-### Decision criteria (derived from Section 8 “Strategy C” and Section 9 anti‑patterns)
+1. **First line:** one of the three tokens `sound`, `needs-more-evidence`, or `rejected`.
+2. **Second line:** a brief justification (1‑2 sentences) that cites the checklist items below and notes any anti‑pattern violations.
 
-1. **Empirical validation** – Has the team performed real‑world or high‑fidelity simulated testing that demonstrates the agent can consistently perform the action safely?
-2. **Failure‑mode & risk analysis** – Is there a documented analysis of what could go wrong, including worst‑case scenarios, and mitigations or safe‑fallback procedures?
-3. **Auditability & traceability** – Does the proposal include an immutable audit trail (e.g., logs, timestamps, decision provenance) that allows post‑action review?
-4. **Human‑baseline comparison** – Are the agent’s decisions compared against a human‑performed baseline, showing equal or better safety/quality outcomes?
-5. **Alignment with anti‑patterns (Section 9)** – The proposal must NOT exhibit any of the following:
-   - **Uncontrolled delegation** – removing oversight without a compensating safety mechanism.
-   - **Opaque decision‑making** – lacking explainability or traceability.
-   - **Insufficient monitoring** – no real‑time health or performance monitoring.
-   - **No rollback / emergency stop** – inability to revert or halt the action quickly.
-   - **Over‑reliance on a single model** – no redundancy or diversity in decision sources.
+### Checklist (derived from Section 8 “Strategy C” and Section 9 anti‑patterns)
 
-### How to respond
-- **First line:** one of the exact tokens `sound`, `needs-more-evidence`, or `rejected`.
-- **Second line (optional but recommended):** a concise rationale (1‑3 sentences) that references the checklist items above, indicating which criteria are satisfied, which are missing, or which anti‑pattern is triggered.
+1. **Empirical validation** – evidence of real‑world or high‑fidelity simulation showing the agent can perform the action safely and consistently.  
+2. **Failure‑mode & risk analysis** – documented identification of worst‑case failures, their impacts, and corresponding mitigations or safe‑fallback procedures.  
+3. **Auditability & traceability** – immutable logs, timestamps, or provenance data that enable post‑action review.  
+4. **Human‑baseline comparison** – quantitative comparison with human‑executed actions demonstrating equal or superior safety/quality.  
+5. **Anti‑pattern compliance** – the proposal must **not** contain any of the following:
+   - Uncontrolled delegation (removing oversight without compensating safety)
+   - Opaque decision‑making (no explainability or traceability)
+   - Insufficient monitoring (no real‑time health/performance checks)
+   - No rollback / emergency stop (cannot quickly revert or halt the action)
+   - Over‑reliance on a single model (lack of redundancy or diversity)
 
-**Example output**
-```
-sound
-The submission includes extensive field testing, a full failure‑mode analysis with safe‑fallback, complete audit logs, and a quantitative human‑baseline comparison. No anti‑patterns are present.
-```
-Follow this format exactly; do not add extra headings or formatting.+### Decision rule
+- **Reject** (`rejected`) if any anti‑pattern is present or a critical safety/risk item is missing.
+- **Sound** (`sound`) if **all** five checklist items are satisfied and no anti‑patterns are found.
+- Otherwise, label **needs-more-evidence** (`needs-more-evidence`) when one or more items are partially addressed or missing but no fatal flaw exists.
+
+Follow the format precisely; do not add headings, bullet points, or extra lines.
```

### Island 0, cell (1, 2), scalar 0.3497

parent `06b6e346ce71a1ab` -> candidate `a55a8f92b3792310`

```diff
--- parent 06b6e346ce71a1ab
+++ candidate a55a8f92b3792310
@@ -1,20 +1,22 @@
-You are evaluating a proposal to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are reviewing a proposal to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, determine a single verdict: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-Assess the submission against the following checklist:
+**Checklist**
 
-1. **Empirical validation** – has the team performed realistic testing or simulation of the capability in the target environment?
-2. **Risk analysis** – are potential failure modes, safety impacts, and fallback strategies identified and addressed?
-3. **Auditability** – is there a clear, tamper‑evident log or trace that records the agent’s decisions and actions?
-4. **Human‑equivalence comparison** – does the evidence show that the autonomous decisions match or exceed the quality of a human operator in comparable scenarios?
-5. **Compliance with anti‑patterns** – does the proposal avoid the prohibited patterns from Section 9 (e.g., “no‑fallback”, “opaque decision‑making”, “unbounded escalation”)?
+1. **Empirical validation** – Has realistic testing or high‑fidelity simulation demonstrated safe performance in the target environment?  
+2. **Risk analysis** – Are failure modes, safety impacts, and fallback/rollback procedures identified and mitigated?  
+3. **Auditability** – Is there an immutable, tamper‑evident log or trace of decisions and actions?  
+4. **Human‑equivalence** – Does evidence show the autonomous decision‑making matches or exceeds a human operator’s quality/safety?  
+5. **Anti‑pattern compliance** – Does the proposal avoid all prohibited patterns from Section 9 (e.g., no‑fallback, opaque decision‑making, unbounded escalation, uncontrolled delegation, insufficient monitoring, single‑model reliance)?
 
 **Decision rule**
 
-- If the submission meets most checklist items, demonstrates robust testing, and shows no anti‑pattern violations, label it **sound**.
-- If one or more critical items are missing or only partially addressed, but there is no fatal flaw, label it **needs‑more‑evidence**.
-- If any checklist item reveals a serious breach of safety, auditability, or an anti‑pattern, label it **rejected**.
+- **sound** – most checklist items are fully satisfied, testing is robust, and no anti‑patterns are present.  
+- **needs‑more‑evidence** – one or more critical items are missing or only partially addressed, but no fatal safety or anti‑pattern violation is found.  
+- **rejected** – any item reveals a serious breach of safety, auditability, or a disallowed anti‑pattern.
 
-**Output**  
-Provide the verdict (exactly one of the three labels) followed by a concise justification referencing the relevant checklist items and any anti‑pattern concerns.
+**Output format**
 
-Respond with your verdict and your reasoning.+- **First line:** exactly one of the tokens `sound`, `needs-more-evidence`, or `rejected`.  
+- **Second line (optional but recommended):** a brief justification (1‑3 sentences) that cites the relevant checklist items and notes any anti‑pattern concerns.
+
+Provide the verdict and justification following this format, with no additional headings or formatting.
```

### Island 2, cell (1, 2), scalar 0.3548

parent `6690dcfc4f27ede8` -> candidate `3c98dee94f42075d`

```diff
--- parent 6690dcfc4f27ede8
+++ candidate 3c98dee94f42075d
@@ -1,24 +1,19 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are reviewing a capability case that seeks to remove per‑action human approval for an operational‑change gateway.
 
-**Task:**  
-Read the submitted case and classify it into one of three verdicts, exactly as the words below:
+**Goal**: Choose one of the exact labels below:
+- `sound` – the submission provides sufficient evidence that the automation is safe.  
+- `needs-more-evidence` – the case has notable gaps but no fatal flaw.  
+- `rejected` – a clear violation of a Section 9 anti‑pattern or an unaddressed high‑impact risk is present.
 
-- **sound** – the evidence sufficiently demonstrates that the change can be safely automated.  
-- **needs‑more‑evidence** – the case has notable gaps (e.g., missing testing, incomplete risk analysis, lacking audit‑trail, or insufficient comparison to human decisions) that prevent a confident approval.  
-- **rejected** – the submission contains a serious red‑flag — a clear violation of the anti‑patterns in Section 9, an unaddressed high‑impact risk, or any other condition that makes the proposal untenable.
+**Checklist (derived from Sections 8 and 9)**  
+1. **End‑to‑end testing** – realistic, production‑like trials covering normal and edge cases, with documented results.  
+2. **Failure‑mode & risk analysis** – identified failure modes, quantified impacts, and mitigation strategies.  
+3. **Auditability** – tamper‑evident log of inputs, decisions, and outcomes.  
+4. **Human‑baseline comparison** – systematic benchmarking against a qualified human operator, with performance metrics and acceptance thresholds.  
+5. **Anti‑pattern compliance** – no presence of any disallowed patterns from Section 9 (e.g., removal of all manual overrides, single‑point automation without fallback, hidden state propagation).
 
-**Evaluation criteria (derived from Section 8 and Section 9 of the ITOT‑boundary‑as‑architecture whitepaper):**
+**Output format** – exactly two lines:
+1. Verdict line: `sound`, `needs-more-evidence`, or `rejected`.  
+2. Reasoning line: a concise paragraph (no more than three sentences) indicating which checklist items are satisfied or lacking, and naming any specific red‑flag if the verdict is `rejected`.
 
-1. **Empirical testing** – has the team performed realistic, end‑to‑end tests of the automated decision‑making under expected and edge‑case conditions?  
-2. **Risk & failure analysis** – are potential failure modes identified, quantified, and mitigated?  
-3. **Auditability** – is there a robust, tamper‑evident log that records the agent’s decisions, inputs, and outcomes?  
-4. **Human‑equivalence comparison** – does the submission show a systematic comparison between the agent’s actions and those a qualified human would take, with performance metrics and acceptance thresholds?  
-5. **Compliance with anti‑patterns** – does the proposal avoid the disallowed patterns listed in Section 9 (e.g., delegating safety‑critical shutdowns without fallback, removing all manual overrides, or obscuring accountability)?
-
-**Output format:**  
-Provide a two‑part response:
-
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reasoning:** a concise paragraph (or short bullet list) explaining which criteria were satisfied or deficient, referencing any red‑flags if the verdict is `rejected`.
-
-Do not include any additional text, headings, or formatting beyond the two parts described.+Do not include any other text, headings, or formatting. 
```

### Island 3, cell (1, 2), scalar 0.3532

parent `3525d788dd8c46a7` -> candidate `ab1920e43e3bc867`

```diff
--- parent 3525d788dd8c46a7
+++ candidate ab1920e43e3bc867
@@ -1,25 +1,27 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are reviewing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway.
 
-**Task**
-- Read the submission and output **exactly one** verdict word followed by a brief reasoning (2‑4 sentences).  
-- The verdict must be one of the three literal strings: **sound**, **needs-more-evidence**, or **rejected**.
+**Your job**
+- Read the submission.
+- Write **exactly two lines**:
+  1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.
+  2. A concise justification (2‑3 sentences) that cites the relevant criteria.
 
-**Evaluation criteria**
-1. **Real‑world testing** – evidence of functional tests, pilot runs, or simulations that exercise the relaxed approval flow.  
-2. **Failure‑mode analysis** – identification of what could go wrong, mitigation strategies, and risk assessment.  
-3. **Auditability** – existence of logs, traceability, or other mechanisms that allow post‑hoc review of the system’s decisions.  
-4. **Human‑decision alignment** – comparison of the agent’s decisions with those a human would make, including any validation results.  
-5. **Compliance with Section 8 (Strategy C)** – the case must demonstrate a capability‑based justification for opening the gateway.  
-6. **Absence of anti‑patterns from Section 9** – any listed anti‑pattern (e.g., “no fallback”, “unbounded autonomy”, “opaque decision logic”) automatically forces a **rejected** verdict.
+**Evaluation checklist**
+1. **Real‑world evidence** – functional or pilot testing that actually exercises the relaxed flow.  
+2. **Failure‑mode analysis** – identified risks, mitigation plans, and a risk‑assessment summary.  
+3. **Auditability** – logging, traceability, or other post‑hoc review mechanisms.  
+4. **Human‑baseline comparison** – data showing the automated decision matches or exceeds human performance.  
+5. **Section 8 compliance** – a clear capability‑based justification for opening the gateway.  
+6. **Section 9 anti‑patterns** – any listed anti‑pattern (e.g., no fallback, unbounded autonomy, opaque logic) is an automatic **rejected**.
 
-**Decision rules**
-- If **all** applicable criteria are satisfied and no anti‑pattern is present, return **sound**.  
-- If the submission lacks sufficient evidence for one or more criteria but contains no outright red‑flags, return **needs-more-evidence**.  
-- If any anti‑pattern from Section 9 is identified, or if a critical safety or compliance issue is evident, return **rejected**.
+**Decision logic**
+- **Reject** if any anti‑pattern is present or a critical safety/compliance flaw is evident.  
+- **Needs‑more‑evidence** if one or more checklist items are absent or insufficient, but no anti‑pattern appears.  
+- **Sound** only when *all* checklist items are satisfied and no anti‑pattern is found.
 
 **Output format**
 ```
 <verdict>
 <reasoning>
 ```
-Replace `<verdict>` with the selected verdict word and `<reasoning>` with your concise justification referencing the criteria above.+Replace `<verdict>` with the chosen word and `<reasoning>` with your brief justification referencing the checklist items above.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629
