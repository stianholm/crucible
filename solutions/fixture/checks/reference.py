"""Ground-truth reference implementations for the fixture's task set.

Used only by generate_tasks.py to compute the `expected` field for each
task. Never shipped to the proposer and never imported by candidate.py —
the candidate must solve these independently. See PHASE-1.md task 1.1's
note on the evaluator never being reachable from the candidate.
"""

from __future__ import annotations

import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def reverse_string(s: str) -> str:
    return s[::-1]


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def sum_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def max_subarray_sum(nums: list[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def is_anagram(a: str, b: str) -> bool:
    norm = lambda s: sorted(c.lower() for c in s if c.isalnum())
    return norm(a) == norm(b)


def binary_search(nums: list[int], target: int) -> int:
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


def flatten_list(nested: list) -> list:
    out = []
    for item in nested:
        if isinstance(item, list):
            out.extend(flatten_list(item))
        else:
            out.append(item)
    return out


REFERENCE_OPS = {
    "is_prime": is_prime,
    "reverse_string": reverse_string,
    "fibonacci": fibonacci,
    "gcd": gcd,
    "is_palindrome": is_palindrome,
    "sum_digits": sum_digits,
    "factorial": factorial,
    "max_subarray_sum": max_subarray_sum,
    "count_vowels": count_vowels,
    "is_anagram": is_anagram,
    "binary_search": binary_search,
    "flatten_list": flatten_list,
}
