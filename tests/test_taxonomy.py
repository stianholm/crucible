"""See PHASE-4.md task 4.1's verify: at least 80% of failures assigned to
an existing category, and the unassigned tail is genuinely novel.

Real end-to-end verification against capability_case's actual failure
data (338 real evidence items, an honest train/holdout split across
generations, not a self-fulfilling check against the same data the
clusters were fit on) lives in TODO.md's decision log, not here - 99.3%
holdout assignment. These are the fast, offline unit tests: the parts of
the pipeline that don't need a live judge call, plus name_cluster with a
mocked one, matching tests/test_capability_case.py's existing pattern.
"""

from __future__ import annotations

from pathlib import Path

from harness.taxonomy import (
    EvidenceItem,
    assign,
    build_taxonomy,
    cluster,
    extract_evidence,
    load_taxonomy,
    name_cluster,
    save_taxonomy,
)


def test_extract_evidence_pulls_failed_checks_and_gates():
    details = [
        {"checks": {"floor_correct": [0.0, "floor requires reject"], "judge": [1.0, "BAND: 3"]}},
        {"gate": "shape", "got": "None"},
        {"checks": {"judge": [1.0, "BAND: 3"]}},  # nothing failed here
    ]
    items = extract_evidence(details, generations=[0, 1, 2])
    assert len(items) == 2
    assert items[0] == EvidenceItem(text="floor requires reject", check_name="floor_correct", generation=0)
    assert items[1] == EvidenceItem(text="None", check_name="gate:shape", generation=1)


def test_cluster_separates_two_obviously_distinct_groups():
    texts = ["off by one on empty input " * 3] * 10 + ["timeout waiting for response " * 3] * 10
    _vectorizer, _km, labels = cluster(texts, n_clusters=2, random_state=0)
    # the two textually distinct halves should not all land in one cluster
    assert len(set(labels[:10])) == 1
    assert len(set(labels[10:])) == 1
    assert labels[0] != labels[10]


def test_assign_finds_nearest_and_flags_novelty():
    evidence = [
        EvidenceItem(text="off by one on empty input", check_name="c", generation=0),
        EvidenceItem(text="off by one when list is empty", check_name="c", generation=1),
        EvidenceItem(text="timeout waiting for the response", check_name="c", generation=0),
        EvidenceItem(text="request timed out after 30 seconds", check_name="c", generation=1),
    ]
    categories, vectorizer = build_taxonomy(evidence, n_clusters=2, samples_per_cluster=2, seed=0, _name_fn=lambda samples: ("test", "test"))

    cat_id, sim = assign("off by one on an empty list", vectorizer, categories)
    assert cat_id is not None
    assert sim > 0

    novel_id, novel_sim = assign("completely unrelated gibberish about weather patterns", vectorizer, categories)
    assert novel_id is None


def test_save_and_load_taxonomy_roundtrip(tmp_path: Path):
    evidence = [
        EvidenceItem(text="off by one on empty input", check_name="c", generation=0),
        EvidenceItem(text="timeout waiting for response", check_name="c", generation=1),
    ]
    categories, vectorizer = build_taxonomy(evidence, n_clusters=2, samples_per_cluster=2, seed=0, _name_fn=lambda samples: ("test", "test"))

    yaml_path, pkl_path = tmp_path / "taxonomy.yaml", tmp_path / "taxonomy_vectorizer.pkl"
    save_taxonomy(categories, vectorizer, yaml_path, pkl_path)
    loaded_categories, loaded_vectorizer = load_taxonomy(yaml_path, pkl_path)

    assert len(loaded_categories) == len(categories)
    assert loaded_categories[0].id == categories[0].id
    assert loaded_categories[0].centroid == categories[0].centroid
    # the loaded vectorizer must classify the same text into the same category
    assert assign("off by one", loaded_vectorizer, loaded_categories)[0] == assign(
        "off by one", vectorizer, categories
    )[0]


def test_name_cluster_parses_a_well_formed_response(monkeypatch):
    class FakeMessage:
        content = "NAME: Off-by-one errors\nDESCRIPTION: Candidate mishandles empty or boundary input."

    class FakeChoice:
        message = FakeMessage()

    class FakeResponse:
        choices = [FakeChoice()]

    class FakeCompletions:
        def create(self, **kwargs):
            return FakeResponse()

    class FakeChat:
        completions = FakeCompletions()

    class FakeClient:
        chat = FakeChat()

    monkeypatch.setattr("harness.taxonomy.judge_client", lambda: FakeClient())
    name, description = name_cluster(["off by one on empty input", "index error on boundary"])
    assert name == "Off-by-one errors"
    assert "boundary" in description
