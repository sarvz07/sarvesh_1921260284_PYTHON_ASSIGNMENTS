import sqlite3
from pathlib import Path

print('Air quality CSV fields: date, station, pm25, temp_c, humidity, aqi')
print('Missing values, invalid values, negative readings and impossible values should be flagged before analysis.')

db_path = Path(__file__).resolve().parent.parent / 'database' / 'air_quality.db'
db_path.parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS readings')
cur.execute('DROP TABLE IF EXISTS stations')
cur.execute('CREATE TABLE stations (station_id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
cur.execute('CREATE TABLE readings (reading_id INTEGER PRIMARY KEY, station_id INTEGER, day TEXT, pm25 REAL, temp_c REAL, humidity REAL)')
print('Schema created.')
conn.close()
print('CSV is useful for raw data export; SQL helps with filtering and aggregation.')
