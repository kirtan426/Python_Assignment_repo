# Use condition blocks for each slab.
# Accumulate and print per-slab and total cost.

def calc_bill(units):
    bill = 0
    if units <= 100:
        bill += units * 5
    elif units <= 300:
        bill += 100 * 5 + (units - 100) * 7
    elif units <= 500:
        bill += 100 * 5 + 200 * 7 + (units - 300) * 10
    else:
        bill += 100 * 5 + 200 * 7 + 200 * 10 + (units - 500) * 15
    return bill

usage = 450
print("Electricity Bill:")
print(f"Total Amount Payable = ₹{calc_bill(usage)}")