from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'day': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'pm25': [22, 35, 30],
    'temp_c': [18, 21, 20],
    'station': ['A', 'A', 'B']
})

plt.plot(df['day'], df['pm25'])
plt.title('Daily PM2.5 trend')
plt.xlabel('Day')
plt.ylabel('PM2.5')
plt.tight_layout()
out = Path(__file__).resolve().parent.parent / 'charts' / 'daily_pm25.png'
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out)
print('Chart saved to', out)
print('Line charts show trends; bar charts compare stations; scatter plots show relationships with temperature.')
