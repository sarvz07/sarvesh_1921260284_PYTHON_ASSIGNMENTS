def attendance_summary(rows):
    summary = {}
    for student, status in rows:
        summary.setdefault(student, {'present': 0, 'absent': 0})
        if status == 'P':
            summary[student]['present'] += 1
        else:
            summary[student]['absent'] += 1
    return summary

rows = [('Asha', 'P'), ('Ravi', 'A'), ('Asha', 'P'), ('Ravi', 'P'), ('Asha', 'A')]
print(attendance_summary(rows))
print('This solves the attendance problem by summarising data without mixing business rules with file logic.')
