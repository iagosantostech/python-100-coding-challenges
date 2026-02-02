"""
Description:

- Write a Python program that checks if all values in a dictionary are equal.

- If they are, print True. Else, print False.

- If the dictionary is empty, print "Empty".
"""

my_dict = {"a": 4, "b": 4, "c": 4, "d": 4, "e": 6}

# Solution 1
if len(my_dict) == 0:
    print("Empty dictionary.")
else:
    print(
        "All values are equal."
        if len(set(my_dict.values())) == 1
        else "Not all values are equal."
    )

# Solution 2
first_value = my_dict["a"]

for value in my_dict.values():
    if value != first_value:
        print("Not all values are equal.")
        break
else:
    print("All values are equal.")
