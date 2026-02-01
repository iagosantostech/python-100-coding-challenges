"""
Description:

- Write a Python program that multiplies all the items in a list by the value of the variable factor.

- The program must print the list as the output.

- The program should also allow multiplying the variable factor by a string in case the list contains strings.

- You may assume that the value of factor will be a positive integer.
"""

elements = [3, 4, 5, 6]
# elements = ["a", "b", "c"]
factor = 2

# Solution 1
print([element * factor for element in elements])

# Solution 2
new_elements_list = []

for element in elements:
    new_elements_list.append(element * factor)

print(new_elements_list)

# Solution 3
elements = ["a", "b", "c"]
for i in range(len(elements)):
    elements[i] *= factor

print(elements)

# Solution 4
elements = ["a", "b", "c"]
for i, element in enumerate(elements):
    elements[i] = element * factor

print(elements)
