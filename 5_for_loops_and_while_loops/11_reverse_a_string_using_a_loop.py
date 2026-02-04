"""
Description:

- Write a Python program that prints a string reversed using a loop.

- All the characters must be on the same line in reverse order.
"""

string_to_reverse = "Python"

# Solution 1
string_reversed = ""
for i in range(-1, -len(string_to_reverse) - 1, -1):
    string_reversed += string_to_reverse[i]
print(string_reversed, end="")
print("\n")

# Solution 2
for char in string_to_reverse[::-1]:
    print(char, end="")
print("\n")

# Solution 3
for char in reversed(string_to_reverse):
    print(char, end="")
print("\n")

# Solution 4
for i in reversed(range(len(string_to_reverse))):
    print(string_to_reverse[i], end="")
print("\n")

# Solution 5
for i in range(len(string_to_reverse) - 1, -1, -1):
    print(string_to_reverse[i], end="")
print("\n")
