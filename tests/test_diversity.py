"""PHASE-5.md task 5.5: the diversity metric and the reseed rule."""

from sklearn.feature_extraction.text import TfidfVectorizer

from harness import diversity


def test_identical_proposals_have_zero_diversity():
    X = TfidfVectorizer().fit_transform(["reject when absent"] * 3 + ["something else entirely"])
    assert diversity.mean_pairwise_distance(X[:3]) == 0.0
    assert diversity.mean_pairwise_distance(X) > 0.0


def test_one_proposal_has_no_diversity_figure():
    X = TfidfVectorizer().fit_transform(["alpha beta gamma", "delta epsilon zeta"])
    assert diversity.mean_pairwise_distance(X[:1]) is None


def test_reseed_fires_on_round_count():
    due, why = diversity.reseed_due(4, [1.0])
    assert due and "4 rounds" in why


def test_reseed_fires_on_diversity_drop_beyond_fifteen_percent():
    assert diversity.reseed_due(1, [0.80, 0.82])[0]
    assert not diversity.reseed_due(1, [0.90, 0.88])[0]


def test_reseed_quiet_within_limits():
    assert diversity.reseed_due(0, []) == (False, "within limits")
