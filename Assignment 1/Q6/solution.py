                               
                                                                    
                                                      

from functools import lru_cache
import sys

calls = 0


def ways_naive(n):
    """Plain recursive Fibonacci-like; O(φ^n) calls, O(n) stack depth."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    """Memoised: same recurrence, O(n) calls total, O(n) cache + stack."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_iter(n):
    """Iterative DP: O(n) time, O(1) space, no recursion limit issues."""
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


                                             
             
                                     
                                     
                   
                   
                    
print("=== Correctness (n=1..6) ===")
for n in range(1, 7):
    print(f"  ways({n}) = {ways_iter(n)}")
print("Matches Fibonacci: 1, 2, 3, 5, 8, 13")


                                           
calls = 0
print(f"\nnaive: {ways_naive(25)}, calls = {calls}")
calls = 0
print(f"memo : {ways_memo(25)}, calls = {calls}")


                                            
print("\n=== Call counts ===")
for n in [10, 20, 25, 30]:
    calls = 0
    r = ways_naive(n)
    print(f"  n={n:2d}  naive: {r:>8d}  calls = {calls}")
    calls = 0
    r = ways_memo(n)
    print(f"  n={n:2d}  memo : {r:>8d}  calls = {calls}")


                                          
print("\n=== Call growth (naive exponential, memo linear) ===")
print("  naive calls ≈ 2 * Fib(n+1) - 1  (exponential ~ φ^n)")
print("  memo calls = n + 2  (one per n from n down to 0 + base cases)")


                                        
print(f"\n=== Recursion limit ===")
print(f"sys.getrecursionlimit() = {sys.getrecursionlimit()}")

print("\nAttempting ways_memo(1000) with default limit...")
try:
    calls = 0
    result = ways_memo(1000)
    print(f"  memo(1000) = {result}, calls = {calls}")
except RecursionError as e:
    print(f"  RecursionError: {e}")
    print("  Depth ~1000 exceeds default limit (1000 frames include overhead).")

print("\nAttempting with raised limit...")
sys.setrecursionlimit(10000)
try:
    calls = 0
    result = ways_memo(1000)
    print(f"  memo(1000) = {result}, calls = {calls}")
except RecursionError as e:
    print(f"  Still failed: {e}")


print("\n=== Iterative version for n = 1000 ===")
import time
start = time.perf_counter()
iter_result = ways_iter(1000)
iter_time = time.perf_counter() - start
print(f"  ways_iter(1000) computed in {iter_time:.6f} s")
print(f"  Result length: {len(str(iter_result))} digits")
print(f"  First 10 digits: {str(iter_result)[:10]}...")


                                                  
print("\n=== Timing comparison for n=30 ===")
for label, fn in [("naive", ways_naive), ("memo", ways_memo), ("iter", ways_iter)]:
    calls = 0 if label != "iter" else None
    start = time.perf_counter()
    if label == "naive":
        r = fn(30)
    elif label == "memo":
        ways_memo.cache_clear()
        r = fn(30)
    else:
        r = fn(30)
    elapsed = time.perf_counter() - start
    if label != "iter":
        print(f"  {label:5s}: {elapsed:.6f} s  (calls = {calls})")
    else:
        print(f"  {label:5s}: {elapsed:.6f} s")


                                    
print("\n=== Call tree for n=5 (naive) ===")
print("""
ways(5)
├─ ways(4)
│  ├─ ways(3)
│  │  ├─ ways(2)
│  │  │  ├─ ways(1) -> 1
│  │  │  └─ ways(0) -> 1
│  │  └─ ways(1) -> 1
│  └─ ways(2)
│     ├─ ways(1) -> 1
│     └─ ways(0) -> 1
└─ ways(3)
   ├─ ways(2)
   │  ├─ ways(1) -> 1
   │  └─ ways(0) -> 1
   └─ ways(1) -> 1
Total calls: 15 (including all leaf nodes)
Each interior node is a repeated sub-problem — memoisation avoids this.
""")


                                              
print("=== Alternative: loop keeping last two values ===")
print("  Time: O(n) for both memo and loop.")
print("  Space: memo O(n) cache + O(n) stack; loop O(1) space, O(1) stack.")
print("  For n=1000, loop is safest: no recursion limit, minimal memory.")