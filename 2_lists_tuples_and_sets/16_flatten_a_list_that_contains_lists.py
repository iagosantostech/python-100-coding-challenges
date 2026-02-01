"""
Description:

- Write a Python program that prints a "flattened" version of a list that contains nested lists.

- "Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't
contain any nested lists, just the individual.

- The list could contain other elements that are not lists or other sequences, so you must check
the type of each element and act appropriately.

- If the list is empty, print an empty list.
"""

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list = [1, 2, 3, 4, 5, 6, [7, 8, 9], {10, 11, 12}]

new_list = []

for element in nested_list:
    if (
        isinstance(element, list)
        or isinstance(element, tuple)
        or isinstance(element, set)
        or isinstance(element, dict)
    ):
        for el in element:
            new_list.append(el)
    else:
        new_list.append(element)

print(new_list)
