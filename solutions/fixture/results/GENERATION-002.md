# Generation 2 — fixture

## Throughput

- Peak queue depth: 33
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 34.0%

## Archive

- Island 0: coverage 11.1%, QD score 3.996, unique ancestors 1
- Island 1: coverage 11.1%, QD score 3.996, unique ancestors 3
- Island 2: coverage 11.1%, QD score 3.996, unique ancestors 1
- Island 3: coverage 11.1%, QD score 3.996, unique ancestors 3
- Cells newly claimed this generation: 8

## Quality

- Best scalar this generation: 0.9991
- Median scalar of newly-claimed: 0.9991

## Cost

- Budget: {'generation': 2, 'max_generations': 5, 'tokens_used_total': 596495, 'max_tokens': 10000000, 'elapsed_s_total': 1331.4, 'generation_wall_s': 478.6}
- Candidates proposed: 64
- Parsed: 62 (96.9%)
- Admissible: 62 (96.9%)
- Scored: 62

## Content — newly claimed elites

### Island 0, cell (0, 5), scalar 0.9991

parent `d534d5cb63b2ef75` -> candidate `d281ea43cd4a7030`

```diff
--- parent d534d5cb63b2ef75
+++ candidate d281ea43cd4a7030
@@ -2,30 +2,33 @@
         n = args[0]
         if n < 2:
             return False
-        if n % 2 == 0:
-            return n == 2
-        if n % 3 == 0:
-            return n == 3
+        if n in (2, 3):
+            return True
+        if n % 2 == 0 or n % 3 == 0:
+            return False
         i = 5
-        step = 2
         while i * i <= n:
-            if n % i == 0:
+            if n % i == 0 or n % (i + 2) == 0:
                 return False
-            i += step
-            step = 6 - step
+            i += 6
         return True
 
     elif op == "reverse_string":
-        return ''.join(reversed(args[0]))
+        s = args[0]
+        return s[::-1]
 
     elif op == "fibonacci":
         n = args[0]
-        from functools import reduce
-        return reduce(lambda t, _: (t[1], t[0] + t[1]), range(n), (0, 1))[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
 
     elif op == "gcd":
-        import math
-        return math.gcd(*args)
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
 
     elif op == "is_palindrome":
         s = args[0]
@@ -33,52 +36,67 @@
         return cleaned == cleaned[::-1]
 
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
             raise ValueError("factorial not defined for negative numbers")
-        import math
-        return math.prod(range(1, n + 1)) if n else 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        from itertools import accumulate
-        max_sofar = current = nums[0]
-        for val in accumulate(nums[1:], lambda acc, x: max(x, acc + x)):
-            current = val
-            if current > max_sofar:
-                max_sofar = current
+        max_ending = max_sofar = nums[0]
+        for x in nums[1:]:
+            max_ending = x if max_ending < 0 else max_ending + x
+            if max_ending > max_sofar:
+                max_sofar = max_ending
         return max_sofar
 
     elif op == "count_vowels":
         s = args[0].lower()
-        return sum(1 for ch in s if ch in "aeiou")
+        vowels = set("aeiou")
+        return sum(1 for ch in s if ch in vowels)
 
     elif op == "is_anagram":
-        from collections import Counter
         a, b = args
-        normalize = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
     elif op == "binary_search":
         nums, target = args
-        import bisect
-        i = bisect.bisect_left(nums, target)
-        return i if i < len(nums) and nums[i] == target else -1
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
-        def _flatten(it):
-            for el in it:
-                if isinstance(el, list):
-                    yield from _flatten(el)
-                else:
-                    yield el
-        return list(_flatten(args[0]))
+        stack = [args[0]]
+        result = []
+        while stack:
+            cur = stack.pop()
+            if isinstance(cur, list):
+                stack.extend(reversed(cur))
+            else:
+                result.append(cur)
+        result.reverse()
+        return result
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (0, 5), scalar 0.9991

parent `4c1ef043ea25734d` -> candidate `c20fdab3f8eb3f39`

```diff
--- parent 4c1ef043ea25734d
+++ candidate c20fdab3f8eb3f39
@@ -1,101 +1,85 @@
     import re
+    import math
+    import collections
+    import bisect
 
-    def _is_prime(n):
-        if n < 2:
-            return False
-        if n % 2 == 0:
-            return n == 2
-        i = 3
-        while i * i <= n:
-            if n % i == 0:
+    match op:
+        case "is_prime":
+            n = args[0]
+            if n < 2:
                 return False
-            i += 2
-        return True
+            if n % 2 == 0:
+                return n == 2
+            if n % 3 == 0:
+                return n == 3
+            i, step = 5, 2
+            while i * i <= n:
+                if n % i == 0:
+                    return False
+                i += step
+                step = 6 - step
+            return True
 
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
+            n = args[0]
+            return sum(map(int, str(abs(n))))
 
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
+            s = args[0].lower()
+            return sum(1 for ch in s if ch in {"a", "e", "i", "o", "u"})
 
-    def _is_anagram(a, b):
-        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
-        return norm(a) == norm(b)
+        case "is_anagram":
+            a, b = args
+            norm = lambda s: collections.Counter(ch.lower() for ch in s if not ch.isspace())
+            return norm(a) == norm(b)
 
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

### Island 1, cell (0, 5), scalar 0.9991

parent `a03d45b9825e99dd` -> candidate `e9bec38fdb930549`

```diff
--- parent a03d45b9825e99dd
+++ candidate e9bec38fdb930549
@@ -2,79 +2,102 @@
         n = args[0]
         if n < 2:
             return False
-        if n % 2 == 0:
-            return n == 2
-        limit = int(n ** 0.5) + 1
-        return all(n % d for d in range(3, limit, 2))
+        if n in (2, 3):
+            return True
+        if n % 2 == 0 or n % 3 == 0:
+            return False
+        i = 5
+        w = 2
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += w
+            w = 6 - w
+        return True
 
     elif op == "reverse_string":
-        return args[0][::-1]
+        s = args[0]
+        rev = []
+        for ch in s:
+            rev.append(ch)
+        return ''.join(reversed(rev))
 
     elif op == "fibonacci":
         n = args[0]
         a, b = 0, 1
-        for _ in range(n):
+        while n:
             a, b = b, a + b
+            n -= 1
         return a
 
     elif op == "gcd":
-        import math
         a, b = args
-        return math.gcd(a, b)
+        while b:
+            a, b = b, a % b
+        return abs(a)
 
     elif op == "is_palindrome":
         s = args[0]
-        filtered = ''.join(filter(str.isalnum, s)).lower()
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
         return filtered == filtered[::-1]
 
     elif op == "sum_digits":
         n = args[0]
-        return sum(map(int, str(abs(n))))
+        return sum(int(d) for d in str(abs(n)))
 
     elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial undefined for negative numbers")
-        import math
-        return math.prod(range(1, n + 1)) if n else 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
 
     elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
-        best = cur = nums[0]
+        max_ending = max_sofar = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
-        return best
+            max_ending = x if max_ending < 0 else max_ending + x
+            if max_ending > max_sofar:
+                max_sofar = max_ending
+        return max_sofar
 
     elif op == "count_vowels":
         s = args[0].lower()
-        return sum(c in "aeiou" for c in s)
+        return sum(1 for ch in s if ch in "aeiou")
 
     elif op == "is_anagram":
         a, b = args
-        from collections import Counter
-        norm = lambda s: Counter(ch.lower() for ch in s if not ch.isspace())
-        return norm(a) == norm(b)
+        normalize = lambda txt: sorted(ch.lower() for ch in txt if not ch.isspace())
+        return normalize(a) == normalize(b)
 
     elif op == "binary_search":
         nums, target = args
-        import bisect
-        i = bisect.bisect_left(nums, target)
-        return i if i < len(nums) and nums[i] == target else -1
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
         nested = args[0]
-
-        def _flatten(item):
-            for elem in item:
-                if isinstance(elem, list):
-                    yield from _flatten(elem)
-                else:
-                    yield elem
-
-        return list(_flatten(nested))
+        stack = [nested]
+        flat = []
+        while stack:
+            current = stack.pop()
+            if isinstance(current, list):
+                stack.extend(reversed(current))
+            else:
+                flat.append(current)
+        return flat
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (2, 5), scalar 0.9991

parent `47c08d9c76290661` -> candidate `cfdbebfdaa48cff3`

```diff
--- parent 47c08d9c76290661
+++ candidate cfdbebfdaa48cff3
@@ -1,18 +1,27 @@
+    # Imports needed for alternative implementations
+    from math import gcd as _gcd, prod as _prod, isqrt
+    from collections import Counter
+    from bisect import bisect_left
+
     if op == "is_prime":
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
+        w = 2
         while i * i <= n:
             if n % i == 0:
                 return False
-            i += 2
+            i += w
+            w = 6 - w  # alternate between checking 6k-1 and 6k+1
         return True
 
     elif op == "reverse_string":
-        return args[0][::-1]
+        return ''.join(reversed(args[0]))
 
     elif op == "fibonacci":
         n = args[0]
@@ -23,9 +32,7 @@
 
     elif op == "gcd":
         a, b = args
-        while b:
-            a, b = b, a % b
-        return a
+        return _gcd(a, b)
 
     elif op == "is_palindrome":
         s = args[0]
@@ -34,60 +41,46 @@
 
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
+        return 1 if n == 0 else _prod(range(1, n + 1))
 
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
         a, b = args
-        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
-        return normalize(a) == normalize(b)
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
+        idx = bisect_left(nums, target)
+        return idx if idx < len(nums) and nums[idx] == target else -1
 
     elif op == "flatten_list":
-        nested = args[0]
-        out = []
-        stack = [nested]
-        while stack:
-            current = stack.pop()
-            if isinstance(current, list):
-                stack.extend(reversed(current))
-            else:
-                out.append(current)
-        return out
+        def _flatten(seq):
+            for item in seq:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+        return list(_flatten(args[0]))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (0, 5), scalar 0.9991

parent `47c08d9c76290661` -> candidate `3d8fceed105874f9`

```diff
--- parent 47c08d9c76290661
+++ candidate 3d8fceed105874f9
@@ -1,52 +1,40 @@
-    if op == "is_prime":
-        n = args[0]
+    import math
+    import bisect
+    import collections
+
+    def _is_prime(n):
         if n < 2:
             return False
         if n % 2 == 0:
             return n == 2
-        i = 3
-        while i * i <= n:
-            if n % i == 0:
-                return False
-            i += 2
-        return True
+        limit = math.isqrt(n)
+        return all(n % p for p in range(3, limit + 1, 2))
 
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
-        while b:
-            a, b = b, a % b
-        return a
+    def _gcd(a, b):
+        return math.gcd(a, b)
 
-    elif op == "is_palindrome":
-        s = args[0]
+    def _is_palindrome(s):
         filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
         return filtered == filtered[::-1]
 
-    elif op == "sum_digits":
-        n = args[0]
+    def _sum_digits(n):
         return sum(int(d) for d in str(abs(n)))
 
-    elif op == "factorial":
-        n = args[0]
+    def _factorial(n):
         if n < 0:
             raise ValueError("factorial undefined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        return math.prod(range(1, n + 1)) if n else 1
 
-    elif op == "max_subarray_sum":
-        nums = args[0]
+    def _max_subarray_sum(nums):
         if not nums:
             return 0
         best = cur = nums[0]
@@ -55,39 +43,45 @@
             best = max(best, cur)
         return best
 
-    elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+    def _count_vowels(s):
+        vowels = set("aeiou")
+        return sum(ch in vowels for ch in s.lower())
 
-    elif op == "is_anagram":
-        a, b = args
-        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
-        return normalize(a) == normalize(b)
+    def _is_anagram(a, b):
+        norm = lambda s: collections.Counter(ch.lower() for ch in s if not ch.isspace())
+        return norm(a) == norm(b)
 
-    elif op == "binary_search":
-        nums, target = args
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
+    def _binary_search(nums, target):
+        i = bisect.bisect_left(nums, target)
+        return i if i < len(nums) and nums[i] == target else -1
 
-    elif op == "flatten_list":
-        nested = args[0]
-        out = []
-        stack = [nested]
-        while stack:
-            current = stack.pop()
-            if isinstance(current, list):
-                stack.extend(reversed(current))
-            else:
-                out.append(current)
-        return out
+    def _flatten_list(nested):
+        def _gen(item):
+            for elem in item:
+                if isinstance(elem, list):
+                    yield from _gen(elem)
+                else:
+                    yield elem
+        return list(_gen(nested))
 
-    else:
-        raise ValueError(f"unknown op: {op}")+    _dispatch = {
+        "is_prime": lambda *a: _is_prime(a[0]),
+        "reverse_string": lambda *a: _reverse_string(a[0]),
+        "fibonacci": lambda *a: _fibonacci(a[0]),
+        "gcd": lambda *a: _gcd(a[0], a[1]),
+        "is_palindrome": lambda *a: _is_palindrome(a[0]),
+        "sum_digits": lambda *a: _sum_digits(a[0]),
+        "factorial": lambda *a: _factorial(a[0]),
+        "max_subarray_sum": lambda *a: _max_subarray_sum(a[0]),
+        "count_vowels": lambda *a: _count_vowels(a[0]),
+        "is_anagram": lambda *a: _is_anagram(a[0], a[1]),
+        "binary_search": lambda *a: _binary_search(a[0], a[1]),
+        "flatten_list": lambda *a: _flatten_list(a[0]),
+    }
+
+    try:
+        func = _dispatch[op]
+    except KeyError:
+        raise ValueError(f"unknown op: {op}")
+
+    return func(*args)
```

### Island 2, cell (0, 5), scalar 0.9991

parent `7244127087b31f1f` -> candidate `8e3fe9c23d278ea7`

```diff
--- parent 7244127087b31f1f
+++ candidate 8e3fe9c23d278ea7
@@ -2,15 +2,17 @@
         n = args[0]
         if n < 2:
             return False
-        if n in (2, 3):
-            return True
         if n % 2 == 0:
-            return False
-        import math
-        limit = math.isqrt(n)
-        for i in range(3, limit + 1, 2):
+            return n == 2
+        if n % 3 == 0:
+            return n == 3
+        i, step = 5, 2
+        limit = int(n ** 0.5)
+        while i <= limit:
             if n % i == 0:
                 return False
+            i += step
+            step = 6 - step  # toggle between 2 and 4
         return True
 
     elif op == "reverse_string":
@@ -20,33 +22,35 @@
         n = args[0]
         if n < 0:
             raise ValueError("negative index for fibonacci")
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        def _fib(k):
+            if k == 0:
+                return (0, 1)
+            a, b = _fib(k >> 1)
+            c = a * (2 * b - a)
+            d = a * a + b * b
+            return (d, c + d) if k & 1 else (c, d)
+        return _fib(n)[0]
 
     elif op == "gcd":
+        import math
         a, b = args
-        a, b = abs(a), abs(b)
-        while b:
-            a, b = b, a % b
-        return a
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
         import math
-        return math.prod(range(1, n + 1)) if n > 0 else 1
+        return math.factorial(n)
 
     elif op == "max_subarray_sum":
         nums = args[0]
@@ -54,13 +58,14 @@
             return 0
         best = cur = nums[0]
         for x in nums[1:]:
-            cur = x if cur < 0 else cur + x
+            cur = max(x, cur + x)
             best = max(best, cur)
         return best
 
     elif op == "count_vowels":
         s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        vowels = set("aeiou")
+        return sum(ch in vowels for ch in s.lower())
 
     elif op == "is_anagram":
         a, b = args
@@ -82,19 +87,13 @@
         return -1
 
     elif op == "flatten_list":
-        nested = args[0]
-        stack = [iter([nested])]
-        result = []
-        while stack:
-            try:
-                item = next(stack[-1])
+        def _flatten(seq):
+            for item in seq:
                 if isinstance(item, list):
-                    stack.append(iter(item))
+                    yield from _flatten(item)
                 else:
-                    result.append(item)
-            except StopIteration:
-                stack.pop()
-        return result
+                    yield item
+        return list(_flatten(args[0]))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (1, 5), scalar 0.9990

parent `3a2baedd645d487d` -> candidate `b4141d84a4fd3d48`

```diff
--- parent 3a2baedd645d487d
+++ candidate b4141d84a4fd3d48
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
+            raise ValueError("fibonacci is not defined for negative numbers")
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
 
@@ -61,10 +63,10 @@
         return sum(1 for c in s.lower() if c in "aeiou")
 
     elif op == "is_anagram":
+        from collections import Counter
         a, b = args
-        a_clean = sorted(c.lower() for c in a if not c.isspace())
-        b_clean = sorted(c.lower() for c in b if not c.isspace())
-        return a_clean == b_clean
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

### Island 3, cell (0, 5), scalar 0.9991

parent `db772eb8f9c682bc` -> candidate `2e32195558cd1b7b`

```diff
--- parent db772eb8f9c682bc
+++ candidate 2e32195558cd1b7b
@@ -2,14 +2,21 @@
         n = args[0]
         if n < 2:
             return False
-        if n % 2 == 0:
-            return n == 2
-        i = 3
-        limit = int(n ** 0.5) + 1
+        # quick checks for small primes and even numbers
+        small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
+        if n in small_primes:
+            return True
+        for p in small_primes:
+            if n % p == 0:
+                return False
+        # 6k ± 1 trial division up to sqrt(n)
+        import math
+        limit = math.isqrt(n)
+        i = 5
         while i <= limit:
-            if n % i == 0:
+            if n % i == 0 or n % (i + 2) == 0:
                 return False
-            i += 2
+            i += 6
         return True
 
     elif op == "reverse_string":
@@ -17,81 +24,83 @@
 
     elif op == "fibonacci":
         n = args[0]
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        if n < 0:
+            raise ValueError("n must be non‑negative")
+        def _fib_pair(k):
+            if k == 0:
+                return (0, 1)
+            a, b = _fib_pair(k >> 1)
+            c = a * (2 * b - a)
+            d = a * a + b * b
+            if k & 1:
+                return (d, c + d)
+            else:
+                return (c, d)
+        return _fib_pair(n)[0]
 
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
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
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
+        if n == 0:
+            return 1
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
+        cur, best = functools.reduce(_step, nums[1:], (nums[0], nums[0]))
         return best
 
     elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        s = args[0].lower()
+        vowels = set("aeiou")
+        return sum(1 for ch in s if ch in vowels)
 
     elif op == "is_anagram":
         a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
-        return normalize(a) == normalize(b)
+        from collections import Counter
+        def _norm(s):
+            return Counter(ch.lower() for ch in s if not ch.isspace())
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
-        out = []
-        stack = [iter(nested)]
-        while stack:
-            try:
-                item = next(stack[-1])
-                if isinstance(item, list):
-                    stack.append(iter(item))
+        def _flatten(item):
+            for elem in item:
+                if isinstance(elem, list):
+                    yield from _flatten(elem)
                 else:
-                    out.append(item)
-            except StopIteration:
-                stack.pop()
-        return out
+                    yield elem
+        return list(_flatten(nested))
 
     else:
         raise ValueError(f"unknown op: {op}")
```

