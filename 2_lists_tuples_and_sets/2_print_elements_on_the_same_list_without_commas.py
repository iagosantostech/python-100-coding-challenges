"""
Description:

- Write a Python program that prints the elements of a list on the same line.

- The elements should be separated only by a space (not by a comma).

- The output should not include the opening and closing square brackets [ ].
"""

elements = [3, 4, 5, 6]

# Solution 1
str_elements = ""
for element in elements:
    str_elements += f"{element} "

print(str_elements.rstrip())

# Solution 2
print(" ".join(map(str, elements)))

# Solution 3
print(*elements, sep=" ")

# Solution 4
for element in elements:
    print(element, end=" ")
