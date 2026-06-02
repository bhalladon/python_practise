# # def numbers():
# #     return [1,2,3]
# #
# # print(numbers())
# #
# # def numbers1():
# #     yield 1
# #     yield 2
# #     yield 3
# #
# #
# # gen = numbers1()
# # print(next(gen))
# # print(next(gen))
# #
# # def count(num):
# #     for i in range(num):
# #         yield i
# #
# # gen = count(5)
# #
# # print(next(gen))
# # print(next(gen))
#
# import sys
#
# list_num = [x for x in range(100000)]
#
# gen_num = (x for x in range(100000))
#
# print(sys.getsizeof(list_num))
# print(sys.getsizeof(gen_num))
#
# print(next(gen_num))
# print(next(gen_num))
import os


# Practical example of generators
def fibbonaci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b
fib = fibbonaci(10)
print(next(fib))

# Another example
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
large_file_generator = read_large_file(os.path.join(os.getcwd(), "..", "main.py" ))

list1 = [1,2,3,4,5,1]






