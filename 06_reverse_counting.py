
def print_reverse(n):
    if n < 1:
        return
    print(n)
    print_reverse(n - 1)

print_reverse(1000)