import sqlite3

complaints = [
    'good air quality today',
    'bad smell from station',
    'not bad at all',
    'good but not great',
    'awful weather',
    'excellent and clean',
]

def sentiment_score(text):
    pos = {'good': 1, 'clean': 1, 'excellent': 2, 'great': 2}
    neg = {'bad': -1, 'smell': -1, 'awful': -2}
    score = 0
    words = text.lower().split()
    for i, word in enumerate(words):
        if word in pos:
            score += pos[word]
        elif word in neg:
            score += neg[word]
        if i > 0 and words[i - 1] in {'not', 'never'}:
            score *= -1
    return score

for c in complaints:
    s = sentiment_score(c)
    label = 'positive' if s > 0 else 'negative' if s < 0 else 'neutral'
    print(c, '->', label)

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE readings (station TEXT, day TEXT, pm25 REAL)')
for i in range(2000):
    cur.execute('INSERT INTO readings VALUES (?, ?, ?)', (f'S{i % 10}', f'2024-01-{(i % 28) + 1:02d}', i % 50))
cur.execute('CREATE INDEX idx_station_day ON readings(station, day)')
print('Index created on (station, day) for faster lookups.')
print('A production solution should store cleaned data in SQLite, use SQL for summary queries and keep simple AI patterns explainable and testable.')
