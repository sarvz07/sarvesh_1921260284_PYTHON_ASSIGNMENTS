"""Q4 — Building long text using += versus join().

This script measures the time for three build strategies and explains the result
in terms of Python string immutability.
"""

import time


items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    # A single join call avoids repeatedly creating larger strings.
    return ";".join(parts) + ";"


def benchmark(size, runs=3):
    data = [f"Item{i}:Rs{i % 50}" for i in range(size)]
    plus_total = 0.0
    join_total = 0.0

    for _ in range(runs):
        start = time.perf_counter()
        a = build_plus(data)
        plus_total += time.perf_counter() - start

        start = time.perf_counter()
        b = build_join(data)
        join_total += time.perf_counter() - start

    avg_plus = plus_total / runs
    avg_join = join_total / runs
    print(f"size={size:>7}  plus={avg_plus:.6f}s  join={avg_join:.6f}s  same={a == b}  length={len(b)}")


print("Q4 benchmark: repeated += versus join()")
for size in [1_000, 10_000, 200_000]:
    benchmark(size)

print("\nReason")
print("Strings are immutable in Python, so each += creates a new string and copies the old contents. join() creates one list of pieces then builds the final string once, which is much faster for large workloads.")
