"""The restore check's comparison (docs/backup.md): a restore is verified by
the manifest, not hoped at."""

from harness.backup import compare

MANIFEST = {"rows": {"iteration": 10, "elite": 2, "event": 5, "lesson": 1},
            "dump": {"sha256": "abc"}, "candidates": {"objects": 3},
            "files": {"data/s/held_out.jsonl": "h1", "adapters/a/w.bin": "h2"}}
FILES = {"data/s/held_out.jsonl": "h1", "adapters/a/w.bin": "h2"}


def test_a_matching_restore_has_no_problems():
    assert compare(MANIFEST, dict(MANIFEST["rows"]), "abc", 3, dict(FILES)) == []


def test_every_kind_of_difference_is_named():
    rows = dict(MANIFEST["rows"], event=4)
    bad = compare(MANIFEST, rows, "xyz", 2, {"data/s/held_out.jsonl": "other"})
    assert "event: manifest 5, restored 4" in bad
    assert "dump sha256 differs from the manifest" in bad
    assert "candidates: manifest 3, found 2" in bad
    assert "data/s/held_out.jsonl: missing or changed" in bad
    assert "adapters/a/w.bin: missing or changed" in bad
