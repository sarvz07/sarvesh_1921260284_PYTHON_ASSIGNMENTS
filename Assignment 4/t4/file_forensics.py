from pathlib import Path

path = Path('sample_log.txt')
path.write_text('2024-01-01 08:30 login\n2024-01-01 08:40 update\n', encoding='utf-8')
print('File size (bytes):', path.stat().st_size)
print('Extension:', path.suffix)
print('This analysis checks size and extension to understand suspicious file changes.')
