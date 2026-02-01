"""
Description:

- Write a Python program that prints (as a list) the elements of listA that are not in listB.

- If the lists have the same elements, print an empty list.

- If listA is an empty list, print an empty list.

- Please assume that listA will be smaller than listB (will have fewer elements).
"""

list_a = [1, 2, 3, 4]
list_b = [1, 2, 3, 4]

if len(list_a) == 0 or list_a == list_b:
    print([])
else:
    print(list(filter(lambda x: x not in list_b, list_a)))
