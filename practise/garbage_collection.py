import sys, gc
# a = []
# print(sys.getrefcount(a))

# Problem with reference counting - it cannot clean up circular references.
# example

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()

a.ref = b
b.ref = a

# Now a references b
# b references a

# even if"
del a
del b

print(gc.collect())

print(gc.isenabled())

# the objects still reference each other manually
# Reference counts never becomes 9
# This causes a MEMORY LEAK if only reference counting is used.


x = 5
y = x
print(id(x), id(y))

x = x + 1
print(id(x), id(y))
print(y)

z = 5
print(id(z), id(y))




