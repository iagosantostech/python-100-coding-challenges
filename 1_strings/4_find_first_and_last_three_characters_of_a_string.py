"""
Description:

- Write a Python program that prints the first and last three characters of the string s as a single string.

- If the string has less than six characters, print an empty string (blank output).
"""

text = input("Type something: ")

# Solution 1
if len(text) < 6:
    print()
else:
    print(f"{text[:3]}{text[-3::]}")

# Solution 2
letters = ""
for index, char in enumerate(text):
    if index in [0, 1, 2, len(text) - 1, len(text) - 2, len(text) - 3]:
        letters += char

print(letters)

# Solution 3
if len(text) < 6:
    print("")
else:
    new_string = text[:3] + text[len(text) - 3 :]
    print(new_string)

# Solution 4
num_chars = 3
if len(text) < 6:
    print("")
else:
    new_string = text[:num_chars] + text[len(text) - num_chars :]
    print(new_string)
