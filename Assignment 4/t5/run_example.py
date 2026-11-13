from attendance import reader, stats, report

rows = [('Asha', 'P'), ('Ravi', 'A'), ('Asha', 'P')]
print('Present count:', stats.present_count(reader.read_rows(rows)))
report.print_summary(rows)
print('Python package initialisation uses __init__.py, not init.py.')
