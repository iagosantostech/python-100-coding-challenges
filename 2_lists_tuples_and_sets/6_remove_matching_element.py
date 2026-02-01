"""
Description:

- Write a Python program that removes all occurrences of the element elem_to_remove from a list.

- The output of the program should be the new list with the element removed.

- If the element is not found in the list, print the message "Not Found".

- If the list is empty, print "Empty List".
"""

elements = [1, 2, 2, 3, 4]
new_list_elements = []
element_to_remove = 2

# Solution 1
if elements:
    if element_to_remove in elements:
        for current_element in elements:
            if current_element != element_to_remove:
                new_list_elements.append(current_element)
        print(new_list_elements)
    else:
        print("Element not found!")
else:
    print("Empty List.")

# Solution 2
if not elements:
    print("Empty List.")
elif element_to_remove not in elements:
    print("Element not found!")
else:
    print(list(filter(lambda x: x != element_to_remove, elements)))

# Solution 3
if not elements:
    print("Empty List.")
elif elements.count(element_to_remove) == 0:
    print("Element not found!")
else:
    for i in range(elements.count(element_to_remove)):
        elements.remove(element_to_remove)

print(elements)
