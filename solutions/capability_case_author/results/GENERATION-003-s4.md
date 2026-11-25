# Generation 3 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 77.9%
- Aggregate throughput: 153.7 tok/s (555788 completion tokens / 3616.5s)

## Archive

- Island 0: coverage 5.6%, QD score 1.548, unique ancestors 2
- Island 1: coverage 13.9%, QD score 3.644, unique ancestors 3
- Island 2: coverage 13.9%, QD score 3.793, unique ancestors 3
- Island 3: coverage 8.3%, QD score 2.306, unique ancestors 2
- Cells newly claimed this generation: 5

## Quality

- Best scalar this generation: 0.8245
- Median scalar of newly-claimed: 0.7889

## Cost

- Budget: {'generation': 3, 'max_generations': 10, 'tokens_used_total': 4991834, 'max_tokens': 20000000, 'elapsed_s_total': 14228.7, 'generation_wall_s': 3616.5}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 1, cell (3, 5), scalar 0.8192

parent `fdfc52c53f9e6652` -> candidate `caaec5102bd79b15`

```diff
--- parent fdfc52c53f9e6652
+++ candidate caaec5102bd79b15
@@ -1,28 +1,40 @@
-You are to draft a capability case for requesting the removal of per‑action human approval for an operational‑change gateway action on an industrial site. Follow the instructions below exactly.
+You are to compose a **Capability Case** that requests the removal of per‑action human approval for an operational‑change gateway action. Use only the raw evidence notes supplied as input; do not invent or extrapolate any information.
 
-**Input** – You will be given the team’s raw evidence notes.
+### Input
+The team’s raw evidence notes (free‑form text).
 
-**Output** – A complete, honest, and compliant capability case that adheres to Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Do **not** fabricate any evidence; only reference items that appear explicitly in the notes.
+### Output
+A single, self‑contained case that follows the outline below, written in a professional, factual tone and compliant with Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Structure of the case**
-1. **Brief summary** of the request and its context.  
-2. **Evidence Overview** – for each of the four required dimensions, list the evidence that is present in the notes:
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
-   If a dimension is missing, note that it is absent (do not treat this as a disqualifier unless it triggers condition 4 below).  
-3. **Assessment** – objectively discuss strengths, weaknesses, and any thin evidence, and suggest additional evidence gathering where appropriate.  
-4. **Recommendation** – based on the criteria below, state either “Proceed” or “Do not proceed.” If the recommendation is “Do not proceed,” explicitly name every disqualifying condition that applies.
+#### Required sections (in this order)
 
-**Disqualifying conditions (must trigger “Do not proceed” if any are present)**
-1. The evaluation runs only as a nightly batch rather than before each action (p. 29).  
-2. Governance for the relaxation is not defined up‑front; the notes say “we will govern it later” (p. 29).  
-3. The case relies on the autonomous agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
-4. Any one of the four evidence dimensions (test results, failure‑mode analysis, audit findings, comparison against baseline) is **entirely absent** from the notes (p. 25).
+1. **Summary** – One‑paragraph description of the requested relaxation and the operational context.
+2. **Evidence Overview** – For each of the four mandatory dimensions, state exactly what appears in the notes:
+   - **Test results**
+   - **Failure‑mode analysis**
+   - **Audit findings**
+   - **Comparison to the human‑approved baseline**  
+   Use the phrasing “*Evidence present:* …” when items exist, “*Evidence absent*” when a dimension is completely missing, and “*Limited evidence; further data recommended*” when the material is sparse (this does **not** count as a disqualifier).
+3. **Risk & Evidence Assessment** – Objectively discuss strengths, weaknesses, and any thin evidence identified above. Propose additional evidence collection where appropriate.
+4. **Recommendation** – State either **“Proceed”** or **“Do not proceed.”**  
+   - If **“Do not proceed”**, list **all** disqualifying conditions that apply (see list below).  
+   - The full case (all four sections) must be provided even when disqualifiers are present.
 
-**Special note on thin evidence** – If evidence exists but is sparse, the case should recommend gathering more evidence; this **does not** constitute a disqualifier.
+#### Disqualifying conditions (must force “Do not proceed”)
+Any one of the following found in the notes triggers a negative recommendation:
 
-**Tone and style** – Professional, objective, and balanced. Highlight genuine strengths, acknowledge gaps, and avoid any persuasive language that overstretches the supplied data.
+1. Evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **not defined up‑front**; e.g., the notes contain “we will govern it later” (p. 29).  
+3. The argument relies on the autonomous agent **“knowing when to stop”** instead of an independent architectural safeguard (p. 28).  
+4. **Any** of the four evidence dimensions (test results, failure‑mode analysis, audit findings, baseline comparison) is **entirely absent** (p. 25).
 
-Produce the case exactly as described; no additional commentary or formatting outside the required sections is needed.+#### Special note on thin evidence
+Sparse but present evidence does **not** constitute a disqualifier; it should be flagged in the Assessment section with a recommendation to gather more data.
+
+#### Style guidelines
+- Be concise, objective, and balanced.  
+- Cite evidence exactly as it appears in the notes; do not paraphrase beyond the literal content.  
+- Avoid persuasive language that overstretches the supplied data.  
+- Reference Section 8 (Strategy C) where relevant, especially when discussing architectural safeguards or governance.
+
+Produce the case exactly as specified; no extra sections, commentary, or formatting outside the four required parts. 
```

### Island 1, cell (3, 5), scalar 0.8245

parent `fdfc52c53f9e6652` -> candidate `5ba2a857fe3a051a`

```diff
--- parent fdfc52c53f9e6652
+++ candidate 5ba2a857fe3a051a
@@ -1,28 +1,44 @@
-You are to draft a capability case for requesting the removal of per‑action human approval for an operational‑change gateway action on an industrial site. Follow the instructions below exactly.
+You are to create a **Capability Case** that requests the removal of per‑action human approval for an operational‑change gateway action on an industrial site. Follow every instruction exactly; the surrounding system will add any required headings or formatting.
 
-**Input** – You will be given the team’s raw evidence notes.
+**Input** – The raw evidence notes supplied by the team.
 
-**Output** – A complete, honest, and compliant capability case that adheres to Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Do **not** fabricate any evidence; only reference items that appear explicitly in the notes.
+**Output** – A complete, truthful, and Section 8 (Strategy C)‑compliant case. Do **not** invent or paraphrase evidence; only cite items that appear verbatim in the notes.
 
-**Structure of the case**
-1. **Brief summary** of the request and its context.  
-2. **Evidence Overview** – for each of the four required dimensions, list the evidence that is present in the notes:
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
-   If a dimension is missing, note that it is absent (do not treat this as a disqualifier unless it triggers condition 4 below).  
-3. **Assessment** – objectively discuss strengths, weaknesses, and any thin evidence, and suggest additional evidence gathering where appropriate.  
-4. **Recommendation** – based on the criteria below, state either “Proceed” or “Do not proceed.” If the recommendation is “Do not proceed,” explicitly name every disqualifying condition that applies.
+### Required structure (present the sections in this order)
 
-**Disqualifying conditions (must trigger “Do not proceed” if any are present)**
-1. The evaluation runs only as a nightly batch rather than before each action (p. 29).  
-2. Governance for the relaxation is not defined up‑front; the notes say “we will govern it later” (p. 29).  
-3. The case relies on the autonomous agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
-4. Any one of the four evidence dimensions (test results, failure‑mode analysis, audit findings, comparison against baseline) is **entirely absent** from the notes (p. 25).
+1. **Summary** – One‑ to two‑sentence description of the requested relaxation and the operational context.
 
-**Special note on thin evidence** – If evidence exists but is sparse, the case should recommend gathering more evidence; this **does not** constitute a disqualifier.
+2. **Evidence Summary** – For each of the four mandatory dimensions list what the notes contain:
+   - **Test results**
+   - **Failure‑mode analysis**
+   - **Audit findings**
+   - **Comparison to the human‑approved baseline**  
+   Use the exact wording from the notes.  
+   - If a dimension is missing, write **“Evidence absent.”**  
+   - If a dimension is present but the material is sparse, write **“Limited evidence; further data recommended.”** (this does **not** trigger a disqualification).
 
-**Tone and style** – Professional, objective, and balanced. Highlight genuine strengths, acknowledge gaps, and avoid any persuasive language that overstretches the supplied data.
+3. **Assessment** – Objectively discuss:
+   - strengths supported by the supplied evidence,
+   - weaknesses or gaps identified,
+   - any thin‑evidence notes from the previous section,
+   - suggestions for additional data collection or analysis.
 
-Produce the case exactly as described; no additional commentary or formatting outside the required sections is needed.+4. **Recommendation** – State **“Proceed”** or **“Do not proceed.”**  
+   - If the decision is **“Do not proceed,”** enumerate **all** disqualifying conditions that apply (see list below).  
+   - The full case (all four sections) must still be provided even when disqualifiers exist.
+
+### Disqualifying conditions (must force “Do not proceed” if any are true)
+
+1. The evaluation is performed **only as a nightly batch** and not before each individual action (p. 29).  
+2. Governance for the relaxation is **not defined up‑front**; the notes contain language such as “we will govern it later” (p. 29).  
+3. The argument relies on the autonomous agent **“knowing when to stop”** rather than on an independent architectural safeguard (p. 28).  
+4. **Any one** of the four evidence dimensions (test results, failure‑mode analysis, audit findings, baseline comparison) is **completely absent** from the notes (p. 25).
+
+### General guidance
+
+- **Honesty:** Cite only the exact evidence present; do not extrapolate or fabricate.  
+- **Completeness:** Provide the entire case even when disqualifiers are present so reviewers can see the full context.  
+- **Tone:** Professional, factual, balanced. Avoid persuasive language that exceeds the supplied data.  
+- **Compliance language:** Reference compliance with Section 8 (Strategy C) where relevant, especially concerning architectural safeguards and defined governance.
+
+Produce the case exactly as described; do not add extra sections, commentary, or formatting beyond the four required parts. 
```

### Island 1, cell (3, 4), scalar 0.7003

parent `fdfc52c53f9e6652` -> candidate `0b118bbf5b7075d3`

```diff
--- parent fdfc52c53f9e6652
+++ candidate 0b118bbf5b7075d3
@@ -1,28 +1,35 @@
-You are to draft a capability case for requesting the removal of per‑action human approval for an operational‑change gateway action on an industrial site. Follow the instructions below exactly.
+You are to create a **Capability Case** that requests the removal of per‑action human approval for an operational‑change gateway action on an industrial site. Use only the raw evidence notes supplied as input; do not add or infer any information.
 
-**Input** – You will be given the team’s raw evidence notes.
+**Output must contain exactly the following sections, in this order**
 
-**Output** – A complete, honest, and compliant capability case that adheres to Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Do **not** fabricate any evidence; only reference items that appear explicitly in the notes.
+1. **Summary** – a brief statement of the requested relaxation and the operational context.  
+2. **Evidence Summary** – for each of the four mandatory dimensions, list what appears in the notes:  
+   - *Test results*  
+   - *Failure‑mode analysis*  
+   - *Audit findings*  
+   - *Baseline comparison*  
 
-**Structure of the case**
-1. **Brief summary** of the request and its context.  
-2. **Evidence Overview** – for each of the four required dimensions, list the evidence that is present in the notes:
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
-   If a dimension is missing, note that it is absent (do not treat this as a disqualifier unless it triggers condition 4 below).  
-3. **Assessment** – objectively discuss strengths, weaknesses, and any thin evidence, and suggest additional evidence gathering where appropriate.  
-4. **Recommendation** – based on the criteria below, state either “Proceed” or “Do not proceed.” If the recommendation is “Do not proceed,” explicitly name every disqualifying condition that applies.
+   • If a dimension is present, reproduce the items verbatim.  
+   • If a dimension is missing, write **Evidence absent**.  
+   • If a dimension is present but the material is sparse, write **Limited evidence; further data recommended**. (This is *not* a disqualifier.)  
+3. **Risk & Evidence Assessment** – objectively discuss strengths, weaknesses, and any thin evidence identified above. Suggest additional evidence collection where appropriate.  
+4. **Recommendation** – state **Proceed** or **Do not proceed**.  
 
-**Disqualifying conditions (must trigger “Do not proceed” if any are present)**
-1. The evaluation runs only as a nightly batch rather than before each action (p. 29).  
-2. Governance for the relaxation is not defined up‑front; the notes say “we will govern it later” (p. 29).  
-3. The case relies on the autonomous agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
-4. Any one of the four evidence dimensions (test results, failure‑mode analysis, audit findings, comparison against baseline) is **entirely absent** from the notes (p. 25).
+   • If the recommendation is **Do not proceed**, list **all** disqualifying conditions that apply (see list below).  
+   • The full case (all four sections) must be provided even when disqualifiers exist.
 
-**Special note on thin evidence** – If evidence exists but is sparse, the case should recommend gathering more evidence; this **does not** constitute a disqualifier.
+**Disqualifying conditions (must force “Do not proceed”)**
 
-**Tone and style** – Professional, objective, and balanced. Highlight genuine strengths, acknowledge gaps, and avoid any persuasive language that overstretches the supplied data.
+- **Batch‑only evaluation** – the notes indicate the evaluation runs only as a nightly batch, not before each action (p. 29).  
+- **Undefined governance** – the notes contain a statement such as “we will govern it later” with no upfront governance plan (p. 29).  
+- **Reliance on agent intuition** – the argument depends on the autonomous agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
+- **Missing evidence dimension** – any one of the four required dimensions is completely absent from the notes (p. 25).
 
-Produce the case exactly as described; no additional commentary or formatting outside the required sections is needed.+**General guidance**
+
+- **Honesty:** Cite only evidence that appears explicitly in the notes; never fabricate.  
+- **Completeness:** Even when a disqualifier is present, deliver the entire case so reviewers see the full context.  
+- **Tone:** Professional, factual, balanced. Avoid persuasive language that exceeds the supplied data.  
+- **Compliance:** Refer to Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper where relevant, especially regarding architectural safeguards and defined governance.
+
+Produce the case exactly as specified; do not add extra sections, commentary, or formatting outside the four required parts.  
```

### Island 2, cell (4, 4), scalar 0.7407

parent `4427f2f2e9322ed6` -> candidate `e282e5601f248935`

```diff
--- parent 4427f2f2e9322ed6
+++ candidate e282e5601f248935
@@ -1,34 +1,37 @@
-You are assisting an operations team in drafting a **capability case** that seeks to relax per‑action human approval for an operational‑change gateway action on an industrial site.
+You are to draft a **capability case** that requests relaxing per‑action human approval for a specific operational‑change gateway action. Use **only** the raw evidence notes supplied; do not add, infer, or assume any information not explicitly present.
 
-Using **only** the raw evidence notes provided, produce a complete, honest, and compliant case that adheres to Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Structure the output with the following sections (you may add brief headings, but keep the format simple as the surrounding template will enforce the final layout):
+### Output requirements
+Produce a complete, factual case that complies with Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Follow the logical order below; exact headings will be added by the surrounding template.
 
-1. **Objective & Recommendation** – State the action being proposed and the overall recommendation (“Proceed” or “Do not proceed”).  
-2. **Evidence Summary** – For each of the four required evidence dimensions, report what is present in the notes:
+1. **Objective & Recommendation**  
+   - State the proposed action.  
+   - Give a single recommendation: **“Proceed”** or **“Do not proceed.”**
+
+2. **Evidence Summary** – For each of the four required dimensions list what the notes contain (or state “absent”):
    - Test results  
    - Failure‑mode analysis  
    - Audit findings  
-   - Comparison against the human‑approved baseline  
+   - Comparison to the human‑approved baseline  
 
-   If a dimension is missing, note that it is absent and that additional evidence should be gathered, but **do not** treat this as a disqualifier.
+   If a dimension is absent, note that additional evidence should be collected, but **do not** treat this as a disqualifier.
 
-3. **Compliance Check** – Verify the case against the disqualifying criteria listed below.  
+3. **Disqualification Assessment** – Check the case against the four disqualifying conditions. If **any** condition applies, the recommendation **must be “Do not proceed.”** List every applicable disqualifier using the exact phrases:
 
-   **Disqualifying criteria (must trigger a “Do not proceed” recommendation and be explicitly named):**  
-   - The evaluation runs only as a nightly batch instead of before each action (p. 29).  
-   - Governance for the relaxation is not defined upfront, e.g., “we will govern it later” (p. 29).  
-   - The case relies on the agent knowing when to stop rather than an independent architectural safeguard (p. 28).  
-   - Any of the four evidence dimensions is **entirely absent** (test results, failure‑mode analysis, audit findings, or baseline comparison) (p. 25).  
+   - **Disqualifier: evaluation runs only as nightly batch** (p. 29)  
+   - **Disqualifier: governance undefined or deferred** (p. 29)  
+   - **Disqualifier: reliance on agent self‑termination** (p. 28)  
+   - **Disqualifier: missing <dimension>** where <dimension> is one of test results, failure‑mode analysis, audit findings, or baseline comparison (p. 25)
 
-   If any of these conditions apply, the case must conclude with **“Do not proceed”** and explicitly name the specific disqualifier(s) (e.g., “Disqualifier: evaluation runs only as nightly batch”).  
+   When a disqualifier is present, do not include mitigations or a “Proceed” recommendation.
 
-4. **Strengths & Mitigations** – Highlight any genuine strengths evident in the notes (e.g., robust test coverage, thorough audit comments) and, where appropriate, propose mitigations for gaps that do **not** meet a disqualifying condition.
+4. **Strengths & Non‑Disqualifying Gaps** – Highlight any genuine strengths evident in the notes (e.g., robust test coverage, clear audit outcomes). For gaps that are **not** disqualifying (thin evidence, partial data), suggest concrete mitigation or data‑gathering steps.
 
-5. **Final Decision Rationale** – Summarize why the recommendation is justified, referencing the evidence and compliance check.  
+5. **Rationale** – Concisely explain why the recommendation follows from the evidence and the disqualification check.
 
-**General rules:**  
-- Do **not** fabricate or extrapolate evidence; only include items that appear in the provided notes.  
-- Be concise, factual, and balanced—avoid persuasive language that overstates the evidence.  
-- If thin evidence is present (some data but not exhaustive), note the need for further data collection, but this alone does not constitute a disqualifier.  
-- Follow the exact wording “Do not proceed” when recommending rejection, and list each applicable disqualifier by name.
+### General rules
+- **No fabrication:** only cite evidence that appears in the notes.  
+- **Clarity:** be concise, objective, and avoid persuasive exaggeration.  
+- **Thin evidence:** may be flagged for further collection but never triggers a “Do not proceed” unless the entire dimension is missing.  
+- Use the exact wording **“Do not proceed”** for a rejection and list each disqualifier verbatim as shown above.
 
-Produce the case now according to these instructions.+Generate the case now following these instructions.
```

### Island 3, cell (4, 5), scalar 0.7889

parent `e77a5e0959a4ab18` -> candidate `25549c648cabbf50`

```diff
--- parent e77a5e0959a4ab18
+++ candidate 25549c648cabbf50
@@ -1,38 +1,49 @@
-You are an analyst tasked with drafting a capability case for the Operations Review Board, requesting relaxation of per‑action human approval for an operational‑change gateway action. Using **only** the raw evidence notes supplied by the team, produce a complete, honest, and standards‑compliant case that follows Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an analyst drafting a **Capability Case** for the Operations Review Board to request relaxation of per‑action human approval for an operational‑change gateway action.  
+Use **only** the raw evidence notes supplied by the team; do not add, infer, or extrapolate any information.
 
-Your output must contain the following sections in this exact order:
+Your response must follow **exactly** the structure below, in the given order, and use the specified headings (case‑sensitive).
 
-1. **Title**  
-   - “Capability Case: Relaxation of Per‑Action Human Approval”
+---
 
-2. **Summary of Evidence** – For each of the four required evidence dimensions, list what is actually present in the notes (use bullet points). The dimensions are:  
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
+### 1. Title  
+`Capability Case: Relaxation of Per‑Action Human Approval`
 
-   If a dimension is missing, note its absence explicitly. **Do not fabricate or extrapolate any evidence.**
+### 2. Evidence Summary  
+For each of the four required evidence dimensions list **exactly** what appears in the notes (bullet points). If a dimension is not mentioned, write `Absent`.  
+- **Test results**  
+- **Failure‑mode analysis**  
+- **Audit findings**  
+- **Comparison against the human‑approved baseline**  
 
-3. **Disqualifier Assessment** – Examine the notes for any of the following disqualifying conditions (cite the page numbers from the whitepaper):  
-   - Evaluation runs are performed only as a nightly batch rather than before each action (p. 29).  
-   - Governance for the relaxation is undefined or deferred (“we will govern it later”) (p. 29).  
-   - The case relies on the agent’s internal decision‑to‑stop rather than an independent architectural safeguard (p. 28).  
-   - Any of the four evidence dimensions is completely absent.  
+*Do not fabricate any bullet; if the notes contain only partial data, list the partial items and note that the evidence is thin.*
 
-   - If any disqualifier is present, list each one by name, explain why it fails the criteria, and **must** set the overall recommendation to **“Do not proceed.”**  
-   - If no disqualifier is found, state “No disqualifiers identified.”
+### 3. Disqualifier Assessment  
+Check the notes for any of the following disqualifying conditions (cite the white‑paper page number). For each condition that applies, list it on its own line, include a brief quote or paraphrase from the notes, and explain why it fails the criteria.
 
-4. **Recommendation** – State clearly either:  
-   - “Proceed with relaxation” (if no disqualifiers were found), **or**  
-   - “Do not proceed” (if one or more disqualifiers were identified).  
+- Evaluation runs are performed **only as a nightly batch** instead of before each action (p. 29).  
+- Governance for the relaxation is **undefined or deferred** (“we will govern it later”) (p. 29).  
+- The case relies on the **agent’s internal “knowledge of when to stop”** rather than an independent architectural safeguard (p. 28).  
+- **Any** of the four evidence dimensions is **completely absent** (p. 25).  
 
-5. **Rationale** – Provide a concise justification linking the evidence (or lack thereof) to the recommendation.  
-   - When recommending “Proceed with relaxation,” highlight only the strengths that are explicitly documented in the notes.  
-   - When recommending “Do not proceed,” summarize the disqualifier(s) and note any corrective actions needed (e.g., define governance, add pre‑action evaluation runs, implement an independent safeguard, or collect the missing evidence dimension).
+If one or more disqualifiers are found, **set the overall recommendation to “Do not proceed.”**  
+If none are found, write `No disqualifiers identified.`
 
-**Additional guidance**
+### 4. Recommendation  
+Write a single line containing **only** one of the following exact phrases:
 
-- Thin or incomplete evidence (e.g., partial test results) is **not** a disqualifier; simply note that further evidence should be gathered.  
-- The case must be transparent, evidence‑driven, and must not rely on undocumented safeguards or postponed governance, in line with Section 8 (Strategy C).  
-- Use a professional, objective tone; avoid exaggeration or persuasive language not supported by the notes.  
-- If the notes contain no evidence at all, the case should explicitly state the lack of evidence, list the relevant disqualifiers, and recommend “Do not proceed.”+- `Proceed with relaxation`  
+- `Do not proceed`
+
+### 5. Rationale  
+Provide a concise justification that directly ties the evidence (or its absence) to the recommendation.
+
+- For **Proceed with relaxation**: highlight only the strengths that are explicitly documented in the notes.  
+- For **Do not proceed**: summarize the disqualifier(s) and list the corrective actions required (e.g., define governance, add pre‑action evaluation runs, implement an independent safeguard, or obtain the missing evidence dimension).
+
+---
+
+#### Additional Rules
+- **Thin or incomplete evidence is NOT a disqualifier**; simply note that additional evidence would be beneficial.  
+- The case must be transparent, evidence‑driven, and must not reference any undocumented safeguards or postponed governance.  
+- Use a professional, objective tone; avoid persuasive language not supported by the notes.  
+- If the notes contain **no evidence at all**, explicitly state the lack of evidence, list the applicable disqualifiers, and issue a `Do not proceed` recommendation.
```

