"""PHASE-5.md task 5.4's paired A/B: how a generation splits into arms."""

import asyncio
import io
import json
import random

import pytest

from harness import generation, proposal


def _parents(n):
    return [(i % 4, {"block": f"parent {i}"}, [f"insp {i}"], [f"lesson {i}"]) for i in range(n)]


def test_one_model_is_the_ordinary_generation():
    slots = generation._expand_arms(_parents(5), ("proposer",), random.Random(0))
    assert [s[4] for s in slots] == ["proposer"] * 5
    assert [s[5] for s in slots] == [0, 1, 2, 3, 4]


def test_two_models_pair_every_parent_with_identical_context():
    parents = _parents(16)
    slots = generation._expand_arms(parents, ("proposer", "proposer-distilled"), random.Random(0))
    assert len(slots) == 32
    by_pair = {}
    for island, p, insp, retrieved, model, pair in slots:
        by_pair.setdefault(pair, []).append((island, p["block"], insp, retrieved, model))
    for pair, members in by_pair.items():
        assert sorted(m[4] for m in members) == ["proposer", "proposer-distilled"]
        assert members[0][:4] == members[1][:4], "both arms must see the same parent, inspirations and lessons"


def test_arm_order_within_pairs_is_shuffled_not_fixed():
    slots = generation._expand_arms(_parents(32), ("proposer", "proposer-distilled"), random.Random(0))
    firsts = [slots[i][4] for i in range(0, len(slots), 2)]
    assert 0 < firsts.count("proposer") < len(firsts)


def test_stock_label_needs_no_server():
    assert generation._model_label("proposer") == "proposer"


def _fake_models(monkeypatch, entries):
    import urllib.request

    monkeypatch.setattr(urllib.request, "urlopen",
                        lambda url, timeout=0: io.BytesIO(json.dumps({"data": entries}).encode()))


def test_distilled_label_names_the_adapter(monkeypatch):
    _fake_models(monkeypatch, [{"id": "proposer", "root": "openai/gpt-oss-120b"},
                               {"id": "distilled", "root": "/adapters/20261018"}])
    assert generation._model_label("proposer-distilled") == "proposer-distilled@/adapters/20261018"


def test_distilled_arm_refuses_to_start_without_an_adapter(monkeypatch):
    _fake_models(monkeypatch, [{"id": "proposer", "root": "openai/gpt-oss-120b"}])
    with pytest.raises(RuntimeError, match="no adapter is loaded"):
        generation._model_label("proposer-distilled")


def test_propose_async_sends_the_requested_model():
    sent = {}

    class Message:
        content = "<candidate>\nx\n</candidate>"

    class Response:
        choices = [type("C", (), {"message": Message()})()]
        usage = type("U", (), {"total_tokens": 1, "completion_tokens": 1})()

    class Client:
        class chat:
            class completions:
                @staticmethod
                async def create(**kw):
                    sent.update(kw)
                    return Response()

    asyncio.run(proposal.propose_async("t", "b", 0.5, 0, 0.0, "", client=Client, model="proposer-distilled"))
    assert sent["model"] == "proposer-distilled"


def test_async_client_is_rebuilt_for_each_event_loop():
    """One client per asyncio.run: a client cached across loops reuses pooled
    connections bound to a closed loop (decision 77)."""
    async def get():
        return proposal.async_judge_client()

    first = asyncio.run(get())

    async def same_loop_twice():
        return proposal.async_judge_client(), proposal.async_judge_client()

    a, b = asyncio.run(same_loop_twice())
    assert a is b, "within one loop the client is shared"
    assert a is not first, "a new loop gets a new client"


def test_closing_the_client_inside_its_loop_leaves_none_to_collect_later():
    """Decision 87: close the per-loop client before the loop ends."""
    async def use_then_close():
        c = proposal.async_judge_client()
        await proposal.close_async_client()
        return c

    c = asyncio.run(use_then_close())
    assert proposal._async_client is None and c.is_closed()
