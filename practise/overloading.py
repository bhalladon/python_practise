"""
Python Overloading (Complete Guide)

Overloading means having multiple methods/operators with the same name but different behavior based on the arguments or operands.

Unlike Java and C++, Python does not support traditional method overloading directly, but it supports:

Operator Overloading
Constructor Overloading (using default arguments)
Method Overloading (using variable arguments)
Function Overloading (using functools.singledispatch)

"""

"""
1. Operator Overloading

Python allows operators to work differently for custom objects using dunder methods.

Example: + Operator
"""

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary
    def __ge__(self, other):
        return self.salary >= other.salary


e1 = Employee(5000)
e2 = Employee(10000)
print(e1 + e2)
print(e1 - e2)
print(e1 * e2)
print(e1 == e2)
print(e1 > e2)
print(e1 < e2)

"""
Internally how it works:
e1.__add__(e2)
e1.__sub__(e2)
"""

#####################################################################################################

"""
2. Constructor Overloading
Python does not support multiple constructors like Java.
Java Example (Not Possible in Python)
"""
# Python Solution: Default Arguments

class Employee:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


e1 = Employee()
e2 = Employee("Rajiv")
e3 = Employee("Rajiv", 40)

print(e1.name)
print(e2.name)
print(e3.age)
