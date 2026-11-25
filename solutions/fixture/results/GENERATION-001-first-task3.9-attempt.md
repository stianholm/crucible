# Generation 1 — fixture

## Throughput

- Peak queue depth: 8
- Sustained (median) queue depth: 8.0
- Prefix cache hit rate: 81.9%

## Archive

- Island 0: coverage 5.6%, QD score 1.997, unique ancestors 1
- Island 1: coverage 8.3%, QD score 2.996, unique ancestors 1
- Island 2: coverage 11.1%, QD score 3.995, unique ancestors 1
- Island 3: coverage 8.3%, QD score 2.996, unique ancestors 1
- Cells newly claimed this generation: 6

## Quality

- Best scalar this generation: 0.9988
- Median scalar of newly-claimed: 0.9986

## Cost

- Budget: {'generation': 1, 'max_generations': 3, 'tokens_used_total': 38903, 'max_tokens': 10000000, 'elapsed_s_total': 210.4, 'generation_wall_s': 108.9}
- Candidates proposed: 8
- Parsed: 7 (87.5%)
- Admissible: 7 (87.5%)
- Scored: 7

## Content — newly claimed elites

### Island 0, cell (2, 5), scalar 0.9986

parent `43fa7a374e6aad07` -> candidate `b3fa12c0a5311a1b`

```diff
--- parent 43fa7a374e6aad07
+++ candidate b3fa12c0a5311a1b
@@ -1,5 +1,5 @@
-    # Dispatch table mapping operation names to handler functions
-    def _is_prime(args):
+    # Direct if/elif dispatcher – each branch handles its own logic using the supplied args list.
+    if op == "is_prime":
         n = args[0]
         if n < 2:
             return False
@@ -12,32 +12,32 @@
             i += 2
         return True
 
-    def _reverse_string(args):
+    elif op == "reverse_string":
         return args[0][::-1]
 
-    def _fibonacci(args):
+    elif op == "fibonacci":
         n = args[0]
         a, b = 0, 1
         for _ in range(n):
             a, b = b, a + b
         return a
 
-    def _gcd(args):
+    elif op == "gcd":
         a, b = args
         while b:
             a, b = b, a % b
         return a
 
-    def _is_palindrome(args):
+    elif op == "is_palindrome":
         s = args[0]
         filtered = ''.join(c.lower() for c in s if c.isalnum())
         return filtered == filtered[::-1]
 
-    def _sum_digits(args):
+    elif op == "sum_digits":
         n = args[0]
         return sum(int(d) for d in str(abs(n)))
 
-    def _factorial(args):
+    elif op == "factorial":
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
@@ -46,7 +46,7 @@
             result *= i
         return result
 
-    def _max_subarray_sum(args):
+    elif op == "max_subarray_sum":
         nums = args[0]
         if not nums:
             return 0
@@ -56,16 +56,16 @@
             best = max(best, cur)
         return best
 
-    def _count_vowels(args):
+    elif op == "count_vowels":
         s = args[0]
         return sum(1 for c in s.lower() if c in "aeiou")
 
-    def _is_anagram(args):
+    elif op == "is_anagram":
         a, b = args
         normalize = lambda s: sorted(c.lower() for c in s if not c.isspace())
         return normalize(a) == normalize(b)
 
-    def _binary_search(args):
+    elif op == "binary_search":
         nums, target = args
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
@@ -78,7 +78,7 @@
                 hi = mid - 1
         return -1
 
-    def _flatten_list(args):
+    elif op == "flatten_list":
         nested = args[0]
         out = []
         stack = [iter(nested)]
@@ -93,25 +93,5 @@
                 stack.pop()
         return out
 
-    # Mapping dictionary
-    _dispatch_map = {
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
-        handler = _dispatch_map[op]
-    except KeyError:
-        raise ValueError(f"unknown op: {op}")
-
-    return handler(args)+    else:
+        raise ValueError(f"unknown op: {op}")
```

### Island 1, cell (1, 5), scalar 0.9986

parent `fd6702ef21b6d873` -> candidate `b517a8e0c4ab929a`

```diff
--- parent fd6702ef21b6d873
+++ candidate b517a8e0c4ab929a
@@ -1,5 +1,6 @@
-    # Helper functions for each operation
-    def _is_prime(n):
+    # Direct if/elif dispatcher without auxiliary tables or helper definitions
+    if op == "is_prime":
+        n = args[0]
         if n < 2:
             return False
         if n % 2 == 0:
@@ -11,54 +12,59 @@
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
@@ -70,34 +76,19 @@
                 hi = mid - 1
         return -1
 
-    def _flatten_list(nested):
-        out = []
-        def _extend(item):
+    elif op == "flatten_list":
+        nested = args[0]
+        result = []
+
+        def _flatten(item):
             if isinstance(item, list):
                 for sub in item:
-                    _extend(sub)
+                    _flatten(sub)
             else:
-                out.append(item)
-        _extend(nested)
-        return out
+                result.append(item)
 
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
+        _flatten(nested)
+        return result
 
-    try:
-        return _dispatch_table[op](args)
-    except KeyError:
+    else:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (1, 5), scalar 0.9988

parent `8dfa4f61cfad6929` -> candidate `a8d6df3bc7c8a7f3`

```diff
--- parent 8dfa4f61cfad6929
+++ candidate a8d6df3bc7c8a7f3
@@ -1,4 +1,8 @@
-    if op == "is_prime":
+    # Import once for operations that need it
+    import re
+
+    # Define each operation as a zero‑argument helper that closes over `args`
+    def _is_prime():
         n = args[0]
         if n < 2:
             return False
@@ -12,10 +16,10 @@
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
@@ -24,23 +28,22 @@
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
@@ -49,27 +52,26 @@
             result *= i
         return result
 
-    elif op == "max_subarray_sum":
+    def _max_subarray_sum():
         nums = args[0]
         if not nums:
-            return 0
+            raise ValueError("max_subarray_sum requires a non‑empty list")
         best = cur = nums[0]
         for x in nums[1:]:
             cur = max(x, cur + x)
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
@@ -82,18 +84,36 @@
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
+                # push in reverse so that left‑most items are processed first
+                stack.extend(reversed(cur))
             else:
-                out.append(current)
+                out.append(cur)
         return out
 
-    else:
+    # Dispatch table mapping operation names to their helpers
+    _dispatch_table = {
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
+        return _dispatch_table[op]()
+    except KeyError:
         raise ValueError(f"unknown op: {op}")
```

### Island 2, cell (3, 5), scalar 0.9986

parent `8dfa4f61cfad6929` -> candidate `ede97152b59ab931`

```diff
--- parent 8dfa4f61cfad6929
+++ candidate ede97152b59ab931
@@ -1,21 +1,20 @@
-    if op == "is_prime":
+    # Helper functions implementing each operation
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
@@ -24,23 +23,22 @@
             a, b = b, a + b
         return a
 
-    elif op == "gcd":
+    def _gcd():
+        import math
         a, b = args
-        while b:
-            a, b = b, a % b
-        return abs(a)
+        return abs(math.gcd(a, b))
 
-    elif op == "is_palindrome":
+    def _is_palindrome():
         import re
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
@@ -49,7 +47,7 @@
             result *= i
         return result
 
-    elif op == "max_subarray_sum":
+    def _max_subarray_sum():
         nums = args[0]
         if not nums:
             return 0
@@ -59,17 +57,16 @@
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
@@ -82,18 +79,35 @@
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
+    # Dispatch table mapping operation names to the corresponding callables
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
+        return _dispatch_map[op]()
+    except KeyError:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (2, 5), scalar 0.9987

parent `56992b0a96655bf2` -> candidate `d2c5db2e66c73849`

```diff
--- parent 56992b0a96655bf2
+++ candidate d2c5db2e66c73849
@@ -1,5 +1,5 @@
-    if op == "is_prime":
-        n = args[0]
+    # Helper implementations for each operation
+    def _is_prime(n):
         if n < 2:
             return False
         if n % 2 == 0:
@@ -12,11 +12,10 @@
             i += 2
         return True
 
-    elif op == "reverse_string":
-        return args[0][::-1]
+    def _reverse_string(s):
+        return s[::-1]
 
-    elif op == "fibonacci":
-        n = args[0]
+    def _fibonacci(n):
         if n < 0:
             raise ValueError("fibonacci index must be non‑negative")
         a, b = 0, 1
@@ -24,23 +23,19 @@
             a, b = b, a + b
         return a
 
-    elif op == "gcd":
-        a, b = args
+    def _gcd(a, b):
         while b:
             a, b = b, a % b
         return abs(a)
 
-    elif op == "is_palindrome":
-        import re
-        s = re.sub(r'[^A-Za-z0-9]', '', args[0]).lower()
-        return s == s[::-1]
+    def _is_palindrome(s):
+        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
+        return filtered == filtered[::-1]
 
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
@@ -48,8 +43,7 @@
             result *= i
         return result
 
-    elif op == "max_subarray_sum":
-        nums = args[0]
+    def _max_subarray_sum(nums):
         if not nums:
             return 0
         best = cur = nums[0]
@@ -58,17 +52,14 @@
             best = max(best, cur)
         return best
 
-    elif op == "count_vowels":
-        s = args[0]
+    def _count_vowels(s):
         return sum(1 for c in s.lower() if c in "aeiou")
 
-    elif op == "is_anagram":
-        a, b = args
-        normalize = lambda s: sorted(s.replace(" ", "").lower())
+    def _is_anagram(a, b):
+        normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
-    elif op == "binary_search":
-        nums, target = args
+    def _binary_search(nums, target):
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
             mid = (lo + hi) // 2
@@ -80,17 +71,36 @@
                 hi = mid - 1
         return -1
 
-    elif op == "flatten_list":
-        nested = args[0]
+    def _flatten_list(nested):
         out = []
-        def _flatten(item):
+
+        def _recurse(item):
             if isinstance(item, list):
                 for sub in item:
-                    _flatten(sub)
+                    _recurse(sub)
             else:
                 out.append(item)
-        _flatten(nested)
+
+        _recurse(nested)
         return out
 
-    else:
+    # Dispatch table mapping operation names to callables
+    _dispatch_map = {
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
+        return _dispatch_map[op](args)
+    except KeyError:
         raise ValueError(f"unknown op: {op}")
```

### Island 3, cell (1, 5), scalar 0.9986

parent `9673b26800dc3d25` -> candidate `1b4174da2380e8d2`

```diff
--- parent 9673b26800dc3d25
+++ candidate 1b4174da2380e8d2
@@ -1,4 +1,4 @@
-    if op == "is_prime":
+    def _is_prime(args):
         n = args[0]
         if n < 2:
             return False
@@ -11,10 +11,10 @@
             i += 2
         return True
 
-    elif op == "reverse_string":
+    def _reverse_string(args):
         return args[0][::-1]
 
-    elif op == "fibonacci":
+    def _fibonacci(args):
         n = args[0]
         if n < 0:
             raise ValueError("fibonacci index must be non‑negative")
@@ -23,22 +23,22 @@
             a, b = b, a + b
         return a
 
-    elif op == "gcd":
+    def _gcd(args):
         a, b = args
         while b:
             a, b = b, a % b
         return abs(a)
 
-    elif op == "is_palindrome":
+    def _is_palindrome(args):
         s = args[0]
         filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
         return filtered == filtered[::-1]
 
-    elif op == "sum_digits":
+    def _sum_digits(args):
         n = args[0]
         return sum(int(d) for d in str(abs(n)))
 
-    elif op == "factorial":
+    def _factorial(args):
         n = args[0]
         if n < 0:
             raise ValueError("factorial not defined for negative numbers")
@@ -47,26 +47,25 @@
             result *= i
         return result
 
-    elif op == "max_subarray_sum":
+    def _max_subarray_sum(args):
         nums = args[0]
         if not nums:
             return 0
-        max_ending_here = max_so_far = nums[0]
+        max_ending = max_sofar = nums[0]
         for x in nums[1:]:
-            max_ending_here = max(x, max_ending_here + x)
-            max_so_far = max(max_so_far, max_ending_here)
-        return max_so_far
+            max_ending = max(x, max_ending + x)
+            max_sofar = max(max_sofar, max_ending)
+        return max_sofar
 
-    elif op == "count_vowels":
-        s = args[0]
-        return sum(1 for c in s.lower() if c in "aeiou")
+    def _count_vowels(args):
+        return sum(1 for c in args[0].lower() if c in "aeiou")
 
-    elif op == "is_anagram":
+    def _is_anagram(args):
         a, b = args
         normalize = lambda s: sorted(ch.lower() for ch in s if not ch.isspace())
         return normalize(a) == normalize(b)
 
-    elif op == "binary_search":
+    def _binary_search(args):
         nums, target = args
         lo, hi = 0, len(nums) - 1
         while lo <= hi:
@@ -79,17 +78,34 @@
                 hi = mid - 1
         return -1
 
-    elif op == "flatten_list":
+    def _flatten_list(args):
         nested = args[0]
 
-        def _flatten(item):
+        def _gen(item):
             if isinstance(item, list):
                 for sub in item:
-                    yield from _flatten(sub)
+                    yield from _gen(sub)
             else:
                 yield item
 
-        return list(_flatten(nested))
+        return list(_gen(nested))
 
-    else:
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
+        return _dispatch_map[op](args)
+    except KeyError:
         raise ValueError(f"unknown op: {op}")
```

