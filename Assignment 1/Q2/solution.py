                                
                                                                   
                                                       
                                                             

CORRECT_OTP = "1234"
MAX_ATTEMPTS = 3

                                          
def verify_while(user_inputs):
    """user_inputs is an iterable of strings the user would type.
    Returns (locked, attempts_used, correct_found)."""
    attempts = 0
    locked = False
    correct = False
    it = iter(user_inputs)
    while attempts < MAX_ATTEMPTS:
        try:
            entry = next(it)
        except StopIteration:
            break
        if entry == "":
                                                       
            continue
        attempts += 1
        if entry == CORRECT_OTP:
            correct = True
            break
        if attempts == MAX_ATTEMPTS:
            break
                                                    
    else:
                                                                           
                                                          
        locked = True
    return locked, attempts, correct


                                        
def verify_for(user_inputs):

    attempts = 0
    locked = False
    correct = False
    it = iter(user_inputs)
                                                                            
                                                                    
    for _ in range(MAX_ATTEMPTS):
                                                  
        entry = ""
        while entry == "":
            try:
                entry = next(it)
            except StopIteration:
                return locked, attempts, correct
                                
        attempts += 1
        if entry == CORRECT_OTP:
            correct = True
            break
    else:
                                                             
        locked = True
    return locked, attempts, correct


                                                                    
             
tests = [
    (["1234"],                    "immediate correct"),
    (["", "", "1234"],            "two blanks then correct"),
    (["0000", "1111", "2222"],    "three wrong -> lock"),
    (["", "1111", "", "2222"],    "blank then wrong, blank, wrong -> lock"),
    (["1111", "", "2222"],        "wrong, blank, wrong -> lock"),
    (["0000", "", "", "1234"],    "wrong, two blanks, correct"),
]

print("=== while loop ===")
for inputs, desc in tests:
    locked, used, ok = verify_while(inputs)
    print(f"  {desc:30} locked={locked!s:5} attempts={used} correct={ok!s:5}  inputs={inputs}")

print("\n=== for loop ===")
for inputs, desc in tests:
    locked, used, ok = verify_for(inputs)
    print(f"  {desc:30} locked={locked!s:5} attempts={used} correct={ok!s:5}  inputs={inputs}")


                                                   
print("\n--- Design notes ---")
print("while is more natural when the number of attempts is NOT fixed in advance, e.g.,")
print("if the bank allows 2 extra attempts after a security question, the upper bound")
print("becomes dynamic. A for loop needs the count up front; a while condition can")
print("change during execution.")
print("\nBug if counter updated in wrong place (before blank-check):")
print("  attempts = 0")
print("  while attempts < MAX_ATTEMPTS:")
print("      entry = input()")
print("      attempts += 1   # BUG: blank entry still increments counter")
print("      if entry == '': continue")
print("This wastes attempts on blank lines.")


                                                                                   
print("\n--- Changed Condition: security question grants 2 extra attempts ---")
def verify_while_dynamic(user_inputs):
    """Now max_attempts can grow after a security question."""
    base_max = MAX_ATTEMPTS
    max_attempts = base_max
    attempts = 0
    locked = False
    correct = False
    it = iter(user_inputs)
    while attempts < max_attempts:
        try:
            entry = next(it)
        except StopIteration:
            break
        if entry == "":
            continue
        attempts += 1
        if entry == CORRECT_OTP:
            correct = True
            break
                                                               
        if attempts == base_max and max_attempts == base_max:
                                                          
            max_attempts = base_max + 2
            print(f"    [security question passed -> max_attempts now {max_attempts}]")
    else:
        locked = True
    return locked, attempts, correct


                                                              
inputs = ["0000", "1111", "2222", "3333", "4444"]
locked, used, ok = verify_while_dynamic(inputs)
print(f"  Test: locked={locked} attempts={used} correct={ok}")
print("  while loop naturally supports dynamic max_attempts; for loop would need")
print("  a second loop or a break/continue pattern to re-enter.")