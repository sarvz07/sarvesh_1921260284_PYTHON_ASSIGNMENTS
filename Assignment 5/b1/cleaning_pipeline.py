import sqlite3
from pathlib import Path

rows = [
    {'date': '2024-01-01', 'station': 'A', 'pm25': '12', 'temp_c': '26'},
    {'date': '2024-01-02', 'station': 'A', 'pm25': 'NaN', 'temp_c': '30'},
    {'date': '2024-01-03', 'station': 'B', 'pm25': '1001', 'temp_c': '31'},
]

cleaned = []
for row in rows:
    out = {k:None if v in ('', 'NaN', None) else v for k,v in row.items()}
    if out['pm25'] is not None:
        pm = float(out['pm25'])
        if pm < 0 or pm > 999:
            out['pm25'] = None
    cleaned.append(out)

print('Raw rows:', rows)
print('Cleaned rows:', cleaned)

db_path = Path(__file__).resolve().parent.parent / 'database' / 'air_quality.db'
db_path.parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS readings')
cur.execute('CREATE TABLE readings (date TEXT, station TEXT, pm25 REAL, temp_c REAL)')
cur.executemany('INSERT INTO readings VALUES (?, ?, ?, ?)', [(r['date'], r['station'], r['pm25'], r['temp_c']) for r in cleaned])
print('Database rows:', cur.execute('SELECT COUNT(*) FROM readings').fetchone()[0])
conn.close()
