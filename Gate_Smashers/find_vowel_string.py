def print_vowels_from_a_given_string(string: str):
	vowels = ['a','e','i','o','u']
	vowel_str = ""
	for char in string.lower():
		if char in vowels:
			vowel_str += char
	return vowel_str

print(print_vowels_from_a_given_string("HELLO"))
