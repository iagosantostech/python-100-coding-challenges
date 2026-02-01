"""
Description:

- Write a Python program that checks if a list is empty or not.

- If the list is empty, print "Empty". Else, print "Not Empty".
"""

elements = [1, 2, 3, 4, 5]
# elements = []

# Solution 1
print("Empty" if len(elements) == 0 else "Not Empty")

# Solution 2
print("Not Empty" if elements else "Empty")
