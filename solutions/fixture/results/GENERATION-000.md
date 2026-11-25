# Generation 0 — fixture

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 27.8%

## Archive

- Island 0: coverage 8.3%, QD score 2.997, unique ancestors 3
- Island 1: coverage 11.1%, QD score 3.996, unique ancestors 4
- Island 2: coverage 8.3%, QD score 2.997, unique ancestors 3
- Island 3: coverage 11.1%, QD score 3.996, unique ancestors 4
- Cells newly claimed this generation: 33

## Quality

- Best scalar this generation: 0.9991
- Median scalar of newly-claimed: 0.9990

## Cost

- Budget: {'generation': 0, 'max_generations': 5, 'tokens_used_total': 130816, 'max_tokens': 10000000, 'elapsed_s_total': 320.6, 'generation_wall_s': 320.6}
- Candidates proposed: 64
- Parsed: 64 (100.0%)
- Admissible: 64 (100.0%)
- Scored: 64

## Content — newly claimed elites

### Island 0, cell (1, 5), scalar 0.9987

parent `c0bf3a9266582777` -> candidate `9c3b2cf26f0416d2`

```diff
--- parent c0bf3a9266582777
+++ candidate 9c3b2cf26f0416d2
@@ -0,0 +1,96 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n ** 0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("fibonacci index must be non‑negative")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        clean = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return clean(a) == clean(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    _flatten(sub)
+            else:
+                out.append(item)
+        _flatten(nested)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (0, 5), scalar 0.9987

parent `c0bf3a9266582777` -> candidate `67e1d6d8344b7bf4`

```diff
--- parent c0bf3a9266582777
+++ candidate 67e1d6d8344b7bf4
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n ** 0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        a_clean = sorted(c.lower() for c in a if not c.isspace())
+        b_clean = sorted(c.lower() for c in b if not c.isspace())
+        return a_clean == b_clean
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (0, 5), scalar 0.9987

parent `c0bf3a9266582777` -> candidate `cb06b35c1d9ff762`

```diff
--- parent c0bf3a9266582777
+++ candidate cb06b35c1d9ff762
@@ -0,0 +1,92 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n == 2:
+            return True
+        if n % 2 == 0:
+            return False
+        limit = int(n ** 0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        clean = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return clean(a) == clean(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        def _flatten(lst):
+            for item in lst:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (1, 5), scalar 0.9987

parent `c0bf3a9266582777` -> candidate `efcb976dafc4e00a`

```diff
--- parent c0bf3a9266582777
+++ candidate efcb976dafc4e00a
@@ -0,0 +1,92 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        limit = int(n ** 0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(c.lower() for c in s if c.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (2, 5), scalar 0.9988

parent `c0bf3a9266582777` -> candidate `f2dd9c9289cdcde7`

```diff
--- parent c0bf3a9266582777
+++ candidate f2dd9c9289cdcde7
@@ -0,0 +1,92 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n == 2:
+            return True
+        if n % 2 == 0:
+            return False
+        limit = int(n ** 0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (0, 5), scalar 0.9987

parent `c0bf3a9266582777` -> candidate `ded5685a9f8c70e5`

```diff
--- parent c0bf3a9266582777
+++ candidate ded5685a9f8c70e5
@@ -0,0 +1,97 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        limit = int(n**0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        # returns the nth Fibonacci number (0‑indexed)
+        n = args[0]
+        if n < 0:
+            raise ValueError("n must be non‑negative")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        import re
+        s = args[0]
+        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial is not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        import re
+        clean = lambda s: sorted(re.sub(r'\s+', '', s).lower())
+        return clean(a) == clean(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    _flatten(sub)
+            else:
+                out.append(item)
+        _flatten(nested)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (1, 5), scalar 0.9987

parent `c0bf3a9266582777` -> candidate `ba23455a5a1155b2`

```diff
--- parent c0bf3a9266582777
+++ candidate ba23455a5a1155b2
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(ch.lower() for ch in s if ch.isalnum())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    _flatten(sub)
+            else:
+                out.append(item)
+        _flatten(nested)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `23a46010a1a2f2a6`

```diff
--- parent c0bf3a9266582777
+++ candidate 23a46010a1a2f2a6
@@ -0,0 +1,91 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(item):
+            for elem in item:
+                if isinstance(elem, list):
+                    yield from _flatten(elem)
+                else:
+                    yield elem
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (0, 5), scalar 0.9989

parent `c0bf3a9266582777` -> candidate `8d1052ea3922385a`

```diff
--- parent c0bf3a9266582777
+++ candidate 8d1052ea3922385a
@@ -0,0 +1,97 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n ** 0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative values")
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        a_clean = sorted(ch.lower() for ch in a if not ch.isspace())
+        b_clean = sorted(ch.lower() for ch in b if not ch.isspace())
+        return a_clean == b_clean
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    _flatten(sub)
+            else:
+                out.append(item)
+        _flatten(nested)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (1, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `0f57a12b0bf4cbae`

```diff
--- parent c0bf3a9266582777
+++ candidate 0f57a12b0bf4cbae
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        clean = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return clean(a) == clean(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        stack = [nested]
+        while stack:
+            current = stack.pop()
+            if isinstance(current, list):
+                stack.extend(reversed(current))
+            else:
+                out.append(current)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (0, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `fd680af85710627f`

```diff
--- parent c0bf3a9266582777
+++ candidate fd680af85710627f
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        filter_chars = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return filter_chars(a) == filter_chars(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+
+        def _flatten(lst):
+            for item in lst:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `bb9b3ee05a7cb615`

```diff
--- parent c0bf3a9266582777
+++ candidate bb9b3ee05a7cb615
@@ -0,0 +1,94 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("fibonacci is undefined for negative n")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `b092df57c3d9bb5f`

```diff
--- parent c0bf3a9266582777
+++ candidate b092df57c3d9bb5f
@@ -0,0 +1,96 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n == 2:
+            return True
+        if n % 2 == 0:
+            return False
+        limit = int(n**0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("fibonacci index must be non‑negative")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(c.lower() for c in s if c.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        cleanse = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return cleanse(a) == cleanse(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (0, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `3c6d7596f922d7e1`

```diff
--- parent c0bf3a9266582777
+++ candidate 3c6d7596f922d7e1
@@ -0,0 +1,97 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n ** 0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("negative index for fibonacci")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        stack = [nested]
+        while stack:
+            current = stack.pop()
+            if isinstance(current, list):
+                # Extend stack in reverse to preserve order
+                stack.extend(reversed(current))
+            else:
+                out.append(current)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (0, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `47c08d9c76290661`

```diff
--- parent c0bf3a9266582777
+++ candidate 47c08d9c76290661
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        stack = [nested]
+        while stack:
+            current = stack.pop()
+            if isinstance(current, list):
+                stack.extend(reversed(current))
+            else:
+                out.append(current)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (1, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `6231b0902dc80247`

```diff
--- parent c0bf3a9266582777
+++ candidate 6231b0902dc80247
@@ -0,0 +1,92 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n == 2:
+            return True
+        if n % 2 == 0:
+            return False
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return norm(a) == norm(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(lst):
+            for item in lst:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+        return list(_flatten(args[0]))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (2, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `cf751ef6d88ddcca`

```diff
--- parent c0bf3a9266582777
+++ candidate cf751ef6d88ddcca
@@ -0,0 +1,94 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial is undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        clean_a = sorted(ch.lower() for ch in a if not ch.isspace())
+        clean_b = sorted(ch.lower() for ch in b if not ch.isspace())
+        return clean_a == clean_b
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+
+        def _flatten(item):
+            for elem in item:
+                if isinstance(elem, list):
+                    yield from _flatten(elem)
+                else:
+                    yield elem
+
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (3, 5), scalar 0.9989

parent `c0bf3a9266582777` -> candidate `f4aa352c6727f289`

```diff
--- parent c0bf3a9266582777
+++ candidate f4aa352c6727f289
@@ -0,0 +1,95 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        limit = int(n ** 0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(c.lower() for c in s if c.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial() not defined for negative values")
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        norm_a = sorted(c.lower() for c in a if not c.isspace())
+        norm_b = sorted(c.lower() for c in b if not c.isspace())
+        return norm_a == norm_b
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+
+        def _flatten(item):
+            for elem in item:
+                if isinstance(elem, list):
+                    yield from _flatten(elem)
+                else:
+                    yield elem
+
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (3, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `6ea99e6e5e7b3429`

```diff
--- parent c0bf3a9266582777
+++ candidate 6ea99e6e5e7b3429
@@ -0,0 +1,96 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        stack = [iter(nested)]
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
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (1, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `d518653a2ee83199`

```diff
--- parent c0bf3a9266582777
+++ candidate d518653a2ee83199
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^a-z0-9]', '', args[0].lower())
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        norm = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return norm(a) == norm(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (2, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `3a2baedd645d487d`

```diff
--- parent c0bf3a9266582777
+++ candidate 3a2baedd645d487d
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n == 2:
+            return True
+        if n % 2 == 0:
+            return False
+        limit = int(n ** 0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        a_clean = sorted(c.lower() for c in a if not c.isspace())
+        b_clean = sorted(c.lower() for c in b if not c.isspace())
+        return a_clean == b_clean
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (0, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `b8d990e960a9f56b`

```diff
--- parent c0bf3a9266582777
+++ candidate b8d990e960a9f56b
@@ -0,0 +1,94 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("negative index for fibonacci")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("negative factorial")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        def normalize(s):
+            return sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(seq):
+            for item in seq:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (1, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `f47ae8e57a90715e`

```diff
--- parent c0bf3a9266582777
+++ candidate f47ae8e57a90715e
@@ -0,0 +1,95 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n ** 0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("fibonacci is not defined for negative numbers")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial is not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from flatten(sub)
+            else:
+                yield item
+
+        nested = args[0]
+        return list(flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `8622c0fe987e363a`

```diff
--- parent c0bf3a9266582777
+++ candidate 8622c0fe987e363a
@@ -0,0 +1,91 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        norm = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return norm(a) == norm(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        def _flatten(lst):
+            for item in lst:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (1, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `6f594d28893edeb4`

```diff
--- parent c0bf3a9266582777
+++ candidate 6f594d28893edeb4
@@ -0,0 +1,95 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n**0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        clean = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return clean(a) == clean(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        stack = [nested]
+        while stack:
+            current = stack.pop()
+            if isinstance(current, list):
+                # extend stack in reverse to preserve order
+                stack.extend(reversed(current))
+            else:
+                out.append(current)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (0, 5), scalar 0.9989

parent `c0bf3a9266582777` -> candidate `85022d25a4b9bf8d`

```diff
--- parent c0bf3a9266582777
+++ candidate 85022d25a4b9bf8d
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        limit = int(n ** 0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        # returns the nth Fibonacci number (0-indexed)
+        n = args[0]
+        if n < 0:
+            raise ValueError("n must be non‑negative")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^a-z0-9]', '', args[0].lower())
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (3, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `db772eb8f9c682bc`

```diff
--- parent c0bf3a9266582777
+++ candidate db772eb8f9c682bc
@@ -0,0 +1,97 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n ** 0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        stack = [iter(nested)]
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
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (1, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `65de6e5f0e6363e6`

```diff
--- parent c0bf3a9266582777
+++ candidate 65de6e5f0e6363e6
@@ -0,0 +1,94 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n ** 0.5) + 1
+        while i < limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[\W_]+', '', args[0]).lower()
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(item):
+            if isinstance(item, list):
+                result = []
+                for sub in item:
+                    result.extend(_flatten(sub))
+                return result
+            else:
+                return [item]
+        nested = args[0]
+        return _flatten(nested)
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `e85212edac727387`

```diff
--- parent c0bf3a9266582777
+++ candidate e85212edac727387
@@ -0,0 +1,97 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        limit = int(n**0.5) + 1
+        while i <= limit:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        clean_a = sorted(ch.lower() for ch in a if not ch.isspace())
+        clean_b = sorted(ch.lower() for ch in b if not ch.isspace())
+        return clean_a == clean_b
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    _flatten(sub)
+            else:
+                out.append(item)
+
+        _flatten(nested)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (0, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `7407ab7bbf9d96b6`

```diff
--- parent c0bf3a9266582777
+++ candidate 7407ab7bbf9d96b6
@@ -0,0 +1,95 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[^a-z0-9]', '', args[0].lower())
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(s.replace(" ", "").lower())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    _flatten(sub)
+            else:
+                out.append(item)
+
+        _flatten(nested)
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `6ab2b6b35eafe54b`

```diff
--- parent c0bf3a9266582777
+++ candidate 6ab2b6b35eafe54b
@@ -0,0 +1,99 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("n must be non‑negative")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        import re
+        s = re.sub(r'[\W_]', '', args[0]).lower()
+        return s == s[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial undefined for negative integers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        a_clean = sorted(c.lower() for c in a if not c.isspace())
+        b_clean = sorted(c.lower() for c in b if not c.isspace())
+        return a_clean == b_clean
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        out = []
+        stack = [iter(nested)]
+        while stack:
+            for item in stack[-1]:
+                if isinstance(item, list):
+                    stack.append(iter(item))
+                    break
+                else:
+                    out.append(item)
+            else:
+                stack.pop()
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (1, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `3c9d0b198e7509df`

```diff
--- parent c0bf3a9266582777
+++ candidate 3c9d0b198e7509df
@@ -0,0 +1,94 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n % 2 == 0:
+            return n == 2
+        i = 3
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 2
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        if n < 0:
+            raise ValueError("negative index not allowed")
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return abs(a)
+
+    elif op == "is_palindrome":
+        import re
+        s = args[0]
+        cleaned = re.sub(r'[\W_]', '', s).lower()
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        def _flatten(lst):
+            for item in lst:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+        nested = args[0]
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (1, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `8376bf500f1a3f75`

```diff
--- parent c0bf3a9266582777
+++ candidate 8376bf500f1a3f75
@@ -0,0 +1,93 @@
+    if op == "is_prime":
+        n = args[0]
+        if n < 2:
+            return False
+        if n == 2:
+            return True
+        if n % 2 == 0:
+            return False
+        limit = int(n ** 0.5) + 1
+        for i in range(3, limit, 2):
+            if n % i == 0:
+                return False
+        return True
+
+    elif op == "reverse_string":
+        return args[0][::-1]
+
+    elif op == "fibonacci":
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    elif op == "gcd":
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    elif op == "is_palindrome":
+        s = args[0]
+        cleaned = ''.join(c.lower() for c in s if c.isalnum())
+        return cleaned == cleaned[::-1]
+
+    elif op == "sum_digits":
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    elif op == "factorial":
+        n = args[0]
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    elif op == "max_subarray_sum":
+        nums = args[0]
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    elif op == "count_vowels":
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    elif op == "is_anagram":
+        a, b = args
+        def normalize(s):
+            return sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    elif op == "binary_search":
+        nums, target = args
+        lo, hi = 0, len(nums) - 1
+        while lo <= hi:
+            mid = (lo + hi) // 2
+            if nums[mid] == target:
+                return mid
+            if nums[mid] < target:
+                lo = mid + 1
+            else:
+                hi = mid - 1
+        return -1
+
+    elif op == "flatten_list":
+        nested = args[0]
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        return list(_flatten(nested))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

