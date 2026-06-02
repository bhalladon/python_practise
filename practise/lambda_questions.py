# lambda with map
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)

even_numes_first_ten = list(map(lambda x: x * 2, range(1, 11)))
print(even_numes_first_ten)

# lambda with filter()
even_numes_first_ten = list(filter(lambda x: x % 2 != 0, range(1, 21)))
print(even_numes_first_ten)

# sorted data
data = [(1, 5), (2, 1), (4, 3)]
result = sorted(data, key=lambda x: x[1], reverse=True)
print(result)

data = {
    "a": 5,
    "b": 1,
    "c": 3
}

result = sorted(data.items(), key=lambda x: x[1])
sorted_dict = {}
for k, v in result:
    sorted_dict[k] = v

print(sorted_dict)

# Nested lambda functions
multiply = lambda x: lambda y: x * y
