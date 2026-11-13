import re

rows = [('Asha', 'asha@example.com', 'CS'), ('Ravi', 'ravi@example.com', 'IT'), ('Asha', 'asha@example.com', 'CS'), ('Nia', 'bad', 'ME')]

def valid_email(email):
    return bool(re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email))

def clean_rows(items):
    seen = set()
    out = []
    for name, email, dept in items:
        if not valid_email(email):
            continue
        key = (name.lower(), email.lower(), dept.lower())
        if key not in seen:
            seen.add(key)
            out.append((name, email, dept))
    return out

print('Clean registrations:', clean_rows(rows))
print('This validates user input, deduplicates and prepares a clean master list.')
