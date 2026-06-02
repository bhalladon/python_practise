# def decorator(func):
#     def wrapper():
#         print("before function call")
#         func()
#         print("After function call")
#
#     return wrapper
#
# @decorator
# def greet():
#     print("Hello")
#
# greet()
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         result = func(*args, **kwargs)
#         print("After")
#         return result
#     return wrapper
#
#
# @decorator
# def add(a, b):
#     return a + b
#
#
# print(add(2, 3))
#
# def screenshot_on_failure(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print("Take screenshot")
#             raise e
#     return wrapper

def calculate_function_time(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end - start} seconds")
        return result

    return wrapper


def welcome_message(func):
    def wrapper(*agrs, **kwargs):
        print("Welcome to the my world")
        result = func(*agrs, **kwargs)
        print("Test execution completed")
        return result
    return wrapper


@calculate_function_time
@welcome_message
def sum_of_two_numbers(a, b):
    print("Hello executing function")
    return a + b


f = sum_of_two_numbers(5, 6)
for i in range(f):
    print(i)
