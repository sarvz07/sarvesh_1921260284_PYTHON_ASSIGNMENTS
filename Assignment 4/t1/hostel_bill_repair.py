from pathlib import Path

def read_bills(filename):
    rows = []
    rejected = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_no, line in enumerate(f, 1):
                if not line.strip():
                    continue
                name, amount = line.strip().split(',', 1)
                try:
                    val = float(amount.strip())
                except ValueError:
                    rejected.append((line_no, 'bad_amount', line.strip()))
                    continue
                rows.append((name.strip(), val))
    except FileNotFoundError:
        print(f'File not found: {filename}')
        return [], []
    return rows, rejected

Path('sample.csv').write_text('Asha,120.50\nRavi,75\nBad,abc\n', encoding='utf-8')
print(read_bills('sample.csv'))
print('The repaired version uses with, line-by-line reading, specific exceptions and an error list to prevent silent corruption.')
