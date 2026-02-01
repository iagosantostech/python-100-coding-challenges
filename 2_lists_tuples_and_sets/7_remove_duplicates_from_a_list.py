"""
Description:

- Write a Python program that removes duplicate elements from a list, only keeping one
occurrence of each element in the list.

- The original list should not be mutated (modified).

- The program must print the final version of the list.
"""

elements = [1, 2, 3, 3, 3, 4, 4, 5, 5]

# Solution 1
elements_without_duplicates = []
for element in elements:
    if element not in elements_without_duplicates:
        elements_without_duplicates.append(element)

print(elements_without_duplicates)

# Solution 2
elements_without_duplicates = list(set(elements))
print(elements_without_duplicates)

# Solution 3
elements_without_duplicates = list(dict.fromkeys(elements))
print(elements_without_duplicates)
