"""Builds the fixture's task set from reference.py and writes it split three
ways. See PHASE-1.md task 1.2. Re-run to regenerate deterministically —
argument lists here are the only thing that needs hand-checking, since
`expected` is always computed from the reference implementation, never
typed by hand.

Usage: python -m solutions.fixture.checks.generate_tasks
"""

from __future__ import annotations

import json
from pathlib import Path

from harness.split import split_of
from solutions.fixture.checks.reference import REFERENCE_OPS

SOL_DIR = Path(__file__).resolve().parent.parent

# (op, args) pairs. Each becomes one task. Four to five cases per op,
# chosen to cover a typical case, an edge case, and a boundary condition.
CASES: list[tuple[str, list]] = [
    # is_prime
    ("is_prime", [2]),
    ("is_prime", [1]),
    ("is_prime", [17]),
    ("is_prime", [18]),
    ("is_prime", [97]),
    # reverse_string
    ("reverse_string", ["hello"]),
    ("reverse_string", [""]),
    ("reverse_string", ["a"]),
    ("reverse_string", ["racecar"]),
    ("reverse_string", ["Crucible Harness"]),
    # fibonacci (0-indexed: fibonacci(0) == 0, fibonacci(1) == 1)
    ("fibonacci", [0]),
    ("fibonacci", [1]),
    ("fibonacci", [2]),
    ("fibonacci", [10]),
    ("fibonacci", [20]),
    # gcd
    ("gcd", [12, 18]),
    ("gcd", [17, 5]),
    ("gcd", [0, 7]),
    ("gcd", [100, 75]),
    # is_palindrome
    ("is_palindrome", ["racecar"]),
    ("is_palindrome", ["hello"]),
    ("is_palindrome", ["A man a plan a canal Panama"]),
    ("is_palindrome", [""]),
    ("is_palindrome", ["ab"]),
    # sum_digits
    ("sum_digits", [12345]),
    ("sum_digits", [0]),
    ("sum_digits", [-987]),
    ("sum_digits", [7]),
    # factorial
    ("factorial", [0]),
    ("factorial", [1]),
    ("factorial", [5]),
    ("factorial", [10]),
    # max_subarray_sum
    ("max_subarray_sum", [[1, -2, 3, 4, -1]]),
    ("max_subarray_sum", [[-5, -1, -3]]),
    ("max_subarray_sum", [[5]]),
    ("max_subarray_sum", [[1, 2, 3, 4, 5]]),
    # count_vowels
    ("count_vowels", ["hello world"]),
    ("count_vowels", ["xyz"]),
    ("count_vowels", ["AEIOU"]),
    ("count_vowels", [""]),
    # is_anagram
    ("is_anagram", ["listen", "silent"]),
    ("is_anagram", ["hello", "world"]),
    ("is_anagram", ["Dormitory", "Dirty Room"]),
    ("is_anagram", ["a", "a"]),
    # binary_search
    ("binary_search", [[1, 3, 5, 7, 9, 11], 7]),
    ("binary_search", [[1, 3, 5, 7, 9, 11], 4]),
    ("binary_search", [[], 1]),
    ("binary_search", [[5], 5]),
    # flatten_list
    ("flatten_list", [[1, [2, 3], [4, [5, 6]]]]),
    ("flatten_list", [[]]),
    ("flatten_list", [[1, 2, 3]]),
    ("flatten_list", [[[1, [2, [3, [4]]]]]]),
]


def build_tasks() -> list[dict]:
    tasks = []
    counters: dict[str, int] = {}
    for op, args in CASES:
        counters[op] = counters.get(op, 0) + 1
        task_id = f"{op}-{counters[op]:02d}"
        expected = REFERENCE_OPS[op](*args)
        tasks.append(
            {
                "task_id": task_id,
                "input": json.dumps({"op": op, "args": args}),
                "expected": expected,
            }
        )
    return tasks


def main() -> None:
    tasks = build_tasks()
    assert len(tasks) == len({t["task_id"] for t in tasks}), "duplicate task_id"

    buckets: dict[str, list[dict]] = {"dev": [], "rotation": [], "held_out": []}
    for t in tasks:
        buckets[split_of(t["task_id"])].append(t)

    for name, items in buckets.items():
        out_dir = SOL_DIR / "data" / name
        out_dir.mkdir(parents=True, exist_ok=True)
        for existing in out_dir.glob("*.json"):
            existing.unlink()
        for item in items:
            (out_dir / f"{item['task_id']}.json").write_text(json.dumps(item, indent=2) + "\n")
        print(f"{name}: {len(items)} tasks")

    if not buckets["held_out"]:
        raise SystemExit("held_out split is empty — task set is too small for a safe split")


if __name__ == "__main__":
    main()
