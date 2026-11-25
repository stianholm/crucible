"""train/harvest.py's offline parts: claim parsing, dedup, balance, and the
review gate. The database and Langfuse joins are verified against real runs,
see PHASE-5.md task 5.1."""

import json

import pytest
import yaml

from train import harvest


def _report(tmp_path, name, claims, count=None):
    body = [f"- Cells newly claimed this generation: {len(claims) if count is None else count}", ""]
    for cand in claims:
        body += [f"### Island 0, cell (1, 2), scalar 0.5000", "", f"parent `{'a' * 16}` -> candidate `{cand}`", ""]
    (tmp_path / name).write_text("\n".join(body))


def test_claims_from_reports_reads_every_generation(tmp_path, monkeypatch):
    monkeypatch.setattr(harvest, "REPO_ROOT", tmp_path)
    _report(tmp_path, "GENERATION-000-x.md", ["1" * 16, "2" * 16])
    _report(tmp_path, "GENERATION-001-x.md", ["3" * 16])
    assert harvest.claims_from_reports("GENERATION-*-x.md") == ["1" * 16, "2" * 16, "3" * 16]


def test_claims_from_reports_refuses_a_count_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(harvest, "REPO_ROOT", tmp_path)
    _report(tmp_path, "GENERATION-000-x.md", ["1" * 16], count=2)
    with pytest.raises(SystemExit, match="count line says 2"):
        harvest.claims_from_reports("GENERATION-*-x.md")


def _ex(sha, text, scalar, category="F00", iid=0):
    return {"candidate_sha": sha, "candidate": text, "scalar": scalar, "category": category,
            "iteration_id": iid, "source": "s"}


def test_dedup_keeps_the_higher_scoring_near_copy():
    a = _ex("a", "reject when failure mode analysis is absent entirely", 0.6, iid=1)
    b = _ex("b", "reject when failure mode analysis is absent entirely", 0.8, iid=2)
    c = _ex("c", "accept every floor pass and list checklist items in order", 0.7, iid=3)
    kept, dropped = harvest.dedup([a, b, c])
    assert {e["candidate_sha"] for e in kept} == {"b", "c"}
    assert dropped[0][:2] == ("a", "b")


def test_balance_caps_each_category_by_scalar(monkeypatch):
    monkeypatch.setattr(harvest, "PER_CATEGORY_CAP", 2)
    es = [_ex(str(i), "x", s, "F00", i) for i, s in enumerate([0.1, 0.9, 0.5])] + [_ex("z", "y", 0.2, "F01", 9)]
    kept, cut = harvest.balance(es)
    assert {e["candidate_sha"] for e in kept} == {"1", "2", "z"}
    assert cut == {"F00": 1}


def _selection():
    e = _ex("a" * 16, "cand", 0.7)
    e |= {"messages": [{"role": "user", "content": "ctx"}], "response": {"content": "<candidate>", "reasoning": "r"},
          "weight": 1.5, "solution_id": "s", "run_id": "r", "generation": 0, "parent_sha": "p", "parent_scalar": 0.6,
          "delta": 0.1, "lessons_injected": [], "trace_id": "t"}
    return {"selection": "sel1", "examples": [e], "counts": {"claims": 1}, "categories": {"F00": 1},
            "category_cut": {}, "dedup_dropped": [], "params": {}, "sources": ["s"]}


def _review(tmp_path, monkeypatch, **fields):
    monkeypatch.setattr(harvest, "REPO_ROOT", tmp_path)
    p = tmp_path / "review.yaml"
    p.write_text(yaml.safe_dump({"selection": "sel1", "reviewer": "", "excluded": {}} | fields))
    return p


def test_emit_refuses_an_unsigned_review(tmp_path, monkeypatch):
    p = _review(tmp_path, monkeypatch)
    with pytest.raises(SystemExit, match="no reviewer"):
        harvest.emit(_selection(), p, tmp_path / "out.jsonl")


def test_emit_refuses_a_review_of_a_different_selection(tmp_path, monkeypatch):
    p = _review(tmp_path, monkeypatch, selection="other", reviewer="me")
    with pytest.raises(SystemExit, match="Run `review` again"):
        harvest.emit(_selection(), p, tmp_path / "out.jsonl")


def test_emit_applies_exclusions_and_writes_a_manifest(tmp_path, monkeypatch):
    sel = _selection()
    p = _review(tmp_path, monkeypatch, reviewer="me")
    out = tmp_path / "out.jsonl"
    m = harvest.emit(sel, p, out)
    row = json.loads(out.read_text())
    assert row["messages"][-1] == {"role": "assistant", "content": "<candidate>", "thinking": "r"}
    assert row["weight"] == 1.5 and m["examples"] == 1

    p = _review(tmp_path, monkeypatch, reviewer="me", excluded={"a" * 16: "games the judge"})
    m = harvest.emit(sel, p, out)
    assert out.read_text() == "" and m["counts"]["after human review"] == 0


def test_select_drops_claims_below_the_scalar_floor(monkeypatch):
    rows = [_ex("lo", "reject when absent", 0.30, iid=1), _ex("hi", "accept floor passes", 0.70, iid=2)]
    monkeypatch.setattr(harvest, "load_sources", lambda: [{"label": "s"}])
    monkeypatch.setattr(harvest, "collect", lambda conn, sources: (rows, __import__("collections").Counter(claims=2)))
    sel = harvest.select(conn=object())
    assert [e["candidate_sha"] for e in sel["examples"]] == ["hi"]
    assert sel["counts"]["after scalar floor"] == 1


def test_emit_accepts_a_review_path_relative_to_the_repo(tmp_path, monkeypatch):
    """ops/nightly.sh passes train/reviews/<sel>.yaml, relative. emit crashed on
    it on 2026-10-17, the first real night, while every test used absolute paths."""
    monkeypatch.setattr(harvest, "REPO_ROOT", tmp_path)
    monkeypatch.chdir(tmp_path)
    (tmp_path / "train" / "reviews").mkdir(parents=True)
    rel = harvest.Path("train/reviews/r.yaml")
    rel.write_text(yaml.safe_dump({"selection": "sel1", "reviewer": "me", "excluded": {}}))
    m = harvest.emit(_selection(), rel, tmp_path / "out.jsonl")
    assert m["review"] == "train/reviews/r.yaml" and m["examples"] == 1
