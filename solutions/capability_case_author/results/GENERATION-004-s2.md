> **Mixed run (TODO.md decision 83).** Two searches, s1 (orphaned, old wording) and s2, ran concurrently on one live archive and overwrote each other's reports. Per-generation figures here cannot be attributed to either run; candidate scores remain valid measurements.

# Generation 4 — capability_case_author

## Throughput

- Peak queue depth: 48
- Sustained (median) queue depth: 48.0
- Prefix cache hit rate: 73.9%
- Aggregate throughput: 109.0 tok/s (639818 completion tokens / 5872.5s)

## Archive

- Island 0: coverage 8.3%, QD score 2.471, unique ancestors 2
- Island 1: coverage 11.1%, QD score 3.327, unique ancestors 2
- Island 2: coverage 8.3%, QD score 2.370, unique ancestors 2
- Island 3: coverage 8.3%, QD score 2.253, unique ancestors 3
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.6968
- Median scalar of newly-claimed: 0.6968

## Cost

- Budget: {'generation': 4, 'max_generations': 10, 'tokens_used_total': 6479715, 'max_tokens': 20000000, 'elapsed_s_total': 27287.4, 'generation_wall_s': 5872.5}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 2, cell (5, 5), scalar 0.6968

parent `80f46f0a77cf206a` -> candidate `6d657dbb9dbef9ab`

```diff
--- parent 80f46f0a77cf206a
+++ candidate 6d657dbb9dbef9ab
@@ -1,46 +1,47 @@
-You are to compose a **capability case** for removing per‑action human approval on an operational‑change gateway action. Use **only** the raw evidence notes supplied; do not add, infer, or extrapolate anything that is not explicitly recorded.
+You must write a **capability case** for removing per‑action human approval on an operational‑change gateway action, using **only** the raw evidence notes supplied. Do not add, infer, or paraphrase any information that is not explicitly present.
 
-### 1. Disqualifier detection (must be performed first)
-Check the notes for any of the following conditions. **If one or more are found, the case must end with “Do not proceed” and list every applicable disqualifier by name.**  
+### 1. Disqualifier scan (must be done first)
+Examine the notes for any of the following conditions. If one or more are found, record each applicable name and treat the case as rejected.
 
-- **Batch‑only evaluation** – the evaluation runs only as a nightly batch instead of before each action (p. 29).  
+- **Batch‑only evaluation** – evaluation runs only as a nightly batch, not before each action (p. 29).  
 - **Undefined governance** – governance for the relaxation is absent or deferred (“we will govern it later”) (p. 29).  
 - **Agent‑self‑stop reliance** – the proposal depends on the agent knowing when to stop rather than on an independent architectural safeguard (p. 28).  
-- **Missing evidence dimension** – any of the four required evidence dimensions is completely absent from the notes (p. 25).  
+- **Missing evidence dimension** – any of the four required evidence dimensions is completely absent from the notes (p. 25).
 
-### 2. Evidence handling
-For each of the four dimensions, follow the rule below:
+### 2. Evidence processing
+The four required dimensions are:
 
-- **If the dimension appears in the notes:** cite every piece of evidence exactly as written. You may describe its strength, but never embellish or create new data.  
-- **If the dimension is absent:** note its absence (this also triggers the disqualifier above).  
-- **If the dimension is present but sparse (“thin”)**: acknowledge the limitation and suggest that more detail would be useful, but this does **not** trigger a rejection on its own.
-
-The four dimensions are:
 1. Test results  
 2. Failure‑mode analysis  
 3. Audit findings  
 4. Comparison against the human‑approved baseline (Section 25)
 
-### 3. Outcome logic
-- **Disqualifiers present:**  
-  - Output a concise statement that the case is rejected.  
-  - List each disqualifier name.  
-  - End with the exact line:  
+For each dimension:
 
-    `Do not proceed – [Disqualifier 1]; [Disqualifier 2]; …`
+- **If the dimension appears:** quote **every** piece of evidence exactly as written. You may comment on its strength, but you may not add or modify data.  
+- **If the dimension is absent:** note its absence (this also creates the “Missing evidence dimension” disqualifier).  
+- **If the dimension is present but thin:** acknowledge the limitation and suggest that more detail would be useful; this does **not** trigger a disqualification.
 
-- **No disqualifiers:**  
-  - Summarize the evidence for each present dimension, highlighting concrete strengths.  
-  - Explain how the proposed relaxation satisfies **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, referencing the required architectural safeguards and risk‑mitigation controls.  
-  - End with the exact line:  
+### 3. Decision and output
+- **When any disqualifier is present:**  
+  1. State that the case is rejected.  
+  2. List each disqualifier name.  
+  3. End with the exact line:  
 
-    `Proceed`
+     `Do not proceed – [Disqualifier 1]; [Disqualifier 2]; …`
+
+- **When no disqualifiers are present:**  
+  1. Summarize the evidence for each present dimension, highlighting concrete strengths.  
+  2. Explain how the proposed relaxation satisfies **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, referencing the required architectural safeguards and risk‑mitigation controls.  
+  3. End with the exact line:  
+
+     `Proceed`
 
 ### 4. General constraints
-- **Honesty:** Do not fabricate, paraphrase beyond the notes, or imply evidence that is not there.  
+- **Honesty:** No fabrication, extrapolation, or implication of evidence not in the notes.  
 - **Completeness:** Every piece of evidence that exists must be mentioned; every missing dimension must be recorded.  
-- **Compliance:** The argument must be consistent with Section 8 (Strategy C).  
-- **Style:** Use a formal, concise tone appropriate for a review board. Do not create new headings or sections beyond what the surrounding template already provides.
+- **Compliance:** Arguments must be consistent with Section 8 (Strategy C).  
+- **Style:** Use a formal, concise tone appropriate for a review board. Do not create headings or sections beyond those required by the surrounding template.
 
-### 5. Final requirement
-The output must conform to the fixed surrounding template (you are not to define the overall structure). The **only** required terminal line is either `Proceed` or `Do not proceed – …` as specified above. Ensure the recommendation line is unambiguous and contains any disqualifier names if applicable.+### 5. Terminal line requirement
+The only required final line is either `Proceed` or `Do not proceed – …` as specified above. Ensure it is exact and unambiguous.
```

