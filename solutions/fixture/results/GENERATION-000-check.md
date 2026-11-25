# Generation 0 — fixture

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 4.6%
- Aggregate throughput: 220.7 tok/s (31137 completion tokens / 141.1s)

## Archive

- Island 0: coverage 2.8%, QD score 0.998, unique ancestors 1
- Island 1: coverage 2.8%, QD score 0.999, unique ancestors 1
- Island 2: coverage 2.8%, QD score 0.999, unique ancestors 1
- Island 3: coverage 2.8%, QD score 0.999, unique ancestors 1
- Cells newly claimed this generation: 13

## Quality

- Best scalar this generation: 0.9991
- Median scalar of newly-claimed: 0.9990

## Cost

- Budget: {'generation': 0, 'max_generations': 1, 'tokens_used_total': 63521, 'max_tokens': 20000000, 'elapsed_s_total': 141.1, 'generation_wall_s': 141.1}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (2, 5), scalar 0.9984

parent `c0bf3a9266582777` -> candidate `c58a201847eb60ad`

```diff
--- parent c0bf3a9266582777
+++ candidate c58a201847eb60ad
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
+        if n <= 1:
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

### Island 0, cell (2, 5), scalar 0.9985

parent `c0bf3a9266582777` -> candidate `1ec073bcd916024f`

```diff
--- parent c0bf3a9266582777
+++ candidate 1ec073bcd916024f
@@ -0,0 +1,92 @@
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

### Island 1, cell (2, 5), scalar 0.9991

parent `c0bf3a9266582777` -> candidate `e520dc07cfd199ff`

```diff
--- parent c0bf3a9266582777
+++ candidate e520dc07cfd199ff
@@ -0,0 +1,93 @@
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

### Island 2, cell (2, 5), scalar 0.9989

parent `c0bf3a9266582777` -> candidate `5a3eefd514f2e8b0`

```diff
--- parent c0bf3a9266582777
+++ candidate 5a3eefd514f2e8b0
@@ -0,0 +1,98 @@
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
+        # returns the nth Fibonacci number (0-indexed)
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
+        # ignore case, spaces, and punctuation
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

### Island 2, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `688b3c71eb1efe5b`

```diff
--- parent c0bf3a9266582777
+++ candidate 688b3c71eb1efe5b
@@ -0,0 +1,96 @@
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
+        norm = lambda s: sorted(c.lower() for c in s if c != ' ')
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

### Island 2, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `c4a8204bd3c705c3`

```diff
--- parent c0bf3a9266582777
+++ candidate c4a8204bd3c705c3
@@ -0,0 +1,94 @@
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
+        # returns the n-th Fibonacci number (0-indexed)
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

### Island 2, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `8a596ac331aba7d7`

```diff
--- parent c0bf3a9266582777
+++ candidate 8a596ac331aba7d7
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
+        import re
+
+        s = re.sub(r'[\W_]+', '', args[0]).lower()
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

### Island 2, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `b3453d0d1ccaf963`

```diff
--- parent c0bf3a9266582777
+++ candidate b3453d0d1ccaf963
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
+        if n < 0:
+            raise ValueError("fibonacci undefined for negative n")
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
+        def _flatten(item):
+            if isinstance(item, list):
+                for sub in item:
+                    yield from _flatten(sub)
+            else:
+                yield item
+        return list(_flatten(args[0]))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9989

parent `c0bf3a9266582777` -> candidate `906c4a52b25e4b6e`

```diff
--- parent c0bf3a9266582777
+++ candidate 906c4a52b25e4b6e
@@ -0,0 +1,99 @@
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
+        import re
+        s = args[0]
+        cleaned = re.sub(r'[\W_]+', '', s).lower()
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

### Island 3, cell (2, 5), scalar 0.9989

parent `c0bf3a9266582777` -> candidate `855e008cc6d73a70`

```diff
--- parent c0bf3a9266582777
+++ candidate 855e008cc6d73a70
@@ -0,0 +1,89 @@
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
+        return abs(a)
+
+    elif op == "is_palindrome":
+        s = ''.join(ch.lower() for ch in args[0] if ch.isalnum())
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
+        norm = lambda t: sorted(ch.lower() for ch in t if not ch.isspace())
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
+        def _flatten(x):
+            for item in x:
+                if isinstance(item, list):
+                    yield from _flatten(item)
+                else:
+                    yield item
+        return list(_flatten(args[0]))
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9989

parent `c0bf3a9266582777` -> candidate `22f95f96644dd046`

```diff
--- parent c0bf3a9266582777
+++ candidate 22f95f96644dd046
@@ -0,0 +1,97 @@
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

### Island 3, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `3aadb045b14530c7`

```diff
--- parent c0bf3a9266582777
+++ candidate 3aadb045b14530c7
@@ -0,0 +1,101 @@
+    # Define helper functions for each operation
+    def _is_prime(n):
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
+    def _reverse_string(s):
+        return s[::-1]
+
+    def _fibonacci(n):
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    def _gcd(a, b):
+        while b:
+            a, b = b, a % b
+        return a
+
+    def _is_palindrome(s):
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
+
+    def _sum_digits(n):
+        return sum(int(d) for d in str(abs(n)))
+
+    def _factorial(n):
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    def _max_subarray_sum(nums):
+        if not nums:
+            return 0
+        best = cur = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    def _count_vowels(s):
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    def _is_anagram(a, b):
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
+        return normalize(a) == normalize(b)
+
+    def _binary_search(nums, target):
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
+    def _flatten_list(nested):
+        out = []
+        stack = [nested]
+        while stack:
+            item = stack.pop()
+            if isinstance(item, list):
+                stack.extend(reversed(item))
+            else:
+                out.append(item)
+        out.reverse()
+        return out
+
+    # Dispatch table linking operation names to their handlers
+    _ops = {
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
+    if op not in _ops:
+        raise ValueError(f"unknown op: {op}")
+    return _ops[op]()
```

### Island 3, cell (2, 5), scalar 0.9990

parent `c0bf3a9266582777` -> candidate `78f595977aad636e`

```diff
--- parent c0bf3a9266582777
+++ candidate 78f595977aad636e
@@ -0,0 +1,93 @@
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
+        # returns the nth Fibonacci number (0-indexed)
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
+            raise ValueError("factorial not defined for negative values")
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


## Held-out check (best-ever candidate)

- Candidate: `e520dc07cfd199ff` (rotation scalar 0.9991)
- Held-out quality: 1.0000 (passes: 1.0000, 1.0000)
- Held-out scalar: 0.9991 (passes: 0.9991, 0.9991)
- All held-out tasks valid: True
