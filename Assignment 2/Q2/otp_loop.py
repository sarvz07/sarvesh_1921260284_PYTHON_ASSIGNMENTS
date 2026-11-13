"""Q2 — OTP verification using while and for loops.

The main points:
- blank entries do not count as attempts
- break exits early on success or lockout
- continue skips invalid blank entries without incrementing attempts
- pass marks an intentionally empty branch
- loop-else can lock the account when no break happened
"""


def otp_while(correct_otp, entries):
    attempts = 0
    print("\nwhile-loop design")
    for entry in entries:
        if entry == "":
            print("  blank input ignored; not counted")
            pass
            continue

        attempts += 1
        if entry == correct_otp:
            print(f"  correct OTP entered on attempt {attempts}")
            print("  Access granted.")
            break
        print(f"  wrong OTP, attempt {attempts} of 3")
        if attempts == 3:
            print("  Account locked for 30 minutes.")
            break
    else:
        print("  Account locked for 30 minutes.")


def otp_for(correct_otp, entries):
    print("\nfor-loop design")
    for attempt in range(1, 4):
        entry = entries[attempt - 1] if attempt - 1 < len(entries) else ""
        if entry == "":
            print(f"  attempt {attempt}: blank input ignored; not counted")
            pass
            continue

        if entry == correct_otp:
            print(f"  attempt {attempt}: correct OTP")
            print("  Access granted.")
            break
        print(f"  attempt {attempt}: wrong OTP")
    else:
        print("  Account locked for 30 minutes.")


def otp_with_security_question(correct_otp, entries, security_answer_correct):
    """Extra attempts when the security question is answered correctly."""
    max_attempts = 5 if security_answer_correct else 3
    attempts = 0
    print(f"\nSecurity question answered: {security_answer_correct} -> {max_attempts} total attempts")

    while attempts < max_attempts:
        entry = entries[attempts] if attempts < len(entries) else ""
        if entry == "":
            print("  blank input ignored; not counted")
            attempts = attempts
            continue
        attempts += 1
        if entry == correct_otp:
            print("  Access granted.")
            return True
        if attempts < max_attempts:
            print(f"  wrong OTP, attempt {attempts} of {max_attempts}")
    print("  Account locked for 30 minutes.")
    return False


correct = "4821"
entries = ["", "4821", "1111", "2222"]
print("OTP example with blank entry first")
otp_while(correct, entries)
otp_for(correct, entries)

print("\nExtra attempts after security question")
otp_with_security_question(correct, ["1234", "5678", "4821", "9999", "1111"], True)
print("\nBug explanation")
print("If the counter is incremented in the wrong place, the program may count the same attempt twice or skip a valid attempt. For example, updating attempts before checking for a blank value makes a blank entry count as a failed attempt.")
