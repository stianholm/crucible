"""The failure taxonomy. See PHASE-4.md task 4.1.

Two stages, run rarely, not per failure: cluster, then name. Classifying a
new failure afterward is nearest-centroid lookup, no model call.

Clustering here uses TF-IDF, not the embedding model PLAN.md's roster
calls for (Qwen3-Embedding-0.6B). Confirmed 2026-09-27: proposer (0.74)
and judge (0.09) already hold 83% of this machine's unified memory as a
standing reservation, and no third CUDA process can even initialize
alongside them - not a tuning problem, verified with both a persistent
server and a fresh ephemeral container, both hit a raw
`torch.AcceleratorError: CUDA error: out of memory` at basic device init.
TF-IDF costs no GPU memory and is a real, if coarser, substitute: failure
evidence text here is short and formulaic (gate names, check names, error
snippets, judge band lines) - exactly the kind of text where term-frequency
similarity captures most of the real categorical structure.

The vectorizer is saved alongside taxonomy.yaml (as a separate pickle) and
regenerated together on every re-cluster, since a centroid is only
meaningful in the feature space that produced it.
"""

from __future__ import annotations

import pickle
import random
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import yaml
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from harness.judge import judge_client

TAXONOMY_VERSION = 1

# Below this cosine similarity to every existing centroid, a failure is
# genuinely novel rather than a poor fit for an existing category - left
# unassigned rather than forced into the nearest-but-wrong bucket. Not
# measured against a large held-out set yet; a reasonable opening value
# for TF-IDF cosine similarity, tightened once real re-cluster history
# exists.
NOVELTY_THRESHOLD = 0.15

NAMING_PROMPT = """You are naming a cluster of failure-evidence snippets from an automated \
search system. Each snippet below is real evidence explaining why one candidate failed \
or lost points on one task. They were grouped together because they are textually similar.

Read all the samples, then respond with exactly two lines, nothing else:
NAME: <a short, specific name for this failure category, 3-6 words>
DESCRIPTION: <one sentence describing what actually goes wrong in this category>

Samples:
{samples}
"""


@dataclass
class EvidenceItem:
    text: str
    check_name: str
    generation: int | None


@dataclass
class FailureCategory:
    id: str
    name: str
    description: str
    centroid: list[float]
    count: int
    first_seen_gen: int | None
    last_seen_gen: int | None
    still_active: bool = True


def extract_evidence(details: list[dict[str, Any]], generations: list[int | None]) -> list[EvidenceItem]:
    """Pulls one EvidenceItem per failed check (score < 1.0) or gate
    failure out of a list of harness.fitness.Fitness.detail dicts - the
    same generic shape harness/scorer.py's evaluate() always produces,
    across every solution, not just capability_case."""
    items: list[EvidenceItem] = []
    for detail, gen in zip(details, generations):
        if "gate" in detail:
            text = detail.get("error") or str(detail.get("got", ""))
            if text:
                items.append(EvidenceItem(text=text, check_name=f"gate:{detail['gate']}", generation=gen))
            continue
        for check_name, (score, evidence) in detail.get("checks", {}).items():
            if score < 1.0 and evidence:
                items.append(EvidenceItem(text=evidence, check_name=check_name, generation=gen))
    return items


def cluster(texts: list[str], n_clusters: int, random_state: int = 0) -> tuple[TfidfVectorizer, KMeans, np.ndarray]:
    """Stage 1 - cluster. Tens of categories, not hundreds, per PHASE-4.md."""
    vectorizer = TfidfVectorizer(max_features=2000, stop_words="english", min_df=1)
    X = vectorizer.fit_transform(texts)
    km = KMeans(n_clusters=n_clusters, n_init=10, random_state=random_state)
    labels = km.fit_predict(X)
    return vectorizer, km, labels


def _sample_per_cluster(texts: list[str], labels: np.ndarray, n_clusters: int, k: int, rng: random.Random) -> dict[int, list[str]]:
    samples: dict[int, list[str]] = {}
    for c in range(n_clusters):
        members = [t for t, lab in zip(texts, labels) if lab == c]
        samples[c] = rng.sample(members, min(k, len(members)))
    return samples


def _parse_naming_response(text: str) -> tuple[str, str]:
    name, description = "unnamed", "no description produced"
    for line in text.splitlines():
        line = line.strip()
        if line.upper().startswith("NAME:"):
            name = line.split(":", 1)[1].strip()
        elif line.upper().startswith("DESCRIPTION:"):
            description = line.split(":", 1)[1].strip()
    return name, description


def name_cluster(samples: list[str]) -> tuple[str, str]:
    """Stage 2 - name. A handful of judge calls, once, not per-failure."""
    prompt = NAMING_PROMPT.format(samples="\n".join(f"- {s[:300]}" for s in samples))
    r = judge_client().chat.completions.create(
        model="judge",
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )
    text = r.choices[0].message.content or ""
    if "</think>" in text:
        text = text.split("</think>", 1)[-1]
    return _parse_naming_response(text)


def build_taxonomy(
    evidence: list[EvidenceItem],
    n_clusters: int,
    samples_per_cluster: int = 5,
    seed: int = 0,
    _name_fn=name_cluster,
) -> tuple[list[FailureCategory], TfidfVectorizer]:
    """_name_fn is a seam for tests to skip the real judge call - defaults
    to the real name_cluster for every actual caller."""
    texts = [e.text for e in evidence]
    vectorizer, km, labels = cluster(texts, n_clusters, random_state=seed)
    rng = random.Random(seed)
    samples = _sample_per_cluster(texts, labels, n_clusters, samples_per_cluster, rng)

    categories = []
    for c in range(n_clusters):
        member_gens = [e.generation for e, lab in zip(evidence, labels) if lab == c and e.generation is not None]
        name, description = _name_fn(samples[c])
        categories.append(
            FailureCategory(
                id=f"F{c:02d}",
                name=name,
                description=description,
                centroid=km.cluster_centers_[c].tolist(),
                count=int((labels == c).sum()),
                first_seen_gen=min(member_gens) if member_gens else None,
                last_seen_gen=max(member_gens) if member_gens else None,
                still_active=True,
            )
        )
    return categories, vectorizer


def assign(text: str, vectorizer: TfidfVectorizer, categories: list[FailureCategory]) -> tuple[str | None, float]:
    """Nearest-centroid classification - no model call. Returns (category
    id, similarity), or (None, best similarity) if the failure falls
    outside every centroid by NOVELTY_THRESHOLD: genuinely novel, not a
    bad fit for an existing category."""
    if not categories:
        return None, 0.0
    vec = vectorizer.transform([text])
    centroids = np.array([c.centroid for c in categories])
    sims = cosine_similarity(vec, centroids)[0]
    best = int(np.argmax(sims))
    if sims[best] < NOVELTY_THRESHOLD:
        return None, float(sims[best])
    return categories[best].id, float(sims[best])


def save_taxonomy(categories: list[FailureCategory], vectorizer: TfidfVectorizer, yaml_path: Path, vectorizer_path: Path) -> None:
    doc = {"version": TAXONOMY_VERSION, "failures": [asdict(c) for c in categories]}
    yaml_path.write_text(yaml.safe_dump(doc, sort_keys=False))
    vectorizer_path.write_bytes(pickle.dumps(vectorizer))


def load_taxonomy(yaml_path: Path, vectorizer_path: Path) -> tuple[list[FailureCategory], TfidfVectorizer]:
    doc = yaml.safe_load(yaml_path.read_text())
    categories = [FailureCategory(**c) for c in doc["failures"]]
    vectorizer = pickle.loads(vectorizer_path.read_bytes())
    return categories, vectorizer
