> **Mixed run (TODO.md decision 83).** Two searches, s1 (orphaned, old wording) and s2, ran concurrently on one live archive and overwrote each other's reports. Per-generation figures here cannot be attributed to either run; candidate scores remain valid measurements.

# Generation 1 — capability_case_author

## Throughput

- Peak queue depth: 48
- Sustained (median) queue depth: 47.0
- Prefix cache hit rate: 71.5%
- Aggregate throughput: 108.4 tok/s (571877 completion tokens / 5277.2s)

## Archive

- Island 0: coverage 8.3%, QD score 2.336, unique ancestors 1
- Island 1: coverage 11.1%, QD score 3.294, unique ancestors 2
- Island 2: coverage 8.3%, QD score 2.119, unique ancestors 3
- Island 3: coverage 8.3%, QD score 2.247, unique ancestors 2
- Cells newly claimed this generation: 6

## Quality

- Best scalar this generation: 0.8422
- Median scalar of newly-claimed: 0.8082

## Cost

- Budget: {'generation': 1, 'max_generations': 10, 'tokens_used_total': 2459547, 'max_tokens': 20000000, 'elapsed_s_total': 10025.2, 'generation_wall_s': 5277.2}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (5, 5), scalar 0.7359

parent `bd32585020d44377` -> candidate `041c44bfbc5622dd`

```diff
--- parent bd32585020d44377
+++ candidate 041c44bfbc5622dd
@@ -1,31 +1,45 @@
-You are an analyst drafting a **Capability Case** that requests the removal of per‑action human approval for an operational‑change gateway action on an industrial site.  
+You are an analyst preparing a **Capability Relaxation Case** to request removal of per‑action human approval for a specific operational‑change gateway action.  
+Work **exclusively** from the raw evidence notes supplied; do not add, infer, or modify any information. Every statement must be traceable to those notes.
 
-Using **only** the raw evidence notes provided by the operations team, produce a complete, honest, and compliant case that follows the structure below. Do **not** invent any evidence; every claim must be directly supported by the notes.
+### Workflow
 
-### Required Structure
-1. **Executive Summary** – Briefly state the purpose of the case and the overall recommendation.  
-2. **Evidence Summary** – For each of the four evidence dimensions, list what the notes contain (or explicitly state “not provided” if absent):  
+1. **Collect Evidence**  
+   For each of the four mandatory evidence dimensions, copy exactly what the notes provide (verbatim or quoted). If a dimension has no entry, record **“Absent”**.  
    - Test results  
    - Failure‑mode analysis  
    - Audit findings  
-   - Comparison against the human‑approved baseline  
-3. **Gap Analysis** – Identify any missing or incomplete evidence dimensions. Note that missing evidence **is not** a disqualifier; it should be recorded here for future work.  
-4. **Disqualification Check** – Evaluate the four disqualifier conditions. If **any** condition holds, **must**:
-   - Set the recommendation to **“Do not proceed.”**  
-   - Name the specific disqualifier(s) that triggered this outcome.  
-   The disqualifiers are:  
-   a. Evaluation runs only as a nightly batch rather than before each action (p.29).  
-   b. Governance for the relaxation is undefined or deferred (“we will govern it later”) (p.29).  
-   c. The case relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p.28).  
-   d. Any of the four evidence dimensions is **entirely absent**.  
-5. **Compliance Statement** – Confirm that the case complies with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper.  
-6. **Recommendation** –  
-   - If no disqualifiers are present, recommend **“Proceed”** and justify the decision based on the available evidence.  
-   - If disqualifiers are present, recommend **“Do not proceed”** as required in step 4.  
+   - Comparison with the human‑approved baseline  
 
-### Writing Guidelines
-- Maintain a formal, objective tone; avoid persuasive language that exaggerates strengths.  
-- Cite the evidence explicitly (e.g., “The test results show … as recorded in the notes on …”).  
-- When noting gaps, suggest next steps for gathering the missing evidence rather than rejecting the case outright.  
-- Ensure the final output is self‑contained and ready for the review board, adhering to the output format prescribed by the surrounding system (the surrounding template will handle headings, but include the headings above verbatim).  
-- Do not reference these instructions in the final case.+2. **Identify Gaps**  
+   List any dimensions marked “Absent”. Gaps are **not** automatic disqualifiers; they should be noted for future data‑gathering.
+
+3. **Apply Disqualifier Rules**  
+   Examine the notes for the four disqualifier conditions. If **any** condition is true, the case **must** conclude **“Do not proceed”** and must name every condition that applies. The conditions are:
+   - **Batch‑only evaluation** – notes say evaluation runs only as a nightly batch, not before each action (p. 29).  
+   - **Undefined governance** – notes contain “we will govern it later”, or otherwise lack a defined governance model for the relaxation (p. 29).  
+   - **Agent‑self‑stop reliance** – the proposed approach depends on the agent knowing when to stop instead of an independent architectural safeguard (p. 28).  
+   - **Fully missing evidence dimension** – any of the four dimensions is completely absent **and** the case attempts to proceed without acknowledging that gap. (If the gap is acknowledged, it is not a disqualifier.)
+
+4. **Compliance Confirmation**  
+   State that the case follows **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, referencing the independent safeguard and pre‑action evaluation requirements.
+
+5. **Recommendation**  
+   - If no disqualifiers are triggered, recommend **“Proceed”** and justify the recommendation using the collected evidence.  
+   - If one or more disqualifiers are triggered, recommend **“Do not proceed”** and list the triggering disqualifier(s).
+
+### Output Structure (headings must appear exactly as written; surrounding template will format them)
+
+1. **Executive Summary** – purpose of the request and overall recommendation.  
+2. **Evidence Inventory** – four subsections (Test results, Failure‑mode analysis, Audit findings, Comparison with baseline) showing the verbatim notes or “Absent”.  
+3. **Gap Analysis** – enumerate any “Absent” dimensions and suggest next steps for obtaining them.  
+4. **Disqualifier Evaluation** – list each disqualifier that applies; if none apply, state “No disqualifiers found”.  
+5. **Compliance Statement** – confirm adherence to Section 8 (Strategy C).  
+6. **Final Recommendation** – “Proceed” or “Do not proceed” with the required justification.
+
+### Writing Rules
+- Use a formal, objective tone; avoid persuasive fluff.  
+- Every claim must cite the original note (e.g., “The notes state …”).  
+- Do not mention these instructions in the final case.  
+- Ensure the case is self‑contained and ready for the review board.
+
+Follow this process precisely; any deviation (fabricated evidence, omitted disqualifier check, or missing heading) will cause downstream rejection.
```

### Island 0, cell (3, 5), scalar 0.7682

parent `bd32585020d44377` -> candidate `0ac90b9988b6b808`

```diff
--- parent bd32585020d44377
+++ candidate 0ac90b9988b6b808
@@ -1,31 +1,30 @@
-You are an analyst drafting a **Capability Case** that requests the removal of per‑action human approval for an operational‑change gateway action on an industrial site.  
+You are an analyst tasked with producing a **Capability Relaxation Case** that asks to remove the per‑action human‑approval step for a specific operational‑change gateway action.  
+Use **only** the raw evidence notes supplied by the operations team—do not add, infer, or paraphrase beyond what is explicitly written.
 
-Using **only** the raw evidence notes provided by the operations team, produce a complete, honest, and compliant case that follows the structure below. Do **not** invent any evidence; every claim must be directly supported by the notes.
+### Output Structure (headings will be added by the outer template, but keep this logical order)
 
-### Required Structure
-1. **Executive Summary** – Briefly state the purpose of the case and the overall recommendation.  
-2. **Evidence Summary** – For each of the four evidence dimensions, list what the notes contain (or explicitly state “not provided” if absent):  
+1. **Executive Summary** – one‑sentence purpose of the request and the final recommendation.  
+2. **Evidence Inventory** – for each of the four required dimensions, copy exactly what appears in the notes or state **“absent”** if nothing is provided:  
    - Test results  
    - Failure‑mode analysis  
    - Audit findings  
-   - Comparison against the human‑approved baseline  
-3. **Gap Analysis** – Identify any missing or incomplete evidence dimensions. Note that missing evidence **is not** a disqualifier; it should be recorded here for future work.  
-4. **Disqualification Check** – Evaluate the four disqualifier conditions. If **any** condition holds, **must**:
-   - Set the recommendation to **“Do not proceed.”**  
-   - Name the specific disqualifier(s) that triggered this outcome.  
-   The disqualifiers are:  
-   a. Evaluation runs only as a nightly batch rather than before each action (p.29).  
-   b. Governance for the relaxation is undefined or deferred (“we will govern it later”) (p.29).  
-   c. The case relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p.28).  
-   d. Any of the four evidence dimensions is **entirely absent**.  
-5. **Compliance Statement** – Confirm that the case complies with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper.  
+   - Comparison with the human‑approved baseline  
+3. **Missing‑Evidence Record** – list any dimension marked *absent*. This is a gap to be filled later; it does **not** by itself force a “Do not proceed” decision.  
+4. **Disqualification Evaluation** – check the four disqualifier rules. For each rule that applies, list it verbatim and note the page reference. If **any** rule applies, the case must end with the recommendation **“Do not proceed.”** The rules are:  
+   a. Evaluation is performed only as a nightly batch, not before each individual action (p. 29).  
+   b. Governance for the relaxation is undefined or deferred (“we will govern it later”) (p. 29).  
+   c. The approach relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard (p. 28).  
+   d. Any evidence dimension is completely absent **and** the case attempts to proceed without acknowledging that gap.  
+5. **Compliance Statement** – affirm that the case follows **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, citing the independent safeguard and pre‑action evaluation requirements where relevant.  
 6. **Recommendation** –  
-   - If no disqualifiers are present, recommend **“Proceed”** and justify the decision based on the available evidence.  
-   - If disqualifiers are present, recommend **“Do not proceed”** as required in step 4.  
+   *If no disqualifiers are found*: write **“Proceed”** and justify the decision with the evidence present.  
+   *If one or more disqualifiers are found*: write **“Do not proceed”** and enumerate the triggering disqualifier(s).  
 
-### Writing Guidelines
-- Maintain a formal, objective tone; avoid persuasive language that exaggerates strengths.  
-- Cite the evidence explicitly (e.g., “The test results show … as recorded in the notes on …”).  
-- When noting gaps, suggest next steps for gathering the missing evidence rather than rejecting the case outright.  
-- Ensure the final output is self‑contained and ready for the review board, adhering to the output format prescribed by the surrounding system (the surrounding template will handle headings, but include the headings above verbatim).  
-- Do not reference these instructions in the final case.+### Writing Rules
+- Keep a neutral, factual tone; avoid marketing‑style language.  
+- Every factual statement must be traceable to the supplied notes (e.g., “The notes state …”).  
+- When a dimension is absent, suggest a concrete next step for obtaining it rather than rejecting the whole case.  
+- Do **not** reference these instructions in the final output.  
+- The case must be self‑contained and ready for review; the surrounding system will insert heading formatting, so do not add extra decorative headings.  
+
+Follow this exact flow; any deviation (missing section, invented evidence, or omitted disqualifier check) will cause downstream rejection.  
```

### Island 1, cell (3, 5), scalar 0.8132

parent `fa702b401675487a` -> candidate `28c98607f4490ad0`

```diff
--- parent fa702b401675487a
+++ candidate 28c98607f4490ad0
@@ -1,24 +1,51 @@
-You are to read the team’s raw evidence notes and draft a capability case that requests the removal of per‑action human approval for an operational‑change gateway action. Follow these exact rules:
+You will turn the team’s raw evidence notes into a capability case that requests removal of per‑action human approval for an operational‑change gateway action. Follow the procedure below **exactly** and do **not** add any information that is not in the notes.
 
-1. **Identify the evidence dimensions** – locate any mention of the four required pieces of evidence:
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
+### 1. Extract the four evidence dimensions
+For each of the following, check the notes and record the content **exactly as written** (no paraphrasing that adds new facts):
+- **Test results**
+- **Failure‑mode analysis**
+- **Audit findings**
+- **Comparison against the human‑approved baseline**
 
-   Record which dimensions are present and which are absent. Do not invent any evidence; only cite what is explicitly in the notes.
+Create two lists:
+- **Present dimensions** – include a concise quote or bullet summarising the evidence.
+- **Absent dimensions** – list any of the four that have no mention at all.
 
-2. **Check for disqualifying conditions**. If any of the following are present, the case must end with the recommendation **“Do not proceed”** and must name the disqualifier(s):
-   - The evaluation is performed only as a nightly batch rather than before each action (p.29).  
-   - Governance for the relaxation is left undefined or deferred (“we will govern it later”) (p.29).  
-   - The case relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p.28).  
-   - Any one of the four evidence dimensions is completely missing (p.25).
+### 2. Identify disqualifying conditions
+Examine the notes for any of these items. If one or more are found, the case must end with a “Do not proceed” recommendation and you must name every disqualifier that applies.
 
-3. **If no disqualifier is found**:
-   - Summarize the evidence that is present, emphasizing strengths in testing, analysis, audits, and human‑operator comparison.
-   - Clearly note any missing evidence dimensions as gaps that require additional collection, but do **not** treat these gaps as a reason to reject the case.
-   - Conclude with the recommendation **“Proceed”** (or “Do not proceed” if a disqualifier was identified).
+1. Evaluation is performed **only as a nightly batch** rather than before each individual action (p. 29).  
+2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal relies on the **agent’s internal knowledge of when to stop** instead of an independent architectural safeguard (p. 28).  
+4. **Any** of the four evidence dimensions is completely missing (p. 25).
 
-4. **Compliance** – Ensure the language and reasoning comply with Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Be honest, complete, and avoid any overstated claims.
+### 3. Draft the case
+Structure the output with the headings exactly as shown (do not add extra sections).
 
-Write the case in a persuasive yet factual style, adhering to the above structure.+**Proposed Relaxation**  
+- One‑sentence description of the requested removal of per‑action human approval.
+
+**Evidence Summary**  
+- For each **present** dimension, include the quoted evidence or a bullet‑point summary taken directly from the notes.  
+- Do **not** fabricate detail.
+
+**Missing Evidence**  
+- List any **absent** dimensions identified in step 1. State that these are gaps to be filled later; they are **not** a disqualifier on their own.
+
+**Disqualifier Evaluation**  
+- For each condition in step 2 that is true, write a line: “Disqualifier: *<description>*”.  
+- If none apply, write: “No disqualifier identified.”
+
+**Recommendation**  
+- If any disqualifier was listed, output:  
+  `Recommendation: Do not proceed. Disqualifier(s): <list all identified>.`  
+- If no disqualifier was found, output:  
+  `Recommendation: Proceed.`  
+  (still keep the “Missing Evidence” list from above).
+
+### 4. Compliance and style
+- Use a factual, neutral tone; avoid exaggeration or persuasive language beyond what the evidence supports.  
+- Ensure the reasoning aligns with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper.  
+- Be complete: include every piece of evidence that exists and mention every disqualifier that applies.
+
+Follow this exact flow; the downstream system expects the headings and wording shown. Do not deviate.
```

### Island 1, cell (2, 5), scalar 0.8032

parent `09a5a1d39f01cca6` -> candidate `a01cab2b26cd078c`

```diff
--- parent 09a5a1d39f01cca6
+++ candidate a01cab2b26cd078c
@@ -1,27 +1,50 @@
-You are an analyst tasked with drafting a capability case for relaxing per‑action human approval on an operational‑change gateway action.  
+You are a compliance analyst. From the **raw evidence notes** supplied by the operations team, compose a capability case that evaluates the request to **relax per‑action human approval** for an operational‑change gateway action.  
 
-Using **only** the raw evidence notes provided by the operations team, produce a complete, honest, and structured case that complies with Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. The case must contain the following sections, in order:
+Your write‑up must follow the exact order below and use plain headings (e.g., `## Proposed Relaxation`).  Use short bullet points for lists; do **not** add any narrative beyond what is requested.
 
-1. **Proposed Relaxation** – a concise description of the requested removal of per‑action human approval.  
-2. **Evidence Summary** – for each of the four evidence dimensions, state whether the notes contain:  
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
-   Include the key points from the notes for each dimension that is present.  
-3. **Missing Evidence** – list any of the four dimensions that are entirely absent. Do **not** treat thin or incomplete evidence as a disqualifier; simply note that additional evidence may be desirable.  
-4. **Disqualifier Evaluation** – examine each of the following conditions. If a condition holds, **explicitly name it** and set the overall recommendation to **“Do not proceed.”** If none hold, note that no disqualifier applies.  
-   - Evaluation runs only as a nightly batch instead of before each action (p.29).  
-   - Governance for the relaxation is not defined upfront, e.g., “we will govern it later” (p.29).  
-   - The case relies on the agent knowing when to stop rather than an independent architectural safeguard (p.28).  
-   - Any of the four evidence dimensions is completely missing (p.25).  
-5. **Recommendation** –  
-   - If any disqualifier is present, state: **“Recommendation: Do not proceed. Disqualifier(s): …”** listing the applicable items.  
-   - If no disqualifier applies, you may recommend proceeding, but still mention any missing evidence dimensions as items for further collection.  
+---
 
-**Important constraints**
-- Do not fabricate or embellish evidence; only report what is explicitly present in the notes.  
-- Do not attempt to persuade the review board beyond what the evidence supports.  
-- Maintain a neutral, factual tone throughout.  
+### 1. Proposed Relaxation  
+*State in one sentence what approval step is being removed.*
 
-Deliver the case with clear headings for each section and concise bullet points where appropriate.+### 2. Evidence Summary  
+For each of the four required evidence dimensions, indicate **Present** or **Absent**.  
+- **Test results** – list the key observations that appear in the notes (if present).  
+- **Failure‑mode analysis** – list the main findings (if present).  
+- **Audit findings** – list any audit citations (if present).  
+- **Comparison to human‑approved baseline** – list the comparison points (if present).  
+
+### 3. Missing Evidence  
+List any dimensions marked **Absent** in the previous section.  
+*Note:* the absence of a dimension is **not** a disqualifier; simply record it as a gap that may need further collection.
+
+### 4. Disqualifier Check  
+Examine the following conditions **exactly as written**. If a condition is true, write the condition name verbatim and mark it as a disqualifier.
+
+- **Evaluation runs only as a nightly batch instead of before each action** (p.29)  
+- **Governance for the relaxation is not defined upfront** (e.g., “we will govern it later”) (p.29)  
+- **Reliance on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard** (p.28)  
+- **Any evidence dimension is completely missing** (p.25)  
+
+If a condition holds, add a line `Disqualifier: <condition text>` under this heading.
+
+### 5. Recommendation  
+- If **any** disqualifier was recorded, output exactly:  
+
+  `Recommendation: Do not proceed. Disqualifier(s): <list each disqualifier separated by commas>`  
+
+- If **no** disqualifier applies, output:  
+
+  `Recommendation: Proceed.`  
+
+  After this sentence, optionally list the missing evidence dimensions identified in Section 3 as items for future collection.
+
+---
+
+**Critical rules**
+
+1. **No invention** – report only what is explicitly in the notes; do not infer or fabricate evidence.  
+2. **Neutral tone** – stay factual; avoid persuasive language or arguments not supported by the notes.  
+3. **Compliance** – ensure the whole document is consistent with Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper.
+
+Deliver the case exactly as described, with clear headings and bullet points.
```

### Island 1, cell (4, 5), scalar 0.8383

parent `fa702b401675487a` -> candidate `4b8d3e5823b2c229`

```diff
--- parent fa702b401675487a
+++ candidate 4b8d3e5823b2c229
@@ -1,24 +1,37 @@
-You are to read the team’s raw evidence notes and draft a capability case that requests the removal of per‑action human approval for an operational‑change gateway action. Follow these exact rules:
+You will read the team’s raw evidence notes and produce a **Capability Case** that argues for removing per‑action human approval on the specified operational‑change gateway action. Follow **exactly** the steps below; do not add, omit, or reinterpret any information beyond what is written in the notes.
 
-1. **Identify the evidence dimensions** – locate any mention of the four required pieces of evidence:
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison against the human‑approved baseline  
+### 1. Evidence inventory
+For each of the four mandatory evidence dimensions, indicate whether the notes contain **any** entry:
 
-   Record which dimensions are present and which are absent. Do not invent any evidence; only cite what is explicitly in the notes.
+- **Test results**
+- **Failure‑mode analysis**
+- **Audit findings**
+- **Comparison against the human‑approved baseline**
 
-2. **Check for disqualifying conditions**. If any of the following are present, the case must end with the recommendation **“Do not proceed”** and must name the disqualifier(s):
-   - The evaluation is performed only as a nightly batch rather than before each action (p.29).  
-   - Governance for the relaxation is left undefined or deferred (“we will govern it later”) (p.29).  
-   - The case relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p.28).  
-   - Any one of the four evidence dimensions is completely missing (p.25).
+If a dimension appears, quote the relevant passage (or a concise paraphrase) and mark it **present**. If the notes contain **no** mention of that dimension, mark it **absent**. *Do not* infer or fabricate evidence.
 
-3. **If no disqualifier is found**:
-   - Summarize the evidence that is present, emphasizing strengths in testing, analysis, audits, and human‑operator comparison.
-   - Clearly note any missing evidence dimensions as gaps that require additional collection, but do **not** treat these gaps as a reason to reject the case.
-   - Conclude with the recommendation **“Proceed”** (or “Do not proceed” if a disqualifier was identified).
+### 2. Disqualifier check
+Evaluate the four disqualifying conditions. **If any condition holds, the case must end with a “Do not proceed” recommendation and must list every applicable disqualifier.**
 
-4. **Compliance** – Ensure the language and reasoning comply with Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper. Be honest, complete, and avoid any overstated claims.
+1. **Batch‑only evaluation** – the evaluation runs only as a nightly batch rather than before each action (p.29).  
+2. **Undefined governance** – the relaxation’s governance is left unspecified or deferred (e.g., “we will govern it later”) (p.29).  
+3. **Agent‑only safeguard** – the argument relies on the autonomous agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p.28).  
+4. **Missing evidence dimension** – any one of the four dimensions is **completely absent** from the notes (p.25).
 
-Write the case in a persuasive yet factual style, adhering to the above structure.+### 3. Case composition
+Produce the document in the order listed, using clear headings (you may choose the exact wording of the headings).  
+
+1. **Proposed relaxation** – a brief statement of the requested removal of per‑action human approval.  
+2. **Evidence summary** – for each dimension marked *present* in step 1, provide the extracted key points; for each *absent* dimension, simply note “Absent”.  
+3. **Missing‑evidence note** – list any absent dimensions as gaps that should be collected later. *Do not* treat these gaps as a reason to reject the case unless they trigger disqualifier 4 above.  
+4. **Disqualifier evaluation** – list each disqualifier that applies (from step 2). If none apply, state “No disqualifier identified.”  
+5. **Recommendation** –  
+   - If any disqualifier is present: **“Recommendation: Do not proceed. Disqualifier(s): …”** (enumerate).  
+   - If no disqualifier is present: **“Recommendation: Proceed.”** (still mention the missing‑evidence note from step 3).
+
+### 4. Compliance & style
+- Align all reasoning with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper.  
+- Be truthful, exhaustive, and avoid exaggeration.  
+- Use a factual, persuasive tone but never claim evidence that is not in the notes.
+
+Deliver the final case exactly as described; no extra commentary or meta‑instructions are allowed.
```

### Island 3, cell (3, 5), scalar 0.8422

parent `0de3cd324993843b` -> candidate `f9d1bcf34ed0a1e8`

```diff
--- parent 0de3cd324993843b
+++ candidate f9d1bcf34ed0a1e8
@@ -1,41 +1,43 @@
-You are an analyst tasked with drafting a capability case to request the removal of per‑action human approval for an operational‑change gateway action on an industrial site. Using **only** the raw evidence notes supplied, produce a complete, honest case that adheres to Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an analyst tasked with drafting a **Capability Case** to request removal of per‑action human approval for an operational‑change gateway action. Use **only** the raw evidence notes supplied; do not add, infer, or exaggerate any information.
 
-**Include the following sections in the case (use the fixed output format defined elsewhere; you only need to provide the content described):**
+**Required case content (follow the fixed output format defined elsewhere; provide only the sections described):**
 
-1. **Evidence Summary** – For each of the four required evidence dimensions, state whether the notes contain:
-   - Test results
-   - Failure‑mode analysis
-   - Audit findings
+1. **Evidence Summary** – For each of the four evidence dimensions, state whether the notes contain evidence and give a brief description of what is present. Use exactly the wording below for a missing dimension:  
+   *“No [dimension] evidence was provided in the source notes.”*  
+   Dimensions:  
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings  
    - Comparison against the human‑approved baseline  
 
-   Briefly summarise the content that is present. If a dimension is missing, note the absence, but do **not** treat a single missing dimension as a disqualification. Only if **all four** dimensions are absent should you recommend gathering more evidence rather than recommending a rejection.
+2. **Disqualification Check** – Examine the notes for any of the following absolute blockers. If **any** condition is found, the case **must** end with the block shown in step 3.
 
-2. **Disqualification Check** – Examine the notes for any of the following disqualifying conditions (each is a separate, absolute blocker):
-   - (a) Evaluation runs only as a nightly batch instead of before each action (p. 29).
-   - (b) Governance for the relaxation is not defined up‑front, e.g., “we will govern it later” (p. 29).
-   - (c) The case relies on the agent knowing when to stop rather than an independent architectural safeguard (p. 28).
-   - (d) Any one of the four evidence dimensions is **entirely absent** (i.e., no evidence at all for that dimension).
+   a. Evaluation runs only as a nightly batch instead of before each action (p. 29).  
+   b. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).  
+   c. The case relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).  
+   d. Any one of the four evidence dimensions is entirely absent (i.e., no evidence at all for that dimension).
 
-   If **any** of these conditions are present, the case **must** conclude with the recommendation:
+3. **Recommendation** – Output **exactly** one of the two blocks below, depending on the result of step 2.
 
+   *If any disqualifier is present:*  
    ```
    Recommendation: Do not proceed
-   Disqualifier(s): <list each applicable condition by letter and brief description>
+   Disqualifier(s): <list each applicable condition by letter (a‑d) and a brief description>
    ```
 
-3. **Recommendation (if no disqualifiers)** – If none of the disqualifying conditions apply, conclude with:
-
+   *If no disqualifier is present:*  
    ```
    Recommendation: Proceed with relaxation
-   Rationale: <concise justification showing how the presented evidence satisfies Section 8 (Strategy C)>
+   Rationale: <concise justification showing how the supplied evidence satisfies Section 8 (Strategy C)>
    ```
 
-4. **Transparency Clause** – Clearly state that the case does not contain any evidence or strengths that are not found in the supplied notes. Do not fabricate, exaggerate, or infer information beyond what is provided.
+4. **Transparency Clause** – State clearly that the case contains no evidence, strengths, or conclusions beyond what is found in the supplied notes.
 
-**Guidelines:**
-- Be persuasive only where the evidence genuinely supports it; honesty and completeness are paramount.
-- Explicitly name any disqualifier(s) that trigger a “Do not proceed” recommendation.
-- If evidence is thin (e.g., only one dimension present) but no disqualifier is triggered, note the limitation and suggest additional evidence collection, but still follow the recommendation logic above.
-- Do not add any extra instructions, commentary, or formatting beyond the required content.
+**Guidelines**
+- Be honest and complete; only cite evidence that appears in the notes.
+- If a dimension is missing, note it as prescribed; this automatically triggers a disqualification (step 2‑d).
+- Do not add any extra headings, commentary, or formatting beyond the sections above.
+- If evidence is thin but none of the disqualifying conditions apply, you may briefly note the limitation in the Rationale, but the recommendation must follow the logic above.
+- Follow the exact wording for the recommendation blocks; the surrounding template will handle final formatting.
 
 Proceed to write the capability case according to these instructions.
```

