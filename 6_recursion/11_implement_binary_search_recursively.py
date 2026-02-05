"""
Description:

- Write a Python program that implements the Binary Search algorithm recursively.

- The function should search for an element in a list or sequence and return its index.

- If the element is not found, the value returned should be -1.
"""


def find_number_recursively(my_list, low_index, high_index, target):
    if low_index > high_index:
        return -1
    else:
        middle_index = (low_index + high_index) // 2

        if target == my_list[middle_index]:
            return middle_index
        elif target < my_list[middle_index]:
            return find_number_recursively(my_list, low_index, middle_index - 1, target)
        else:
            return find_number_recursively(
                my_list, middle_index + 1, high_index, target
            )


my_list = [4, 5, 6, 7, 8]
print(find_number_recursively(my_list, 0, len(my_list) - 1, 9))
