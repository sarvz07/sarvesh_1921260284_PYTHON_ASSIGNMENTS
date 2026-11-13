import time

raw = [10, 'bad', 22, -5, 30, 'oops', 28, 19, 50, 90]

def clean_loop(values):
    cleaned = []
    for v in values:
        try:
            temp = float(v)
            if -20 <= temp <= 60:
                cleaned.append(temp)
        except (TypeError, ValueError):
            pass
    return cleaned


def clean_comp(values):
    cleaned = []
    for v in values:
        try:
            temp = float(v)
            if -20 <= temp <= 60:
                cleaned.append(temp)
        except (TypeError, ValueError):
            pass
    return cleaned


def clean_map(values):
    def valid(v):
        try:
            t = float(v)
            return -20 <= t <= 60
        except (TypeError, ValueError):
            return False
    return list(map(float, filter(valid, values)))

print('Loop:', clean_loop(raw))
print('Comprehension:', clean_comp(raw))
print('Map/filter:', clean_map(raw))
print('Fahrenheit for celsius [0,10,25]:', [c * 9 / 5 + 32 for c in [0, 10, 25]])
print('Alarm minutes:', [i for i, v in enumerate([44,45,46,80,90]) if v > 50])

for n in (10000, 100000, 1000000):
    data = [x if x % 7 else 'bad' for x in range(n)]
    start = time.perf_counter(); clean_loop(data); t1 = time.perf_counter()-start
    start = time.perf_counter(); clean_comp(data); t2 = time.perf_counter()-start
    start = time.perf_counter(); clean_map(data); t3 = time.perf_counter()-start
    print(f'n={n}: loop={t1:.6f}s, comp={t2:.6f}s, map={t3:.6f}s')

print('List comprehension is usually the clearest and best choice for this kind of cleaning.')
