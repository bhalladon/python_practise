# merge two dictionaries
d1 = {"a":1}
d2 = {"b":2}

result = d1 | d2

print(result)

# . Sort Dictionary by Value
data = {"a":3, "b":1, "c":2}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data)

# Anothwr way of sortiung a dictionary based on value
data = {"a": 3, "b": 1, "c": 2}
# convert the dict into a list of tuples
items = list(data.items())
n = len(items)

# Bubble sort implementation
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print(items)

# Rebuild the dictionary from the sorted items
sorted_dict = {}
for key, value in items:
    sorted_dict[key] = value

print(sorted_dict)
