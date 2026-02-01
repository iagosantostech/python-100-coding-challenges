"""
Description:

- Write a Python program that prints the largest and smallest values in a list

- Print the two values on the same line, separated by a space.

- The largest value should appear first and the smallest value should appear second.

- You may assume that the list only contains numeric values.

- If the list is empty, print None.
"""

elements = []

# Solution 1
if len(elements) == 0:
    print(None)
else:
    print(
        f"The largest value in the list is {max(elements)} and the smallest value is {min(elements)}."
    )

# Solution 2
if len(elements) == 0:
    print(None)
else:
    max_value = -9999
    min_value = 9999
    for element in elements:
        if element > max_value:
            max_value = element

        if element < min_value:
            min_value = element

    print(
        f"The largest value in the list is {max_value} and the smallest value is {min_value}."
    )
