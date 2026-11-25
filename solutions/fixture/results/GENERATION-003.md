# Generation 3 — fixture

## Throughput

- Peak queue depth: 33
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 35.5%

## Archive

- Island 0: coverage 11.1%, QD score 3.996, unique ancestors 1
- Island 1: coverage 11.1%, QD score 3.996, unique ancestors 2
- Island 2: coverage 11.1%, QD score 3.996, unique ancestors 1
- Island 3: coverage 11.1%, QD score 3.996, unique ancestors 2
- Cells newly claimed this generation: 11

## Quality

- Best scalar this generation: 0.9992
- Median scalar of newly-claimed: 0.9991

## Cost

- Budget: {'generation': 3, 'max_generations': 5, 'tokens_used_total': 838712, 'max_tokens': 10000000, 'elapsed_s_total': 1828.0, 'generation_wall_s': 496.5}
- Candidates proposed: 64
- Parsed: 63 (98.4%)
- Admissible: 63 (98.4%)
- Scored: 63

## Content — newly claimed elites

### Island 0, cell (0, 5), scalar 0.9991

parent `4c1ef043ea25734d` -> candidate `c3f0afec49138704`

```diff
--- parent 4c1ef043ea25734d
+++ candidate c3f0afec49138704
@@ -1,101 +1,102 @@
     import re
+    import math
+    import collections
+    import bisect
 
-    def _is_prime(n):
+    def _is_prime(n: int) -> bool:
         if n < 2:
             return False
-        if n % 2 == 0:
-            return n == 2
-        i = 3
+        if n in (2, 3):
+            return True
+        if n % 2 == 0 or n % 3 == 0:
+            return False
+        i = 5
+        step = 2
         while i * i <= n:
             if n % i == 0:
                 return False
-            i += 2
+            i += step
+            step = 6 - step
         return True
 
-    def _reverse_string(s):
+    def _reverse_string(s: str) -> str:
         return s[::-1]
 
-    def _fibonacci(n):
+    def _fibonacci(n: int) -> int:
         a, b = 0, 1
         for _ in range(n):
             a, b = b, a + b
         return a
 
-    def _gcd(a, b):
-        while b:
-            a, b = b, a % b
-        return a
+    def _gcd(a: int, b: int) -> int:
+        return math.gcd(a, b)
 
-    def _is_palindrome(s):
-        clean = re.sub(r'[^A-Za-z0-9]', '', s).lower()
-        return clean == clean[::-1]
+    def _is_palindrome(s: str) -> bool:
+        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
+        return cleaned == cleaned[::-1]
 
-    def _sum_digits(n):
-        return sum(int(d) for d in str(abs(n)))
+    def _sum_digits(n: int) -> int:
+        return sum(map(int, str(abs(n))))
 
-    def _factorial(n):
+    def _factorial(n: int) -> int:
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        res = 1
-        for i in range(2, n + 1):
-            res *= i
-        return res
+        return math.prod(range(1, n + 1)) if n else 1
 
     def _max_subarray_sum(nums):
         if not nums:
             return 0
         best = cur = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
+            cur = x if cur + x < x else cur + x
+            if cur > best:
+                best = cur
         return best
 
-    def _count_vowels(s):
-        return sum(1 for c in s.lower() if c in "aeiou")
+    def _count_vowels(s: str) -> int:
+        return sum(ch in "aeiou" for ch in s.lower())
 
-    def _is_anagram(a, b):
-        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+    def _is_anagram(a: str, b: str) -> bool:
+        norm = lambda s: collections.Counter(ch.lower() for ch in s if not ch.isspace())
         return norm(a) == norm(b)
 
     def _binary_search(seq, target):
-        lo, hi = 0, len(seq) - 1
-        while lo <= hi:
-            mid = (lo + hi) // 2
-            if seq[mid] == target:
-                return mid
-            if seq[mid] < target:
-                lo = mid + 1
+        i = bisect.bisect_left(seq, target)
+        return i if i < len(seq) and seq[i] == target else -1
+
+    def _flatten_list(item):
+        def _gen(x):
+            if isinstance(x, list):
+                for e in x:
+                    yield from _gen(e)
             else:
-                hi = mid - 1
-        return -1
+                yield x
+        return list(_gen(item))
 
-    def _flatten_list(nested):
-        out = []
-        stack = [nested]
-        while stack:
-            cur = stack.pop()
-            if isinstance(cur, list):
-                stack.extend(reversed(cur))
-            else:
-                out.append(cur)
-        return out
-
-    _dispatch = {
-        "is_prime": lambda args: _is_prime(args[0]),
-        "reverse_string": lambda args: _reverse_string(args[0]),
-        "fibonacci": lambda args: _fibonacci(args[0]),
-        "gcd": lambda args: _gcd(*args),
-        "is_palindrome": lambda args: _is_palindrome(args[0]),
-        "sum_digits": lambda args: _sum_digits(args[0]),
-        "factorial": lambda args: _factorial(args[0]),
-        "max_subarray_sum": lambda args: _max_subarray_sum(args[0]),
-        "count_vowels": lambda args: _count_vowels(args[0]),
-        "is_anagram": lambda args: _is_anagram(*args),
-        "binary_search": lambda args: _binary_search(*args),
-        "flatten_list": lambda args: _flatten_list(args[0]),
-    }
-
-    try:
-        return _dispatch[op](args)
-    except KeyError:
-        raise ValueError(f"unknown op: {op}")+    match op:
+        case "is_prime":
+            return _is_prime(args[0])
+        case "reverse_string":
+            return _reverse_string(args[0])
+        case "fibonacci":
+            return _fibonacci(args[0])
+        case "gcd":
+            return _gcd(*args)
+        case "is_palindrome":
+            return _is_palindrome(args[0])
+        case "sum_digits":
+            return _sum_digits(args[0])
+        case "factorial":
+            return _factorial(args[0])
+        case "max_subarray_sum":
+            return _max_subarray_sum(args[0])
+        case "count_vowels":
+            return _count_vowels(args[0])
+        case "is_anagram":
+            return _is_anagram(*args)
+        case "binary_search":
+            return _binary_search(*args)
+        case "flatten_list":
+            return _flatten_list(args[0])
+        case _:
+            raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (2, 5), scalar 0.9990

parent `d534d5cb63b2ef75` -> candidate `dc3e256d1ed41a23`

```diff
--- parent d534d5cb63b2ef75
+++ candidate dc3e256d1ed41a23
@@ -1,13 +1,15 @@
-    if op == "is_prime":
-        n = args[0]
+    # Standard library imports used by several operations
+    import math, bisect, re, collections
+
+    # ---- Helper functions for each operation ----
+    def _is_prime(n):
         if n < 2:
             return False
         if n % 2 == 0:
             return n == 2
         if n % 3 == 0:
             return n == 3
-        i = 5
-        step = 2
+        i, step = 5, 2
         while i * i <= n:
             if n % i == 0:
                 return False
@@ -15,70 +17,77 @@
             step = 6 - step
         return True
 
-    elif op == "reverse_string":
-        return ''.join(reversed(args[0]))
+    def _reverse_string(s):
+        return s[::-1]
 
-    elif op == "fibonacci":
-        n = args[0]
-        from functools import reduce
-        return reduce(lambda t, _: (t[1], t[0] + t[1]), range(n), (0, 1))[0]
+    def _fibonacci(n):
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
 
-    elif op == "gcd":
-        import math
-        return math.gcd(*args)
+    def _gcd(a, b):
+        return math.gcd(a, b)
 
-    elif op == "is_palindrome":
-        s = args[0]
-        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+    def _is_palindrome(s):
+        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
         return cleaned == cleaned[::-1]
 
-    elif op == "sum_digits":
-        n = args[0]
-        return sum(map(int, str(abs(n))))
+    def _sum_digits(n):
+        return sum(int(d) for d in str(abs(n)))
 
-    elif op == "factorial":
-        n = args[0]
+    def _factorial(n):
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        import math
         return math.prod(range(1, n + 1)) if n else 1
 
-    elif op == "max_subarray_sum":
-        nums = args[0]
+    def _max_subarray_sum(nums):
         if not nums:
             return 0
-        from itertools import accumulate
-        max_sofar = current = nums[0]
-        for val in accumulate(nums[1:], lambda acc, x: max(x, acc + x)):
-            current = val
-            if current > max_sofar:
-                max_sofar = current
-        return max_sofar
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = x if cur + x < x else cur + x
+            if cur > best:
+                best = cur
+        return best
 
-    elif op == "count_vowels":
-        s = args[0].lower()
-        return sum(1 for ch in s if ch in "aeiou")
+    def _count_vowels(s):
+        return sum(1 for ch in s.lower() if ch in "aeiou")
 
-    elif op == "is_anagram":
-        from collections import Counter
-        a, b = args
-        normalize = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
-        return normalize(a) == normalize(b)
+    def _is_anagram(a, b):
+        norm = lambda s: collections.Counter(ch.lower() for ch in s if not ch.isspace())
+        return norm(a) == norm(b)
 
-    elif op == "binary_search":
-        nums, target = args
-        import bisect
-        i = bisect.bisect_left(nums, target)
-        return i if i < len(nums) and nums[i] == target else -1
+    def _binary_search(seq, target):
+        i = bisect.bisect_left(seq, target)
+        return i if i < len(seq) and seq[i] == target else -1
 
-    elif op == "flatten_list":
-        def _flatten(it):
+    def _flatten_list(nested):
+        def _recurse(it):
             for el in it:
                 if isinstance(el, list):
-                    yield from _flatten(el)
+                    yield from _recurse(el)
                 else:
                     yield el
-        return list(_flatten(args[0]))
+        return list(_recurse(nested))
 
-    else:
+    # ---- Dispatch table ----
+    _dispatch = {
+        "is_prime":        lambda args: _is_prime(args[0]),
+        "reverse_string": lambda args: _reverse_string(args[0]),
+        "fibonacci":      lambda args: _fibonacci(args[0]),
+        "gcd":             lambda args: _gcd(*args),
+        "is_palindrome":  lambda args: _is_palindrome(args[0]),
+        "sum_digits":     lambda args: _sum_digits(args[0]),
+        "factorial":      lambda args: _factorial(args[0]),
+        "max_subarray_sum":lambda args: _max_subarray_sum(args[0]),
+        "count_vowels":   lambda args: _count_vowels(args[0]),
+        "is_anagram":     lambda args: _is_anagram(*args),
+        "binary_search":  lambda args: _binary_search(*args),
+        "flatten_list":   lambda args: _flatten_list(args[0]),
+    }
+
+    try:
+        return _dispatch[op](args)
+    except KeyError:
         raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (2, 5), scalar 0.9990

parent `4c1ef043ea25734d` -> candidate `a2fb973e807a3948`

```diff
--- parent 4c1ef043ea25734d
+++ candidate a2fb973e807a3948
@@ -1,101 +1,88 @@
     import re
+    import math
+    import collections
+    import itertools
+    import bisect
 
-    def _is_prime(n):
-        if n < 2:
-            return False
-        if n % 2 == 0:
-            return n == 2
-        i = 3
-        while i * i <= n:
-            if n % i == 0:
-                return False
-            i += 2
-        return True
+    match op:
+        case "is_prime":
+            n = args[0]
+            if n < 2:
+                result = False
+            elif n % 2 == 0:
+                result = n == 2
+            elif n % 3 == 0:
+                result = n == 3
+            else:
+                i, step = 5, 2
+                result = True
+                while i * i <= n:
+                    if n % i == 0:
+                        result = False
+                        break
+                    i += step
+                    step = 6 - step
+            return result
 
-    def _reverse_string(s):
-        return s[::-1]
+        case "reverse_string":
+            return args[0][::-1]
 
-    def _fibonacci(n):
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        case "fibonacci":
+            n = args[0]
+            a, b = 0, 1
+            for _ in range(n):
+                a, b = b, a + b
+            return a
 
-    def _gcd(a, b):
-        while b:
-            a, b = b, a % b
-        return a
+        case "gcd":
+            return math.gcd(*args)
 
-    def _is_palindrome(s):
-        clean = re.sub(r'[^A-Za-z0-9]', '', s).lower()
-        return clean == clean[::-1]
+        case "is_palindrome":
+            s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+            return s == s[::-1]
 
-    def _sum_digits(n):
-        return sum(int(d) for d in str(abs(n)))
+        case "sum_digits":
+            return sum(map(int, str(abs(args[0]))))
 
-    def _factorial(n):
-        if n < 0:
-            raise ValueError("factorial not defined for negative numbers")
-        res = 1
-        for i in range(2, n + 1):
-            res *= i
-        return res
+        case "factorial":
+            n = args[0]
+            if n < 0:
+                raise ValueError("factorial not defined for negative numbers")
+            return math.prod(range(1, n + 1)) if n else 1
 
-    def _max_subarray_sum(nums):
-        if not nums:
-            return 0
-        best = cur = nums[0]
-        for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
-        return best
+        case "max_subarray_sum":
+            nums = args[0]
+            if not nums:
+                return 0
+            best = cur = nums[0]
+            for x in nums[1:]:
+                cur = x if cur + x < x else cur + x
+                if cur > best:
+                    best = cur
+            return best
 
-    def _count_vowels(s):
-        return sum(1 for c in s.lower() if c in "aeiou")
+        case "count_vowels":
+            return sum(1 for ch in args[0].lower() if ch in {"a", "e", "i", "o", "u"})
 
-    def _is_anagram(a, b):
-        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
-        return norm(a) == norm(b)
+        case "is_anagram":
+            a, b = args
+            ca = collections.Counter(ch.lower() for ch in a if not ch.isspace())
+            cb = collections.Counter(ch.lower() for ch in b if not ch.isspace())
+            return ca == cb
 
-    def _binary_search(seq, target):
-        lo, hi = 0, len(seq) - 1
-        while lo <= hi:
-            mid = (lo + hi) // 2
-            if seq[mid] == target:
-                return mid
-            if seq[mid] < target:
-                lo = mid + 1
-            else:
-                hi = mid - 1
-        return -1
+        case "binary_search":
+            seq, target = args
+            i = bisect.bisect_left(seq, target)
+            return i if i < len(seq) and seq[i] == target else -1
 
-    def _flatten_list(nested):
-        out = []
-        stack = [nested]
-        while stack:
-            cur = stack.pop()
-            if isinstance(cur, list):
-                stack.extend(reversed(cur))
-            else:
-                out.append(cur)
-        return out
+        case "flatten_list":
+            def _flatten(it):
+                for el in it:
+                    if isinstance(el, list):
+                        yield from _flatten(el)
+                    else:
+                        yield el
+            return list(_flatten(args[0]))
 
-    _dispatch = {
-        "is_prime": lambda args: _is_prime(args[0]),
-        "reverse_string": lambda args: _reverse_string(args[0]),
-        "fibonacci": lambda args: _fibonacci(args[0]),
-        "gcd": lambda args: _gcd(*args),
-        "is_palindrome": lambda args: _is_palindrome(args[0]),
-        "sum_digits": lambda args: _sum_digits(args[0]),
-        "factorial": lambda args: _factorial(args[0]),
-        "max_subarray_sum": lambda args: _max_subarray_sum(args[0]),
-        "count_vowels": lambda args: _count_vowels(args[0]),
-        "is_anagram": lambda args: _is_anagram(*args),
-        "binary_search": lambda args: _binary_search(*args),
-        "flatten_list": lambda args: _flatten_list(args[0]),
-    }
-
-    try:
-        return _dispatch[op](args)
-    except KeyError:
-        raise ValueError(f"unknown op: {op}")+        case _:
+            raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (2, 5), scalar 0.9991

parent `4c1ef043ea25734d` -> candidate `1a60d64b48143abc`

```diff
--- parent 4c1ef043ea25734d
+++ candidate 1a60d64b48143abc
@@ -1,19 +1,27 @@
     import re
+    import math
+    import bisect
+    import collections
+    import itertools
 
     def _is_prime(n):
         if n < 2:
             return False
         if n % 2 == 0:
             return n == 2
-        i = 3
+        if n % 3 == 0:
+            return n == 3
+        i, step = 5, 2
         while i * i <= n:
             if n % i == 0:
                 return False
-            i += 2
+            i += step
+            step = 6 - step
         return True
 
     def _reverse_string(s):
-        return s[::-1]
+        # using reversed iterator
+        return ''.join(reversed(s))
 
     def _fibonacci(n):
         a, b = 0, 1
@@ -22,80 +30,76 @@
         return a
 
     def _gcd(a, b):
-        while b:
-            a, b = b, a % b
-        return a
+        return math.gcd(a, b)
 
     def _is_palindrome(s):
-        clean = re.sub(r'[^A-Za-z0-9]', '', s).lower()
-        return clean == clean[::-1]
+        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
+        return cleaned == cleaned[::-1]
 
     def _sum_digits(n):
-        return sum(int(d) for d in str(abs(n)))
+        return sum(map(int, str(abs(n))))
 
     def _factorial(n):
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        res = 1
-        for i in range(2, n + 1):
-            res *= i
-        return res
+        return math.prod(range(1, n + 1)) if n else 1
 
     def _max_subarray_sum(nums):
         if not nums:
             return 0
-        best = cur = nums[0]
-        for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
-        return best
+        # Kadane via accumulate
+        max_sofar = cur = nums[0]
+        for val in itertools.accumulate(nums[1:], lambda acc, x: max(x, acc + x)):
+            cur = val
+            if cur > max_sofar:
+                max_sofar = cur
+        return max_sofar
 
     def _count_vowels(s):
-        return sum(1 for c in s.lower() if c in "aeiou")
+        vowels = set('aeiou')
+        return sum(1 for ch in s.lower() if ch in vowels)
 
     def _is_anagram(a, b):
-        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
-        return norm(a) == norm(b)
+        counter = lambda s: collections.Counter(ch.lower() for ch in s if not ch.isspace())
+        return counter(a) == counter(b)
 
     def _binary_search(seq, target):
-        lo, hi = 0, len(seq) - 1
-        while lo <= hi:
-            mid = (lo + hi) // 2
-            if seq[mid] == target:
-                return mid
-            if seq[mid] < target:
-                lo = mid + 1
-            else:
-                hi = mid - 1
-        return -1
+        i = bisect.bisect_left(seq, target)
+        return i if i < len(seq) and seq[i] == target else -1
 
     def _flatten_list(nested):
-        out = []
-        stack = [nested]
-        while stack:
-            cur = stack.pop()
-            if isinstance(cur, list):
-                stack.extend(reversed(cur))
-            else:
-                out.append(cur)
-        return out
+        def _gen(it):
+            for el in it:
+                if isinstance(el, list):
+                    yield from _gen(el)
+                else:
+                    yield el
+        return list(_gen(nested))
 
-    _dispatch = {
-        "is_prime": lambda args: _is_prime(args[0]),
-        "reverse_string": lambda args: _reverse_string(args[0]),
-        "fibonacci": lambda args: _fibonacci(args[0]),
-        "gcd": lambda args: _gcd(*args),
-        "is_palindrome": lambda args: _is_palindrome(args[0]),
-        "sum_digits": lambda args: _sum_digits(args[0]),
-        "factorial": lambda args: _factorial(args[0]),
-        "max_subarray_sum": lambda args: _max_subarray_sum(args[0]),
-        "count_vowels": lambda args: _count_vowels(args[0]),
-        "is_anagram": lambda args: _is_anagram(*args),
-        "binary_search": lambda args: _binary_search(*args),
-        "flatten_list": lambda args: _flatten_list(args[0]),
-    }
-
-    try:
-        return _dispatch[op](args)
-    except KeyError:
-        raise ValueError(f"unknown op: {op}")+    match op:
+        case "is_prime":
+            return _is_prime(args[0])
+        case "reverse_string":
+            return _reverse_string(args[0])
+        case "fibonacci":
+            return _fibonacci(args[0])
+        case "gcd":
+            return _gcd(*args)
+        case "is_palindrome":
+            return _is_palindrome(args[0])
+        case "sum_digits":
+            return _sum_digits(args[0])
+        case "factorial":
+            return _factorial(args[0])
+        case "max_subarray_sum":
+            return _max_subarray_sum(args[0])
+        case "count_vowels":
+            return _count_vowels(args[0])
+        case "is_anagram":
+            return _is_anagram(*args)
+        case "binary_search":
+            return _binary_search(*args)
+        case "flatten_list":
+            return _flatten_list(args[0])
+        case _:
+            raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (1, 5), scalar 0.9991

parent `cfdbebfdaa48cff3` -> candidate `472bdf840606f1a6`

```diff
--- parent cfdbebfdaa48cff3
+++ candidate 472bdf840606f1a6
@@ -1,86 +1,143 @@
-    # Imports needed for alternative implementations
-    from math import gcd as _gcd, prod as _prod, isqrt
-    from collections import Counter
-    from bisect import bisect_left
+    # Minimal imports for helper utilities
+    from math import isqrt
 
     if op == "is_prime":
         n = args[0]
         if n < 2:
             return False
-        if n in (2, 3):
+        # Quick checks for small primes and even numbers
+        small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
+        for p in small_primes:
+            if n == p:
+                return True
+            if n % p == 0:
+                return False
+
+        # Deterministic Miller‑Rabin for 32‑bit integers
+        def _miller_rabin(num: int) -> bool:
+            d = num - 1
+            s = 0
+            while d % 2 == 0:
+                d //= 2
+                s += 1
+            # Bases that are sufficient for n < 2^32
+            for a in (2, 7, 61):
+                if a % num == 0:
+                    continue
+                x = pow(a, d, num)
+                if x == 1 or x == num - 1:
+                    continue
+                for _ in range(s - 1):
+                    x = (x * x) % num
+                    if x == num - 1:
+                        break
+                else:
+                    return False
             return True
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
+
+        return _miller_rabin(n)
 
     elif op == "reverse_string":
-        return ''.join(reversed(args[0]))
+        return args[0][::-1]
 
     elif op == "fibonacci":
         n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+
+        def _fib_pair(k: int):
+            if k == 0:
+                return (0, 1)
+            else:
+                a, b = _fib_pair(k >> 1)
+                c = a * ((b << 1) - a)
+                d = a * a + b * b
+                if k & 1:
+                    return (d, c + d)
+                else:
+                    return (c, d)
+
+        return _fib_pair(n)[0]
 
     elif op == "gcd":
         a, b = args
-        return _gcd(a, b)
+        while b:
+            a, b = b, a % b
+        return abs(a)
 
     elif op == "is_palindrome":
         s = args[0]
-        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
-        return filtered == filtered[::-1]
+        i, j = 0, len(s) - 1
+        while i < j:
+            while i < j and not s[i].isalnum():
+                i += 1
+            while i < j and not s[j].isalnum():
+                j -= 1
+            if s[i].lower() != s[j].lower():
+                return False
+            i += 1
+            j -= 1
+        return True
 
     elif op == "sum_digits":
-        n = args[0]
-        return sum(map(int, str(abs(n))))
+        n = abs(args[0])
+        total = 0
+        while n:
+            total += n % 10
+            n //= 10
+        return total
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial undefined for negative numbers")
-        return 1 if n == 0 else _prod(range(1, n + 1))
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
 
     elif op == "max_subarray_sum":
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
+            max_sofar = max(max_sofar, max_ending)
+        return max_sofar
 
     elif op == "count_vowels":
-        s = args[0].lower()
-        return sum(c in "aeiou" for c in s)
+        s = args[0]
+        vowels = set("aeiouAEIOU")
+        return sum(ch in vowels for ch in s)
 
     elif op == "is_anagram":
         a, b = args
-        norm = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
+        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
         return norm(a) == norm(b)
 
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
-                if isinstance(item, list):
-                    yield from _flatten(item)
-                else:
-                    yield item
-        return list(_flatten(args[0]))
+        nested = args[0]
+        result = []
+        stack = [nested]
+        while stack:
+            cur = stack.pop()
+            if isinstance(cur, list):
+                stack.extend(reversed(cur))
+            else:
+                result.append(cur)
+        return result
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (3, 5), scalar 0.9992

parent `b4141d84a4fd3d48` -> candidate `8f5f65b7098bbb60`

```diff
--- parent b4141d84a4fd3d48
+++ candidate 8f5f65b7098bbb60
@@ -2,15 +2,20 @@
         n = args[0]
         if n < 2:
             return False
-        if n in (2, 3):
-            return True
-        if n % 2 == 0:
-            return False
-        import math
-        limit = math.isqrt(n)
-        for i in range(3, limit + 1, 2):
+        # quick checks for small primes
+        for p in (2, 3, 5, 7):
+            if n == p:
+                return True
+            if n % p == 0:
+                return n == p
+        # 6k ± 1 test
+        i, step = 5, 2
+        limit = int(n ** 0.5)
+        while i <= limit:
             if n % i == 0:
                 return False
+            i += step
+            step = 6 - step  # toggle between 2 and 4
         return True
 
     elif op == "reverse_string":
@@ -19,53 +24,52 @@
     elif op == "fibonacci":
         n = args[0]
         if n < 0:
-            raise ValueError("fibonacci is not defined for negative numbers")
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+            raise ValueError("negative index for fibonacci")
+        def _fib(k):
+            if k == 0:
+                return (0, 1)
+            a, b = _fib(k >> 1)
+            c = a * (2 * b - a)
+            d = a * a + b * b
+            return (c, d) if k & 1 == 0 else (d, c + d)
+        return _fib(n)[0]
 
     elif op == "gcd":
-        a, b = args
-        a, b = abs(a), abs(b)
-        while b:
-            a, b = b, a % b
-        return a
+        import math
+        return math.gcd(*args)
 
     elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        s = ''.join(ch.lower() for ch in args[0] if ch.isalnum())
         return s == s[::-1]
 
     elif op == "sum_digits":
-        n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        return sum(map(int, str(abs(args[0]))))
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
         import math
-        return math.prod(range(1, n + 1)) if n > 0 else 1
+        return math.factorial(n)
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        best = cur = nums[0]
+        cur = best = nums[0]
         for x in nums[1:]:
-            cur = x if cur < 0 else cur + x
+            cur = max(x, cur + x)
             best = max(best, cur)
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        vowels = {"a", "e", "i", "o", "u"}
+        return sum(ch in vowels for ch in s)
 
     elif op == "is_anagram":
-        from collections import Counter
         a, b = args
-        normalize = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
     elif op == "binary_search":
@@ -82,19 +86,13 @@
         return -1
 
     elif op == "flatten_list":
-        nested = args[0]
-        stack = [iter([nested])]
-        result = []
-        while stack:
-            try:
-                item = next(stack[-1])
-                if isinstance(item, list):
-                    stack.append(iter(item))
-                else:
-                    result.append(item)
-            except StopIteration:
-                stack.pop()
-        return result
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        return list(_flatten(args[0]))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (0, 5), scalar 0.9991

parent `3a2baedd645d487d` -> candidate `8984f06163a2347d`

```diff
--- parent 3a2baedd645d487d
+++ candidate 8984f06163a2347d
@@ -2,49 +2,61 @@
         n = args[0]
         if n < 2:
             return False
-        if n == 2:
+        if n in (2, 3):
             return True
-        if n % 2 == 0:
+        if n % 2 == 0 or n % 3 == 0:
             return False
+        i = 5
+        step = 2
         limit = int(n ** 0.5) + 1
-        for i in range(3, limit, 2):
+        while i < limit:
             if n % i == 0:
                 return False
+            i += step
+            step = 6 - step  # toggle between 2 and 4
         return True
 
     elif op == "reverse_string":
-        return args[0][::-1]
+        return ''.join(reversed(args[0]))
 
     elif op == "fibonacci":
         n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        if n < 0:
+            raise ValueError("negative index for fibonacci")
+        def _fib(k):
+            if k == 0:
+                return (0, 1)
+            else:
+                a, b = _fib(k >> 1)
+                c = a * (2 * b - a)
+                d = a * a + b * b
+                return (d, c + d) if k & 1 else (c, d)
+        return _fib(n)[0]
 
     elif op == "gcd":
         a, b = args
-        while b:
-            a, b = b, a % b
-        return a
+        import math
+        return math.gcd(a, b)
 
     elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        s = ''.join(ch.lower() for ch in args[0] if ch.isalnum())
         return s == s[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        total = 0
+        n = abs(n)
+        while n:
+            total += n % 10
+            n //= 10
+        return total
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        import math
+        return math.prod(range(1, n + 1)) if n > 0 else 1
 
     elif op == "max_subarray_sum":
         nums = args[0]
@@ -52,42 +64,50 @@
             return 0
         best = cur = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
+            cur = x if cur < 0 else cur + x
+            if cur > best:
+                best = cur
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        import re
+        matches = re.findall(r'[aeiou]', args[0], flags=re.IGNORECASE)
+        return len(matches)
 
     elif op == "is_anagram":
         a, b = args
-        a_clean = sorted(c.lower() for c in a if not c.isspace())
-        b_clean = sorted(c.lower() for c in b if not c.isspace())
-        return a_clean == b_clean
+        from collections import Counter
+        norm = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
+        return norm(a) == norm(b)
 
     elif op == "binary_search":
         nums, target = args
-        lo, hi = 0, len(nums) - 1
-        while lo <= hi:
+        def _search(lo, hi):
+            if lo > hi:
+                return -1
             mid = (lo + hi) // 2
             if nums[mid] == target:
                 return mid
-            if nums[mid] < target:
-                lo = mid + 1
+            elif nums[mid] < target:
+                return _search(mid + 1, hi)
             else:
-                hi = mid - 1
-        return -1
+                return _search(lo, mid - 1)
+        return _search(0, len(nums) - 1)
 
     elif op == "flatten_list":
-        def _flatten(item):
-            if isinstance(item, list):
-                for sub in item:
-                    yield from _flatten(sub)
-            else:
-                yield item
         nested = args[0]
-        return list(_flatten(nested))
+        stack = [iter([nested])]
+        result = []
+        while stack:
+            try:
+                item = next(stack[-1])
+                if isinstance(item, list):
+                    stack.append(iter(item))
+                else:
+                    result.append(item)
+            except StopIteration:
+                stack.pop()
+        return result
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (1, 5), scalar 0.9991

parent `3a2baedd645d487d` -> candidate `69d7c6ca7db901fe`

```diff
--- parent 3a2baedd645d487d
+++ candidate 69d7c6ca7db901fe
@@ -2,14 +2,18 @@
         n = args[0]
         if n < 2:
             return False
-        if n == 2:
+        if n in (2, 3):
             return True
-        if n % 2 == 0:
+        if n % 2 == 0 or n % 3 == 0:
             return False
-        limit = int(n ** 0.5) + 1
-        for i in range(3, limit, 2):
+        import math
+        i, step = 5, 2
+        limit = math.isqrt(n)
+        while i <= limit:
             if n % i == 0:
                 return False
+            i += step
+            step = 6 - step  # toggle between 2 and 4
         return True
 
     elif op == "reverse_string":
@@ -17,34 +21,37 @@
 
     elif op == "fibonacci":
         n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        if n < 0:
+            raise ValueError("negative index for fibonacci")
+        def _fib(k):
+            if k == 0:
+                return (0, 1)
+            a, b = _fib(k >> 1)
+            c = a * (2 * b - a)
+            d = a * a + b * b
+            return (d, c + d) if k & 1 else (c, d)
+        return _fib(n)[0]
 
     elif op == "gcd":
         a, b = args
-        while b:
-            a, b = b, a % b
-        return a
+        import math
+        return math.gcd(a, b)
 
     elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
-        return s == s[::-1]
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        return sum(map(int, str(abs(n))))
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        import math
+        return math.prod(range(1, n + 1)) if n > 0 else 1
 
     elif op == "max_subarray_sum":
         nums = args[0]
@@ -57,14 +64,14 @@
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        return sum(c in "aeiou" for c in s)
 
     elif op == "is_anagram":
         a, b = args
-        a_clean = sorted(c.lower() for c in a if not c.isspace())
-        b_clean = sorted(c.lower() for c in b if not c.isspace())
-        return a_clean == b_clean
+        from collections import Counter
+        normalize = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
 
     elif op == "binary_search":
         nums, target = args
@@ -80,14 +87,16 @@
         return -1
 
     elif op == "flatten_list":
-        def _flatten(item):
+        nested = args[0]
+        result = []
+        stack = [nested]
+        while stack:
+            item = stack.pop()
             if isinstance(item, list):
-                for sub in item:
-                    yield from _flatten(sub)
+                stack.extend(reversed(item))
             else:
-                yield item
-        nested = args[0]
-        return list(_flatten(nested))
+                result.append(item)
+        return result
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (0, 5), scalar 0.9991

parent `db772eb8f9c682bc` -> candidate `b6b628d85fdbb83e`

```diff
--- parent db772eb8f9c682bc
+++ candidate b6b628d85fdbb83e
@@ -4,94 +4,95 @@
             return False
         if n % 2 == 0:
             return n == 2
-        i = 3
-        limit = int(n ** 0.5) + 1
-        while i <= limit:
+        if n % 3 == 0:
+            return n == 3
+        i, step = 5, 2
+        while i * i <= n:
             if n % i == 0:
                 return False
-            i += 2
+            i += step
+            step = 6 - step  # alternate between 2 and 4
         return True
 
     elif op == "reverse_string":
-        return args[0][::-1]
+        return "".join(reversed(args[0]))
 
     elif op == "fibonacci":
         n = args[0]
         a, b = 0, 1
-        for _ in range(n):
+        count = 0
+        while count < n:
             a, b = b, a + b
+            count += 1
         return a
 
     elif op == "gcd":
+        import math
         a, b = args
-        while b:
-            a, b = b, a % b
-        return abs(a)
+        return abs(math.gcd(a, b))
 
     elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
-        return s == s[::-1]
+        s = args[0]
+        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        return sum(map(int, str(abs(n))))
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial undefined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        import math
+        return math.prod(range(1, n + 1)) if n > 0 else 1
 
     elif op == "max_subarray_sum":
+        from itertools import accumulate
         nums = args[0]
         if not nums:
             return 0
+        kadane = (max(x, y) for x, y in zip(accumulate(nums, lambda a, b: a + b), accumulate(nums, lambda a, b: max(b, a + b))))
+        # Simpler explicit Kadane without copy‑paste of previous logic
         best = cur = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
+            cur = x if cur < 0 else cur + x
             best = max(best, cur)
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        vowels = set("aeiou")
+        return sum(ch in vowels for ch in s)
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        normalize = lambda s: Counter(c.lower() for c in s if not c.isspace())
         return normalize(a) == normalize(b)
 
     elif op == "binary_search":
         nums, target = args
-        lo, hi = 0, len(nums) - 1
-        while lo <= hi:
+        def recurse(lo, hi):
+            if lo > hi:
+                return -1
             mid = (lo + hi) // 2
             if nums[mid] == target:
                 return mid
             if nums[mid] < target:
-                lo = mid + 1
-            else:
-                hi = mid - 1
-        return -1
+                return recurse(mid + 1, hi)
+            return recurse(lo, mid - 1)
+        return recurse(0, len(nums) - 1)
 
     elif op == "flatten_list":
         nested = args[0]
-        out = []
-        stack = [iter(nested)]
-        while stack:
-            try:
-                item = next(stack[-1])
-                if isinstance(item, list):
-                    stack.append(iter(item))
-                else:
-                    out.append(item)
-            except StopIteration:
-                stack.pop()
-        return out
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        return list(_flatten(nested))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (0, 5), scalar 0.9992

parent `db772eb8f9c682bc` -> candidate `1d1b4f48dbd92b14`

```diff
--- parent db772eb8f9c682bc
+++ candidate 1d1b4f48dbd92b14
@@ -2,96 +2,97 @@
         n = args[0]
         if n < 2:
             return False
-        if n % 2 == 0:
-            return n == 2
-        i = 3
+        if n in (2, 3):
+            return True
+        if n % 2 == 0 or n % 3 == 0:
+            return False
+        i = 5
+        step = 2
         limit = int(n ** 0.5) + 1
         while i <= limit:
             if n % i == 0:
                 return False
-            i += 2
+            i += step
+            step = 6 - step  # alternate between +2 and +4 (6k ± 1)
         return True
 
     elif op == "reverse_string":
-        return args[0][::-1]
+        return ''.join(reversed(args[0]))
 
     elif op == "fibonacci":
         n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        if n < 0:
+            raise ValueError("n must be non‑negative")
+        def _fib(k):
+            a, b = 0, 1
+            for _ in range(k):
+                a, b = b, a + b
+            return a
+        return _fib(n)
 
     elif op == "gcd":
+        import math
         a, b = args
-        while b:
-            a, b = b, a % b
-        return abs(a)
+        return abs(math.gcd(a, b))
 
     elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        s = ''.join(c.lower() for c in args[0] if c.isalnum())
         return s == s[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        return sum(map(int, str(abs(n))))
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial undefined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        from functools import reduce
+        return reduce(lambda x, y: x * y, range(2, n + 1), 1)
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        best = cur = nums[0]
+        cur = best = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
+            cur = x if cur < 0 else cur + x
+            best = best if best > cur else cur
         return best
 
     elif op == "count_vowels":
+        import re
         s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        return len(re.findall(r'[aeiou]', s, flags=re.I))
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        normalize = lambda s: Counter(c.lower() for c in s if not c.isspace())
         return normalize(a) == normalize(b)
 
     elif op == "binary_search":
         nums, target = args
-        lo, hi = 0, len(nums) - 1
-        while lo <= hi:
+        def _search(lo, hi):
+            if lo > hi:
+                return -1
             mid = (lo + hi) // 2
             if nums[mid] == target:
                 return mid
             if nums[mid] < target:
-                lo = mid + 1
-            else:
-                hi = mid - 1
-        return -1
+                return _search(mid + 1, hi)
+            return _search(lo, mid - 1)
+        return _search(0, len(nums) - 1)
 
     elif op == "flatten_list":
         nested = args[0]
-        out = []
-        stack = [iter(nested)]
-        while stack:
-            try:
-                item = next(stack[-1])
-                if isinstance(item, list):
-                    stack.append(iter(item))
-                else:
-                    out.append(item)
-            except StopIteration:
-                stack.pop()
-        return out
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        return list(_flatten(nested))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9991

parent `8376bf500f1a3f75` -> candidate `5dce7ad294059e73`

```diff
--- parent 8376bf500f1a3f75
+++ candidate 5dce7ad294059e73
@@ -2,14 +2,17 @@
         n = args[0]
         if n < 2:
             return False
-        if n == 2:
+        if n in (2, 3):
             return True
-        if n % 2 == 0:
+        if n % 2 == 0 or n % 3 == 0:
             return False
-        limit = int(n ** 0.5) + 1
-        for i in range(3, limit, 2):
-            if n % i == 0:
+        import math
+        limit = math.isqrt(n)
+        i = 5
+        while i <= limit:
+            if n % i == 0 or n % (i + 2) == 0:
                 return False
+            i += 6
         return True
 
     elif op == "reverse_string":
@@ -17,76 +20,80 @@
 
     elif op == "fibonacci":
         n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        if n < 0:
+            raise ValueError("n must be non‑negative")
+        def _fib(k):
+            if k == 0:
+                return (0, 1)
+            a, b = _fib(k >> 1)
+            c = a * (2 * b - a)
+            d = a * a + b * b
+            return (d, c + d) if k & 1 else (c, d)
+        return _fib(n)[0]
 
     elif op == "gcd":
         a, b = args
-        while b:
-            a, b = b, a % b
-        return a
+        import math
+        return abs(math.gcd(a, b))
 
     elif op == "is_palindrome":
         s = args[0]
-        cleaned = ''.join(c.lower() for c in s if c.isalnum())
+        import re
+        cleaned = re.sub(r'[\W_]', '', s).lower()
         return cleaned == cleaned[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        return sum(map(int, str(abs(n))))
 
     elif op == "factorial":
         n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative integers")
         if n == 0:
             return 1
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        import math
+        return math.prod(range(1, n + 1))
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        best = cur = nums[0]
-        for x in nums[1:]:
+        import functools
+        def _step(acc, x):
+            cur, best = acc
             cur = max(x, cur + x)
             best = max(best, cur)
+            return (cur, best)
+        _, best = functools.reduce(_step, nums[1:], (nums[0], nums[0]))
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        vowels = set("aeiou")
+        return sum(1 for ch in s if ch in vowels)
 
     elif op == "is_anagram":
         a, b = args
-        def normalize(s):
-            return sorted(c.lower() for c in s if not c.isspace())
-        return normalize(a) == normalize(b)
+        from collections import Counter
+        def _norm(txt):
+            return Counter(ch.lower() for ch in txt if not ch.isspace())
+        return _norm(a) == _norm(b)
 
     elif op == "binary_search":
         nums, target = args
-        lo, hi = 0, len(nums) - 1
-        while lo <= hi:
-            mid = (lo + hi) // 2
-            if nums[mid] == target:
-                return mid
-            if nums[mid] < target:
-                lo = mid + 1
-            else:
-                hi = mid - 1
-        return -1
+        import bisect
+        i = bisect.bisect_left(nums, target)
+        return i if i < len(nums) and nums[i] == target else -1
 
     elif op == "flatten_list":
         nested = args[0]
         def _flatten(item):
-            if isinstance(item, list):
-                for sub in item:
-                    yield from _flatten(sub)
-            else:
-                yield item
+            for elem in item:
+                if isinstance(elem, list):
+                    yield from _flatten(elem)
+                else:
+                    yield elem
         return list(_flatten(nested))
 
     else:

```

