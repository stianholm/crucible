# Generation 1 — fixture

## Throughput

- Peak queue depth: 34
- Sustained (median) queue depth: 33.0
- Prefix cache hit rate: 31.7%

## Archive

- Island 0: coverage 11.1%, QD score 3.996, unique ancestors 2
- Island 1: coverage 11.1%, QD score 3.996, unique ancestors 3
- Island 2: coverage 11.1%, QD score 3.996, unique ancestors 2
- Island 3: coverage 11.1%, QD score 3.996, unique ancestors 3
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.9991
- Median scalar of newly-claimed: 0.9990

## Cost

- Budget: {'generation': 1, 'max_generations': 5, 'tokens_used_total': 367306, 'max_tokens': 10000000, 'elapsed_s_total': 852.7, 'generation_wall_s': 532.0}
- Candidates proposed: 64
- Parsed: 62 (96.9%)
- Admissible: 62 (96.9%)
- Scored: 62

## Content — newly claimed elites

### Island 0, cell (3, 5), scalar 0.9987

parent `23a46010a1a2f2a6` -> candidate `5fea1ad6d6fe2a48`

```diff
--- parent 23a46010a1a2f2a6
+++ candidate 5fea1ad6d6fe2a48
@@ -4,88 +4,99 @@
             return False
         if n % 2 == 0:
             return n == 2
-        i = 3
+        if n % 3 == 0:
+            return n == 3
+        i = 5
+        w = 2
         while i * i <= n:
             if n % i == 0:
                 return False
-            i += 2
+            i += w
+            w = 6 - w  # alternate between checking 6k‑1 and 6k+1
         return True
 
     elif op == "reverse_string":
-        return args[0][::-1]
+        return ''.join(reversed(args[0]))
 
     elif op == "fibonacci":
         n = args[0]
         a, b = 0, 1
-        for _ in range(n):
+        while n:
             a, b = b, a + b
+            n -= 1
         return a
 
     elif op == "gcd":
         a, b = args
-        while b:
-            a, b = b, a % b
-        return a
+        # recursive Euclidean algorithm
+        def _gcd(x, y):
+            return x if y == 0 else _gcd(y, x % y)
+        return _gcd(a, b)
 
     elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
-        return s == s[::-1]
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        return sum(map(int, str(abs(n))))
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
+        # tail‑recursive style using a loop to avoid recursion depth limits
         result = 1
-        for i in range(2, n + 1):
-            result *= i
+        while n > 1:
+            result *= n
+            n -= 1
         return result
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        best = cur = nums[0]
+        max_ending_here = max_so_far = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
-        return best
+            max_ending_here = max(x, max_ending_here + x)
+            max_so_far = max(max_so_far, max_ending_here)
+        return max_so_far
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        return sum(c in "aeiou" for c in s)
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        normalize = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
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
-        def _flatten(item):
-            for elem in item:
-                if isinstance(elem, list):
-                    yield from _flatten(elem)
-                else:
-                    yield elem
         nested = args[0]
-        return list(_flatten(nested))
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

### Island 0, cell (3, 5), scalar 0.9990

parent `23a46010a1a2f2a6` -> candidate `d534d5cb63b2ef75`

```diff
--- parent 23a46010a1a2f2a6
+++ candidate d534d5cb63b2ef75
@@ -4,88 +4,81 @@
             return False
         if n % 2 == 0:
             return n == 2
-        i = 3
+        if n % 3 == 0:
+            return n == 3
+        i = 5
+        step = 2
         while i * i <= n:
             if n % i == 0:
                 return False
-            i += 2
+            i += step
+            step = 6 - step
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
+        from functools import reduce
+        return reduce(lambda t, _: (t[1], t[0] + t[1]), range(n), (0, 1))[0]
 
     elif op == "gcd":
-        a, b = args
-        while b:
-            a, b = b, a % b
-        return a
+        import math
+        return math.gcd(*args)
 
     elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
-        return s == s[::-1]
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
 
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
+        return math.prod(range(1, n + 1)) if n else 1
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        best = cur = nums[0]
-        for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
-        return best
+        from itertools import accumulate
+        max_sofar = current = nums[0]
+        for val in accumulate(nums[1:], lambda acc, x: max(x, acc + x)):
+            current = val
+            if current > max_sofar:
+                max_sofar = current
+        return max_sofar
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        return sum(1 for ch in s if ch in "aeiou")
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        normalize = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
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
-        def _flatten(item):
-            for elem in item:
-                if isinstance(elem, list):
-                    yield from _flatten(elem)
+        def _flatten(it):
+            for el in it:
+                if isinstance(el, list):
+                    yield from _flatten(el)
                 else:
-                    yield elem
-        nested = args[0]
-        return list(_flatten(nested))
+                    yield el
+        return list(_flatten(args[0]))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (1, 5), scalar 0.9991

parent `23a46010a1a2f2a6` -> candidate `4c1ef043ea25734d`

```diff
--- parent 23a46010a1a2f2a6
+++ candidate 4c1ef043ea25734d
@@ -1,5 +1,6 @@
-    if op == "is_prime":
-        n = args[0]
+    import re
+
+    def _is_prime(n):
         if n < 2:
             return False
         if n % 2 == 0:
@@ -11,42 +12,36 @@
             i += 2
         return True
 
-    elif op == "reverse_string":
-        return args[0][::-1]
+    def _reverse_string(s):
+        return s[::-1]
 
-    elif op == "fibonacci":
-        n = args[0]
+    def _fibonacci(n):
         a, b = 0, 1
         for _ in range(n):
             a, b = b, a + b
         return a
 
-    elif op == "gcd":
-        a, b = args
+    def _gcd(a, b):
         while b:
             a, b = b, a % b
         return a
 
-    elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
-        return s == s[::-1]
+    def _is_palindrome(s):
+        clean = re.sub(r'[^A-Za-z0-9]', '', s).lower()
+        return clean == clean[::-1]
 
-    elif op == "sum_digits":
-        n = args[0]
+    def _sum_digits(n):
         return sum(int(d) for d in str(abs(n)))
 
-    elif op == "factorial":
-        n = args[0]
+    def _factorial(n):
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
-        result = 1
+        res = 1
         for i in range(2, n + 1):
-            result *= i
-        return result
+            res *= i
+        return res
 
-    elif op == "max_subarray_sum":
-        nums = args[0]
+    def _max_subarray_sum(nums):
         if not nums:
             return 0
         best = cur = nums[0]
@@ -55,37 +50,52 @@
             best = max(best, cur)
         return best
 
-    elif op == "count_vowels":
-        s = args[0]
+    def _count_vowels(s):
         return sum(1 for c in s.lower() if c in "aeiou")
 
-    elif op == "is_anagram":
-        a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
-        return normalize(a) == normalize(b)
+    def _is_anagram(a, b):
+        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return norm(a) == norm(b)
 
-    elif op == "binary_search":
-        nums, target = args
-        lo, hi = 0, len(nums) - 1
+    def _binary_search(seq, target):
+        lo, hi = 0, len(seq) - 1
         while lo <= hi:
             mid = (lo + hi) // 2
-            if nums[mid] == target:
+            if seq[mid] == target:
                 return mid
-            if nums[mid] < target:
+            if seq[mid] < target:
                 lo = mid + 1
             else:
                 hi = mid - 1
         return -1
 
-    elif op == "flatten_list":
-        def _flatten(item):
-            for elem in item:
-                if isinstance(elem, list):
-                    yield from _flatten(elem)
-                else:
-                    yield elem
-        nested = args[0]
-        return list(_flatten(nested))
+    def _flatten_list(nested):
+        out = []
+        stack = [nested]
+        while stack:
+            cur = stack.pop()
+            if isinstance(cur, list):
+                stack.extend(reversed(cur))
+            else:
+                out.append(cur)
+        return out
 
-    else:
+    _dispatch = {
+        "is_prime": lambda args: _is_prime(args[0]),
+        "reverse_string": lambda args: _reverse_string(args[0]),
+        "fibonacci": lambda args: _fibonacci(args[0]),
+        "gcd": lambda args: _gcd(*args),
+        "is_palindrome": lambda args: _is_palindrome(args[0]),
+        "sum_digits": lambda args: _sum_digits(args[0]),
+        "factorial": lambda args: _factorial(args[0]),
+        "max_subarray_sum": lambda args: _max_subarray_sum(args[0]),
+        "count_vowels": lambda args: _count_vowels(args[0]),
+        "is_anagram": lambda args: _is_anagram(*args),
+        "binary_search": lambda args: _binary_search(*args),
+        "flatten_list": lambda args: _flatten_list(args[0]),
+    }
+
+    try:
+        return _dispatch[op](args)
+    except KeyError:
         raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (2, 5), scalar 0.9991

parent `47c08d9c76290661` -> candidate `a03d45b9825e99dd`

```diff
--- parent 47c08d9c76290661
+++ candidate a03d45b9825e99dd
@@ -4,12 +4,8 @@
             return False
         if n % 2 == 0:
             return n == 2
-        i = 3
-        while i * i <= n:
-            if n % i == 0:
-                return False
-            i += 2
-        return True
+        limit = int(n ** 0.5) + 1
+        return all(n % d for d in range(3, limit, 2))
 
     elif op == "reverse_string":
         return args[0][::-1]
@@ -22,28 +18,25 @@
         return a
 
     elif op == "gcd":
+        import math
         a, b = args
-        while b:
-            a, b = b, a % b
-        return a
+        return math.gcd(a, b)
 
     elif op == "is_palindrome":
         s = args[0]
-        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        filtered = ''.join(filter(str.isalnum, s)).lower()
         return filtered == filtered[::-1]
 
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
+        return math.prod(range(1, n + 1)) if n else 1
 
     elif op == "max_subarray_sum":
         nums = args[0]
@@ -56,38 +49,32 @@
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        return sum(c in "aeiou" for c in s)
 
     elif op == "is_anagram":
         a, b = args
-        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
-        return normalize(a) == normalize(b)
+        from collections import Counter
+        norm = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
+        return norm(a) == norm(b)
 
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
-        out = []
-        stack = [nested]
-        while stack:
-            current = stack.pop()
-            if isinstance(current, list):
-                stack.extend(reversed(current))
-            else:
-                out.append(current)
-        return out
+
+        def _flatten(item):
+            for elem in item:
+                if isinstance(elem, list):
+                    yield from _flatten(elem)
+                else:
+                    yield elem
+
+        return list(_flatten(nested))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (0, 5), scalar 0.9991

parent `f47ae8e57a90715e` -> candidate `66cba593c0b0aef8`

```diff
--- parent f47ae8e57a90715e
+++ candidate 66cba593c0b0aef8
@@ -2,14 +2,16 @@
         n = args[0]
         if n < 2:
             return False
-        if n % 2 == 0:
-            return n == 2
-        i = 3
-        limit = int(n ** 0.5) + 1
-        while i <= limit:
+        if n in (2, 3):
+            return True
+        if n % 2 == 0 or n % 3 == 0:
+            return False
+        i, step = 5, 2
+        while i * i <= n:
             if n % i == 0:
                 return False
-            i += 2
+            i += step
+            step = 6 - step  # toggle between 2 and 4
         return True
 
     elif op == "reverse_string":
@@ -19,34 +21,39 @@
         n = args[0]
         if n < 0:
             raise ValueError("fibonacci is not defined for negative numbers")
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        def _fib_pair(k):
+            if k == 0:
+                return (0, 1)
+            a, b = _fib_pair(k >> 1)
+            c = a * (2 * b - a)
+            d = a * a + b * b
+            if k & 1:
+                return (d, c + d)
+            return (c, d)
+        return _fib_pair(n)[0]
 
     elif op == "gcd":
+        import math
         a, b = args
-        while b:
-            a, b = b, a % b
-        return abs(a)
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
             raise ValueError("factorial is not defined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        if n == 0:
+            return 1
+        import math
+        return math.prod(range(2, n + 1))
 
     elif op == "max_subarray_sum":
         nums = args[0]
@@ -54,17 +61,18 @@
             return 0
         best = cur = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
+            cur = x if cur < 0 else cur + x
             best = max(best, cur)
         return best
 
     elif op == "count_vowels":
         s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        return sum(c in "aeiou" for c in s.lower())
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        normalize = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
     elif op == "binary_search":
@@ -81,15 +89,20 @@
         return -1
 
     elif op == "flatten_list":
-        def flatten(item):
-            if isinstance(item, list):
-                for sub in item:
-                    yield from flatten(sub)
-            else:
-                yield item
-
+        def _flatten(seq):
+            stack = [iter(seq)]
+            while stack:
+                try:
+                    item = next(stack[-1])
+                except StopIteration:
+                    stack.pop()
+                    continue
+                if isinstance(item, list):
+                    stack.append(iter(item))
+                else:
+                    yield item
         nested = args[0]
-        return list(flatten(nested))
+        return list(_flatten(nested))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (3, 5), scalar 0.9990

parent `3a2baedd645d487d` -> candidate `7244127087b31f1f`

```diff
--- parent 3a2baedd645d487d
+++ candidate 7244127087b31f1f
@@ -2,12 +2,13 @@
         n = args[0]
         if n < 2:
             return False
-        if n == 2:
+        if n in (2, 3):
             return True
         if n % 2 == 0:
             return False
-        limit = int(n ** 0.5) + 1
-        for i in range(3, limit, 2):
+        import math
+        limit = math.isqrt(n)
+        for i in range(3, limit + 1, 2):
             if n % i == 0:
                 return False
         return True
@@ -17,6 +18,8 @@
 
     elif op == "fibonacci":
         n = args[0]
+        if n < 0:
+            raise ValueError("negative index for fibonacci")
         a, b = 0, 1
         for _ in range(n):
             a, b = b, a + b
@@ -24,6 +27,7 @@
 
     elif op == "gcd":
         a, b = args
+        a, b = abs(a), abs(b)
         while b:
             a, b = b, a % b
         return a
@@ -41,10 +45,8 @@
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
@@ -52,7 +54,7 @@
             return 0
         best = cur = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
+            cur = x if cur < 0 else cur + x
             best = max(best, cur)
         return best
 
@@ -62,9 +64,9 @@
 
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
@@ -80,14 +82,19 @@
         return -1
 
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

### Island 3, cell (0, 5), scalar 0.9990

parent `db772eb8f9c682bc` -> candidate `432cf80d03e99ae3`

```diff
--- parent db772eb8f9c682bc
+++ candidate 432cf80d03e99ae3
@@ -4,29 +4,40 @@
             return False
         if n % 2 == 0:
             return n == 2
-        i = 3
+        if n % 3 == 0:
+            return n == 3
+        i = 5
         limit = int(n ** 0.5) + 1
         while i <= limit:
-            if n % i == 0:
+            if n % i == 0 or n % (i + 2) == 0:
                 return False
-            i += 2
+            i += 6
         return True
 
     elif op == "reverse_string":
-        return args[0][::-1]
+        s = args[0]
+        # slice is already optimal, but we keep it explicit for clarity
+        return s[::-1]
 
     elif op == "fibonacci":
         n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+
+        def _fib(k: int):
+            # fast‑doubling method
+            if k == 0:
+                return (0, 1)
+            else:
+                a, b = _fib(k >> 1)
+                c = a * (2 * b - a)
+                d = a * a + b * b
+                return (c, d) if k & 1 == 0 else (d, c + d)
+
+        return _fib(n)[0]
 
     elif op == "gcd":
+        import math
         a, b = args
-        while b:
-            a, b = b, a % b
-        return abs(a)
+        return math.gcd(a, b)
 
     elif op == "is_palindrome":
         import re
@@ -34,64 +45,57 @@
         return s == s[::-1]
 
     elif op == "sum_digits":
-        n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        n = abs(args[0])
+        total = 0
+        while n:
+            total, n = total + n % 10, n // 10
+        return total
 
     elif op == "factorial":
+        import math
         n = args[0]
         if n < 0:
             raise ValueError("factorial undefined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        # math.factorial is highly optimized and handles large n efficiently
+        return math.factorial(n)
 
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
+            best = cur if cur > best else best
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        return sum(c in "aeiou" for c in s)
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        normalize = lambda s: Counter(c.lower() for c in s if not c.isspace())
         return normalize(a) == normalize(b)
 
     elif op == "binary_search":
+        import bisect
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
+        idx = bisect.bisect_left(nums, target)
+        return idx if idx < len(nums) and nums[idx] == target else -1
 
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
+
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+
+        return list(_flatten(nested))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

