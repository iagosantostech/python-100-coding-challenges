"""
Description:

- Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A"
should be equivalent to "a").

- If it does, print True. Else, print False.

- Before comparing the characters, you should convert the string to lowercase.

- If the string contains spaces, ignore them before finding the result.

- You may assume that the string doesn't contain numbers or any other symbols, only spaces (possibly).

- Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'
"""

import string

text = input("Type something: ")
text_lower = text.lower()

# Solution 1
alphabet = "abcdefghijklmnopqrstuvwxyz"

letters_in_text = []
for letter in alphabet:
    if letter in text_lower:
        letters_in_text.append(letter)

print(
    "String has all letters of the alphabet."
    if len(alphabet) == len(letters_in_text)
    else "String doesn't have all letters of the alphabet."
)

# Solution 2
set_text = set(text_lower)
set_text.remove(" ")

print(set_text == set(string.ascii_lowercase))

# Solution 3
is_pangram = True
for char in string.ascii_lowercase:
    if char not in text_lower:
        is_pangram = False

print(is_pangram)

# Solution 4
is_pangram = True
for char in string.ascii_lowercase:
    if char not in text_lower:
        is_pangram = False
        break

print(is_pangram)
