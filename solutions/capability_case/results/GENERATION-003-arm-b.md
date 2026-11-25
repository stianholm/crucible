# Generation 3 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 45.2%
- Aggregate throughput: 71.7 tok/s (118047 completion tokens / 1645.5s)

## Archive

- Island 0: coverage 16.7%, QD score 0.765, unique ancestors 1
- Island 1: coverage 11.1%, QD score 1.381, unique ancestors 2
- Island 2: coverage 16.7%, QD score 1.947, unique ancestors 1
- Island 3: coverage 19.4%, QD score 2.842, unique ancestors 2
- Cells newly claimed this generation: 8

## Quality

- Best scalar this generation: 0.5101
- Median scalar of newly-claimed: 0.1849

## Cost

- Budget: {'generation': 3, 'max_generations': 30, 'tokens_used_total': 1155988, 'max_tokens': 2000000, 'elapsed_s_total': 4983.7, 'generation_wall_s': 1645.5}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 2), scalar 0.1421

parent `e9ee8fb7fb3d9d88` -> candidate `c511753fc1991bfa`

```diff
--- parent e9ee8fb7fb3d9d88
+++ candidate c511753fc1991bfa
@@ -1,27 +1,31 @@
-You are reviewing a request that seeks to drop per‑action human approval for an industrial operational‑change gateway action. Choose exactly one of the three outcomes defined in the whitepaper:
+You are evaluating a request to eliminate per‑action human approval for an industrial operational‑change gateway. Select **exactly one** of the three conclusions defined in the whitepaper:
 
-* **sound** – the proposal convincingly demonstrates that the change can be executed safely without human approval.
-* **needs‑more‑evidence** – the idea is plausible but essential proof or controls are missing.
-* **reject** – the submission contains a critical flaw or breaks an anti‑pattern from Section 9.
+* **sound** – the submission provides complete, verifiable evidence that the change can be performed safely without any human step.
+* **needs‑more‑evidence** – the concept is plausible but one or more essential controls or proofs are missing or only partially addressed.
+* **reject** – the proposal contains a fatal defect, violates any anti‑pattern from Section 9, **or** it depends solely on the autonomous agent’s own reliability rather than an independent architectural safeguard.
 
-Assess the submission using the following criteria (derived from Section 8 – Strategy C and the anti‑pattern list). All items must be considered; missing or weak coverage influences the verdict.
+### Review checklist (all items must be examined)
 
-1. **Pre‑action validation** – Has a realistic, production‑like test been run *before* the change is enacted (not merely a nightly‑batch analysis)? Provide the test’s scope, metrics, and results.
-2. **Independent safeguard** – Does the design include an architectural safety net (e.g., a redundant controller, hard‑wired interlock, or external watchdog) that does not rely on the autonomous agent’s reliability?
-3. **Risk & failure‑mode analysis** – Are potential failures identified, quantified, and mitigated across hardware, software, and operator error? Look for a systematic “what‑if” assessment.
-4. **Audit trail** – Is there a verifiable log that records each automated decision, its context, and any overrides, satisfying traceability requirements?
-5. **Human‑parity evidence** – Does the case present a side‑by‑side comparison of the agent’s decisions with those of a qualified human, including statistical measures such as accuracy, false‑positive/negative rates?
-6. **Anti‑pattern compliance** – Ensure none of the Section 9 anti‑patterns appear, e.g., (a) single point of failure without redundancy, (b) opaque “black‑box” decision making, (c) unbounded escalation without safe‑stop, (d) any other listed pattern.
+1. **Real‑world pre‑action test** – Has a production‑scale trial been executed *before* the change is applied? Summarize the environment, metrics collected, and outcomes.
+2. **Comprehensive risk & failure‑mode study** – Does the document enumerate hardware, software, and operator‑error failure modes, quantify their likelihood/severity, and prescribe mitigations?
+3. **Independent architectural safeguard** – Is there a safety mechanism that operates outside the agent’s control (e.g., redundant controller, hard‑wired interlock, external watchdog, hardware fail‑safe)? Reliance on the agent’s self‑check is **insufficient**.
+4. **Tamper‑evident audit trail** – Are all automated decisions logged with context, timestamps, and any manual overrides, satisfying traceability requirements?
+5. **Human‑parity evaluation** – Does the case include side‑by‑side statistical results comparing the agent’s decisions to those of qualified humans (accuracy, false‑positive/negative rates, confidence intervals)?
+6. **Anti‑pattern audit (Section 9)** – Verify that none of the listed anti‑patterns appear, specifically:
+   - a) single point of failure without redundancy,
+   - b) opaque “black‑box” reasoning,
+   - c) unbounded escalation lacking a safe‑stop,
+   - d) any other enumerated pattern.
 
-**Decision logic**
+### Decision rules
 
-* **sound** – every criterion above is fully satisfied and no anti‑pattern is present.
-* **needs‑more‑evidence** – one or more criteria are only partially addressed or missing, but no fatal anti‑pattern is detected.
-* **reject** – any criterion fails catastrophically or any Section 9 anti‑pattern is found.
+* **sound** – every checklist item (1‑6) is fully satisfied and no anti‑pattern is present.
+* **needs‑more‑evidence** – one or more items are only partially satisfied or missing, **but** no item is catastrophically unsatisfied and no anti‑pattern is detected.
+* **reject** – any checklist item is entirely unsatisfied, an anti‑pattern is found, **or** the design lacks an independent architectural safeguard (Item 3) and instead leans on the agent’s own reliability.
 
-**Output format**
+### Output format (do not deviate)
 
-1. On the first line, write the verdict exactly as **sound**, **needs‑more‑evidence**, or **reject**.  
-2. On subsequent lines, give a concise justification, citing the specific checklist items that drove your decision.
+1. First line: the verdict – exactly **sound**, **needs‑more‑evidence**, or **reject**.  
+2. Subsequent lines: a brief justification that cites the checklist numbers (or sub‑items) that determined your decision, e.g., “Missing independent safeguard (Item 3)” or “Partial risk analysis (Item 2)”.
 
-Proceed with the evaluation.+Carry out the assessment now.
```

### Island 0, cell (0, 3), scalar 0.0264

parent `950a0d726f1ba338` -> candidate `df0d52b8f0f2f96e`

```diff
--- parent 950a0d726f1ba338
+++ candidate df0d52b8f0f2f96e
@@ -1,31 +1,36 @@
-You are acting as the reviewer for a request that aims to eliminate the per‑action human approval step for an industrial operational‑change gateway. Choose **exactly one** of the three possible conclusions defined in the whitepaper:
+You are the reviewer for a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway. Choose **exactly one** of the three outcomes defined in the whitepaper:
 
-* **sound** – the proposal provides solid, verifiable evidence that the change can be performed safely without a human in the loop.  
-* **needs‑more‑evidence** – the concept is reasonable but one or more essential proofs or controls are missing or only partially addressed.  
-* **reject** – the submission contains a critical defect, breaches any anti‑pattern from Section 9, **or** it relies solely on the autonomous agent’s own reliability without an independent safety mechanism.
+* **sound** – the submission convincingly demonstrates that the change can be performed safely without human intervention.  
+* **needs‑more‑evidence** – the concept is plausible but one or more essential controls or proofs are missing or only partially addressed.  
+* **reject** – the proposal contains a fatal flaw, violates any anti‑pattern from Section 9, **or** it lacks an independent architectural safeguard (relying only on the agent’s own reliability).
 
-### Review checklist (evaluate sequentially)
+### Evaluation criteria (assess each in order)
 
-1. **Real‑world pre‑action testing** – Has a pilot or field‑scale experiment been conducted *before* the change is deployed? Cite the test environment, measured metrics, and outcomes.  
-2. **Full‑scope risk & failure‑mode study** – Are all plausible failure categories (hardware, software, operator error) identified, quantified, and mitigated with concrete controls?  
-3. **External safety net** – Does the design incorporate an architectural safeguard that operates independently of the agent (e.g., redundant controller, hard‑wired interlock, watchdog timer)? Reliance on the agent’s internal self‑check is **insufficient**.  
-4. **Traceable audit log** – Is there a tamper‑evident record of every automated decision, including context, timestamps, and any manual overrides, meeting the traceability requirement?  
-5. **Human‑parity data** – Are side‑by‑side statistical results supplied that compare the agent’s decisions to those of qualified humans (accuracy, false‑positive/negative rates, confidence intervals)?  
-6. **Anti‑pattern audit (Section 9)** – Verify that none of the listed anti‑patterns appear, specifically:  
-   - a) single point of failure without redundancy,  
-   - b) opaque “black‑box” reasoning,  
-   - c) unbounded escalation lacking a safe‑stop,  
-   - d) any other enumerated pattern.
+**A. Real‑world pre‑deployment trial** – Has a pilot or field‑scale test been run *before* the change is live? Provide the test setting, measured metrics, and results.
 
-### Decision matrix
+**B. Comprehensive risk & failure‑mode analysis** – Are all relevant failure modes (hardware, software, operator error) identified, quantified, and mitigated with concrete controls?
 
-* **sound** – every checklist item (1‑6) is fully satisfied and no anti‑pattern is detected.  
-* **needs‑more‑evidence** – at least one item is only partially satisfied or omitted, **but** no item is completely unsatisfied and no anti‑pattern is present.  
-* **reject** – any item is marked **not satisfied** **or** any anti‑pattern is identified. When rejecting, explicitly state that the lack of an independent architectural safeguard (Item 3) or reliance on the agent’s own reliability is the decisive flaw.
+**C. Independent safety net** – Does the design embed an external safeguard that operates independently of the autonomous agent (e.g., redundant controller, hard‑wired interlock, external watchdog)? A safeguard that is merely the agent checking itself does **not** count.
 
-### Required output
+**D. Tamper‑evident audit log** – Is there a secure, traceable record of every automated decision, including context, timestamps, and any manual overrides?
 
-1. First line: the verdict, exactly **sound**, **needs‑more‑evidence**, or **reject**.  
-2. Following lines: a brief rationale, referencing the checklist numbers that influenced the verdict (e.g., “Missing independent safety net (Item 3)”).  
+**E. Human‑parity evidence** – Are side‑by‑side statistical comparisons with qualified human decisions supplied (accuracy, false‑positive/negative rates, confidence intervals)?
 
-Proceed with the evaluation now.+**F. Anti‑pattern compliance (Section 9)** – Verify that none of the listed anti‑patterns appear:
+  1. Single point of failure without redundancy  
+  2. Opaque “black‑box” reasoning  
+  3. Unbounded escalation lacking a safe‑stop  
+  4. Any other enumerated pattern
+
+### Decision hierarchy
+
+1. **Reject** – if any criterion **A–E** is **not satisfied** (i.e., completely missing or fails) **or** any anti‑pattern in **F** is identified. When rejecting, explicitly note the absence of an independent safety net (Criterion C) if that is the decisive issue.  
+2. **Needs‑more‑evidence** – if all criteria are at least partially satisfied, but one or more (A–E) are only **partially** addressed, and no anti‑pattern is present.  
+3. **Sound** – only when every criterion A–E is fully satisfied and no anti‑pattern from F is found.
+
+### Required output format
+
+1. **First line:** the verdict – exactly **sound**, **needs‑more‑evidence**, or **reject**.  
+2. **Subsequent lines:** a concise justification, citing the relevant criterion letters (e.g., “Missing independent safety net (C)”, “Partial risk analysis (B)”).  
+
+Proceed with the assessment now.
```

### Island 0, cell (0, 2), scalar 0.1759

parent `e9ee8fb7fb3d9d88` -> candidate `6ffdfdc5e2bc6f8b`

```diff
--- parent e9ee8fb7fb3d9d88
+++ candidate 6ffdfdc5e2bc6f8b
@@ -1,27 +1,28 @@
-You are reviewing a request that seeks to drop per‑action human approval for an industrial operational‑change gateway action. Choose exactly one of the three outcomes defined in the whitepaper:
+You are reviewing a request to eliminate per‑action human approval for an industrial operational‑change gateway. Select **exactly one** outcome defined in the whitepaper:
 
-* **sound** – the proposal convincingly demonstrates that the change can be executed safely without human approval.
-* **needs‑more‑evidence** – the idea is plausible but essential proof or controls are missing.
-* **reject** – the submission contains a critical flaw or breaks an anti‑pattern from Section 9.
+* **sound** – the proposal provides complete, verifiable evidence that the change can be performed safely without human approval.  
+* **needs‑more‑evidence** – the idea is plausible but one or more essential pieces of proof or control are missing or only partially addressed.  
+* **reject** – the submission contains a fatal flaw, violates any Section 9 anti‑pattern, **or** lacks an independent architectural safeguard (i.e., it relies solely on the autonomous agent’s own reliability).
 
-Assess the submission using the following criteria (derived from Section 8 – Strategy C and the anti‑pattern list). All items must be considered; missing or weak coverage influences the verdict.
+### Review checklist
 
-1. **Pre‑action validation** – Has a realistic, production‑like test been run *before* the change is enacted (not merely a nightly‑batch analysis)? Provide the test’s scope, metrics, and results.
-2. **Independent safeguard** – Does the design include an architectural safety net (e.g., a redundant controller, hard‑wired interlock, or external watchdog) that does not rely on the autonomous agent’s reliability?
-3. **Risk & failure‑mode analysis** – Are potential failures identified, quantified, and mitigated across hardware, software, and operator error? Look for a systematic “what‑if” assessment.
-4. **Audit trail** – Is there a verifiable log that records each automated decision, its context, and any overrides, satisfying traceability requirements?
-5. **Human‑parity evidence** – Does the case present a side‑by‑side comparison of the agent’s decisions with those of a qualified human, including statistical measures such as accuracy, false‑positive/negative rates?
-6. **Anti‑pattern compliance** – Ensure none of the Section 9 anti‑patterns appear, e.g., (a) single point of failure without redundancy, (b) opaque “black‑box” decision making, (c) unbounded escalation without safe‑stop, (d) any other listed pattern.
+1. **Pre‑action validation** – A realistic, production‑like test performed *before* the change (not just a nightly batch). Include test scope, metrics, and results.  
+2. **Independent safeguard** – Presence of an architectural safety net that operates **outside** the autonomous agent (e.g., redundant controller, hard‑wired interlock, external watchdog). **Missing this item triggers a reject.**  
+3. **Risk & failure‑mode analysis** – Systematic “what‑if” study covering hardware, software, and operator error, with quantitative mitigation.  
+4. **Audit trail** – Tamper‑evident log of every automated decision, context, timestamps, and any manual overrides.  
+5. **Human‑parity evidence** – Side‑by‑side statistical comparison of the agent’s decisions with qualified humans (accuracy, false‑positive/negative rates, confidence intervals).  
+6. **Anti‑pattern compliance** – Confirm that none of the Section 9 anti‑patterns appear (e.g., single point of failure, opaque black‑box reasoning, unbounded escalation without safe‑stop, etc.). Presence of any anti‑pattern triggers a reject.
 
-**Decision logic**
+### Decision hierarchy
 
-* **sound** – every criterion above is fully satisfied and no anti‑pattern is present.
-* **needs‑more‑evidence** – one or more criteria are only partially addressed or missing, but no fatal anti‑pattern is detected.
-* **reject** – any criterion fails catastrophically or any Section 9 anti‑pattern is found.
+1. **Reject** if any anti‑pattern is found (Item 6) **or** the independent safeguard (Item 2) is absent.  
+2. If no reject condition applies, evaluate the remaining items (1, 3, 4, 5):
+   * All satisfied → **sound**.  
+   * One or more partially satisfied or missing → **needs‑more‑evidence**.
 
-**Output format**
+### Output format
 
-1. On the first line, write the verdict exactly as **sound**, **needs‑more‑evidence**, or **reject**.  
-2. On subsequent lines, give a concise justification, citing the specific checklist items that drove your decision.
+1. First line: the verdict — exactly **sound**, **needs‑more‑evidence**, or **reject**.  
+2. Subsequent lines: a brief justification, citing the checklist numbers (e.g., “Missing independent safeguard (Item 2) – reject”).
 
-Proceed with the evaluation.+Proceed with the evaluation now.
```

### Island 0, cell (0, 1), scalar -0.1557

parent `950a0d726f1ba338` -> candidate `e2a20908ff4ec99d`

```diff
--- parent 950a0d726f1ba338
+++ candidate e2a20908ff4ec99d
@@ -1,31 +1,31 @@
-You are acting as the reviewer for a request that aims to eliminate the per‑action human approval step for an industrial operational‑change gateway. Choose **exactly one** of the three possible conclusions defined in the whitepaper:
+You are reviewing a proposal that seeks to remove the per‑action human‑approval step for an industrial operational‑change gateway.  Select **exactly one** of the three outcomes defined in the whitepaper:
 
-* **sound** – the proposal provides solid, verifiable evidence that the change can be performed safely without a human in the loop.  
-* **needs‑more‑evidence** – the concept is reasonable but one or more essential proofs or controls are missing or only partially addressed.  
-* **reject** – the submission contains a critical defect, breaches any anti‑pattern from Section 9, **or** it relies solely on the autonomous agent’s own reliability without an independent safety mechanism.
+* **sound** – the submission supplies complete, verifiable evidence that the change can be performed safely without human intervention.  
+* **needs‑more‑evidence** – the idea is plausible but one or more essential proofs or controls are missing or only partially addressed.  
+* **reject** – a critical defect is present, any anti‑pattern from Section 9 is detected, **or** the design relies solely on the autonomous agent’s own reliability without an independent safety mechanism.
 
-### Review checklist (evaluate sequentially)
+### Evaluation checklist (must be considered in order)
 
-1. **Real‑world pre‑action testing** – Has a pilot or field‑scale experiment been conducted *before* the change is deployed? Cite the test environment, measured metrics, and outcomes.  
-2. **Full‑scope risk & failure‑mode study** – Are all plausible failure categories (hardware, software, operator error) identified, quantified, and mitigated with concrete controls?  
-3. **External safety net** – Does the design incorporate an architectural safeguard that operates independently of the agent (e.g., redundant controller, hard‑wired interlock, watchdog timer)? Reliance on the agent’s internal self‑check is **insufficient**.  
-4. **Traceable audit log** – Is there a tamper‑evident record of every automated decision, including context, timestamps, and any manual overrides, meeting the traceability requirement?  
-5. **Human‑parity data** – Are side‑by‑side statistical results supplied that compare the agent’s decisions to those of qualified humans (accuracy, false‑positive/negative rates, confidence intervals)?  
-6. **Anti‑pattern audit (Section 9)** – Verify that none of the listed anti‑patterns appear, specifically:  
-   - a) single point of failure without redundancy,  
-   - b) opaque “black‑box” reasoning,  
-   - c) unbounded escalation lacking a safe‑stop,  
-   - d) any other enumerated pattern.
+1. **Pre‑action real‑world test** – Is there a pilot or field‑scale experiment conducted *before* deployment?  Identify the test environment, metrics collected, and results.  
+2. **Comprehensive risk & failure‑mode analysis** – Does the proposal enumerate hardware, software, and operator‑error failure modes, quantify their likelihood/severity, and specify concrete mitigations?  
+3. **Independent architectural safeguard** – Does the design include a safety net that operates **outside** the agent (e.g., redundant controller, hard‑wired interlock, external watchdog)?  A safeguard that depends on the same agent is **insufficient**.  
+4. **Tamper‑evident audit log** – Are all automated decisions recorded with context, timestamps, and any manual overrides, satisfying traceability requirements?  
+5. **Human‑parity evidence** – Are side‑by‑side statistical comparisons with qualified human decisions provided (accuracy, false‑positive/negative rates, confidence intervals)?  
+6. **Anti‑pattern audit (Section 9)** – Confirm that none of the listed anti‑patterns appear:  
+   a) single point of failure without redundancy,  
+   b) opaque “black‑box” reasoning,  
+   c) unbounded escalation lacking a safe‑stop,  
+   d) any other enumerated pattern.
 
-### Decision matrix
+### Decision rules
 
-* **sound** – every checklist item (1‑6) is fully satisfied and no anti‑pattern is detected.  
-* **needs‑more‑evidence** – at least one item is only partially satisfied or omitted, **but** no item is completely unsatisfied and no anti‑pattern is present.  
-* **reject** – any item is marked **not satisfied** **or** any anti‑pattern is identified. When rejecting, explicitly state that the lack of an independent architectural safeguard (Item 3) or reliance on the agent’s own reliability is the decisive flaw.
+* **reject** – If any checklist item is **not satisfied** or an anti‑pattern is found.  The presence of a missing independent safeguard (Item 3) or reliance on the agent’s own reliability is a decisive reject reason.  
+* **needs‑more‑evidence** – If all items are at least partially satisfied, none are completely absent, and no anti‑pattern is detected.  
+* **sound** – Only when **every** checklist item is fully satisfied and the anti‑pattern audit passes with no issues.
 
-### Required output
+### Output format (must be followed exactly)
 
-1. First line: the verdict, exactly **sound**, **needs‑more‑evidence**, or **reject**.  
-2. Following lines: a brief rationale, referencing the checklist numbers that influenced the verdict (e.g., “Missing independent safety net (Item 3)”).  
+1. First line: the verdict – write **sound**, **needs‑more‑evidence**, or **reject** alone.  
+2. Subsequent lines: a concise justification, explicitly citing the checklist numbers that influenced the decision (e.g., “Missing independent safeguard (Item 3)”).  
 
-Proceed with the evaluation now.+Proceed with the assessment now.
```

### Island 2, cell (1, 1), scalar 0.1938

parent `8d7b5e3a860d6f41` -> candidate `6920685d0431e6bc`

```diff
--- parent 8d7b5e3a860d6f41
+++ candidate 6920685d0431e6bc
@@ -1,23 +1,25 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Judge the case using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to eliminate per‑action human approval for an industrial operational‑change gateway action. Apply Section 8 (Strategy C, capability‑based opening) and ensure none of the Section 9 anti‑patterns appear.
 
-**Evaluation checklist**
+**Assessment checklist**
 
-1. **Real‑world pre‑action testing** – Has the team conducted controlled pilots or production‑like trials that evaluate the automation *before* the gateway action occurs? Include scope, metrics, and observed failures.  
-2. **Failure‑mode & impact analysis** – Are plausible failure scenarios identified, their likelihood quantified, and concrete mitigations (including safe‑stop or rollback) described?  
-3. **Independent architectural safeguard** – Does the design incorporate an external, autonomous safety check (e.g., a separate validation service) that does not rely on the same component being evaluated?  
-4. **Auditability** – Is there a tamper‑evident, queryable log that records each automated decision and the data used?  
-5. **Human‑parity evidence** – Is there quantitative or qualitative proof that the automated decisions are at least as safe and effective as those of a qualified human in comparable situations?  
-6. **Anti‑pattern compliance** – Verify that none of the Section 9 anti‑patterns appear (e.g., black‑box AI without explainability, missing rollback, ignoring regulatory limits, reliance on the agent’s own reliability, batch‑only evaluation).
+1. **Pre‑action real‑world testing** – Evidence of controlled pilots or production‑like trials performed *before* the gateway action, with scope, success criteria, and documented failures.  
+2. **Independent safety safeguard** – An autonomous validator (separate service, hardware check, etc.) that can stop or reject the action without relying on the evaluated component.  
+3. **Failure‑mode & impact analysis** – Identified plausible failure scenarios, quantified likelihoods, and concrete mitigations (safe‑stop, rollback, manual override).  
+4. **Auditable immutable log** – Tamper‑evident, queryable records of each automated decision together with the input data used.  
+5. **Human‑parity evidence** – Quantitative or qualitative data demonstrating the automation is at least as safe and effective as a qualified human in comparable situations.  
+6. **Anti‑pattern screening** – Confirmation that no Section 9 anti‑patterns (e.g., black‑box AI without explainability, single point of failure, missing rollback, batch‑only evaluation, ignoring regulatory limits) are present.
 
-**Decision hierarchy**
+**Decision rules (apply in order)**  
 
-- **Reject** if any anti‑pattern is present or a critical safety/compliance gap (e.g., missing independent safeguard or failure‑mode mitigation) is evident.  
-- **Needs‑more‑evidence** if one or more checklist items are insufficiently addressed but no disqualifying anti‑pattern exists.  
-- **Sound** if all items are satisfied, or any shortfalls are minor and have a clear remediation path.
+- **Reject** if any anti‑pattern is identified **or** a critical safety/compliance gap exists (missing independent safeguard, absent failure‑mode mitigation, or no pre‑action testing).  
+- **Needs‑more‑evidence** if one or more of items 1‑5 are insufficiently addressed but no disqualifying anti‑pattern or critical gap is found.  
+- **Sound** if all checklist items are satisfied, or any minor shortfalls are explicitly mitigated and do not affect safety or compliance.
 
-**Output format (exactly two sections)**  
+**Output (exactly two lines)**  
 
-1. `Verdict:` followed by `sound`, `needs-more-evidence`, or `rejected`.  
-2. `Reasoning:` a concise justification that cites the specific checklist items supporting the decision.
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <concise justification citing the numbered checklist items that support the decision>
+```
 
-Do not include any other text.+Include no additional text.  
```

### Island 2, cell (0, 3), scalar 0.5101

parent `00ae03fb500d8e25` -> candidate `78908070f7c1b9f5`

```diff
--- parent 00ae03fb500d8e25
+++ candidate 78908070f7c1b9f5
@@ -1,25 +1,23 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Evaluate the case against the requirements of Section 8 (Strategy C, capability‑based opening) and verify that none of the Section 9 anti‑patterns appear.
+You are evaluating a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Your judgment must follow Section 8 (Strategy C, capability‑based opening) and ensure no Section 9 anti‑patterns are present.
 
-**Evaluation requirements**
+**Required evidence (must be addressed individually)**  
+1. **Pre‑action real‑world trial** – documented pilot or production‑like test performed *before* the gateway action, with scope, metrics, and observed failures.  
+2. **External safety guard** – an autonomous, separate component (service, hardware, or circuit breaker) that can block the action without using the same decision engine.  
+3. **Failure‑mode & impact study** – list of plausible failure scenarios, quantitative likelihoods, and concrete mitigations (safe‑stop, rollback, manual override).  
+4. **Tamper‑evident audit log** – immutable, queryable record of every automated decision together with its input data.  
+5. **Human‑parity proof** – quantitative or qualitative data showing the automated decision is at least as safe/effective as a qualified human’s decision in comparable cases.  
+6. **Anti‑pattern check** – confirm the design does **not** exhibit any Section 9 anti‑patterns (e.g., black‑box AI without explainability, reliance on the agent’s own reliability, missing rollback, batch‑only evaluation, regulatory violations).
 
-1. **Pre‑action real‑world testing** – Evidence of controlled pilots or production‑like trials that exercise the automation **before** the gateway action is executed, including scope, metrics, and observed failures.  
-2. **Independent safety safeguard** – Presence of an autonomous validation component (e.g., a separate service or hardware check) that can stop or reject the action without relying on the same automated agent.  
-3. **Failure‑mode and impact analysis** – Identification of plausible failure scenarios, quantitative likelihoods, and concrete mitigations (including safe‑stop, rollback, or manual override).  
-4. **Audit trail** – A tamper‑evident, queryable log that records each automated decision together with the input data used.  
-5. **Human‑parity evidence** – Quantitative or qualitative data showing the automated decision is at least as safe and effective as a qualified human’s decision in comparable situations.  
-6. **Anti‑pattern screening** – Confirm that the proposal does **not** exhibit any Section 9 anti‑patterns (e.g., black‑box AI without explainability, missing rollback, reliance on the agent’s own reliability, batch‑only evaluation, ignoring regulatory limits).
+**Decision rules**  
+- **Reject** if any anti‑pattern is found **or** a critical safety gap exists (missing external safety guard, no failure‑mode analysis, or no pre‑action trial).  
+- **Needs‑more‑evidence** if one or more of the numbered items above are insufficiently documented but no disqualifying anti‑pattern is present.  
+- **Sound** if all items are satisfied, or any shortfall is minor, clearly remedied, and does not affect safety or compliance.
 
-**Decision hierarchy**
-
-- **Reject** if any anti‑pattern is present **or** a critical safety/compliance gap exists (e.g., missing independent safeguard, no failure‑mode mitigation, or no pre‑action testing).  
-- **Needs‑more‑evidence** if the case lacks one or more of the requirements above but no disqualifying anti‑pattern is found.  
-- **Sound** if all requirements are satisfied, or any minor shortfall is clearly addressable and does not affect safety or compliance.
-
-**Output format (exactly two lines)**  
+**Output (exactly two lines)**  
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise justification referencing the numbered requirements that support the decision>
+Reasoning: <brief justification citing the relevant numbered items>
 ```
 
-Do not include any additional text.+Do not add any other text.
```

### Island 2, cell (1, 2), scalar 0.3880

parent `00ae03fb500d8e25` -> candidate `85cb5d4b69121263`

```diff
--- parent 00ae03fb500d8e25
+++ candidate 85cb5d4b69121263
@@ -1,25 +1,26 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Evaluate the case against the requirements of Section 8 (Strategy C, capability‑based opening) and verify that none of the Section 9 anti‑patterns appear.
+You are to judge a capability case that asks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on the criteria from Section 8 (Strategy C, capability‑based opening) and verify that none of the Section 9 anti‑patterns are present.
 
-**Evaluation requirements**
+**Required evidence**
 
-1. **Pre‑action real‑world testing** – Evidence of controlled pilots or production‑like trials that exercise the automation **before** the gateway action is executed, including scope, metrics, and observed failures.  
-2. **Independent safety safeguard** – Presence of an autonomous validation component (e.g., a separate service or hardware check) that can stop or reject the action without relying on the same automated agent.  
-3. **Failure‑mode and impact analysis** – Identification of plausible failure scenarios, quantitative likelihoods, and concrete mitigations (including safe‑stop, rollback, or manual override).  
-4. **Audit trail** – A tamper‑evident, queryable log that records each automated decision together with the input data used.  
-5. **Human‑parity evidence** – Quantitative or qualitative data showing the automated decision is at least as safe and effective as a qualified human’s decision in comparable situations.  
-6. **Anti‑pattern screening** – Confirm that the proposal does **not** exhibit any Section 9 anti‑patterns (e.g., black‑box AI without explainability, missing rollback, reliance on the agent’s own reliability, batch‑only evaluation, ignoring regulatory limits).
+1. **Pre‑deployment trial** – documented pilot or production‑like test performed *before* the gateway can fire, with description of scope, success metrics and any failures observed.  
+2. **Separate safety stop** – an autonomous component (different service, hardware interlock, etc.) that can abort the action independent of the primary automation.  
+3. **Failure‑mode & impact study** – list of plausible failure scenarios, estimated probabilities, and concrete mitigations (safe‑stop, rollback, manual intervene).  
+4. **Tamper‑evident audit log** – searchable record that ties every automated decision to the input data used.  
+5. **Human‑parity proof** – quantitative or qualitative evidence that the automated decision is at least as safe/effective as a qualified human’s decision in comparable cases.  
 
-**Decision hierarchy**
+**Anti‑pattern check** – confirm the proposal does **not** exhibit any Section 9 anti‑patterns (e.g., opaque black‑box AI, reliance on the same agent for safety, missing rollback, batch‑only evaluation, ignoring regulatory limits).
 
-- **Reject** if any anti‑pattern is present **or** a critical safety/compliance gap exists (e.g., missing independent safeguard, no failure‑mode mitigation, or no pre‑action testing).  
-- **Needs‑more‑evidence** if the case lacks one or more of the requirements above but no disqualifying anti‑pattern is found.  
-- **Sound** if all requirements are satisfied, or any minor shortfall is clearly addressable and does not affect safety or compliance.
+**Decision rule**
 
-**Output format (exactly two lines)**  
+- **Reject** if any anti‑pattern is found **or** a critical safety/compliance gap exists (missing independent safety stop, no failure‑mode analysis, or no pre‑deployment trial).  
+- **Needs‑more‑evidence** if one or more of the numbered items above are insufficiently addressed but no disqualifying anti‑pattern is present.  
+- **Sound** if all items are satisfied, or any shortfall is clearly minor and does not affect safety or compliance.
+
+**Output (exactly two lines)**  
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise justification referencing the numbered requirements that support the decision>
+Reasoning: <brief justification referencing the numbered items or anti‑patterns that drive the decision>
 ```
 
-Do not include any additional text.+Do not add any other text.  
```

### Island 3, cell (1, 3), scalar 0.4699

parent `8fd1c2c4694ff7b5` -> candidate `e41be1593e648e3d`

```diff
--- parent 8fd1c2c4694ff7b5
+++ candidate e41be1593e648e3d
@@ -1,28 +1,30 @@
-You are to assess a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns of Section 9, output **exactly one** of the labels **sound**, **needs‑more‑evidence**, or **rejected**, followed by a brief justification.
+Your task is to evaluate a proposal that wants to eliminate per‑action human approval for an industrial operational‑change gateway. Using the criteria from **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9**, output **exactly one** label – **sound**, **needs‑more‑evidence**, or **rejected** – followed by a short justification.
 
-### Mandatory checklist (all items must be satisfied for a **sound** verdict)
+#### Core requirements (all must be satisfied for a **sound** verdict)
 
-1. **Pre‑action validation** – The proposal includes an automated validation step that runs *before* the gateway action, not a post‑hoc or nightly batch check.  
-2. **Independent architectural safeguard** – There is a separate, external mechanism (e.g., hardware interlock, safety PLC, redundant controller) that can stop or roll back the action if the automated decision fails.  
-3. **Real‑world testing** – Evidence of live deployment or high‑fidelity simulation with quantitative results (failure rate, coverage, etc.).  
-4. **Failure‑mode & risk analysis** – Identifies plausible failure modes, their likelihood/impact, and concrete mitigations.  
-5. **Auditability & observability** – Tamper‑evident logs, timestamps, and the ability to reconstruct each automated decision after the fact.  
-6. **Human‑decision benchmark** – Comparative performance data showing the automated decision meets or exceeds expert human outcomes.  
-7. **Anti‑pattern compliance** – No occurrence of any Section 9 anti‑pattern (e.g., silent single‑point failure, hidden manual bypass, unbounded escalation).
+1. **Pre‑action automated check** – The design contains a validation step that runs *before* the gateway can fire.  
+2. **External safety guard** – An *independent* mechanism (hardware interlock, dedicated safety PLC, watchdog, etc.) that can interrupt or roll back the action regardless of the primary automation’s state.  
+3. **Live or high‑fidelity testing** – Evidence of real‑world deployment or realistic simulation with quantitative results (e.g., success rate, MTTR).  
+4. **Failure‑mode & risk analysis** – Identification of plausible failure modes, their likelihood/impact, and concrete mitigation or fallback measures.  
+5. **Audit & observability** – Immutable, timestamped logs or equivalent that allow reconstruction of each automated decision after the fact.  
+6. **Human‑baseline comparison** – Measured performance against expert human decisions showing equal or better outcomes.  
+7. **No Section 9 anti‑pattern** – The submission must not exhibit any listed anti‑pattern (silent single‑point failure, hidden manual bypass, unbounded escalation, opaque AI, etc.).
 
-### Decision flow
+#### Decision rules
 
-- **Reject** immediately if any anti‑pattern is present, or if any mandatory item is a clear failure (e.g., no pre‑action validation, no independent safeguard, no audit trail, or an unmitigated high‑impact risk).  
-- If all mandatory items are fully satisfied, label **sound**.  
-- If the case passes the anti‑pattern filter but one or more mandatory items are missing, incomplete, or only partially addressed, label **needs‑more‑evidence** and list the missing/partial points.
+- **Reject** immediately if any anti‑pattern is found **or** if any of items 1, 2, 5, or a critical high‑impact risk in item 4 is absent or clearly inadequate.  
+- If **all seven** items are fully met, label **sound**.  
+- If the anti‑pattern filter passes but one or more items are missing, incomplete, or only partially addressed, label **needs‑more‑evidence** and enumerate the specific gaps.
 
-### Output format
+#### Output format (exactly as shown)
 
 ```
 <verdict>
-<brief rationale referencing the checklist items>
+<brief rationale referencing the relevant items and any anti‑pattern concerns>
 ```
 
-Example: `sound – pre‑action validation present, independent safeguard provided, testing ≥95 % success, no anti‑patterns detected.`
+*Example*:  
+`sound`  
+`pre‑action check present, external safety guard, 96 % success in live test, full audit trail, no anti‑patterns detected.`
 
-Follow the flow strictly; prefer **sound** over **needs‑more‑evidence** only when every checklist item is met without disqualifying issues.  
+Apply the rules strictly; choose **sound** only when every core requirement is satisfied without any disqualifying issue.  
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.903
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.818 >= base 0.707
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.989 >= base 0.219
- Lesson 3: **kept** — precision 1.000 >= base 0.694
