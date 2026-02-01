"""
Description:

- Write a Python program that prints the second smallest value in a list.

- If the list is empty or only has one element, print None.
"""

# elements = [45, 34, 78, 89, 101, 445, 332]
elements = [1, 2, 3, 4]

# Solution 1
if len(elements) == 0 or len(elements) == 1:
    print(None)
else:
    print(sorted(elements)[1])


# Solution 2
smallest_value = 9998
second_smallest_value = 9999

if len(elements) == 0 or len(elements) == 1:
    print(None)
else:
    for element in elements:
        if element < smallest_value:
            second_smallest_value = smallest_value
            smallest_value = element
        elif element < second_smallest_value:
            second_smallest_value = element

    print(second_smallest_value)

# Solution 3
if len(elements) > 1:
    no_duplicates = set(elements)
    no_duplicates.remove(min(no_duplicates))
    print(min(no_duplicates))
else:
    print(None)
