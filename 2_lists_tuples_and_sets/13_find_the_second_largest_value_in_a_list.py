"""
Description:

- Write a Python program that prints the second largest value in a list.

- If the list is empty or only has one element, print None.
"""

elements = [45, 34, 78, 89, 101, 445, 332]

# Solution 1
if len(elements) == 0 or len(elements) == 1:
    print(None)
else:
    print(sorted(elements, reverse=True)[1])


# Solution 2
biggest_value = -9998
second_biggest_value = -9999

if len(elements) == 0 or len(elements) == 1:
    print(None)
else:
    for element in elements:
        if element > biggest_value:
            second_biggest_value = biggest_value
            biggest_value = element
        elif element > second_biggest_value:
            second_biggest_value = element

    print(second_biggest_value)

# Solution 3
if len(elements) > 1:
    no_duplicates = set(elements)
    no_duplicates.remove(max(no_duplicates))
    print(max(no_duplicates))
else:
    print(None)
