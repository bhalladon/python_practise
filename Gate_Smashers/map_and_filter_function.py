"""
Map and Filter functions
Syntax: map(function, iterable)
Filter: filter(function, iterable)
Example: map(lambda x: x**2, range(5))
Example: filter(lambda x: x%2 == 0, range(5))
Output: [0, 1, 4, 9, 16]
Output: [0, 2, 4]
The map() function applies a given function to each item of an iterable (like a list or tuple) and returns a map object (which is an iterator).
The filter() function constructs an iterator from elements of an iterable for which a function returns true.
"""

x = list(map(lambda y: y*2, range(1,11)))
# for num in x:
#     print(num)

# Filter example
y = list(filter(lambda x: x % 2 != 0, range(1, 11)))
print(y)
print(x)


