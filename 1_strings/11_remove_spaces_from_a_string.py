"""
Description:

- Write a Python program that prints a copy of the string s without any spaces.

- Words should be connected in the final string.

- If the string doesn't contain spaces, print it intact.
"""

text = input("Type something: ")

# Solution 1
print(text.replace(" ", ""))

# Solution 2
str_to_list = [letter for letter in text if letter != " "]
print("".join(str_to_list))

# Solution 3
new_text = ""
for char in text:
    if char != " ":
        new_text += char

print(new_text)
