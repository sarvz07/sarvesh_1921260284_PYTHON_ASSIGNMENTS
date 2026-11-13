import re, time

contacts = [
    {'name': 'Asha', 'phone': '+91-98765-43210', 'email': 'ASHA@EXAMPLE.COM'},
    {'name': 'Asha', 'phone': '9876543210', 'email': 'asha@example.com'},
    {'name': 'Ravi', 'phone': '99999-11111', 'email': 'ravi@example.com'},
]

def norm_phone(value):
    digits = re.sub(r'\D', '', str(value))
    return digits[-10:]

def norm_email(value):
    return str(value).strip().lower()


def merge_contacts(items):
    merged = {}
    for item in items:
        key = norm_phone(item.get('phone', ''))
        if not key:
            continue
        merged.setdefault(key, {'name': '', 'phones': set(), 'emails': set()})
        merged[key]['name'] = item.get('name', merged[key]['name'])
        merged[key]['phones'].add(key)
        if item.get('email'):
            merged[key]['emails'].add(norm_email(item['email']))
    return merged

print('Merged contacts:', merge_contacts(contacts))

for n in (1000, 100000):
    sample = [{'name': f'User {i}', 'phone': f'+91-{i:08d}', 'email': f'user{i}@example.com'} for i in range(n)]
    start = time.perf_counter(); merge_contacts(sample); t = time.perf_counter() - start
    print(f'n={n}: {t:.6f}s')

print('Using a dictionary keyed by normalised phone number is faster than comparing every contact with every other contact.')
