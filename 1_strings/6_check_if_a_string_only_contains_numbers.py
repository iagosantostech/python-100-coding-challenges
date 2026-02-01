"""
Description:

- Write a Python program that check if a string only contains numbers.

- If it does, print True. Else, print False.
"""

text = input("Type something: ")

# Solution 1
new_list = []
for digit in text:
    new_list.append(digit.isdigit())

print(
    "The string only contains numbers."
    if all(new_list)
    else "The string contains other characters besides numbers."
)

# Solution 2
print(
    "The string only contains numbers."
    if text.isdecimal()
    else "The string contains other characters besides numbers."
)
