"""
Description:

- Write a Python program that checks if a key exists in a dictionary or not.

- If the key exists in the dictionary, print True. Else, print False.

- The key should be stored in the variable key.
"""

dictionary = {"a": 4, "b": 5, "c": 6}
key = "d"

# Solution 1
print(key in dictionary.keys())

# Solution 2
print(key in dictionary)

# Solution 3
for current_key in dictionary.keys():
    if current_key == key:
        print(True)
        break
else:
    print(False)
