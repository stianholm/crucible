# Generation 4 — fixture

## Throughput

- Peak queue depth: 34
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 37.1%

## Archive

- Island 0: coverage 11.1%, QD score 3.996, unique ancestors 1
- Island 1: coverage 11.1%, QD score 3.996, unique ancestors 1
- Island 2: coverage 11.1%, QD score 3.997, unique ancestors 1
- Island 3: coverage 11.1%, QD score 3.996, unique ancestors 2
- Cells newly claimed this generation: 4

## Quality

- Best scalar this generation: 0.9991
- Median scalar of newly-claimed: 0.9991

## Cost

- Budget: {'generation': 4, 'max_generations': 5, 'tokens_used_total': 1077448, 'max_tokens': 10000000, 'elapsed_s_total': 2334.4, 'generation_wall_s': 506.4}
- Candidates proposed: 64
- Parsed: 61 (95.3%)
- Admissible: 59 (92.2%)
- Scored: 59

## Content — newly claimed elites

### Island 0, cell (3, 5), scalar 0.9991

parent `1a60d64b48143abc` -> candidate `236299ffe548b927`

```diff
--- parent 1a60d64b48143abc
+++ candidate 236299ffe548b927
@@ -2,104 +2,108 @@
     import math
     import bisect
     import collections
-    import itertools
 
-    def _is_prime(n):
+    def _is_prime(n: int) -> bool:
         if n < 2:
             return False
-        if n % 2 == 0:
-            return n == 2
-        if n % 3 == 0:
-            return n == 3
-        i, step = 5, 2
-        while i * i <= n:
+        if n in (2, 3):
+            return True
+        if n % 2 == 0 or n % 3 == 0:
+            return False
+        limit = math.isqrt(n)
+        i = 5
+        step = 2
+        while i <= limit:
             if n % i == 0:
                 return False
             i += step
             step = 6 - step
         return True
 
-    def _reverse_string(s):
-        # using reversed iterator
-        return ''.join(reversed(s))
+    def _reverse_string(s: str) -> str:
+        return s[::-1]
 
-    def _fibonacci(n):
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+    def _fib_pair(n: int):
+        """return (F(n), F(n+1)) using fast doubling."""
+        if n == 0:
+            return (0, 1)
+        else:
+            a, b = _fib_pair(n >> 1)
+            c = a * ((b << 1) - a)
+            d = a * a + b * b
+            if n & 1:
+                return (d, c + d)
+            else:
+                return (c, d)
 
-    def _gcd(a, b):
+    def _fibonacci(n: int) -> int:
+        return _fib_pair(n)[0]
+
+    def _gcd(a: int, b: int) -> int:
         return math.gcd(a, b)
 
-    def _is_palindrome(s):
+    def _is_palindrome(s: str) -> bool:
         cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
         return cleaned == cleaned[::-1]
 
-    def _sum_digits(n):
-        return sum(map(int, str(abs(n))))
+    def _sum_digits(n: int) -> int:
+        n = abs(n)
+        total = 0
+        while n:
+            total += n % 10
+            n //= 10
+        return total
 
-    def _factorial(n):
+    def _factorial(n: int) -> int:
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        return math.prod(range(1, n + 1)) if n else 1
+        return math.factorial(n)
 
     def _max_subarray_sum(nums):
-        if not nums:
-            return 0
-        # Kadane via accumulate
-        max_sofar = cur = nums[0]
-        for val in itertools.accumulate(nums[1:], lambda acc, x: max(x, acc + x)):
-            cur = val
-            if cur > max_sofar:
-                max_sofar = cur
-        return max_sofar
+        best = cur = 0
+        for x in nums:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
 
-    def _count_vowels(s):
-        vowels = set('aeiou')
-        return sum(1 for ch in s.lower() if ch in vowels)
+    def _count_vowels(s: str) -> int:
+        return sum(s.lower().count(v) for v in "aeiou")
 
-    def _is_anagram(a, b):
-        counter = lambda s: collections.Counter(ch.lower() for ch in s if not ch.isspace())
-        return counter(a) == counter(b)
+    def _is_anagram(a: str, b: str) -> bool:
+        norm = lambda txt: sorted(ch.lower() for ch in txt if not ch.isspace())
+        return norm(a) == norm(b)
 
     def _binary_search(seq, target):
         i = bisect.bisect_left(seq, target)
         return i if i < len(seq) and seq[i] == target else -1
 
-    def _flatten_list(nested):
-        def _gen(it):
-            for el in it:
-                if isinstance(el, list):
-                    yield from _gen(el)
+    def _flatten_list(item):
+        stack = [iter([item])]
+        result = []
+        while stack:
+            for elem in stack.pop():
+                if isinstance(elem, list):
+                    stack.append(iter([elem]))
                 else:
-                    yield el
-        return list(_gen(nested))
+                    result.append(elem)
+                    break
+        return result
 
-    match op:
-        case "is_prime":
-            return _is_prime(args[0])
-        case "reverse_string":
-            return _reverse_string(args[0])
-        case "fibonacci":
-            return _fibonacci(args[0])
-        case "gcd":
-            return _gcd(*args)
-        case "is_palindrome":
-            return _is_palindrome(args[0])
-        case "sum_digits":
-            return _sum_digits(args[0])
-        case "factorial":
-            return _factorial(args[0])
-        case "max_subarray_sum":
-            return _max_subarray_sum(args[0])
-        case "count_vowels":
-            return _count_vowels(args[0])
-        case "is_anagram":
-            return _is_anagram(*args)
-        case "binary_search":
-            return _binary_search(*args)
-        case "flatten_list":
-            return _flatten_list(args[0])
-        case _:
-            raise ValueError(f"unknown op: {op}")+    _dispatch = {
+        "is_prime": lambda: _is_prime(args[0]),
+        "reverse_string": lambda: _reverse_string(args[0]),
+        "fibonacci": lambda: _fibonacci(args[0]),
+        "gcd": lambda: _gcd(*args),
+        "is_palindrome": lambda: _is_palindrome(args[0]),
+        "sum_digits": lambda: _sum_digits(args[0]),
+        "factorial": lambda: _factorial(args[0]),
+        "max_subarray_sum": lambda: _max_subarray_sum(args[0]),
+        "count_vowels": lambda: _count_vowels(args[0]),
+        "is_anagram": lambda: _is_anagram(*args),
+        "binary_search": lambda: _binary_search(*args),
+        "flatten_list": lambda: _flatten_list(args[0]),
+    }
+
+    if op in _dispatch:
+        return _dispatch[op]()
+    raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (3, 5), scalar 0.9990

parent `cfdbebfdaa48cff3` -> candidate `e7d82e32f54f50b4`

```diff
--- parent cfdbebfdaa48cff3
+++ candidate e7d82e32f54f50b4
@@ -1,34 +1,30 @@
-    # Imports needed for alternative implementations
+    # Required imports for various implementations
     from math import gcd as _gcd, prod as _prod, isqrt
-    from collections import Counter
-    from bisect import bisect_left
+    import re
 
     if op == "is_prime":
         n = args[0]
         if n < 2:
             return False
-        if n in (2, 3):
-            return True
-        if n % 2 == 0 or n % 3 == 0:
-            return False
-        i = 5
-        w = 2
-        while i * i <= n:
-            if n % i == 0:
-                return False
-            i += w
-            w = 6 - w  # alternate between checking 6k-1 and 6k+1
-        return True
+        if n % 2 == 0:
+            return n == 2
+        limit = isqrt(n)
+        return all(n % d for d in range(3, limit + 1, 2))
 
     elif op == "reverse_string":
-        return ''.join(reversed(args[0]))
+        return args[0][::-1]
 
     elif op == "fibonacci":
-        n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        # fast‑doubling method (O(log n))
+        def _fib_pair(k):
+            if k == 0:
+                return (0, 1)
+            else:
+                a, b = _fib_pair(k >> 1)
+                c = a * ((b << 1) - a)
+                d = a * a + b * b
+                return (c, d) if k & 1 == 0 else (d, c + d)
+        return _fib_pair(args[0])[0]
 
     elif op == "gcd":
         a, b = args
@@ -40,8 +36,11 @@
         return filtered == filtered[::-1]
 
     elif op == "sum_digits":
-        n = args[0]
-        return sum(map(int, str(abs(n))))
+        n = abs(args[0])
+        total = 0
+        while n:
+            total, n = total + n % 10, n // 10
+        return total
 
     elif op == "factorial":
         n = args[0]
@@ -53,34 +52,49 @@
         nums = args[0]
         if not nums:
             return 0
-        max_ending_here = max_so_far = nums[0]
+        max_ending = max_sofar = nums[0]
         for x in nums[1:]:
-            max_ending_here = max(x, max_ending_here + x)
-            max_so_far = max(max_so_far, max_ending_here)
-        return max_so_far
+            max_ending = x if max_ending < 0 else max_ending + x
+            if max_ending > max_sofar:
+                max_sofar = max_ending
+        return max_sofar
 
     elif op == "count_vowels":
         s = args[0].lower()
-        return sum(c in "aeiou" for c in s)
+        return len(re.findall(r'[aeiou]', s))
 
     elif op == "is_anagram":
         a, b = args
-        norm = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
-        return norm(a) == norm(b)
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
 
     elif op == "binary_search":
         nums, target = args
-        idx = bisect_left(nums, target)
-        return idx if idx < len(nums) and nums[idx] == target else -1
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            elif nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
 
     elif op == "flatten_list":
-        def _flatten(seq):
-            for item in seq:
+        nested = args[0]
+        stack = [iter(nested)]
+        result = []
+        while stack:
+            try:
+                item = next(stack[-1])
                 if isinstance(item, list):
-                    yield from _flatten(item)
+                    stack.append(iter(item))
                 else:
-                    yield item
-        return list(_flatten(args[0]))
+                    result.append(item)
+            except StopIteration:
+                stack.pop()
+        return result
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (1, 5), scalar 0.9991

parent `8f5f65b7098bbb60` -> candidate `58b598b3720f352e`

```diff
--- parent 8f5f65b7098bbb60
+++ candidate 58b598b3720f352e
@@ -2,20 +2,18 @@
         n = args[0]
         if n < 2:
             return False
-        # quick checks for small primes
-        for p in (2, 3, 5, 7):
-            if n == p:
-                return True
-            if n % p == 0:
-                return n == p
-        # 6k ± 1 test
-        i, step = 5, 2
-        limit = int(n ** 0.5)
-        while i <= limit:
+        if n in (2, 3):
+            return True
+        if n % 2 == 0 or n % 3 == 0:
+            return False
+        i = 5
+        step = 2
+        limit = int(n ** 0.5) + 1
+        while i < limit:
             if n % i == 0:
                 return False
             i += step
-            step = 6 - step  # toggle between 2 and 4
+            step = 6 - step  # alternate 2,4 to test 6k±1
         return True
 
     elif op == "reverse_string":
@@ -25,52 +23,64 @@
         n = args[0]
         if n < 0:
             raise ValueError("negative index for fibonacci")
-        def _fib(k):
-            if k == 0:
-                return (0, 1)
-            a, b = _fib(k >> 1)
-            c = a * (2 * b - a)
+        # fast doubling, iterative
+        a, b = 0, 1  # F(0), F(1)
+        for bit in bin(n)[2:]:
+            c = a * ((b << 1) - a)
             d = a * a + b * b
-            return (c, d) if k & 1 == 0 else (d, c + d)
-        return _fib(n)[0]
+            if bit == '0':
+                a, b = c, d
+            else:
+                a, b = d, c + d
+        return a
 
     elif op == "gcd":
-        import math
-        return math.gcd(*args)
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
 
     elif op == "is_palindrome":
         s = ''.join(ch.lower() for ch in args[0] if ch.isalnum())
         return s == s[::-1]
 
     elif op == "sum_digits":
-        return sum(map(int, str(abs(args[0]))))
+        total = 0
+        n = abs(args[0])
+        while n:
+            total += n % 10
+            n //= 10
+        return total
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        import math
-        return math.factorial(n)
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        cur = best = nums[0]
+        best = cur = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
+            cur = x if cur < 0 else cur + x
+            if cur > best:
+                best = cur
         return best
 
     elif op == "count_vowels":
-        s = args[0].lower()
-        vowels = {"a", "e", "i", "o", "u"}
-        return sum(ch in vowels for ch in s)
+        vowels = set("aeiou")
+        return sum(ch in vowels for ch in args[0].lower())
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
-        return normalize(a) == normalize(b)
+        filter_func = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
+        return filter_func(a) == filter_func(b)
 
     elif op == "binary_search":
         nums, target = args
@@ -86,13 +96,15 @@
         return -1
 
     elif op == "flatten_list":
-        def _flatten(item):
+        stack = [args[0]]
+        result = []
+        while stack:
+            item = stack.pop()
             if isinstance(item, list):
-                for sub in item:
-                    yield from _flatten(sub)
+                stack.extend(reversed(item))
             else:
-                yield item
-        return list(_flatten(args[0]))
+                result.append(item)
+        return result
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9991

parent `1d1b4f48dbd92b14` -> candidate `ce99175a730aefe6`

```diff
--- parent 1d1b4f48dbd92b14
+++ candidate ce99175a730aefe6
@@ -2,97 +2,100 @@
         n = args[0]
         if n < 2:
             return False
-        if n in (2, 3):
-            return True
-        if n % 2 == 0 or n % 3 == 0:
-            return False
-        i = 5
-        step = 2
+        if n % 2 == 0:
+            return n == 2
         limit = int(n ** 0.5) + 1
-        while i <= limit:
+        for i in range(3, limit, 2):
             if n % i == 0:
                 return False
-            i += step
-            step = 6 - step  # alternate between +2 and +4 (6k ± 1)
         return True
 
     elif op == "reverse_string":
-        return ''.join(reversed(args[0]))
+        return args[0][::-1]
 
     elif op == "fibonacci":
         n = args[0]
         if n < 0:
             raise ValueError("n must be non‑negative")
-        def _fib(k):
-            a, b = 0, 1
-            for _ in range(k):
-                a, b = b, a + b
-            return a
-        return _fib(n)
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
 
     elif op == "gcd":
-        import math
         a, b = args
-        return abs(math.gcd(a, b))
+        while b:
+            a, b = b, a % b
+        return abs(a)
 
     elif op == "is_palindrome":
-        s = ''.join(c.lower() for c in args[0] if c.isalnum())
+        import re
+        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
         return s == s[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(map(int, str(abs(n))))
+        return sum(int(d) for d in str(abs(n)))
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial undefined for negative numbers")
-        from functools import reduce
-        return reduce(lambda x, y: x * y, range(2, n + 1), 1)
+        try:
+            from math import prod
+            return prod(range(1, n + 1)) or 1
+        except ImportError:
+            result = 1
+            for i in range(2, n + 1):
+                result *= i
+            return result
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        cur = best = nums[0]
+        max_ending = max_sofar = nums[0]
         for x in nums[1:]:
-            cur = x if cur < 0 else cur + x
-            best = best if best > cur else cur
-        return best
+            max_ending = max(x, max_ending + x)
+            max_sofar = max(max_sofar, max_ending)
+        return max_sofar
 
     elif op == "count_vowels":
-        import re
-        s = args[0]
-        return len(re.findall(r'[aeiou]', s, flags=re.I))
+        s = args[0].lower()
+        return sum(c in "aeiou" for c in s)
 
     elif op == "is_anagram":
-        from collections import Counter
         a, b = args
-        normalize = lambda s: Counter(c.lower() for c in s if not c.isspace())
-        return normalize(a) == normalize(b)
+        return sorted(c.lower() for c in a if not c.isspace()) == \
+               sorted(c.lower() for c in b if not c.isspace())
 
     elif op == "binary_search":
         nums, target = args
-        def _search(lo, hi):
-            if lo > hi:
-                return -1
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
             mid = (lo + hi) // 2
             if nums[mid] == target:
                 return mid
-            if nums[mid] < target:
-                return _search(mid + 1, hi)
-            return _search(lo, mid - 1)
-        return _search(0, len(nums) - 1)
+            elif nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
 
     elif op == "flatten_list":
         nested = args[0]
-        def _flatten(item):
-            if isinstance(item, list):
-                for sub in item:
-                    yield from _flatten(sub)
-            else:
-                yield item
-        return list(_flatten(nested))
+        out = []
+        stack = [iter([nested])]
+        while stack:
+            try:
+                item = next(stack[-1])
+                if isinstance(item, list):
+                    stack.append(iter(item))
+                else:
+                    out.append(item)
+            except StopIteration:
+                stack.pop()
+        return out
 
     else:
         raise ValueError(f"unknown op: {op}")
```


## Held-out check (best-ever candidate)

- Candidate: `8f5f65b7098bbb60` (rotation scalar 0.9992)
- Held-out quality: 1.0000
- Held-out scalar: 0.9991
- All held-out tasks valid: True
