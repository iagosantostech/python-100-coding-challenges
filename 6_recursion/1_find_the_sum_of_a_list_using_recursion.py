"""
Description:

- Write a Python program that finds the sum of a list (or tuple) of numbers recursively.

- Print the total sum.

- If the list (or tuple) is empty, print 0.
"""

my_list = [1, 2, 3]


# Solution 1
def sum_recursion(list_numbers, index):
    if index == 0:
        return list_numbers[index]
    return list_numbers[index] + sum_recursion(list_numbers, index - 1)


if not my_list:
    print(0)
else:
    sum_list = sum_recursion(my_list, len(my_list) - 1)
    print(sum_list)


# Solution 2
def find_sum(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + find_sum(s[1:])
