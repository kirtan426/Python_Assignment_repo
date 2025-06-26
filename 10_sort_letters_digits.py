# Use list comprehensions.
# isalpha() and isdigit() filters.
# Sort both and join.

def separate_sort(s):
    letters = sorted([c for c in s if c.isalpha()])
    digits = sorted([c for c in s if c.isdigit()])
    return ''.join(letters + digits)

print(separate_sort("B4A1D3"))
