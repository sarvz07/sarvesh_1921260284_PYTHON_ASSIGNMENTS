                                      
                                                                                  
                                                             

                       
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


                           
def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


print("=== Bug demonstration ===")
print("add_item_buggy('Tea'), add_item_buggy('Vada'):")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print()
print("add_item('Tea'), add_item('Vada'):")
print(add_item("Tea"), add_item("Vada"))

print("\nBuggy defaults after calls:", add_item_buggy.defaults)
print("The default list object is SHARED — both calls mutate the same list.")


                                                 
print("\n=== Three customers (sequential) ===")
cust1 = add_item("Tea")
cust2 = add_item("Vada")
cust3 = add_item("Samosa")
print("Customer 1:", cust1)
print("Customer 2:", cust2)
print("Customer 3:", cust3)
print("Each order is independent: no item leaks across customers.")


                                                 
def make_order(item, qty=1, *, discount=0):
    """item is positional/keyword; qty has default; discount is keyword-only."""
    return f"{item} x{qty} @{100 - discount}%"


print("\n=== Parameter styles ===")
print("make_order('Tea'):", make_order("Tea"))
print("make_order('Coffee', 2):", make_order("Coffee", 2))
print("make_order('Juice', qty=3):", make_order("Juice", qty=3))
print("make_order('Tea', discount=10):", make_order("Tea", discount=10))


                                                   
def bill(total, gst_rate=0.18):
    """Returns a tuple: (total_without_gst, gst_amount, grand_total)."""
    gst = round(total * gst_rate, 2)
    return total, gst, total + gst


print("\n=== Multiple return values ===")
t, g, gt = bill(100)
print(f"total={t}, gst={g}, grand_total={gt}")


                                        
global_counter = 0

def scope_demo():
    local_var = "local"
    global global_counter
    global_counter += 1
    print(f"  inside scope_demo: local_var={local_var}, global_counter={global_counter}")

def outer():
    x = "enclosing"
    def inner():
        nonlocal x
        x = "modified"
        print(f"  inside inner: x={x}")
    inner()
    print(f"  after inner: x={x}")

print("\n=== Scope demonstration ===")
scope_demo()
print("global_counter after call:", global_counter)
outer()
print("global_counter after outer:", global_counter)


                                                  
def change_global_wrong():
    x = 10                       

def change_global_right():
    global global_counter
    global_counter = 42

print("\n=== Global assignment ===")
print("Before change_global_right:", global_counter)
change_global_right()
print("After change_global_right:", global_counter)


                             
print("\n=== Alternative: closure (per-customer order) ===")
def make_order_taker():
    """Returns a function that keeps its own private order list."""
    order = []
    def add(item):
        order.append(item)
        return order
    return add

cust_a = make_order_taker()
cust_b = make_order_taker()
print("cust_a('Tea'):", cust_a("Tea"))
print("cust_a('Vada'):", cust_a("Vada"))
print("cust_b('Samosa'):", cust_b("Samosa"))
print("Closure gives each customer its own list — no shared default.")


print("\n=== Alternative: caller passes explicit list ===")
def add_item_explicit(item, order):
    """Caller MUST provide a list; no default."""
    order.append(item)
    return order

order1 = []
order2 = []
add_item_explicit("Tea", order1)
add_item_explicit("Vada", order2)
print("order1:", order1)
print("order2:", order2)
print("Explicit passing removes ambiguity about who owns the list.")