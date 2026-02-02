"""
Description:

- Write a Python program that creates and displays a dictionary that maps each letter in a
string to how many times the character occurs in the string (its frequency).

- The dictionary should only include the characters in the string.

- The test should be case-insensitive ("A" should be counted as "a").

- The keys in the dictionary should be lowercase letters.

- Only include letters in the dictionary.
"""

import string

text = "Hello, World!"

letters_dict = {}

for letter in text.lower():
    if letter in string.ascii_lowercase:  # if letter.isalpha
        if letters_dict.get(letter):
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

print(letters_dict)
