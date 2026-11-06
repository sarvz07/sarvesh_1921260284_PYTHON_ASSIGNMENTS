                                       
                                                                              
                                                                                       
                                                                             

import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
                                              
    return "".join(p + ";" for p in parts)


def run_timing(func, data, label):
    start = time.perf_counter()
    result = func(data)
    elapsed = time.perf_counter() - start
    print(f"{label}: {elapsed:.4f} s  (len={len(result)})")
    return elapsed


print("=== 200,000 items (single run) ===")
t1 = run_timing(build_plus, items, "+=")
t2 = run_timing(build_join, items, "join")
print(f"same text: {build_plus(items) == build_join(items)}")
print(f"+= time: {t1:.4f} s   join time: {t2:.4f} s\n")

                                                       
sizes = [1_000, 10_000, 200_000]
print("=== Three runs at each size (averaged) ===")
for sz in sizes:
    data = [f"Item{i}:Rs{i % 50}" for i in range(sz)]
    plus_times = []
    join_times = []
    for run in range(3):
        start = time.perf_counter()
        a = build_plus(data)
        plus_times.append(time.perf_counter() - start)
        start = time.perf_counter()
        b = build_join(data)
        join_times.append(time.perf_counter() - start)
        assert a == b
    print(f"size={sz:7d}  += avg={sum(plus_times)/3:.4f}s  join avg={sum(join_times)/3:.4f}s")


                                                                    
print("\n=== Alternative: io.StringIO (in-memory buffer) ===")
from io import StringIO

def build_stringio(parts):
    buf = StringIO()
    for p in parts:
        buf.write(p + ";")
    return buf.getvalue()

for sz in [1_000, 10_000, 200_000]:
    data = [f"Item{i}:Rs{i % 50}" for i in range(sz)]
    start = time.perf_counter()
    c = build_stringio(data)
    t_io = time.perf_counter() - start
    print(f"size={sz:7d}  StringIO: {t_io:.4f}s  (same text: {c == build_join(data)})")

print("\n=== Alternative: writing directly to file ===")
import os
tmp_file = "statement.tmp"
for sz in [1_000, 10_000, 200_000]:
    data = [f"Item{i}:Rs{i % 50}" for i in range(sz)]
    start = time.perf_counter()
    with open(tmp_file, "w", encoding="utf-8") as f:
        for p in data:
            f.write(p + ";")
    t_file = time.perf_counter() - start
                   
    with open(tmp_file, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"size={sz:7d}  file write: {t_file:.4f}s  (same text: {content == build_join(data)})")
os.remove(tmp_file)


                                                   
print("\n--- Inquiry ---")
print("1. Strings are immutable in Python. 'text += p' creates a brand new string object")
print("   copying all characters seen so far. Repeated += can be O(n²) total characters copied.")
print("2. CPython optimises += when the string's reference count is 1 (no other alias) by")
print("   mutating the underlying buffer in place — making it appear O(n). But this is an")
print("   implementation detail, not guaranteed. Other implementations (PyPy, MicroPython)")
print("   may not have this optimisation.")
print("3. ''.join(parts) is always O(total length): it computes total size once, allocates")
print("   one buffer, and copies each part exactly once. It is the recommended, portable")
print("   way to concatenate many strings.")
print("4. Memory: += builds a growing chain of temporary strings (peak memory ~ O(n²) without")
print("   the CPython optimisation). join() allocates exactly one final buffer (+ list of parts).")