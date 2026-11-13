"""Q3 — Vehicle registration number validator.

Valid numbers are of the form:
  - 2 letters
  - 2 digits
  - 1 or 2 letters
  - 4 digits
Examples: TN09AB1234, KA01M0007
"""


def normalise(text):
    """Remove spaces and hyphens, then convert to uppercase."""
    cleaned = text.replace(" ", "").replace("-", "")
    return cleaned.upper()


def is_valid(reg):
    """Check length and structure using slicing and string methods only."""
    if len(reg) not in (9, 10):
        return False

    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    if not state.isalpha() or not district.isdigit():
        return False
    if not (1 <= len(series) <= 2 and series.isalpha()):
        return False
    if not number.isdigit() or len(number) != 4:
        return False

    return True


def format_receipt(reg):
    """Format a valid registration like: TN 09 AB 1234."""
    if not is_valid(reg):
        return "INVALID"
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"


samples = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "Tn09Ab1234",
    "TN-09-A-1234",
    "TN09AB1234",
]

print("Predictions before execution")
for raw in samples:
    reg = normalise(raw)
    print(f"{raw:15} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")

print("\nReceipt format")
for raw in ["tn 09 ab 1234", "KA-01-M-0007", "Tn09Ab1234"]:
    reg = normalise(raw)
    if is_valid(reg):
        print(f"{raw} -> {format_receipt(reg)}")

print("\nString immutability and slicing")
text = "TN09AB1234"
print("text.upper() ->", text.upper())
print("text itself remains:", text)
print("s[-4:] ->", text[-4:])
print("s[4:-4] ->", text[4:-4])
print("For a 9-character value like TN09AB123, s[-4:] gives 'B123', and s[4:-4] gives 'AB'.")
