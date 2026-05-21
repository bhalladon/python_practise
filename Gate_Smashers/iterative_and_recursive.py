def iterative(n):
    total = 0
    for i in range(n):
        print(i)
        total += 2 ** i
    return total

print(iterative(5))


def recursive(n):
    total = 0
    for i in range(n):
        print(i)
        total += 2 ** int(len(n) -i - 1)
    return total

print(iterative(5))