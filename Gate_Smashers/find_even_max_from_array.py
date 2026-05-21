array = [4,6,8,1,3,40]
# max_num = array[0]

for i in array:
	if i > array[0]:
		array[0] = i

print(array[0])

array = [4,6,8,1,3,40]
min_num, max_num = array[0], array[0]

for num in array:
	if num > max_num:
		max_num = num
	elif num < min_num:
		min_num = num

print(min_num, max_num)
