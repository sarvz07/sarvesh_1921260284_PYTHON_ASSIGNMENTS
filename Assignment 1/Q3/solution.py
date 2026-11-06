                                                       
                                                                                       
                                                 
                                                                                          


def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)."""
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()
    return text


def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
    n = len(reg)
    if n not in (9, 10):
        return False
    state = reg[:2]
    district = reg[2:4]
    series = reg[4:5] if n == 9 else reg[4:6]
    digits = reg[5:] if n == 9 else reg[6:]

    return (
        all(c.isalpha() for c in state)
        and all(c.isdigit() for c in district)
        and all(c.isalpha() for c in series)
        and all(c.isdigit() for c in digits)
    )


def format_receipt(reg):
    """Format a valid number as 'TN 09 AB 1234'."""
    if not is_valid(reg):
        return f"INVALID: {reg}"
    n = len(reg)
    state = reg[:2].upper()
    district = reg[2:4]
    series = reg[4:5] if n == 9 else reg[4:6]
    digits = reg[5:] if n == 9 else reg[6:]
    return f"{state} {district} {series} {digits}"


                                                                    
samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB",
           "DL-01-X-0001", "TN221234AB"]

print(f"{'raw':22} -> {'normalised':12} {'valid':6}  receipt")
print("-" * 58)
for raw in samples:
    reg = normalise(raw)
    valid = is_valid(reg)
    rcpt = format_receipt(reg) if valid else "REJECTED"
    print(f"{raw:22} -> {reg:12} {str(valid):6}  {rcpt}")


                                             
print("\n--- Inquiry: immutability ---")
text = "tn 09 ab 1234"
print(f"original text after upper(): {text!r}")
t2 = text.upper()
print(f"text.upper() result: {t2!r} | text unchanged: {text!r}")
print("Strings are immutable: upper() creates a NEW string; it does not change text.")

print("\nSlicing behaviour:")
for s in ["TN09AB1234", "TN09A0007"]:
    print(f"s={s!r} (len={len(s)})  s[-4:]={s[-4:]!r}   s[4:-4]={s[4:-4]!r}")
print("For a 9-char number: s[-4:] is last 4 digits, s[4:-4] is just the series letter.")
print("For a 10-char number: s[-4:] is last 4 digits, s[4:-4] contains series+1 extra digit.")


                               
                                      
                                      
                                        
                                        
