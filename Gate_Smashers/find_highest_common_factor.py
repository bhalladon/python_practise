def find_highest_common_factor(num1: int, num2: int):
	hcf = 0
	if num1 < num2:
		for i in range(1,num1+1):
			if num1%i == 0 and num2 % i == 0:
				if i > hcf:
					hcf = i
	else:
		for i in range(1, num2+1):
			if num1%i == 0 and num2%i == 0:
				if i > hcf:
					hcf = i
	return hcf

print(find_highest_common_factor(100,10))