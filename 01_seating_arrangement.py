# Use backtracking to permute guests in circular order.
# For each permutation, check if every guest is adjacent to both preferred neighbors.

from itertools import permutations

def is_valid(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        guest = arrangement[i]
        left = arrangement[(i-1) % n]
        right = arrangement[(i+1) % n]
        if not (left in preferences[guest] and right in preferences[guest]):
            return False
    return True

def find_seating(guests):
    for perm in permutations(guests.keys()):
        if is_valid(perm, guests):
            return perm
    return "No valid arrangement."

# Sample input
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

print(find_seating(guests))