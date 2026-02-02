"""
Description:

- Write a Python program that creates a dictionary from the values contained in nested lists.

- Each nested list has this format [value1, value2].

- value1 should be the key in the dictionary and value2 should be its corresponding value.

- If there are no nested lists, print an empty dictionary.
"""

nested_lists = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

my_dict = {}

for nested_list in nested_lists:
    my_dict[nested_list[0]] = nested_list[1]

print(my_dict)
