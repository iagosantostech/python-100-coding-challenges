"""
Description:

- Write a Python program to count the number of repeated characters in the string s.
"""

text = input("Type something: ")

letters_dict = {}

for letter in text.lower():
    if letters_dict.get(letter):
        letters_dict[letter] += 1
    else:
        letters_dict[letter] = 1

text_doesnt_have_repeated_chars = True
for key, value in sorted(letters_dict.items()):
    if value > 1:
        print(
            f"Character {key if key != ' ' else 'space'} appears {value} in the text."
        )
        text_doesnt_have_repeated_chars = False

if text_doesnt_have_repeated_chars:
    print("Text doesn't have repeated characters.")
