# Sort inventory by price (low to high).
# Deduct quantity and cost till the budget is exhausted.

def check_order(inventory, order, budget):
    total = 0
    for item, qty in order.items():
        if item not in inventory:
            return "Item not in inventory"
        inv_qty, price = inventory[item]
        if qty > inv_qty:
            return "Partially fulfillable"
        total += qty * price
    return "Fulfilled" if total <= budget else "Over budget"

inventory = {
    'item1': (10, 5),
    'item2': (5, 20)
}
order = {
    'item1': 2,
    'item2': 2
}

print(check_order(inventory, order, 60))
