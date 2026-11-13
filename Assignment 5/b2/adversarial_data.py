import sqlite3

name = "O'Connor"
print('Unsafe SQL:', f"SELECT * FROM stations WHERE name = '{name}'")

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE stations (name TEXT)')
cur.execute("INSERT INTO stations VALUES (?)", ("O'Connor",))
print('Safe query result:', cur.execute('SELECT name FROM stations WHERE name = ?', ("O'Connor",)).fetchall())
print('This demonstrates the need for parameterised SQL and safe handling of tricky inputs.')
