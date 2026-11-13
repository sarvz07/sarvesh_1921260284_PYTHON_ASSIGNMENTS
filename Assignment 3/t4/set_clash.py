import time

cs = {'S101', 'S102', 'S103', 'S104', 'S105'}
ml = {'S103', 'S104', 'S106', 'S107'}

print('Both electives:', sorted(cs & ml))
print('Only CS:', sorted(cs - ml))
print('Only ML:', sorted(ml - cs))

for n in (10000, 100000, 1000000):
    a = set(range(n))
    b = set(range(n//2, n//2 + n//10))
    start = time.perf_counter(); [x for x in a if x in b]; t1 = time.perf_counter() - start
    start = time.perf_counter(); a & b; t2 = time.perf_counter() - start
    print(f'n={n}: nested_list={t1:.6f}s, set_ops={t2:.6f}s')

print('Sets are faster because hash-based membership is close to constant time, unlike nested loops which compare every element.')
