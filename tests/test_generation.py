"""Regression test for the root_sha collapse bug found 2026-09-24 (see
harness/generation.py's _root_sha_for docstring): every generation-0
candidate was silently given the same root_sha (the shared seed's own
hash), making unique_ancestors read exactly 1 forever regardless of real
search diversity. Never caught before because no test exercised more than
one generation."""

from __future__ import annotations

from harness.generation import _root_sha_for


def test_generation_zero_candidates_get_distinct_roots():
    # Two distinct candidates proposed from the same seed-drawn parent
    # (root_sha None — nothing claimed in this island yet) must become
    # separate founding lineages, not clones of the shared seed.
    parent = {"block": "seed text", "iteration_id": None, "root_sha": None}
    root_a = _root_sha_for(parent, "candidate A text")
    root_b = _root_sha_for(parent, "candidate B text")
    assert root_a != root_b


def test_elite_parent_propagates_its_root_unchanged():
    parent = {"block": "elite text", "iteration_id": 5, "root_sha": "abc123"}
    assert _root_sha_for(parent, "child text") == "abc123"
