"""
Description:

- Write a Python program that prints a list with the elements that listA and listB have in common.

- If they don't have any elements in common, print an empty list.

- The program should not assume that the lists have the same length.

- You may assume that each element will only appear once in each list.
"""

list_a = [4, 5, 6]
list_b = [1, 4, 5]

bigger_list = list_a
smaller_list = list_b

if len(list_b) > len(list_a):
    bigger_list = list_b
    smaller_list = list_a

common_elements = []

for element in smaller_list:
    if element in bigger_list and element not in common_elements:
        common_elements.append(element)

print(common_elements)
