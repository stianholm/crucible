"""PHASE-5.md task 5.5: a fixed general-capability suite, run before and after
every adapter to catch forgetting.

    python -m harness.capability freeze              # (re)generate bench/capability_suite.json
    python -m harness.capability run proposer 3      # 3 passes, prints accuracy per pass
    python -m harness.capability reference 20        # one-time stock reference
    python -m harness.capability gate 5              # adapter vs reference; exit 4 = rejected

Fifty items, entirely unrelated to any onboarded solution, in five families
of ten, every answer computed exactly by the generator so grading needs no
judge: multi-step integer arithmetic, calendar arithmetic, Python code
tracing, ordering puzzles (unique solution checked by brute force) and string
manipulation. Generated from a fixed seed and frozen to a committed file, so
the suite is identical across rounds and needs no dataset download.

The model answers on a final line "ANSWER: <value>"; anything else is wrong.
Answers are compared after whitespace and case normalisation only.
"""

from __future__ import annotations

import datetime as dt
import itertools
import json
import os
import random
import re
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SUITE = Path(__file__).resolve().parent.parent / "bench" / "capability_suite.json"
SEED = 20261017  # v2 difficulty, calibrated 2026-10-17 (see PHASE-5.md task 5.5)
INSTRUCTION = ("Solve the problem. Think it through, then give the final answer alone on the last line, "
               "in the form ANSWER: <value>")


def _arithmetic(r: random.Random) -> tuple[str, str]:
    a, b, c = (r.randint(10_000, 99_999) for _ in range(3))
    d, e, m = r.randint(101, 999), r.randint(1_000, 9_999), r.randint(1_000, 9_999)
    value = ((a * b - c * d) // e) % m + (a % d) * (c % 97)
    expr = f"(({a} * {b} - {c} * {d}) div {e}) mod {m} + ({a} mod {d}) * ({c} mod 97)"
    return (f"Compute {expr}, where div is floor division and mod the non-negative remainder.",
            str(value))


def _calendar(r: random.Random) -> tuple[str, str]:
    start = dt.date(r.randint(1800, 2150), r.randint(1, 12), r.randint(1, 28))
    days = r.randint(20_000, 99_000)
    sign = r.choice([1, -1])
    end = start + dt.timedelta(days=sign * days)
    direction = "after" if sign > 0 else "before"
    return (f"In the Gregorian calendar, what date is {days} days {direction} {start:%d %B %Y}? "
            "Answer as YYYY-MM-DD.", end.isoformat())


def _code(r: random.Random) -> tuple[str, str]:
    n, m, k, s0 = r.randint(18, 40), r.randint(3, 7), r.randint(2, 9), r.randint(1, 9)
    src = (f"xs = [{s0}]\n"
           f"for i in range(1, {n}):\n"
           f"    v = (xs[-1] * {k} + i) % {m * 7 + 3}\n"
           f"    if v % {m} == 0:\n"
           f"        xs.append(v)\n"
           f"    elif len(xs) > 2 and v > xs[-2]:\n"
           f"        xs[-2] = v - xs[-2]\n"
           f"    else:\n"
           f"        xs.append(xs[-1] + v % 5)\n"
           f"print(sum(xs) - len(xs) * xs[0])\n")
    out: list = []
    exec(src.replace("print(", "out.append("), {"out": out})
    return f"What does this Python program print?\n\n```python\n{src}```", str(out[0])


NAMES = ["Ada", "Bo", "Cy", "Di", "Ed", "Fay"]


def _ordering(r: random.Random) -> tuple[str, str]:
    """Six people in a queue, clues until exactly one order satisfies them."""
    people = NAMES[:]
    truth = people[:]
    r.shuffle(truth)
    pos = {p: i for i, p in enumerate(truth)}
    last = len(people) - 1
    kinds = [
        lambda a, b: (f"{a} is somewhere ahead of {b}.", lambda o: o.index(a) < o.index(b)) if pos[a] < pos[b] else None,
        lambda a, b: (f"{a} is directly behind {b}.", lambda o: o.index(a) == o.index(b) + 1) if pos[a] == pos[b] + 1 else None,
        lambda a, b: (f"{a} is not next to {b}.", lambda o: abs(o.index(a) - o.index(b)) != 1) if abs(pos[a] - pos[b]) != 1 else None,
        lambda a, b: (f"Exactly {abs(pos[a] - pos[b]) - 1} people stand between {a} and {b}.",
                      lambda o, g=abs(pos[a] - pos[b]): abs(o.index(a) - o.index(b)) == g) if abs(pos[a] - pos[b]) > 1 else None,
        lambda a, _b: (f"{a} is not first or last.", lambda o: 0 < o.index(a) < last) if 0 < pos[a] < last else None,
    ]
    clues: list = []
    candidates = list(itertools.permutations(people))
    while len(candidates) > 1:
        a, b = r.sample(people, 2)
        made = r.choice(kinds)(a, b)
        if made is None or made[0] in [c[0] for c in clues]:
            continue
        kept = [o for o in candidates if made[1](list(o))]
        if len(kept) < len(candidates):
            clues.append(made)
            candidates = kept
    text = " ".join(c[0] for c in clues)
    return (f"Six people, {', '.join(sorted(people))}, stand in a queue. {text} "
            "Give the queue from first to last as names separated by commas.", ", ".join(candidates[0]))


WORDS = ("lantern orchid granite meadow cobalt harbor willow ember quartz falcon "
         "thistle canyon velvet saffron glacier marble cinder juniper raven topaz").split()


def _strings(r: random.Random) -> tuple[str, str]:
    ws = r.sample(WORDS, 10)
    kind = r.randrange(3)
    if kind == 0:
        k = r.randint(3, 7)
        q = (f"Take the words {', '.join(ws)}. Sort them by their second-to-last letter, breaking ties by "
             f"word length and then alphabetically. Give the word in position {k} (counting from 1).")
        a = sorted(ws, key=lambda w: (w[-2], len(w), w))[k - 1]
    elif kind == 1:
        q = (f"For the words {', '.join(ws)}, count the vowels (a, e, i, o, u) in each word, then add up "
             f"the counts of only those words whose count is odd. What is the total?")
        a = str(sum(c for w in ws if (c := sum(ch in "aeiou" for ch in w)) % 2))
    else:
        q = (f"Reverse each of the words {', '.join(ws)}, sort the reversed words alphabetically, and "
             f"concatenate the first letters of the first five. What string do you get?")
        a = "".join(w[0] for w in sorted(x[::-1] for x in ws)[:5])
    return q, a


FAMILIES = {"arithmetic": _arithmetic, "calendar": _calendar, "code": _code,
            "ordering": _ordering, "strings": _strings}


def generate(seed: int = SEED, per_family: int = 10) -> list[dict]:
    r = random.Random(seed)
    items = []
    for family, make in FAMILIES.items():
        for i in range(per_family):
            q, a = make(r)
            items.append({"id": f"{family}-{i:02d}", "family": family, "question": q, "answer": a})
    return items


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().strip(".").lower())


def grade(item: dict, reply: str | None) -> bool:
    m = re.findall(r"ANSWER:\s*(.+)", reply or "")
    return bool(m) and _norm(m[-1]) == _norm(item["answer"])


def run(model: str, passes: int = 1, threads: int = 32, items: list[dict] | None = None) -> list[dict[str, bool]]:
    """Per pass, {item id: correct}. Each pass sends all items concurrently,
    as real load does (decision 71: concurrency is where the noise is)."""
    from openai import OpenAI

    items = items or json.loads(SUITE.read_text())
    client = OpenAI(base_url=os.environ.get("LITELLM_BASE_URL", "http://localhost:4000"),
                    api_key=os.environ.get("LITELLM_API_KEY", "unused"), timeout=1200, max_retries=0)

    def ask(item):
        r = client.chat.completions.create(model=model, temperature=0.0, messages=[
            {"role": "user", "content": f"{INSTRUCTION}\n\n{item['question']}"}])
        return item["id"], grade(item, r.choices[0].message.content)

    results = []
    for _ in range(passes):
        with ThreadPoolExecutor(threads) as ex:
            results.append(dict(ex.map(ask, items)))
    return results


def summary(results: list[dict[str, bool]]) -> dict:
    accs = [sum(r.values()) / len(r) for r in results]
    return {"passes": len(accs), "accuracy": statistics.mean(accs),
            "sd": statistics.stdev(accs) if len(accs) > 1 else None, "per_pass": accs}


REFERENCE = SUITE.with_name("capability_reference.json")
# Gate (task 5.6, amended 2026-10-17, TODO.md decision 76): reject when the
# adapter's accuracy is below the stock reference by more than this many
# standard errors of the difference. The spec's "regression under 3%" is not
# resolvable here: one pass already varies by sd 0.050 on the same model.
GATE_SIGMA = 2.0
# Grey zone (decision 76): an adapter that passes but shows an apparent
# regression of at least this much is re-measured with as many passes again
# before the verdict stands, buying 3%-level sensitivity only where needed.
GREY_ZONE = 0.03


def gate(reference: dict, model: str = "proposer-distilled", passes: int = 5,
         runner=None) -> dict:
    """compare() after `passes` passes; if that passes but sits in the grey
    zone, run `passes` more and decide on all of them."""
    runner = runner or run
    results = runner(model, passes)
    out = compare(reference, results)
    if out["passes"] and out["regression"] >= GREY_ZONE:
        results = results + runner(model, passes)
        out = compare(reference, results) | {"retested": True}
    return out


def save_reference(results: list[dict[str, bool]], model: str = "proposer") -> dict:
    """The stock model's accuracy, measured once with many passes and reused
    for every adapter: the stock weights never change, and a restart adds no
    noise beyond concurrency's (decision 71)."""
    ref = summary(results) | {"model": model, "suite_items": len(results[0]),
                              "per_item_correct": {k: sum(r[k] for r in results) for k in results[0]}}
    REFERENCE.write_text(json.dumps(ref, indent=1) + "\n")
    return ref


def compare(reference: dict, results: list[dict[str, bool]]) -> dict:
    """Adapter accuracy against the stored reference. The pass-to-pass spread
    is pooled from both, since a single model's passes are the noise."""
    import math

    adapter = summary(results)
    var_r = reference["sd"] ** 2
    var_a = adapter["sd"] ** 2 if adapter["sd"] is not None else var_r
    se = math.sqrt(var_r / reference["passes"] + var_a / adapter["passes"])
    regression = reference["accuracy"] - adapter["accuracy"]
    sigma = regression / se if se else float("inf")
    return {"reference": reference["accuracy"], "adapter": adapter["accuracy"],
            "regression": regression, "se": se, "sigma": sigma,
            "detectable_at_gate": GATE_SIGMA * se, "passes": sigma <= GATE_SIGMA,
            "adapter_per_pass": adapter["per_pass"]}


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "freeze":
        SUITE.write_text(json.dumps(generate(), indent=1) + "\n")
        print(f"wrote {SUITE}")
    elif cmd == "run":
        res = run(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
        print(json.dumps(summary(res), indent=1))
    elif cmd == "reference":  # python -m harness.capability reference 20
        print(json.dumps(save_reference(run("proposer", int(sys.argv[2]))), indent=1))
    elif cmd == "gate":  # python -m harness.capability gate 5   (adapter loaded as "distilled")
        out = gate(json.loads(REFERENCE.read_text()), passes=int(sys.argv[2]))
        print(json.dumps(out, indent=1))
        sys.exit(0 if out["passes"] else 4)
