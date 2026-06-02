# reverse a list
nums = [1, 2, 3, 4]
new_list = []

for i in range(len(nums)):
    new_list.append(nums[len(nums) - i - 1])
print(new_list)

# Find Largest Element
nums = [10, 45, 102, 22, 99]

largest_num = nums[0]

for i in range(1, len(nums)):
    if nums[i] > largest_num:
        largest_num = nums[i]

print(largest_num)

# Find Second largest Number
data = [11, 22, 1, 2, 5, 67, 21, 32]

max1 = data[0]  # largest num
max2 = data[1]  # second largest num

for num in data:
    if num > max1:
        max2 = max1  # Now this number would be second largest
        max1 = num  # This num is largest number in list now.

    # Check with second largest
    elif num > max2:
        max2 = num  # Now this would be second largest.

print(max2)

# Remove Duplicates from List
nums = [1, 2, 2, 3, 4, 4]
unique = list(set(nums))
print(unique)

# Another way to remove duplicates
nums = [1, 2, 2, 3, 4, 4]
unique_list = []

for item in nums:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

# Find Common Elements Between Two Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

list3 = [item for item in list1 and list2]
print(list3)

# Sort list without using inbuilt function sort
nums = [4, 2, 1, 5]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
print(nums)

# Flatten Nested List
nested = [[1, 2], [3, 4], [5, 6]]

flat = [item for sublist in nested for item in sublist]
print(flat)

# Another way of flatten list
nested = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for item in nested:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)
print(flat_list)

# Find Missing Number
nums = [1, 2, 3, 5, 6]
n = 6

missing = sum(range(1, n + 1)) - sum(nums)

print(missing)

# Find Pairs With Given Sum
nums = [1, 2, 3, 4, 5]

target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])

# Find duplicate elements
nums = [1,2,2,3,4,4]
unique = []
duplicate = []

for num in nums:
    if num not in unique:
        unique.append(num)
    else:
        duplicate.append(num)
print(duplicate)

duplicate = set(num for num in nums if nums.count(num) > 1)
print(duplicate)

# Sort List of Tuples by Second Value
data = [(1,4), (2,1), (3,7)]

result = sorted(data, key=lambda x: x[1])
print(result)

# Another way of doing this
data = [(1,4), (2,1), (3,7)]

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i][-1] > data[j][-1]:
            data[i], data[j] = data[j], data[i]
print(data)