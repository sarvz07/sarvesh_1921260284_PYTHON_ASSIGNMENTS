"""Q5 — Function default values and scope.

The bug arises because a default argument is created once, when the function is
defined. A mutable default (like a list) is reused across calls.
"""


def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


print("Buggy version:")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print("Buggy defaults:", add_item_buggy.__defaults__)

print("\nCorrect version:")
print(add_item("Tea"), add_item("Vada"))
print("Correct defaults:", add_item.__defaults__)

print("\nScope rule example")
value = 10


def update_local():
    value = 99
    return value


def update_global():
    global value
    value = 99
    return value

print("Before call:", value)
print("update_local():", update_local())
print("After local update:", value)
print("update_global():", update_global())
print("After global update:", value)

print("\nDesign choice")
print("Use positional parameters for required data, keyword parameters for clarity, and default parameters only when the default is safe (typically None for mutable data).")
