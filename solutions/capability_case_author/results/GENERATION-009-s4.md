# Generation 9 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 78.1%
- Aggregate throughput: 151.4 tok/s (627400 completion tokens / 4143.0s)

## Archive

- Island 0: coverage 8.3%, QD score 2.370, unique ancestors 3
- Island 1: coverage 13.9%, QD score 4.000, unique ancestors 2
- Island 2: coverage 16.7%, QD score 4.653, unique ancestors 3
- Island 3: coverage 11.1%, QD score 3.183, unique ancestors 3
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.7563
- Median scalar of newly-claimed: 0.7563

## Cost

- Budget: {'generation': 9, 'max_generations': 10, 'tokens_used_total': 13003306, 'max_tokens': 20000000, 'elapsed_s_total': 37948.5, 'generation_wall_s': 4143.0}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 1, cell (5, 5), scalar 0.7563

parent `436bcf2dee83e9ba` -> candidate `a69554149e8a8e6d`

```diff
--- parent 436bcf2dee83e9ba
+++ candidate a69554149e8a8e6d
@@ -1,40 +1,36 @@
-You are drafting a **Capability Case** for an operations team that wants to **relax per‑action human approval** on an operational‑change gateway action at an industrial site.
+You are to produce a **Capability Case** for a team that wants to remove per‑action human approval from an operational‑change gateway action. Use only the raw evidence notes supplied; never add, infer, or paraphrase information that is not explicitly present.
 
-**Your task** is to transform the team’s raw evidence notes into a complete, honest, and compliant case that conforms to **Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper**.
+### 1. Mandatory Content (in this exact order)
 
-### Core Requirements
-1. **Use only the evidence that actually appears in the notes.** Do not invent or extrapolate any test results, failure‑mode analyses, audit findings, or baseline comparisons that are not present.
-2. **Structure the output** (the surrounding template will enforce the final format, but you must follow this logical order):
-   - **Purpose & Scope** – brief statement of the requested relaxation.
-   - **Evidence Summary** – list each of the four evidence dimensions (test results, failure‑mode analysis, audit findings, comparison against the human‑approved baseline). For any dimension that is missing, explicitly note “*Evidence absent*”.
-   - **Risk Assessment** – discuss risks identified in the notes, referencing the available evidence.
-   - **Governance & Safeguards** – describe the proposed governance model and any architectural safeguards. If the notes lack a defined governance model, treat that as a missing element.
-   - **Recommendation** – either “**Proceed**” or “**Do not proceed**” with justification.
+1. **Purpose & Scope** – one‑sentence description of the requested relaxation and where it will be applied.  
+2. **Evidence Summary** – for each of the four required dimensions list what the notes contain, using the exact wording from the notes:
+   - **Test results**  
+   - **Failure‑mode analysis**  
+   - **Audit findings**  
+   - **Baseline comparison**  
 
-3. **Disqualifier Rules** – If **any** of the following conditions are true, you **must**:
-   - Recommend **“Do not proceed.”**
-   - Explicitly name each violated condition in the Recommendation section.
-   - Still provide the full case (Purpose, Evidence Summary, Risk Assessment, Governance) so the board sees the full context.
+   For each dimension:
+   - If the notes have no entry → write **Evidence absent.**
+   - If the notes have an entry but it is sparse → write **Limited evidence; further data collection recommended.** (this does **not** trigger a disqualifier).  
+3. **Risk & Assessment** – brief, factual discussion of strengths, weaknesses, and any “Limited evidence” notices identified above. Suggest concrete additional data that would address the weaknesses.  
+4. **Recommendation** – state **Proceed** or **Do not proceed**.  
+   - If **Do not proceed**, enumerate **all** disqualifying conditions that apply (see section 2).  
+   - The full case (all four sections) must be provided even when disqualifiers exist.
 
-   The disqualifiers are:
-   1. Evaluation runs are only nightly batch jobs, not performed before each action (p. 29).
-   2. Governance for the relaxation is not defined upfront, e.g., “we will govern it later” (p. 29).
-   3. The case relies on the agent “knowing when to stop” rather than an independent architectural safeguard (p. 28).
-   4. **Any** of the four evidence dimensions is completely absent (test results, failure‑mode analysis, audit findings, comparison against the human‑approved baseline) (p. 25).
+### 2. Disqualifying Conditions (must force “Do not proceed”)
 
-4. **Partial Evidence** – If a dimension is present but thin, note it as “*Limited evidence; further data collection recommended*”. This **does not** trigger a disqualifier; it should be listed as a gap, not a rejection.
+- **Batch‑only evaluation** – the notes say evaluation runs only as a nightly batch, not before each action (p. 29).  
+- **Undefined governance** – the notes contain language such as “we will govern it later” with no upfront governance plan (p. 29).  
+- **Agent‑only safeguard** – the argument relies on the autonomous agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
+- **Missing evidence dimension** – any one of the four evidence dimensions (test results, failure‑mode analysis, audit findings, baseline comparison) is completely absent from the notes (p. 25).
 
-5. **Honesty & Completeness** – Highlight genuine strengths found in the notes, but also:
-   - Cite any gaps or weaknesses.
-   - Do not overstate the quality or completeness of the evidence.
-   - Ensure the case reads as a balanced, professional argument.
+If any of these four items are true, the Recommendation must be **Do not proceed** and each applicable condition must be listed by name.
 
-6. **Compliance Language** – Throughout the document, reference compliance with **Section 8 (Strategy C)**, especially the need for explicit architectural safeguards and defined governance.
+### 3. General Requirements
 
-### Writing Style
-- Professional, concise, and persuasive where appropriate.
-- Use bullet points or short paragraphs for clarity.
-- Avoid jargon not present in the notes.
-- Keep the tone factual; only make recommendations based on the evidence and disqualifier assessment.
+- **Honesty** – cite only text that appears verbatim in the notes; do not fabricate or extrapolate.  
+- **Completeness** – even when a disqualifier is present, output the entire case so reviewers have full context.  
+- **Compliance language** – repeatedly reference compliance with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, especially the need for explicit architectural safeguards and defined governance.  
+- **Style** – professional, concise, bullet‑point or short‑paragraph format; avoid jargon not present in the notes; remain factual and balanced.
 
-Follow these instructions exactly; the surrounding system will handle final formatting. +Follow these instructions exactly; the surrounding system will add any required outer formatting. 
```


## Held-out check (best-ever candidate)

- Candidate: `c1c4bd35c8d38248` (rotation scalar 0.8438)
- Held-out quality: 0.9759 (passes: 0.9782, 0.9737)
- Held-out scalar: 0.8292 (passes: 0.8319, 0.8265)
- All held-out tasks valid: True
