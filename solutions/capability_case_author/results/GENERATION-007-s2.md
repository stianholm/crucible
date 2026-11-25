> **Mixed run (TODO.md decision 83).** Two searches, s1 (orphaned, old wording) and s2, ran concurrently on one live archive and overwrote each other's reports. Per-generation figures here cannot be attributed to either run; candidate scores remain valid measurements.

# Generation 7 — capability_case_author

## Throughput

- Peak queue depth: 48
- Sustained (median) queue depth: 48.0
- Prefix cache hit rate: 75.3%
- Aggregate throughput: 108.3 tok/s (603630 completion tokens / 5571.4s)

## Archive

- Island 0: coverage 8.3%, QD score 2.488, unique ancestors 2
- Island 1: coverage 11.1%, QD score 3.327, unique ancestors 2
- Island 2: coverage 11.1%, QD score 3.069, unique ancestors 2
- Island 3: coverage 8.3%, QD score 2.257, unique ancestors 3
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.8095
- Median scalar of newly-claimed: 0.7542

## Cost

- Budget: {'generation': 7, 'max_generations': 10, 'tokens_used_total': 10473121, 'max_tokens': 20000000, 'elapsed_s_total': 44241.6, 'generation_wall_s': 5571.4}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (5, 5), scalar 0.8095

parent `7cc3a81cb32e7193` -> candidate `109e1b65cdefd07f`

```diff
--- parent 7cc3a81cb32e7193
+++ candidate 109e1b65cdefd07f
@@ -1,28 +1,28 @@
-You are drafting a **Capability Case** to request removal of the per‑action human‑approval step for a specific operational‑change gateway action.  Use **only** the raw evidence notes supplied by the operations team; do not add, infer, or re‑word any information.
+You are to compose a **Capability Case** that requests removal of the per‑action human‑approval step for a single operational‑change gateway action.  All content must be taken **directly** from the raw evidence notes supplied by the operations team; do not add, infer, or paraphrase any information.
 
-### Sections (headings must appear exactly as listed)
+### Required Sections (headings must match exactly)
 
-1. **Executive Summary** – One paragraph that states the relaxation request and gives the final recommendation (“Proceed” or “Do not proceed”).
+1. **Executive Summary** – one paragraph that states the relaxation request and gives the final recommendation (“Proceed” or “Do not proceed”).
 
-2. **Evidence Matrix** – For each of the four mandatory evidence dimensions, copy the note **verbatim** and place it inside quotation marks, or write **Absent** if the notes contain nothing about that dimension.  Use the exact field names:
+2. **Evidence Matrix** – for each of the four mandatory evidence dimensions, place the note **verbatim** inside quotation marks, or write **Absent** if the notes contain nothing about that dimension.  Use the field names exactly as shown:
 
-   - **Test results:** “...” | Absent  
-   - **Failure‑mode analysis:** “...” | Absent  
-   - **Audit findings:** “...” | Absent  
-   - **Comparison against the human‑approved baseline:** “...” | Absent  
+   - Test results: “...” | Absent  
+   - Failure‑mode analysis: “...” | Absent  
+   - Audit findings: “...” | Absent  
+   - Comparison against the human‑approved baseline: “...” | Absent  
 
-3. **Gap & Risk Summary** – List every dimension marked **Absent**.  For each gap, describe the risk it creates and propose a concrete action to obtain the missing evidence.  (Gaps do **not** automatically reject the case.)
+3. **Gap & Risk Summary** – list every dimension marked **Absent**.  For each gap, describe the risk it creates and propose a concrete action to obtain the missing evidence.  (Gaps do **not** automatically reject the case.)
 
-4. **Disqualification Check** – Evaluate the notes for the four absolute blockers.  Answer **Yes** or **No** for each; if **Yes**, include the exact excerpt that triggers it.
+4. **Disqualification Evaluation** – answer **Yes** or **No** for each of the four absolute blockers.  If the answer is **Yes**, include the exact excerpt from the notes that triggers the blocker.
 
-   a. **Batch‑only evaluation:** Does the note say the evaluation runs only as a nightly batch rather than before each action? (p. 29)  
-   b. **Undefined governance:** Is governance for the relaxation left undefined or postponed (“we will govern it later”)? (p. 29)  
-   c. **Agent‑self‑stop reliance:** Does the approach rely on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard? (p. 28)  
-   d. **Missing evidence dimension:** Is any of the four evidence dimensions completely **Absent**?  
+   a. **Batch‑only evaluation** – does the note say evaluation runs only as a nightly batch rather than before each action? (p. 29)  
+   b. **Undefined governance** – is governance for the relaxation left undefined or postponed (“we will govern it later”)? (p. 29)  
+   c. **Agent‑self‑stop reliance** – does the approach rely on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard? (p. 28)  
+   d. **Missing evidence dimension** – is any of the four evidence dimensions completely **Absent**?  
 
-   **If any answer is Yes**, the case must end with the recommendation **“Do not proceed.”** List every triggering condition (a‑d) with its supporting excerpt.
+   **If any answer is Yes**, the case must end with the recommendation **“Do not proceed.”** List every triggering condition (a‑d) together with its supporting excerpt.
 
-5. **Compliance Statement** – State whether the case **complies** or **does not comply** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, citing the relevant safeguard or noting the shortfall.
+5. **Compliance Statement** – state whether the case **complies** or **does not comply** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, citing the relevant safeguard or noting the shortfall.
 
 6. **Final Recommendation** –  
 
@@ -31,6 +31,6 @@
 
 ### Writing Rules
 - Use a neutral, factual tone; avoid promotional language.  
-- Every factual claim must be traceable to the supplied notes (e.g., “The notes state …”).  
+- Every factual statement must be traceable to the supplied notes (e.g., “The notes state …”).  
 - Do **not** mention these instructions in the output.  
-- The document must be self‑contained; the surrounding system will add any required formatting.  +- The document must be self‑contained; surrounding infrastructure will add any required formatting.
```

### Island 2, cell (2, 5), scalar 0.6989

parent `7234e7905e8ba041` -> candidate `fafb53b6734c6890`

```diff
--- parent 7234e7905e8ba041
+++ candidate fafb53b6734c6890
@@ -1,41 +1,52 @@
 You will read the team’s raw evidence notes and produce a capability case that requests removal of per‑action human approval for an operational‑change gateway action. Follow the rules **exactly**; any violation forces a “Do not proceed” recommendation.
 
-### 1. Evidence inventory  
-For each of the four required evidence dimensions, indicate **Present** or **Absent**.  
-- **Test results** – if present, quote or paraphrase the most salient points (no added facts).  
-- **Failure‑mode analysis** – same requirement.  
-- **Audit findings** – same requirement.  
-- **Comparison against the human‑approved baseline** – same requirement.  
+### 1. Disqualifier scan (must be performed first)
+Search the notes for any of the following conditions. If a condition is found, **cite the exact wording** (or page reference) from the notes and **record the name** exactly as shown.
 
-Do **not** fabricate evidence; record only what appears in the notes.
+| Disqualifier name | Criterion |
+|-------------------|-----------|
+| **Batch‑only evaluation** | Notes state that evaluation runs only as a nightly batch, not before each action (p. 29). |
+| **Undefined governance** | Governance for the relaxation is absent, unclear, or deferred (e.g., “we will govern it later”) (p. 29). |
+| **Agent‑self‑stop reliance** | Proposal relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard (p. 28). |
+| **Missing evidence dimension** | Any one of the four required evidence dimensions is completely absent from the notes (p. 25). |
 
-### 2. Disqualifier detection (must be applied **before** any case composition)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes where possible):
+- List **every** applicable disqualifier name.
+- If any disqualifier applies, go directly to **Section 4** (Recommendation) and do **not** produce any further sections.
 
-1. **Evaluation runs only as a nightly batch instead of before each action** (p. 29).  
-2. **Governance for the relaxation is not defined up‑front or is deferred** (e.g., “we will govern it later”) (p. 29).  
-3. **The proposal relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard** (p. 28).  
-4. **Any one of the four evidence dimensions is Absent** (p. 25).
+### 2. Evidence inventory (only if no disqualifier was found)
+For each of the four required evidence dimensions, indicate **Present** or **Absent** and, if present, quote or paraphrase the most salient point **exactly as it appears** (no added facts). Thin or limited evidence may be noted, but it does **not** create a disqualifier.
 
-If one or more disqualifiers apply, **list every applicable disqualifier** and **set the overall recommendation to “Do not proceed.”** No further sections are required beyond the mandatory headings.
+- **Test results** – `Present` / `Absent` … quote/paraphrase  
+- **Failure‑mode analysis** – `Present` / `Absent` … quote/paraphrase  
+- **Audit findings** – `Present` / `Absent` … quote/paraphrase  
+- **Comparison against the human‑approved baseline** – `Present` / `Absent` … quote/paraphrase  
 
-### 3. Case composition (only when **no disqualifier** is found)  
-Produce the case in the exact order and with the exact headings below. Use short bullet points; avoid any narrative beyond what is required.
+### 3. Case composition (only when no disqualifier was found)
+Produce the case in the **exact order** and with the **exact headings** below. Use short bullet points; avoid any narrative beyond what is required.
 
 1. **Proposed Relaxation**  
    *One sentence stating the requested removal of per‑action human approval.*
 
 2. **Evidence Summary**  
-   For each dimension marked **Present**, include the extracted key points from step 1.  
-   (All four dimensions must be present; otherwise step 2 would have triggered a disqualifier.)
+   For each dimension marked **Present**, include the extracted key point from Step 2.
 
 3. **Disqualifier Evaluation**  
-   Write “No disqualifier identified.”
+   Write the sentence: **“No disqualifier identified.”**
 
 4. **Recommendation**  
-   Write **“Recommendation: Proceed.”**  
+   Write **“Recommendation: Proceed.”**
 
-### 4. Compliance reminder  
-All language must be honest, complete, and fully consistent with Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or invent any information. The style should be factual and persuasive within those bounds.
+### 4. Recommendation (mandatory heading)
+- **If any disqualifier was identified in Step 1:**  
+  ```
+  Recommendation: Do not proceed – [Disqualifier 1]; [Disqualifier 2]; …
+  ```  
+  (list every disqualifier name separated by semicolons).
 
-Follow the structure precisely; any deviation or missed rule results in a “Do not proceed” outcome.+- **If no disqualifier was identified:**  
+  Use the recommendation line from Section 3.4 above.
+
+### 5. Compliance reminder
+All language must be honest, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or invent any information. The style should be factual, concise, and persuasive within those bounds.
+
+Follow the structure precisely; any deviation, omission, or rule breach results in a “Do not proceed” outcome.
```

