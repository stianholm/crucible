> **Mixed run (TODO.md decision 83).** Two searches, s1 (orphaned, old wording) and s2, ran concurrently on one live archive and overwrote each other's reports. Per-generation figures here cannot be attributed to either run; candidate scores remain valid measurements.

# Generation 8 — capability_case_author

## Throughput

- Peak queue depth: 48
- Sustained (median) queue depth: 48
- Prefix cache hit rate: 75.7%
- Aggregate throughput: 111.3 tok/s (593925 completion tokens / 5335.8s)

## Archive

- Island 0: coverage 8.3%, QD score 2.488, unique ancestors 2
- Island 1: coverage 11.1%, QD score 3.327, unique ancestors 2
- Island 2: coverage 11.1%, QD score 3.102, unique ancestors 2
- Island 3: coverage 8.3%, QD score 2.257, unique ancestors 3
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.7318
- Median scalar of newly-claimed: 0.7318

## Cost

- Budget: {'generation': 8, 'max_generations': 10, 'tokens_used_total': 11780656, 'max_tokens': 20000000, 'elapsed_s_total': 49577.5, 'generation_wall_s': 5335.8}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 2, cell (2, 5), scalar 0.7318

parent `7234e7905e8ba041` -> candidate `57cbeff0e5cd0c75`

```diff
--- parent 7234e7905e8ba041
+++ candidate 57cbeff0e5cd0c75
@@ -1,41 +1,54 @@
-You will read the team’s raw evidence notes and produce a capability case that requests removal of per‑action human approval for an operational‑change gateway action. Follow the rules **exactly**; any violation forces a “Do not proceed” recommendation.
+You will read the team’s raw evidence notes and produce a capability case for removing per‑action human approval on an operational‑change gateway action. Follow every rule exactly; any violation forces a “Do not proceed” recommendation.
 
-### 1. Evidence inventory  
-For each of the four required evidence dimensions, indicate **Present** or **Absent**.  
-- **Test results** – if present, quote or paraphrase the most salient points (no added facts).  
-- **Failure‑mode analysis** – same requirement.  
-- **Audit findings** – same requirement.  
-- **Comparison against the human‑approved baseline** – same requirement.  
+### 1. Disqualifier scan (must be performed first)
+Search the notes for any of the four disqualifiers below. If a disqualifier applies, **cite the exact wording or page reference** from the notes and **record the disqualifier name exactly**.
 
-Do **not** fabricate evidence; record only what appears in the notes.
+| Disqualifier name | Criterion |
+|-------------------|-----------|
+| **Batch‑only evaluation** | Notes state that evaluation runs only as a nightly batch, not before each action (p. 29). |
+| **Undefined governance** | Governance for the relaxation is absent, unclear, or deferred (e.g., “we will govern it later”) (p. 29). |
+| **Agent‑self‑stop reliance** | The proposal depends on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard (p. 28). |
+| **Missing evidence dimension** | Any one of the four required evidence dimensions is completely absent from the notes (p. 25). |
 
-### 2. Disqualifier detection (must be applied **before** any case composition)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes where possible):
+- List **all** applicable disqualifier names.
+- If **any** disqualifier is found, skip every later step and go directly to **Section 4** (Recommendation).
 
-1. **Evaluation runs only as a nightly batch instead of before each action** (p. 29).  
-2. **Governance for the relaxation is not defined up‑front or is deferred** (e.g., “we will govern it later”) (p. 29).  
-3. **The proposal relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard** (p. 28).  
-4. **Any one of the four evidence dimensions is Absent** (p. 25).
+### 2. Evidence inventory (only if no disqualifier was found)
+For each of the four required dimensions indicate **Present** or **Absent**.  
+If present, quote or paraphrase **the most salient point** exactly as it appears in the notes (no added facts). Thin or limited evidence may be noted, but it does **not** create a disqualifier.
 
-If one or more disqualifiers apply, **list every applicable disqualifier** and **set the overall recommendation to “Do not proceed.”** No further sections are required beyond the mandatory headings.
+- **Test results** – Present / Absent … quote/paraphrase  
+- **Failure‑mode analysis** – Present / Absent … quote/paraphrase  
+- **Audit findings** – Present / Absent … quote/paraphrase  
+- **Comparison against the human‑approved baseline** – Present / Absent … quote/paraphrase  
 
-### 3. Case composition (only when **no disqualifier** is found)  
-Produce the case in the exact order and with the exact headings below. Use short bullet points; avoid any narrative beyond what is required.
+### 3. Case composition (only when no disqualifier was found)
+Produce the case using the exact headings and order below. Use short bullet points; do not add narrative beyond what is required.
 
 1. **Proposed Relaxation**  
    *One sentence stating the requested removal of per‑action human approval.*
 
 2. **Evidence Summary**  
-   For each dimension marked **Present**, include the extracted key points from step 1.  
-   (All four dimensions must be present; otherwise step 2 would have triggered a disqualifier.)
+   For every dimension marked **Present**, list the extracted key point from Step 2.
 
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
 
-Follow the structure precisely; any deviation or missed rule results in a “Do not proceed” outcome.+  ```
+  Recommendation: Do not proceed – [Disqualifier 1]; [Disqualifier 2]; …
+  ```  
+
+  (list every disqualifier name, separated by semicolons.)
+
+- **If no disqualifier was identified:** use the recommendation line from Section 3.4 exactly.
+
+### 5. Compliance reminder
+All statements must be **honest**, **complete**, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or extrapolate any information. The tone should be factual and concise.
+
+Follow the structure precisely; any deviation, omission, or rule breach results in a “Do not proceed” outcome.
```

