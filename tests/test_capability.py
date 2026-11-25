"""PHASE-5.md task 5.5: the fixed general-capability suite."""

import collections
import json

from harness import capability


def test_generation_is_deterministic_and_balanced():
    items = capability.generate()
    assert items == capability.generate()
    assert len(items) == 50
    assert set(collections.Counter(i["family"] for i in items).values()) == {10}


def test_frozen_suite_matches_the_generator():
    """The committed file is what every round runs. If the generator changes,
    the file must be re-frozen deliberately, and the change is a new suite."""
    assert json.loads(capability.SUITE.read_text()) == capability.generate()


def test_grading_takes_the_last_answer_line_only():
    item = {"answer": "Ed, Fay, Cy"}
    assert capability.grade(item, "thinking...\nANSWER: ed,  fay, cy.")
    assert not capability.grade(item, "ANSWER: Ed, Fay, Cy\nANSWER: Cy")
    assert not capability.grade(item, "Ed, Fay, Cy")
    assert not capability.grade(item, None)


def test_ordering_items_have_exactly_one_solution():
    import itertools

    for item in (i for i in capability.generate() if i["family"] == "ordering"):
        assert len(item["answer"].split(", ")) == 6
        assert sorted(item["answer"].split(", ")) == sorted(capability.NAMES)


def test_summary_reports_mean_and_spread():
    s = capability.summary([{"a": True, "b": False}, {"a": True, "b": True}])
    assert s["accuracy"] == 0.75 and s["passes"] == 2 and s["sd"] > 0


def _passes(accs, n=50):
    return [{f"i{j}": j < round(a * n) for j in range(n)} for a in accs]


def test_gate_passes_noise_and_rejects_a_real_regression():
    ref = capability.summary(_passes([0.94, 0.84, 0.90, 0.88, 0.92] * 4)) | {"model": "proposer"}
    same = capability.compare(ref, _passes([0.90, 0.86, 0.92, 0.88, 0.90]))
    assert same["passes"]
    worse = capability.compare(ref, _passes([0.78, 0.80, 0.76, 0.82, 0.78]))
    assert not worse["passes"] and worse["regression"] > 0.08


def test_gate_retests_only_in_the_grey_zone():
    ref = capability.summary(_passes([0.94, 0.84, 0.90, 0.88, 0.92] * 4)) | {"model": "proposer"}
    calls = []

    def runner(accs):
        def r(model, passes):
            calls.append(passes)
            return _passes(accs[:passes])
        return r

    clean = capability.gate(ref, runner=runner([0.92, 0.86, 0.90, 0.88, 0.92]))
    assert clean["passes"] and "retested" not in clean and calls == [5]
    calls.clear()
    noisy = [0.92, 0.78, 0.88, 0.84, 0.88]  # mean 0.86: about 3.6% down, not significant on 5 passes
    grey = capability.gate(ref, runner=runner(noisy + noisy))
    assert grey.get("retested") and calls == [5, 5]
