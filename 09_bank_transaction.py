# Input as a list of tuples: [("credit", 100), ("debit", 50)]
# Maintain running balance.
# Print after each transaction.

def analyze_transactions(transactions):
    balance = 0
    for t in transactions:
        if t['type'] == 'credit':
            balance += t['amount']
        elif t['type'] == 'debit':
            balance -= t['amount']
        print(f"After {t['type']} ₹{t['amount']} -> Balance: ₹{balance}")
    print(f"Final Balance: ₹{balance}")

transactions = [
    {'type': 'credit', 'amount': 1000},
    {'type': 'debit', 'amount': 200},
    {'type': 'credit', 'amount': 500}
]
analyze_transactions(transactions)