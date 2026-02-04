"""
Description:

- Write a Python program that calculates the factorial of a given number n.

- The value of n should be entered by the user.

- The program must print the result and use a loop to calculate it.
"""

num = int(input("Enter a positive integer number: "))

total = 1

for n in range(1, num + 1):
    total *= n

print(f"The factorial of the number {num} is: {total}")
