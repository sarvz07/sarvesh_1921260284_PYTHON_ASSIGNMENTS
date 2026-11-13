import sqlite3
import time
import pandas as pd

rows = [{'date': f'2024-01-{i:02d}', 'station': f'S{i%3 + 1}', 'pm25': (i * 7) % 40} for i in range(1, 31)]

def mean_python(items):
    summary = {}
    for row in items:
        summary.setdefault(row['date'], []).append(float(row['pm25']))
    return {date: sum(vals)/len(vals) for date, vals in summary.items()}

frame = pd.DataFrame(rows)
print('Python mean sample:', list(mean_python(rows).items())[:3])
print('Pandas mean sample:', frame.groupby('date')['pm25'].mean().head().to_dict())

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE readings (date TEXT, station TEXT, pm25 REAL)')
cur.executemany('INSERT INTO readings VALUES (?, ?, ?)', [(r['date'], r['station'], r['pm25']) for r in rows])
print('SQL mean sample:', cur.execute('SELECT date, AVG(pm25) FROM readings GROUP BY date ORDER BY date LIMIT 3').fetchall())

for n in (1, 12, 120):
    subset = rows[:10*n]
    start = time.perf_counter(); mean_python(subset); t1 = time.perf_counter() - start
    start = time.perf_counter(); pd.DataFrame(subset).groupby('date')['pm25'].mean(); t2 = time.perf_counter() - start
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor(); cur.execute('CREATE TABLE readings (date TEXT, station TEXT, pm25 REAL)'); cur.executemany('INSERT INTO readings VALUES (?, ?, ?)', [(r['date'], r['station'], r['pm25']) for r in subset])
    start = time.perf_counter(); cur.execute('SELECT date, AVG(pm25) FROM readings GROUP BY date').fetchall(); t3 = time.perf_counter() - start
    print(f'n={n}: python={t1:.6f}s, pandas={t2:.6f}s, sql={t3:.6f}s')

print('Pandas and SQL are usually better for large grouped data, while plain Python is clearer for small experiments.')
