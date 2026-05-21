# find the remainder when a positive number X s divided with a positive number Y.
# Not allowed to use /, ,, or %

def find_remainder(x: int, y: int) -> int:
    while x >= y:
        x -= y
    return x
print(find_remainder(10, 3))
