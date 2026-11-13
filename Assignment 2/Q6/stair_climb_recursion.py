"""Q6 — Climbing steps with recursion and memoisation.

A person can climb 1 or 2 steps at a time. We count the number of ways to reach
n steps.
"""

import sys
from functools import lru_cache

calls = 0


def ways_naive(n):
    """Plain recursion with repeated subproblems."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    """Memoised recursion; it reuses proven results and avoids repetition."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


print("Checking values for n = 1..6")
for n in range(1, 7):
    print(f"n={n}: naive={ways_naive(n)}")
    calls = 0

print("\nComparison for n = 25")
calls = 0
print("naive:", ways_naive(25), "calls =", calls)
calls = 0
print("memo :", ways_memo(25), "calls =", calls)

print("\nRecursion limit check")
print("Current recursion limit:", sys.getrecursionlimit())
try:
    print("ways_memo(1000) =", ways_memo(1000))
except RecursionError:
    print("RecursionError: the recursive call depth exceeds Python's recursion limit.")
    print("A loop-based version is better for large n because it uses O(1) extra space.")

print("\nLoop-based redesign")
def ways_iterative(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

for n in [1, 2, 5, 10, 25, 1000]:
    print(f"n={n}: iterative={ways_iterative(n)}")
