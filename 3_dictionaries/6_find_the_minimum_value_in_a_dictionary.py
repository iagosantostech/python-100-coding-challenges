"""
Description:

- Write a Python program that prints the largest value in a dictionary.

- If the dictionary is empty, print None.

- You may assume that the values are numeric.
"""

my_dict = {"a": 4, "b": 6, "c": 35, "d": 1}

# Solution 1
print(min(my_dict.values()))

# Solution 2
smallest_value = 9999

if len(my_dict) == 0:
    print(None)
else:
    for current_value in my_dict.values():
        if current_value < smallest_value:
            smallest_value = current_value
    print(f"The smallest value in the dictionary is: {smallest_value}")
