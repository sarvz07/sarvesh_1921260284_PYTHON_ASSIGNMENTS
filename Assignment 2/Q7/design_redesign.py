"""Q7 — Diagnose, redesign and validate.

Chosen problem: Q6 (counting ways to climb stairs) using plain recursion.
The bottleneck is repeated work because it recalculates the same subproblems.
"""

from functools import lru_cache


# Original version: repeated work
calls_naive = 0

def ways_naive(n):
    global calls_naive
    calls_naive += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


# Redesigned version: keep only the last two values

def ways_iterative(n):
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


print("A. Diagnose the bottleneck")
for n in [10, 20, 25, 30]:
    calls_naive = 0
    result = ways_naive(n)
    print(f"n={n}: naive result={result}, naive calls={calls_naive}")

print("\nB. Design objective")
print("Objective: reduce the number of redundant recursive calls while preserving the exact result for all valid n.")
print("The repeated work is caused by the same subproblems being solved again and again in the recursion tree.")

print("\nC. Revised solution")
print("We replace the recursive tree with a bottom-up iteration that keeps only the last two values.")
print("This exploits the fact that each new value depends only on the previous two values, so we do not need a cache or recursion stack.")
print("Extra memory: O(1) and time: O(n).")

print("\nD. Prediction before implementation")
print("Expected improvement: the iterative version should keep the same result while reducing the work from exponential to linear.")

print("\nE. Implement and validate")
for n in [10, 20, 25, 30]:
    original = ways_naive(n)
    redesigned = ways_iterative(n)
    print(f"n={n}: original={original}, redesigned={redesigned}, match={original == redesigned}")

print("\nF. Final assessment")
print("The redesigned solution satisfies the objective: it is much faster as n grows and uses O(1) extra space. The original recursion is still useful for understanding the problem and for small n, but it does not scale well.")
