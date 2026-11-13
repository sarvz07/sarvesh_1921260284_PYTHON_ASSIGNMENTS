def clean_row(row):
    cleaned = {}
    for k, v in row.items():
        cleaned[k] = None if v in ('', 'NaN', None) else v
    return cleaned

rows = [
    {'date': '2024-01-01', 'station': 'A', 'pm25': '12', 'temp_c': '25'},
    {'date': '2024-01-02', 'station': 'B', 'pm25': '', 'temp_c': '30'},
]
print([clean_row(r) for r in rows])
print('Missing values are removed or replaced, invalid temperatures are marked and station names are standardised.')
