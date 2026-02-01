"""
Description:

- Write a Python program that prints a version of the string s with all commas replaced by dots.
"""

text = input("Type something: ")

# Solution 1
print(text.replace(",", "."))

# solution 2

new_text = ""
for char in text:
    if char == ",":
        new_text += "."
    else:
        new_text += char

print(new_text)
