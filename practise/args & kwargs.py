# args example

def sum_of_numbers(*args):
    print(args)
    print(type(args))
    total = 0
    for num in args:
        total += num
    print(total)
    return total

sum_of_numbers(5)
sum_of_numbers(5,6,7,8)

# Another example of args


def multiply(*args):
    total = 1
    print(args)
    for num in args:
        total *= num
    return total
print(multiply(2, 3, 4, 5,10))

# Example of Kwargs

def my_function(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
my_function(name="Alice", age=30, city="New York")
