"""Adversarial suite for capability_case. See PHASE-1.md task 1.6.

Unlike the fixture and itot_classifier, every invoke() call here is a real
model call — not free, not instant, and not perfectly deterministic even
at temperature 0 (thinking-model output length varies run to run). Most of
what's adversarial-tested here is the adapter's parsing and scoring logic
directly, in isolation (fast, free, exercises the same code paths
evaluate() would hit via hand-built Run/Task objects), with a small number
of real end-to-end calls reserved for properties that can only be
confirmed by actually calling the judge-role model.
"""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from harness.scorer import evaluate
from harness.types import Run, Task
from solutions.capability_case.adapter import CapabilityCaseAdapter, _parse_verdict

SOL_DIR = Path(__file__).resolve().parent.parent / "solutions" / "capability_case"


def _load_split(name: str) -> list[Task]:
    tasks = []
    for f in sorted((SOL_DIR / "data" / name).glob("*.json")):
        d = json.loads(f.read_text())
        tasks.append(Task(task_id=d["task_id"], input=d["input"], expected=d["expected"]))
    return tasks


def _incumbent_block() -> str:
    text = (SOL_DIR / "candidate" / "candidate.txt").read_text()
    return text.split("EVOLVE-BLOCK-START")[1].split("EVOLVE-BLOCK-END")[0].strip("\n")


@pytest.fixture(scope="module")
def adapter() -> CapabilityCaseAdapter:
    return CapabilityCaseAdapter()


@pytest.fixture(scope="module")
def rotation() -> list[Task]:
    return _load_split("rotation")


def _floor_failing_task(rotation: list[Task]) -> Task:
    return next(t for t in rotation if t.expected["must_reject"])


def _floor_passing_task(rotation: list[Task]) -> Task:
    return next(t for t in rotation if not t.expected["must_reject"])


# --- unit-level: parsing and scoring logic, no model call ---


def test_missing_verdict_key_fails_shape_ok(adapter):
    assert adapter.shape_ok('{"reasoning": "looks fine"}') is False


def test_invalid_verdict_value_fails_shape_ok(adapter):
    assert adapter.shape_ok('{"verdict": "probably", "reasoning": "unsure"}') is False


def test_non_json_output_fails_shape_ok(adapter):
    assert adapter.shape_ok("Sure, I'll approve this one.") is False
    assert adapter.shape_ok(None) is False


def test_think_block_is_stripped_before_parsing():
    output = (
        '<think>\nLet me weigh the evidence... seems solid overall.\n</think>\n'
        '{"verdict": "sound", "reasoning": "all four dimensions are thorough"}'
    )
    parsed = _parse_verdict(output)
    assert parsed == {"verdict": "sound", "reasoning": "all four dimensions are thorough"}


def test_json_object_embedded_in_prose_is_found():
    output = 'My assessment: {"verdict": "needs_more_evidence", "reasoning": "thin audit"} — hope that helps.'
    parsed = _parse_verdict(output)
    assert parsed["verdict"] == "needs_more_evidence"


def test_floor_failing_task_requires_reject(adapter, rotation):
    task = _floor_failing_task(rotation)
    wrong = adapter.programmatic_checks('{"verdict": "sound", "reasoning": "fine"}', task)
    assert wrong["floor_correct"][0] == 0.0
    right = adapter.programmatic_checks('{"verdict": "reject", "reasoning": "fine"}', task)
    assert right["floor_correct"][0] == 1.0


def test_floor_passing_task_rejects_reject_as_wrong(adapter, rotation):
    task = _floor_passing_task(rotation)
    wrong = adapter.programmatic_checks('{"verdict": "reject", "reasoning": "fine"}', task)
    assert wrong["floor_correct"][0] == 0.0
    for v in ("sound", "needs_more_evidence"):
        right = adapter.programmatic_checks(json.dumps({"verdict": v, "reasoning": "fine"}), task)
        assert right["floor_correct"][0] == 1.0


def test_needs_judgement_only_for_floor_passing(adapter, rotation):
    assert adapter.needs_judgement(_floor_failing_task(rotation)) is False
    assert adapter.needs_judgement(_floor_passing_task(rotation)) is True


def test_raises_immediately_is_invalid_with_error_captured(adapter, rotation, monkeypatch):
    # simulate a model-call failure without spending a real call
    def boom(*a, **k):
        raise RuntimeError("connection reset")

    fake_client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=boom)))
    monkeypatch.setattr("solutions.capability_case.adapter.judge_client", lambda: fake_client)
    cand_dir = adapter.materialise(_incumbent_block())
    task = _floor_passing_task(rotation)
    run = adapter.invoke(cand_dir, task.input, timeout=10.0)
    assert run.output is None
    assert "connection reset" in run.raw["stderr"]
    assert run.tokens == 0


# --- real end-to-end: needs the judge-role model actually running ---


def test_real_invoke_produces_gradable_output(adapter, rotation):
    task = _floor_passing_task(rotation)
    cand_dir = adapter.materialise(_incumbent_block())
    run = adapter.invoke(cand_dir, task.input, timeout=60.0)
    assert run.output is not None
    assert adapter.shape_ok(run.output)
    assert run.tokens > 0


def test_timeout_is_handled(adapter, rotation):
    task = _floor_passing_task(rotation)
    cand_dir = adapter.materialise(_incumbent_block())
    run = adapter.invoke(cand_dir, task.input, timeout=0.001)
    assert run.output is None
    assert run.raw.get("stderr")


def test_incumbent_end_to_end_quality_is_real(adapter, rotation):
    cand_dir = adapter.materialise(_incumbent_block())
    floor_fail = evaluate(adapter, cand_dir, _floor_failing_task(rotation), rubric=adapter.rubric)
    assert floor_fail.valid
    assert floor_fail.detail["judge_calls"] == 0  # mechanically decided, no judge call spent

    floor_pass = evaluate(adapter, cand_dir, _floor_passing_task(rotation), rubric=adapter.rubric)
    assert floor_pass.valid
    assert floor_pass.detail["judge_calls"] == 1
    assert 0.0 <= floor_pass.quality <= 1.0


def test_output_contract_follows_the_evolved_instructions(adapter, rotation, monkeypatch):
    # Evolved instructions that prescribe their own format were followed over
    # the user turn's contract on ~10% of calls (decision 66); the harness's
    # contract must be the last thing in the system message.
    import solutions.capability_case.adapter as mod
    sent = {}

    def create(**kw):
        sent.update(kw)
        msg = SimpleNamespace(content='{"verdict": "reject", "reasoning": "x"}')
        return SimpleNamespace(choices=[SimpleNamespace(message=msg)], usage=None)

    fake_client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    monkeypatch.setattr(mod, "judge_client", lambda: fake_client)
    cand = adapter.materialise("First line: rejected or sound. Second line: reason.")
    adapter.invoke(cand, rotation[0].input, timeout=5)
    system = sent["messages"][0]["content"]
    assert system.startswith("First line: rejected or sound.")
    assert system.endswith(mod.OUTPUT_CONTRACT)
    assert mod.OUTPUT_CONTRACT in sent["messages"][1]["content"]
