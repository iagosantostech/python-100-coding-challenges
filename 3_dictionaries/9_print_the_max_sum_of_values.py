"""
Description:

- Write a Python program that prints the maximum sum of the values in a dictionary.

- You may assume that all the values in the dictionary are either lists or tuples.
"""

my_dict = {"a": [1, 2, 3], "b": [4, 0, -4], "c": [3, 5, 9], "d": [45, 12, 100]}

max_value = -9999

for key in my_dict:
    sum_of_values = sum(my_dict[key])

    if sum_of_values > max_value:
        max_value = sum_of_values

print(max_value)
