# Generation 0 — fixture

## Throughput

- Peak queue depth: 8
- Sustained (median) queue depth: 8
- Prefix cache hit rate: 89.0%

## Archive

- Island 0: coverage 5.6%, QD score 1.997, unique ancestors 1
- Island 1: coverage 5.6%, QD score 1.997, unique ancestors 1
- Island 2: coverage 5.6%, QD score 1.997, unique ancestors 1
- Island 3: coverage 5.6%, QD score 1.997, unique ancestors 1
- Cells newly claimed this generation: 8

## Quality

- Best scalar this generation: 0.9987
- Median scalar of newly-claimed: 0.9986

## Cost

- Budget: {'generation': 0, 'max_generations': 3, 'tokens_used_total': 17159, 'max_tokens': 10000000, 'elapsed_s_total': 101.5, 'generation_wall_s': 101.5}
- Candidates proposed: 8
- Parsed: 8 (100.0%)
- Admissible: 8 (100.0%)
- Scored: 8

## Content — newly claimed elites

### Island 0, cell (0, 5), scalar 0.9985

parent `126dcfeaef41ee17` -> candidate `674827e87e98b92d`

```diff
--- parent 126dcfeaef41ee17
+++ candidate 674827e87e98b92d
@@ -0,0 +1,101 @@
+    # Helper implementations
+    def _is_prime(n):
+        if n < 2:
+            return False
+        i = 2
+        while i * i <= n:
+            if n % i == 0:
+                return False
+            i += 1
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
+        if n == 0:
+            return 1
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    def _max_subarray_sum(nums):
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
+        a_clean = sorted(ch.lower() for ch in a if not ch.isspace())
+        b_clean = sorted(ch.lower() for ch in b if not ch.isspace())
+        return a_clean == b_clean
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
+    # Dispatch table
+    _dispatch = {
+        "is_prime": lambda a: _is_prime(a[0]),
+        "reverse_string": lambda a: _reverse_string(a[0]),
+        "fibonacci": lambda a: _fibonacci(a[0]),
+        "gcd": lambda a: _gcd(*a),
+        "is_palindrome": lambda a: _is_palindrome(a[0]),
+        "sum_digits": lambda a: _sum_digits(a[0]),
+        "factorial": lambda a: _factorial(a[0]),
+        "max_subarray_sum": lambda a: _max_subarray_sum(a[0]),
+        "count_vowels": lambda a: _count_vowels(a[0]),
+        "is_anagram": lambda a: _is_anagram(*a),
+        "binary_search": lambda a: _binary_search(*a),
+        "flatten_list": lambda a: _flatten_list(a[0]),
+    }
+
+    try:
+        return _dispatch[op](args)
+    except KeyError:
+        raise ValueError(f"unknown op: {op}")
```

### Island 0, cell (2, 5), scalar 0.9986

parent `126dcfeaef41ee17` -> candidate `43fa7a374e6aad07`

```diff
--- parent 126dcfeaef41ee17
+++ candidate 43fa7a374e6aad07
@@ -0,0 +1,117 @@
+    # Dispatch table mapping operation names to handler functions
+    def _is_prime(args):
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
+    def _reverse_string(args):
+        return args[0][::-1]
+
+    def _fibonacci(args):
+        n = args[0]
+        a, b = 0, 1
+        for _ in range(n):
+            a, b = b, a + b
+        return a
+
+    def _gcd(args):
+        a, b = args
+        while b:
+            a, b = b, a % b
+        return a
+
+    def _is_palindrome(args):
+        s = args[0]
+        filtered = ''.join(c.lower() for c in s if c.isalnum())
+        return filtered == filtered[::-1]
+
+    def _sum_digits(args):
+        n = args[0]
+        return sum(int(d) for d in str(abs(n)))
+
+    def _factorial(args):
+        n = args[0]
+        if n < 0:
+            raise ValueError("factorial not defined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    def _max_subarray_sum(args):
+        nums = args[0]
+        if not nums:
+            return 0
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    def _count_vowels(args):
+        s = args[0]
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    def _is_anagram(args):
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
+
+    def _binary_search(args):
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
+    def _flatten_list(args):
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
+    # Mapping dictionary
+    _dispatch_map = {
+        "is_prime": _is_prime,
+        "reverse_string": _reverse_string,
+        "fibonacci": _fibonacci,
+        "gcd": _gcd,
+        "is_palindrome": _is_palindrome,
+        "sum_digits": _sum_digits,
+        "factorial": _factorial,
+        "max_subarray_sum": _max_subarray_sum,
+        "count_vowels": _count_vowels,
+        "is_anagram": _is_anagram,
+        "binary_search": _binary_search,
+        "flatten_list": _flatten_list,
+    }
+
+    try:
+        handler = _dispatch_map[op]
+    except KeyError:
+        raise ValueError(f"unknown op: {op}")
+
+    return handler(args)
```

### Island 1, cell (0, 5), scalar 0.9987

parent `126dcfeaef41ee17` -> candidate `fd6702ef21b6d873`

```diff
--- parent 126dcfeaef41ee17
+++ candidate fd6702ef21b6d873
@@ -0,0 +1,103 @@
+    # Helper functions for each operation
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
+        # Returns the n-th Fibonacci number (0‑indexed)
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
+        import re
+        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
+        return cleaned == cleaned[::-1]
+
+    def _sum_digits(n):
+        return sum(int(d) for d in str(abs(n)))
+
+    def _factorial(n):
+        if n < 0:
+            raise ValueError("factorial undefined for negative numbers")
+        result = 1
+        for i in range(2, n + 1):
+            result *= i
+        return result
+
+    def _max_subarray_sum(nums):
+        if not nums:
+            return 0
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = max(x, cur + x)
+            best = max(best, cur)
+        return best
+
+    def _count_vowels(s):
+        return sum(1 for c in s.lower() if c in "aeiou")
+
+    def _is_anagram(a, b):
+        normalize = lambda t: sorted(t.replace(" ", "").lower())
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
+        def _extend(item):
+            if isinstance(item, list):
+                for sub in item:
+                    _extend(sub)
+            else:
+                out.append(item)
+        _extend(nested)
+        return out
+
+    # Dispatch table mapping operation names to callables
+    _dispatch_table = {
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
+        return _dispatch_table[op](args)
+    except KeyError:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (2, 5), scalar 0.9986

parent `126dcfeaef41ee17` -> candidate `cecd0532deff7aeb`

```diff
--- parent 126dcfeaef41ee17
+++ candidate cecd0532deff7aeb
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
+            elif nums[mid] < target:
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
+        out.reverse()
+        return out
+
+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (0, 5), scalar 0.9987

parent `126dcfeaef41ee17` -> candidate `96fd6f3112c68f86`

```diff
--- parent 126dcfeaef41ee17
+++ candidate 96fd6f3112c68f86
@@ -0,0 +1,96 @@
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
+            raise ValueError("max_subarray_sum requires a non‑empty list")
+        cur = best = nums[0]
+        for x in nums[1:]:
+            cur = x if cur < 0 else cur + x
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

### Island 2, cell (2, 5), scalar 0.9987

parent `126dcfeaef41ee17` -> candidate `8dfa4f61cfad6929`

```diff
--- parent 126dcfeaef41ee17
+++ candidate 8dfa4f61cfad6929
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
+        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
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

### Island 3, cell (0, 5), scalar 0.9987

parent `126dcfeaef41ee17` -> candidate `56992b0a96655bf2`

```diff
--- parent 126dcfeaef41ee17
+++ candidate 56992b0a96655bf2
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

### Island 3, cell (2, 5), scalar 0.9986

parent `126dcfeaef41ee17` -> candidate `9673b26800dc3d25`

```diff
--- parent 126dcfeaef41ee17
+++ candidate 9673b26800dc3d25
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
+        max_ending_here = max_so_far = nums[0]
+        for x in nums[1:]:
+            max_ending_here = max(x, max_ending_here + x)
+            max_so_far = max(max_so_far, max_ending_here)
+        return max_so_far
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

