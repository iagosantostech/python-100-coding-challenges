"""
Description:

- Write a Python program that finds the intersection of two sets (set1 and set2).

- Create a new set called intersection with their intersection.

- Print the new set as the output.

- If the intersection is empty, print an empty set.
"""

set_1 = {1, 2, 3}
set_2 = {4, 5, 6, 1, 2}


# Solution 1
intersection = set_1 & set_2
print(f"{'{}' if not intersection else intersection}")

# Solution 2
intersection_2 = set()

for element in set_1:
    if element in set_2:
        intersection_2.add(element)

print(f"{'{}' if not intersection_2 else intersection_2}")
