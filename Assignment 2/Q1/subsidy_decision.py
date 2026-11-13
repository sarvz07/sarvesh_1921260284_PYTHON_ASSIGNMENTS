"""Q1 — Decisions with many boundaries.

The main idea is that separate if-statements can all be true at once,
while an if-elif-else chain stops after the first matching condition.
"""


def subsidy_separate(units, has_ration_card, has_member_over_80):
    """Naive rule written with several separate if statements.

    This can produce multiple results for a single household.
    """
    results = []

    if units <= 100:
        results.append("Full subsidy")
    if 101 <= units <= 200 and has_ration_card:
        results.append("Partial subsidy")
    if units > 200 and has_member_over_80:
        results.append("Senior-citizen exception subsidy")

    return results


def subsidy_if_elif_else(units, has_ration_card, has_member_over_80):
    """Single-result rule using if-elif-else."""
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if has_ration_card:
            return "Partial subsidy"
        return "No subsidy"
    elif has_member_over_80:
        return "Senior-citizen exception subsidy"
    else:
        return "No subsidy"


households = [
    (80, False, False),
    (100, False, False),
    (101, True, False),
    (150, False, False),
    (200, True, False),
    (201, False, False),
    (250, True, False),
    (250, False, True),
]

print("Predictions before execution")
for idx, (units, has_ration, above_80) in enumerate(households, 1):
    print(f"Household {idx}: units={units}, ration={has_ration}, above_80={above_80}")
    print("  separate-if results:", subsidy_separate(units, has_ration, above_80))
    print("  if-elif-else result:", subsidy_if_elif_else(units, has_ration, above_80))

print("\nBoundary check")
for units in [100, 101, 200, 201]:
    print(f"units={units}: {subsidy_if_elif_else(units, True, False)}")

print("\nWhy separate ifs can give multiple results")
example = (250, True, True)
print(f"Example household: {example}")
print("Separate ifs:", subsidy_separate(*example))
print("Single-result rule:", subsidy_if_elif_else(*example))

print("\nDecision structure choice")
print("Using combined Boolean conditions and if-elif-else is easier to read and change because it enforces one outcome per household.")
