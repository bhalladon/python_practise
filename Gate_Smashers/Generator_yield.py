# A generator function looks like a regular function but uses yield instead of return.
# When called, it does not execute the code immediately but returns a generator object.

def creator1():
    print("Starting Program")
    i = 1
    while i<=200:
        yield i
        i = i + 1
    print("exiting program")

for num in creator1():
    while num <= 10:
        print(num*2)
        break



# x = creator1()
# print(next(x)) # print value 1
# print(next(x)) # print next value 2
# print(list(x)) # print list starting from 3-200

# Advantage of generators
# 1. Memory efficient
# 2. Easy implementation

