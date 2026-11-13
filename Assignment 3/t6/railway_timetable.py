from pprint import pprint

train_schedule = {
    'T1': {'Mon': [('Chennai', '08:00'), ('Vellore', '09:15')], 'Tue': [('Chennai', '08:00'), ('Coimbatore', '11:30')]},
    'T2': {'Mon': [('Madurai', '09:00'), ('Coimbatore', '12:00')], 'Wed': [('Salem', '10:00')]},
    'T3': {'Tue': [('Chennai', '07:30'), ('Salem', '09:45')]},
}

def find_trains(schedule, station, day):
    matches = []
    for train, days in schedule.items():
        for stop, departure in days.get(day, []):
            if stop == station:
                matches.append((train, departure))
    return sorted(matches, key=lambda item: item[1])

print('Chennai on Mon:', find_trains(train_schedule, 'Chennai', 'Mon'))
print('Salem on Tue:', find_trains(train_schedule, 'Salem', 'Tue'))
print('Unknown station:', find_trains(train_schedule, 'Trichy', 'Mon'))
print('Nested data is suitable for this timetable because each train has day-specific departure records.')
