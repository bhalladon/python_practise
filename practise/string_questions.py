# Reverse a string
string1 = "hello"
rev_string = ""
for i in range(len(string1)):
    rev_string += string1[len(string1) - i - 1]

print(rev_string)

# Check Palindrome String
string1 = "level1"
rev_string = ""
for i in range(len(string1)):
    rev_string += string1[len(string1) - i - 1]

if string1 == rev_string:
    print(f"String: {string1} is a palindrome.")
else:
    print(f"String: {string1} is not a palindrome.")

# Count Character Occurrences
string1 = "automation"
char_count = {}

for char in string1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# Find Duplicate Characters
string1 = "programming"
duplicates = set()
not_duplicate = []
duplicate = []

for char in string1:
    if string1.count(char) > 1:
        duplicates.add(char)
print(duplicates)

for char in string1:
    if char not in not_duplicate:
        not_duplicate.append(char)
    else:
        duplicate.append(char)
print(duplicate)

# Remove duplicates from string
string = "programming"
new_string = ""

for char in string:
    if char not in new_string:
        new_string += char
print(new_string)

# Count Vowels
s = "automation testing"
vowels = "aeiou"
count = 0
for char in s:
    if char in vowels:
        count += 1
print(count)

# Find first non-repeating character
s = "aabbcddee"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

# Another method
s = "aabbycddee"
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for ch in freq:
    if freq[ch] == 1:
        print("First non repeating character is", ch)
        break

# Check Anagram
# Two strings containing same characters.
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

# Another way to check Anagram using a function
s1 = "listen"
s2 = "silent1"


def check_for_anagram(s1, s2):
    if len(s1) != len(s2):
        print("Not Anagram")
        return False
    for char in s1:
        if char in s2:
            continue
        else:
            print("Not Anagram")
            return False
    print("Anagram")
    return True


check_for_anagram(s1, s2)

# another way to check anagram without function
s1 = "listen"
s2 = "silent"

anagram = True

# first condition
if len(s1) != len(s2):
    print("strings are not anagram")

# Check second condition
for char in s1:
    if char in s2:
        continue
    else:
        print("Strings are not anagram")
        anagram = False
        break

if anagram:
    print("Strings are anagram")

# Replace spaces with Hyphen
s = "python automation"
print(s.replace(" ", "-"))

# count words in String
s = "python automation testing"
words = s.split(" ")
print(len(words))

# Find Longest Word
s = "python automation with playwright1"
words = s.split(" ")
longest_word = words[0]
for i in range(len(words)):
    if len(words[i]) > len(words[0]):
        words[0] = words[i]
print(words[0])

# Another way
s = "python automation with playwright gerfgertferterter"
words = s.split(" ")

for i in range(0, len(words) - 1):
    if len(words[0]) < len(words[i + 1]):
        words[0] = words[i + 1]
print("Longest word is", words[0])

####################################################
# Remove special characters
import re

s = "py@thon#123!"
result = re.sub(r'[^a-zA-Z0-9]', '', s)
print(result)

# Capitalize First Letter of Every Word
s = "python automation"
print(s.title())

# Find frequency of each word
s = "python java python"
words = s.split(" ")

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

# Sort Characters in String using Bubble Sort
s = "python"
# print("".join(sorted(s)))

chars = list(s)
n = len(chars)
for i in range(n):
    for j in range(0, n - i - 1):
        # compare character ascii values
        if chars[j] > chars[j + 1]:
            # swap characters
            chars[j], chars[j + 1] = chars[j + 1], chars[j]
print("".join(chars))

# Check String Contains Only Digits
s = "12345"


def check_string_contains_only_digit(s):
    for ch in s:
        try:
            if type(int(ch)) != int:
                print("Contains non digit also")
                return False
            continue
        except ValueError:
            print("Contains non digit also")
            return False
    print("Contains all digits")
    return True


# Another way
s = "addff"
new_list = all(ch in "0123456789" for ch in s)
print(new_list)

# Another way
s = "12345sd"
new_list = [ch in "0123456789" for ch in s]
print(new_list)
if False in new_list:
    print("non digit")
else:
    print("digits only")

# Reverse words in Sentence
s = "python automation testing"
# expected output: testing automation python
word = s.split(" ")

rev_str = ""

for i in range(len(word)):
    rev_str += " " + word[len(word) - i - 1]
print(rev_str.lstrip())

# Find Maximum occurring character
s = "automation"
max_char = max(set(s), key=s.count)
print(max_char)

# Another way
s = "automation"
count_chars = {}

for ch in s:
    if ch in count_chars:
        count_chars[ch] += 1
    else:
        count_chars[ch] = 1

max_char = ''
max_count = -1

for char in count_chars:
    if count_chars[char] > max_count:
        max_count = count_chars[char]
        max_char = char

print(max_char)

# Longest substring without repeating characters
s = "pwwkeghw"
new_s = ""
temp_list = []
for ch in s:
    if ch not in new_s:
        new_s += ch
    else:
        temp_list.append(new_s)
        new_s = ch
        continue

max_len = len(temp_list[0])
for i in range(len(temp_list)):
    if len(temp_list[i]) > max_len:
        max_len = len(temp_list[i])

print(max_len)

# String Compression
str1 = "aaabbc"
# expected_output = a3b2c1
str2 = ""

dict1 = {}

for ch in str1:
    if ch in dict1:
        dict1[ch] += 1
    else:
        dict1[ch] = 1

for key, value in dict1.items():
    str2 += str(key) + str(value)

print(str2)
