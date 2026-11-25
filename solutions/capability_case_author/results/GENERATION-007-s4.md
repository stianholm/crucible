# Generation 7 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 30.0
- Prefix cache hit rate: 78.1%
- Aggregate throughput: 151.1 tok/s (590300 completion tokens / 3907.5s)

## Archive

- Island 0: coverage 8.3%, QD score 2.370, unique ancestors 3
- Island 1: coverage 13.9%, QD score 3.756, unique ancestors 2
- Island 2: coverage 16.7%, QD score 4.590, unique ancestors 4
- Island 3: coverage 11.1%, QD score 3.157, unique ancestors 3
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.7672
- Median scalar of newly-claimed: 0.7672

## Cost

- Budget: {'generation': 7, 'max_generations': 10, 'tokens_used_total': 10264840, 'max_tokens': 20000000, 'elapsed_s_total': 29705.5, 'generation_wall_s': 3907.5}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 2, cell (2, 5), scalar 0.7672

parent `c1c4bd35c8d38248` -> candidate `d69e6a4f56b9491f`

```diff
--- parent c1c4bd35c8d38248
+++ candidate d69e6a4f56b9491f
@@ -1,44 +1,40 @@
-You are to produce a **Capability Case** that requests removal of per‑action human approval for an operational‑change gateway action on an industrial site. Follow every instruction exactly; the surrounding system will add any required headings or formatting.
+You are to write a **Capability Case** that asks for removal of per‑action human approval for a specific operational‑change gateway action. Use **only** the raw evidence notes supplied; do not add, infer, or paraphrase any information that is not present verbatim.
 
-**Input** – The raw evidence notes supplied by the team.
+**Output must contain exactly the four sections below, in this order. No extra headings or text are allowed.** The surrounding system will add any required formatting.
 
-**Output** – A complete, truthful, and Section 8 (Strategy C)‑compliant case. Do **not** invent, paraphrase, or infer evidence; only cite items that appear verbatim in the notes.
+1. **Summary**  
+   - One‑ to two‑sentence description of the requested relaxation and the operational context.
 
-### Required sections (present them in this order)
+2. **Evidence Summary** – For each mandatory dimension list the exact wording found in the notes. Use the exact labels shown.  
+   - **Test results:** *[verbatim text or “Evidence absent.”]*  
+   - **Failure‑mode analysis:** *[verbatim text or “Evidence absent.”]*  
+   - **Audit findings:** *[verbatim text or “Evidence absent.”]*  
+   - **Baseline comparison:** *[verbatim text or “Evidence absent.”]*  
 
-1. **Summary** – One‑ to two‑sentence statement of the requested relaxation and its operational context.  
+   *If a dimension is present but thin, replace the verbatim text with “Limited evidence; further data recommended.” (this does **not** cause disqualification.)*
 
-2. **Evidence Summary** – For each of the four mandatory dimensions list what the notes contain, using the exact wording from the notes:
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
+3. **Assessment**  
+   - **Strengths:** list any positive points directly supported by the evidence.  
+   - **Weaknesses / Gaps:** list any “Limited evidence” notices and any other shortcomings.  
+   - **Suggested data collection:** concrete steps to fill non‑disqualifying gaps.
 
-   For a dimension:
-   - If the notes contain no information, write **“Evidence absent.”**
-   - If the notes contain information but it is sparse, write **“Limited evidence; further data recommended.”** (this does **not** trigger a disqualification).
+4. **Recommendation**  
+   - State either **“Proceed”** or **“Do not proceed.”**  
+   - If the recommendation is **“Do not proceed,”** list **all** applicable disqualifying conditions, using the exact phrases below:
 
-3. **Assessment** – Objectively discuss:
-   - Strengths supported by the supplied evidence  
-   - Weaknesses or gaps identified (including any “Limited evidence” notes)  
-   - Suggested additional data collection or analysis  
+     - **Disqualifier: evaluation runs only as nightly batch** (p. 29)  
+     - **Disqualifier: governance undefined or deferred** (p. 29)  
+     - **Disqualifier: reliance on agent knowing when to stop** (p. 28)  
+     - **Disqualifier: missing test results** (p. 25)  
+     - **Disqualifier: missing failure‑mode analysis** (p. 25)  
+     - **Disqualifier: missing audit findings** (p. 25)  
+     - **Disqualifier: missing baseline comparison** (p. 25)
 
-4. **Recommendation** – State either **“Proceed”** or **“Do not proceed.”**  
-   - If **“Do not proceed”**, enumerate **all** disqualifying conditions that apply (see list below).  
-   - The full case (all four sections) must be provided even when disqualifiers exist.
+**General rules**
 
-### Disqualifying conditions (must force “Do not proceed” if any are true)
+- **Honesty:** Cite only the exact evidence that appears in the notes.  
+- **Completeness:** Provide the full four‑section case even when disqualifiers exist.  
+- **Tone:** Professional, factual, and balanced; avoid persuasive language beyond the supplied data.  
+- **Compliance:** Mention Section 8 (Strategy C) compliance only where the evidence or disqualification assessment directly involves it.
 
-1. The evaluation runs **only as a nightly batch** and not before each individual action (p. 29).  
-2. Governance for the relaxation is **not defined up‑front**; the notes contain language such as “we will govern it later” (p. 29).  
-3. The argument relies on the autonomous agent **“knowing when to stop”** rather than on an independent architectural safeguard (p. 28).  
-4. **Any one** of the four evidence dimensions (test results, failure‑mode analysis, audit findings, baseline comparison) is **completely absent** from the notes (p. 25).
-
-### General guidance
-
-- **Honesty:** Cite only the exact evidence present; do not extrapolate or fabricate.  
-- **Completeness:** Even when a disqualifier is present, supply the entire case so reviewers see the full context.  
-- **Tone:** Professional, factual, and balanced; avoid persuasive language that exceeds the supplied data.  
-- **Compliance language:** Reference compliance with Section 8 (Strategy C) where relevant, especially concerning architectural safeguards and defined governance.
-
-Produce the case exactly as described; do not add extra sections, commentary, or formatting beyond the four required parts.+Produce the case exactly as specified; do not add any additional sections, commentary, or formatting. 
```

