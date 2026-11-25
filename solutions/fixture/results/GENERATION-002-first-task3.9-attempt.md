# Generation 2 — fixture

## Throughput

- Peak queue depth: 8
- Sustained (median) queue depth: 8
- Prefix cache hit rate: 77.4%

## Archive

- Island 0: coverage 5.6%, QD score 1.997, unique ancestors 1
- Island 1: coverage 11.1%, QD score 3.995, unique ancestors 1
- Island 2: coverage 11.1%, QD score 3.995, unique ancestors 1
- Island 3: coverage 8.3%, QD score 2.997, unique ancestors 1
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.9990
- Median scalar of newly-claimed: 0.9989

## Cost

- Budget: {'generation': 2, 'max_generations': 3, 'tokens_used_total': 64662, 'max_tokens': 10000000, 'elapsed_s_total': 307.4, 'generation_wall_s': 96.9}
- Candidates proposed: 8
- Parsed: 7 (87.5%)
- Admissible: 7 (87.5%)
- Scored: 7

## Content — newly claimed elites

### Island 0, cell (2, 5), scalar 0.9989

parent `b3fa12c0a5311a1b` -> candidate `3b1aead20a9cbb46`

```diff
--- parent b3fa12c0a5311a1b
+++ candidate 3b1aead20a9cbb46
@@ -1,6 +1,5 @@
-    # Direct if/elif dispatcher – each branch handles its own logic using the supplied args list.
-    if op == "is_prime":
-        n = args[0]
+    # Helper functions implementing each operation.
+    def _is_prime(n):
         if n < 2:
             return False
         if n % 2 == 0:
@@ -12,33 +11,28 @@
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
-        s = args[0]
+    def _is_palindrome(s):
         filtered = ''.join(c.lower() for c in s if c.isalnum())
         return filtered == filtered[::-1]
 
-    elif op == "sum_digits":
-        n = args[0]
+    def _sum_digits(n):
         return sum(int(d) for d in str(abs(n)))
 
-    elif op == "factorial":
-        n = args[0]
+    def _factorial(n):
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
         result = 1
@@ -46,8 +40,7 @@
             result *= i
         return result
 
-    elif op == "max_subarray_sum":
-        nums = args[0]
+    def _max_subarray_sum(nums):
         if not nums:
             return 0
         cur = best = nums[0]
@@ -56,17 +49,14 @@
             best = max(best, cur)
         return best
 
-    elif op == "count_vowels":
-        s = args[0]
+    def _count_vowels(s):
         return sum(1 for c in s.lower() if c in "aeiou")
 
-    elif op == "is_anagram":
-        a, b = args
+    def _is_anagram(a, b):
         normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
         return normalize(a) == normalize(b)
 
-    elif op == "binary_search":
-        nums, target = args
+    def _binary_search(nums, target):
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
             mid = (lo + hi) // 2
@@ -78,8 +68,7 @@
                 hi = mid - 1
         return -1
 
-    elif op == "flatten_list":
-        nested = args[0]
+    def _flatten_list(nested):
         out = []
         stack = [iter(nested)]
         while stack:
@@ -93,5 +82,23 @@
                 stack.pop()
         return out
 
-    else:
+    # Dispatch table mapping operation names to callables.
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

### Island 1, cell (3, 5), scalar 0.9989

parent `fd6702ef21b6d873` -> candidate `2394e187caaa4380`

```diff
--- parent fd6702ef21b6d873
+++ candidate 2394e187caaa4380
@@ -1,5 +1,5 @@
-    # Helper functions for each operation
-    def _is_prime(n):
+    if op == "is_prime":
+        n = args[0]
         if n < 2:
             return False
         if n % 2 == 0:
@@ -11,54 +11,59 @@
             i += 2
         return True
 
-    def _reverse_string(s):
-        return s[::-1]
+    elif op == "reverse_string":
+        return args[0][::-1]
 
-    def _fibonacci(n):
-        # Returns the n-th Fibonacci number (0‑indexed)
+    elif op == "fibonacci":
+        n = args[0]
         a, b = 0, 1
         for _ in range(n):
             a, b = b, a + b
         return a
 
-    def _gcd(a, b):
+    elif op == "gcd":
+        a, b = args
         while b:
             a, b = b, a % b
-        return a
+        return abs(a)
 
-    def _is_palindrome(s):
+    elif op == "is_palindrome":
         import re
-        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
+        cleaned = re.sub(r'[^a-z0-9]', '', args[0].lower())
         return cleaned == cleaned[::-1]
 
-    def _sum_digits(n):
-        return sum(int(d) for d in str(abs(n)))
+    elif op == "sum_digits":
+        return sum(int(d) for d in str(abs(args[0])))
 
-    def _factorial(n):
+    elif op == "factorial":
+        n = args[0]
         if n < 0:
-            raise ValueError("factorial undefined for negative numbers")
+            raise ValueError("factorial not defined for negative numbers")
         result = 1
         for i in range(2, n + 1):
             result *= i
         return result
 
-    def _max_subarray_sum(nums):
+    elif op == "max_subarray_sum":
+        nums = args[0]
         if not nums:
             return 0
         cur = best = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
+            cur = x if cur + x < x else cur + x
+            best = best if best > cur else cur
         return best
 
-    def _count_vowels(s):
-        return sum(1 for c in s.lower() if c in "aeiou")
+    elif op == "count_vowels":
+        return sum(1 for c in args[0].lower() if c in "aeiou")
 
-    def _is_anagram(a, b):
-        normalize = lambda t: sorted(t.replace(" ", "").lower())
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
         return normalize(a) == normalize(b)
 
-    def _binary_search(nums, target):
+    elif op == "binary_search":
+        nums, target = args
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
             mid = (lo + hi) // 2
@@ -70,34 +75,18 @@
                 hi = mid - 1
         return -1
 
-    def _flatten_list(nested):
+    elif op == "flatten_list":
+        nested = args[0]
         out = []
-        def _extend(item):
-            if isinstance(item, list):
-                for sub in item:
-                    _extend(sub)
+        stack = [nested]
+        while stack:
+            cur = stack.pop()
+            if isinstance(cur, list):
+                stack.extend(reversed(cur))
             else:
-                out.append(item)
-        _extend(nested)
+                out.append(cur)
+        out.reverse()
         return out
 
-    # Dispatch table mapping operation names to callables
-    _dispatch_table = {
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
-        return _dispatch_table[op](args)
-    except KeyError:
+    else:
         raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (1, 5), scalar 0.9989

parent `fd6702ef21b6d873` -> candidate `842032c045c0434e`

```diff
--- parent fd6702ef21b6d873
+++ candidate 842032c045c0434e
@@ -1,5 +1,5 @@
-    # Helper functions for each operation
-    def _is_prime(n):
+    if op == "is_prime":
+        n = args[0]
         if n < 2:
             return False
         if n % 2 == 0:
@@ -11,54 +11,59 @@
             i += 2
         return True
 
-    def _reverse_string(s):
-        return s[::-1]
+    elif op == "reverse_string":
+        return args[0][::-1]
 
-    def _fibonacci(n):
-        # Returns the n-th Fibonacci number (0‑indexed)
+    elif op == "fibonacci":
+        n = args[0]
         a, b = 0, 1
         for _ in range(n):
             a, b = b, a + b
         return a
 
-    def _gcd(a, b):
+    elif op == "gcd":
+        a, b = args
         while b:
             a, b = b, a % b
-        return a
+        return abs(a)
 
-    def _is_palindrome(s):
+    elif op == "is_palindrome":
         import re
-        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
+        cleaned = re.sub(r'[^a-z0-9]', '', args[0].lower())
         return cleaned == cleaned[::-1]
 
-    def _sum_digits(n):
-        return sum(int(d) for d in str(abs(n)))
+    elif op == "sum_digits":
+        return sum(int(d) for d in str(abs(args[0])))
 
-    def _factorial(n):
+    elif op == "factorial":
+        n = args[0]
         if n < 0:
-            raise ValueError("factorial undefined for negative numbers")
+            raise ValueError("factorial not defined for negative numbers")
         result = 1
         for i in range(2, n + 1):
             result *= i
         return result
 
-    def _max_subarray_sum(nums):
+    elif op == "max_subarray_sum":
+        nums = args[0]
         if not nums:
             return 0
         cur = best = nums[0]
         for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
+            cur = x if cur + x < x else cur + x
+            best = best if best > cur else cur
         return best
 
-    def _count_vowels(s):
-        return sum(1 for c in s.lower() if c in "aeiou")
+    elif op == "count_vowels":
+        return sum(1 for c in args[0].lower() if c in "aeiou")
 
-    def _is_anagram(a, b):
-        normalize = lambda t: sorted(t.replace(" ", "").lower())
+    elif op == "is_anagram":
+        a, b = args
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
         return normalize(a) == normalize(b)
 
-    def _binary_search(nums, target):
+    elif op == "binary_search":
+        nums, target = args
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
             mid = (lo + hi) // 2
@@ -70,34 +75,18 @@
                 hi = mid - 1
         return -1
 
-    def _flatten_list(nested):
+    elif op == "flatten_list":
+        nested = args[0]
         out = []
-        def _extend(item):
+        stack = [nested]
+        while stack:
+            item = stack.pop()
             if isinstance(item, list):
-                for sub in item:
-                    _extend(sub)
+                stack.extend(reversed(item))
             else:
                 out.append(item)
-        _extend(nested)
+        out.reverse()
         return out
 
-    # Dispatch table mapping operation names to callables
-    _dispatch_table = {
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
-        return _dispatch_table[op](args)
-    except KeyError:
+    else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (0, 5), scalar 0.9989

parent `a8d6df3bc7c8a7f3` -> candidate `652522071d1cbed7`

```diff
--- parent a8d6df3bc7c8a7f3
+++ candidate 652522071d1cbed7
@@ -1,119 +1,96 @@
-    # Import once for operations that need it
-    import re
+    # Dispatch using structural pattern matching (Python 3.10+)
+    match op:
+        case "is_prime":
+            n = args[0]
+            if n < 2:
+                return False
+            if n == 2:
+                return True
+            if n % 2 == 0:
+                return False
+            limit = int(n ** 0.5) + 1
+            for i in range(3, limit, 2):
+                if n % i == 0:
+                    return False
+            return True
 
-    # Define each operation as a zero‑argument helper that closes over `args`
-    def _is_prime():
-        n = args[0]
-        if n < 2:
-            return False
-        if n == 2:
-            return True
-        if n % 2 == 0:
-            return False
-        limit = int(n ** 0.5) + 1
-        for i in range(3, limit, 2):
-            if n % i == 0:
-                return False
-        return True
+        case "reverse_string":
+            return args[0][::-1]
 
-    def _reverse_string():
-        return args[0][::-1]
+        case "fibonacci":
+            n = args[0]
+            if n < 0:
+                raise ValueError("fibonacci index must be non‑negative")
+            a, b = 0, 1
+            for _ in range(n):
+                a, b = b, a + b
+            return a
 
-    def _fibonacci():
-        n = args[0]
-        if n < 0:
-            raise ValueError("fibonacci index must be non‑negative")
-        a, b = 0, 1
-        for _ in range(n):
-            a, b = b, a + b
-        return a
+        case "gcd":
+            a, b = args
+            while b:
+                a, b = b, a % b
+            return abs(a)
 
-    def _gcd():
-        a, b = args
-        while b:
-            a, b = b, a % b
-        return abs(a)
+        case "is_palindrome":
+            import re
+            s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
+            return s == s[::-1]
 
-    def _is_palindrome():
-        s = args[0]
-        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
-        return cleaned == cleaned[::-1]
+        case "sum_digits":
+            return sum(int(d) for d in str(abs(args[0])))
 
-    def _sum_digits():
-        n = args[0]
-        return sum(int(d) for d in str(abs(n)))
+        case "factorial":
+            n = args[0]
+            if n < 0:
+                raise ValueError("factorial not defined for negative numbers")
+            result = 1
+            for i in range(2, n + 1):
+                result *= i
+            return result
 
-    def _factorial():
-        n = args[0]
-        if n < 0:
-            raise ValueError("factorial not defined for negative numbers")
-        result = 1
-        for i in range(2, n + 1):
-            result *= i
-        return result
+        case "max_subarray_sum":
+            nums = args[0]
+            if not nums:
+                raise ValueError("max_subarray_sum requires a non‑empty list")
+            best = cur = nums[0]
+            for x in nums[1:]:
+                cur = max(x, cur + x)
+                best = max(best, cur)
+            return best
 
-    def _max_subarray_sum():
-        nums = args[0]
-        if not nums:
-            raise ValueError("max_subarray_sum requires a non‑empty list")
-        best = cur = nums[0]
-        for x in nums[1:]:
-            cur = max(x, cur + x)
-            best = max(best, cur)
-        return best
+        case "count_vowels":
+            return sum(1 for c in args[0].lower() if c in "aeiou")
 
-    def _count_vowels():
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+        case "is_anagram":
+            a, b = args
+            normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+            return normalize(a) == normalize(b)
 
-    def _is_anagram():
-        a, b = args
-        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
-        return normalize(a) == normalize(b)
+        case "binary_search":
+            nums, target = args
+            lo, hi = 0, len(nums) - 1
+            while lo <= hi:
+                mid = (lo + hi) // 2
+                if nums[mid] == target:
+                    return mid
+                if nums[mid] < target:
+                    lo = mid + 1
+                else:
+                    hi = mid - 1
+            return -1
 
-    def _binary_search():
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
+        case "flatten_list":
+            nested = args[0]
+            out = []
+            stack = [nested]
+            while stack:
+                cur = stack.pop()
+                if isinstance(cur, list):
+                    stack.extend(reversed(cur))
+                else:
+                    out.append(cur)
+            return out
 
-    def _flatten_list():
-        nested = args[0]
-        out = []
-        stack = [nested]
-        while stack:
-            cur = stack.pop()
-            if isinstance(cur, list):
-                # push in reverse so that left‑most items are processed first
-                stack.extend(reversed(cur))
-            else:
-                out.append(cur)
-        return out
-
-    # Dispatch table mapping operation names to their helpers
-    _dispatch_table = {
-        "is_prime": _is_prime,
-        "reverse_string": _reverse_string,
-        "fibonacci": _fibonacci,
-        "gcd": _gcd,
-        "is_palindrome": _is_palindrome,
-        "sum_digits": _sum_digits,
-        "factorial": _factorial,
-        "max_subarray_sum": _max_subarray_sum,
-        "count_vowels": _count_vowels,
-        "is_anagram": _is_anagram,
-        "binary_search": _binary_search,
-        "flatten_list": _flatten_list,
-    }
-
-    try:
-        return _dispatch_table[op]()
-    except KeyError:
-        raise ValueError(f"unknown op: {op}")+        case _:
+            raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (1, 5), scalar 0.9989

parent `8dfa4f61cfad6929` -> candidate `3dfc7f7a12ae2a6c`

```diff
--- parent 8dfa4f61cfad6929
+++ candidate 3dfc7f7a12ae2a6c
@@ -1,21 +1,23 @@
-    if op == "is_prime":
+    # Import modules only once
+    import re
+
+    # Define operation helpers as zero‑argument closures that capture `args`
+    def _is_prime():
         n = args[0]
         if n < 2:
             return False
-        if n == 2:
-            return True
         if n % 2 == 0:
-            return False
+            return n == 2
         limit = int(n ** 0.5) + 1
         for i in range(3, limit, 2):
             if n % i == 0:
                 return False
         return True
 
-    elif op == "reverse_string":
+    def _reverse_string():
         return args[0][::-1]
 
-    elif op == "fibonacci":
+    def _fibonacci():
         n = args[0]
         if n < 0:
             raise ValueError("fibonacci index must be non‑negative")
@@ -24,23 +26,22 @@
             a, b = b, a + b
         return a
 
-    elif op == "gcd":
+    def _gcd():
         a, b = args
         while b:
             a, b = b, a % b
         return abs(a)
 
-    elif op == "is_palindrome":
-        import re
+    def _is_palindrome():
         s = args[0]
         cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
         return cleaned == cleaned[::-1]
 
-    elif op == "sum_digits":
+    def _sum_digits():
         n = args[0]
         return sum(int(d) for d in str(abs(n)))
 
-    elif op == "factorial":
+    def _factorial():
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
@@ -49,7 +50,7 @@
             result *= i
         return result
 
-    elif op == "max_subarray_sum":
+    def _max_subarray_sum():
         nums = args[0]
         if not nums:
             return 0
@@ -59,17 +60,16 @@
             best = max(best, cur)
         return best
 
-    elif op == "count_vowels":
+    def _count_vowels():
         s = args[0]
         return sum(1 for c in s.lower() if c in "aeiou")
 
-    elif op == "is_anagram":
+    def _is_anagram():
         a, b = args
-        a_clean = sorted(c.lower() for c in a if not c.isspace())
-        b_clean = sorted(c.lower() for c in b if not c.isspace())
-        return a_clean == b_clean
+        normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
+        return normalize(a) == normalize(b)
 
-    elif op == "binary_search":
+    def _binary_search():
         nums, target = args
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
@@ -82,18 +82,35 @@
                 hi = mid - 1
         return -1
 
-    elif op == "flatten_list":
+    def _flatten_list():
         nested = args[0]
         out = []
         stack = [nested]
         while stack:
-            current = stack.pop()
-            if isinstance(current, list):
-                # extend stack in reverse to preserve order
-                stack.extend(reversed(current))
+            cur = stack.pop()
+            if isinstance(cur, list):
+                stack.extend(reversed(cur))
             else:
-                out.append(current)
+                out.append(cur)
         return out
 
-    else:
+    # Dispatch table mapping operation names to helpers
+    _dispatch = {
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
+        return _dispatch[op]()
+    except KeyError:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (1, 5), scalar 0.9989

parent `d2c5db2e66c73849` -> candidate `696e06d7c8fac406`

```diff
--- parent d2c5db2e66c73849
+++ candidate 696e06d7c8fac406
@@ -1,5 +1,6 @@
-    # Helper implementations for each operation
-    def _is_prime(n):
+    # Helper functions that receive the raw args list
+    def _is_prime(args):
+        n = args[0]
         if n < 2:
             return False
         if n % 2 == 0:
@@ -12,10 +13,11 @@
             i += 2
         return True
 
-    def _reverse_string(s):
-        return s[::-1]
+    def _reverse_string(args):
+        return args[0][::-1]
 
-    def _fibonacci(n):
+    def _fibonacci(args):
+        n = args[0]
         if n < 0:
             raise ValueError("fibonacci index must be non‑negative")
         a, b = 0, 1
@@ -23,19 +25,23 @@
             a, b = b, a + b
         return a
 
-    def _gcd(a, b):
+    def _gcd(args):
+        a, b = args
         while b:
             a, b = b, a % b
         return abs(a)
 
-    def _is_palindrome(s):
+    def _is_palindrome(args):
+        s = args[0]
         filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
         return filtered == filtered[::-1]
 
-    def _sum_digits(n):
+    def _sum_digits(args):
+        n = args[0]
         return sum(int(d) for d in str(abs(n)))
 
-    def _factorial(n):
+    def _factorial(args):
+        n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
         result = 1
@@ -43,7 +49,8 @@
             result *= i
         return result
 
-    def _max_subarray_sum(nums):
+    def _max_subarray_sum(args):
+        nums = args[0]
         if not nums:
             return 0
         best = cur = nums[0]
@@ -52,14 +59,17 @@
             best = max(best, cur)
         return best
 
-    def _count_vowels(s):
+    def _count_vowels(args):
+        s = args[0]
         return sum(1 for c in s.lower() if c in "aeiou")
 
-    def _is_anagram(a, b):
+    def _is_anagram(args):
+        a, b = args
         normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
-    def _binary_search(nums, target):
+    def _binary_search(args):
+        nums, target = args
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
             mid = (lo + hi) // 2
@@ -71,7 +81,8 @@
                 hi = mid - 1
         return -1
 
-    def _flatten_list(nested):
+    def _flatten_list(args):
+        nested = args[0]
         out = []
 
         def _recurse(item):
@@ -84,23 +95,30 @@
         _recurse(nested)
         return out
 
-    # Dispatch table mapping operation names to callables
-    _dispatch_map = {
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
-        return _dispatch_map[op](args)
-    except KeyError:
+    # Explicit if/elif dispatcher
+    if op == "is_prime":
+        return _is_prime(args)
+    elif op == "reverse_string":
+        return _reverse_string(args)
+    elif op == "fibonacci":
+        return _fibonacci(args)
+    elif op == "gcd":
+        return _gcd(args)
+    elif op == "is_palindrome":
+        return _is_palindrome(args)
+    elif op == "sum_digits":
+        return _sum_digits(args)
+    elif op == "factorial":
+        return _factorial(args)
+    elif op == "max_subarray_sum":
+        return _max_subarray_sum(args)
+    elif op == "count_vowels":
+        return _count_vowels(args)
+    elif op == "is_anagram":
+        return _is_anagram(args)
+    elif op == "binary_search":
+        return _binary_search(args)
+    elif op == "flatten_list":
+        return _flatten_list(args)
+    else:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (0, 5), scalar 0.9990

parent `d2c5db2e66c73849` -> candidate `ccdeb65c05e359e9`

```diff
--- parent d2c5db2e66c73849
+++ candidate ccdeb65c05e359e9
@@ -1,5 +1,6 @@
-    # Helper implementations for each operation
-    def _is_prime(n):
+    # Helper functions that accept the full args tuple
+    def _is_prime(args):
+        n = args[0]
         if n < 2:
             return False
         if n % 2 == 0:
@@ -12,10 +13,11 @@
             i += 2
         return True
 
-    def _reverse_string(s):
-        return s[::-1]
+    def _reverse_string(args):
+        return args[0][::-1]
 
-    def _fibonacci(n):
+    def _fibonacci(args):
+        n = args[0]
         if n < 0:
             raise ValueError("fibonacci index must be non‑negative")
         a, b = 0, 1
@@ -23,19 +25,23 @@
             a, b = b, a + b
         return a
 
-    def _gcd(a, b):
+    def _gcd(args):
+        a, b = args
         while b:
             a, b = b, a % b
         return abs(a)
 
-    def _is_palindrome(s):
+    def _is_palindrome(args):
+        s = args[0]
         filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
         return filtered == filtered[::-1]
 
-    def _sum_digits(n):
+    def _sum_digits(args):
+        n = args[0]
         return sum(int(d) for d in str(abs(n)))
 
-    def _factorial(n):
+    def _factorial(args):
+        n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
         result = 1
@@ -43,7 +49,8 @@
             result *= i
         return result
 
-    def _max_subarray_sum(nums):
+    def _max_subarray_sum(args):
+        nums = args[0]
         if not nums:
             return 0
         best = cur = nums[0]
@@ -52,14 +59,16 @@
             best = max(best, cur)
         return best
 
-    def _count_vowels(s):
-        return sum(1 for c in s.lower() if c in "aeiou")
+    def _count_vowels(args):
+        return sum(1 for c in args[0].lower() if c in "aeiou")
 
-    def _is_anagram(a, b):
+    def _is_anagram(args):
+        a, b = args
         normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
-    def _binary_search(nums, target):
+    def _binary_search(args):
+        nums, target = args
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
             mid = (lo + hi) // 2
@@ -71,7 +80,8 @@
                 hi = mid - 1
         return -1
 
-    def _flatten_list(nested):
+    def _flatten_list(args):
+        nested = args[0]
         out = []
 
         def _recurse(item):
@@ -84,23 +94,31 @@
         _recurse(nested)
         return out
 
-    # Dispatch table mapping operation names to callables
-    _dispatch_map = {
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
-        return _dispatch_map[op](args)
-    except KeyError:
-        raise ValueError(f"unknown op: {op}")+    # Dispatch using structural pattern matching (Python 3.10+)
+    match op:
+        case "is_prime":
+            return _is_prime(args)
+        case "reverse_string":
+            return _reverse_string(args)
+        case "fibonacci":
+            return _fibonacci(args)
+        case "gcd":
+            return _gcd(args)
+        case "is_palindrome":
+            return _is_palindrome(args)
+        case "sum_digits":
+            return _sum_digits(args)
+        case "factorial":
+            return _factorial(args)
+        case "max_subarray_sum":
+            return _max_subarray_sum(args)
+        case "count_vowels":
+            return _count_vowels(args)
+        case "is_anagram":
+            return _is_anagram(args)
+        case "binary_search":
+            return _binary_search(args)
+        case "flatten_list":
+            return _flatten_list(args)
+        case _:
+            raise ValueError(f"unknown op: {op}")
```

