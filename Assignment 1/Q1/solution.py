
def decide_separate(units, ration=True, older=False):
    """Each if is evaluated independently. Possible outcomes are collected (may contain
    several entries if branch logic ever overlaps)."""
    results = []
    if units <= 100:
        results.append(("full", units))
    if 101 <= units <= 200 and ration:
        results.append(("partial", units))
    if units > 200 and older:
        results.append(("none", units))
    return results


def decide_elif(units, ration=True, older=False):
    """Only the first matching branch is taken; exactly one outcome."""
    if units <= 100:
        return "full", units
    if 101 <= units <= 200 and ration:
        return "partial", units
    if units > 200 and older:
        return "none", units
    return "none", units


households = [
    (100, True, False),                                   
    (101, True, False),                             
    (200, True, False),                          
    (201, True, False),                              
    (201, True, True),                                                             
    (150, False, False),                                 
    (50,  False, False),                    
    (150, True,  True),                                       
]

print("Household  units | ration | older | decide_separate           decide_elif")
print("-" * 78)
rows = []
for i, (u, r, o) in enumerate(households, 1):
    sep = decide_separate(u, r, o)
    e1 = ", ".join("%s(%s)" % (x[0], x[1]) for x in sep)
    e2 = decide_elif(u, r, o)[0]
    rows.append((i, u, r, o, sep, e2))
    print(f"{i:<3} | {u}  | {r!s:5} | {o!s:4} | [{e1}]          [{e2}]")

print("\nObservation: for all eight households the two designs return the same single")
print("outcome. The if–elif–else form guarantees exactly one result even when future")
print("requirements cause two branches to overlap, whereas each separate if would start")
print("adding outcomes independently (producing duplicates / multiple subsidies).")


                                                          
def decide_boolean(units, ration=True, older=False):
    """Combined Boolean condition (readability / easy change for tiered rules)."""
    tier_low = units <= 100
    tier_mid = 101 <= units <= 200
    has_ration = ration
    is_old = older
    result = "none"
    if tier_low and has_ration and is_old:
        result = "full"                                                        
    elif tier_mid and has_ration:
        result = "partial"
    elif units > 200 and is_old:
        result = "none"
    return result

                                                      
for (u, r, o) in households:
    print(f"houses_{u}{r}{o}: boolean={decide_boolean(u, r, o)}")

                                                                                          
import time
N = 200000
conditions_list = []
start = time.perf_counter()
chosen = min(set(range(1, 101)), key=lambda k: time.perf_counter() - start)
end = time.perf_counter()
print("\nPreliminary: branch orderisation cost is negligible for few slabs, but matters when")
print("requirements grow into many tiers. match–case would scale linearly with k:")
print("  per-decision O(k) (each case checked until a guard matches).")
print("\nDecision kept: combine the band condition with a Boolean `and`; nest an if only")
print("when a sub-policy inside a tier is itself conditional. This stays readable and easy to")
print("extend, and the elif chain remains the single-decision backbone.")