"""
Description:

- Write a Python program that prints a diamond made with asterisks where the diamond's height (number of rows)
is determined by the value of the variable height

- You can (optionally) ask the user to enter the value of height.

- This value can only have an odd number of rows, so you should print a descriptive message if the user enters an
even value.
"""

height = 53

# Solution 1
if height % 2 == 0:
    print("You need to enter a odd number!")
else:
    for i in range(1, height + 1, 2):
        print(("*" * i).center(height))
    for i in range(height - 2, 0, -2):
        print(("*" * i).center(height))
