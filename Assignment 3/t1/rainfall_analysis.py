import time


def make_readings(n):
    import random
    random.seed(42)
    return [round(random.uniform(0, 30), 2) for _ in range(n)]


def weekly_totals(readings):
    return [sum(readings[i:i+7]) for i in range(0, len(readings), 7)]


def moving_average(readings, window=7):
    if len(readings) < window:
        return []
    return [sum(readings[i:i+window]) / window for i in range(len(readings)-window+1)]


def moving_average_running(readings, window=7):
    if len(readings) < window:
        return []
    total = sum(readings[:window])
    result = [total / window]
    for i in range(window, len(readings)):
        total += readings[i] - readings[i-window]
        result.append(total / window)
    return result

readings = make_readings(365)
print('First five weekly totals:', weekly_totals(readings)[:5])
print('Max rainfall:', max(readings), 'at', readings.index(max(readings)))
print('Min rainfall:', min(readings), 'at', readings.index(min(readings)))
print('Dry days:', sum(1 for x in readings if x == 0))
print('First five 7-day moving averages:', moving_average(readings)[:5])
print('First five running-sum averages:', moving_average_running(readings)[:5])

for n in (365, 36500, 365000):
    data = make_readings(n)
    start = time.perf_counter(); moving_average(data); t1 = time.perf_counter()-start
    start = time.perf_counter(); moving_average_running(data); t2 = time.perf_counter()-start
    print(f'n={n}: naive={t1:.6f}s, running_sum={t2:.6f}s')

print('Empty list test:', moving_average([], 7))
print('Short list test:', moving_average([1,2,3], 7))
print('This uses a list because indexing is simple and direct. The running-sum version is preferred for large data because it avoids repeated full-window summation.')
