"""
Description:

- Write a Python program that prints the largest value in a dictionary.

- If the dictionary is empty, print None.

- You may assume that the values are numeric.
"""

my_dict = {"a": 5, "b": 6, "c": 35, "d": 8}

# Solution 1
print(max(my_dict.values()))

# Solution 2
biggest_value = -9999

if len(my_dict) == 0:
    print(None)
else:
    for current_value in my_dict.values():
        if current_value > biggest_value:
            biggest_value = current_value
    print(f"The biggest value in the dictionary is: {biggest_value}")
