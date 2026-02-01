"""
Description:

- Write a Python program that prints the elements of a list followed their corresponding indices.

- Each element and its index must be on the same line separated by a space.

- If the list is empty, print "Empty List".
"""

elements = [1, 2, 3, 4]

if elements:
    for index, element in enumerate(elements):
        print(element, index)
else:
    print("Empty List")
