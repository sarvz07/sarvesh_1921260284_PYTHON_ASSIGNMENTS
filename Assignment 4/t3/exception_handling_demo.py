def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Division by zero not allowed'

print(safe_divide(10, 5))
print(safe_divide(10, 0))
print('Specific exception handling is safer than a broad except block because it preserves useful error information.')
