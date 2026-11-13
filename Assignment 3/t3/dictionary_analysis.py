from collections import Counter
import time

stop_words = {'the', 'is', 'a', 'and', 'of', 'to', 'in'}
text = 'The weather is good and the roads are good in the city and the market is busy.'

def count_get(text):
    counts = {}
    for word in text.lower().replace('.', '').split():
        if word in stop_words:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def count_setdefault(text):
    counts = {}
    for word in text.lower().replace('.', '').split():
        if word in stop_words:
            continue
        counts.setdefault(word, 0)
        counts[word] += 1
    return counts

print('count_get:', count_get(text))
print('count_setdefault:', count_setdefault(text))
print('Top words:', sorted(count_get(text).items(), key=lambda item: (-item[1], item[0]))[:3])

for n in (1000, 10000, 100000):
    sample = (' '.join(['the weather is good'] * n))
    start = time.perf_counter(); count_get(sample); t1 = time.perf_counter() - start
    start = time.perf_counter(); sample.split().count('the'); t2 = time.perf_counter() - start
    start = time.perf_counter(); Counter(sample.split()); t3 = time.perf_counter() - start
    print(f'n={n}: dict_get={t1:.6f}s, list_count={t2:.6f}s, Counter={t3:.6f}s')

print('Dictionary search is average O(1); list.count() is O(n).')
