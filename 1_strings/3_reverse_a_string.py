"""
Description:

- Write a Python Program that prints the reversed version of a string.

- The program must preserve uppercase and lowercase letters.

- If the string is empty, print it intact.
"""

from functools import reduce

s = input("Print the string that will be reversed: ")

# Solution 1
print(s[::-1])

# Solution 2
reversed_word = "".join(reversed(s))
print(reversed_word)

# Solution 3
reversed_text = ""
for char in s:
    reversed_text = char + reversed_text

print(reversed_text)


# Solution 4
def reverse_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]


print(reverse_recursive(s))

# Solution 5
reversed_text = reduce(lambda x, y: y + x, s)
print(reversed_text)
