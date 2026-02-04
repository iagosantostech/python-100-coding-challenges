"""
Description:

- Write a Python program that prints the first 100 even numbers (from 2 to 200 inclusive).
"""

# Solution 1
for num in range(2, 202, 2):
    print(num)

# Solution 2
for num in range(2, 202):
    if num % 2 == 0:
        print(num)
