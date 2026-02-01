"""
Description:

- Write a Python program that counts the number of elements in a list with value greater than 3.

- You may assume that the list only contains numbers.

- Print the final count.
"""

elements = [-1, 0, 1, 2, 2, 3, 4, 5, 6, 5]

# Solution 1
counter = 0
for element in elements:
    if element > 3:
        counter += 1
print(f"This list has {counter} number(s) greater than 3.")

# Solution 2
print(
    f"This list has {len(list(filter(lambda x: x > 3, elements)))} number(s) greater than 3."
)

# Solution 3
print(
    f"This list has {sum(1 for element in elements if element > 3)} number(s) greater than 3."
)
