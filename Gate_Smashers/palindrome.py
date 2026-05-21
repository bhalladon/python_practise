def check_palindrome(string: str):
    rev = ""
    for i in range(len(string)):
        rev += string[(len(string) - 1 - i)]
    print(f"reverse string is: {rev}")
    if string == rev:
        print("String is palindrome")
    else:
        print("String is not palindrome")

check_palindrome("radar")

# Another way to reverse a string
string1 = "hello"
rev = ''

for char in string1:
    rev = char + rev
    # rev = rev+ char
print(rev)

