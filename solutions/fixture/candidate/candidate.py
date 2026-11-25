"""Fixture candidate. FROZEN signature: `solve(task_input: str, ctx) -> str`.

task_input is a JSON string `{"op": <name>, "args": [...]}`. solve() must
dispatch to the right computation and return `json.dumps(result)`.

Everything between the EVOLVE-BLOCK markers is the proposer's to rewrite.
This starting version is deliberately imperfect — about half the operations
are missing, wrong, or wrong on edge cases — so there's real room for a
search loop to improve it. See solutions/fixture/checks/reference.py for
the ground truth this is scored against (never imported here).
"""

from __future__ import annotations

import json


def solve(task_input: str, ctx=None) -> str:
    req = json.loads(task_input)
    op, args = req["op"], req["args"]
    result = _dispatch(op, args)
    return json.dumps(result)


def _dispatch(op: str, args: list):
    # EVOLVE-BLOCK-START
    if op == "is_prime":
        n = args[0]
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    elif op == "reverse_string":
        return args[0][::-1]

    elif op == "fibonacci":
        # BUG: off-by-one — returns fibonacci(n+1)
        n = args[0]
        a, b = 0, 1
        for _ in range(n + 1):
            a, b = b, a + b
        return a

    elif op == "gcd":
        a, b = args
        while b:
            a, b = b, a % b
        return a

    elif op == "is_palindrome":
        # BUG: doesn't strip spaces/punctuation or lowercase
        s = args[0]
        return s == s[::-1]

    elif op == "sum_digits":
        n = args[0]
        return sum(int(d) for d in str(abs(n)))

    elif op == "factorial":
        # BUG: wrong base case, factorial(0) returns 0 instead of 1
        n = args[0]
        if n == 0:
            return 0
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    elif op == "max_subarray_sum":
        # BUG: doesn't handle all-negative arrays correctly (returns 0 instead of the max single element)
        nums = args[0]
        best = cur = 0
        for x in nums:
            cur = max(0, cur + x)
            best = max(best, cur)
        return best

    elif op == "count_vowels":
        s = args[0]
        return sum(1 for c in s.lower() if c in "aeiou")

    elif op == "is_anagram":
        # BUG: case-sensitive, doesn't strip spaces
        a, b = args
        return sorted(a) == sorted(b)

    elif op == "binary_search":
        nums, target = args
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    elif op == "flatten_list":
        # BUG: only flattens one level deep
        nested = args[0]
        out = []
        for item in nested:
            if isinstance(item, list):
                out.extend(item)
            else:
                out.append(item)
        return out

    else:
        raise ValueError(f"unknown op: {op}")
    # EVOLVE-BLOCK-END
