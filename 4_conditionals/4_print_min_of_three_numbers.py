"""
Description:

- Write a Python program that prints the smallest of three integers a, b, and c.
"""

a = 0
b = 0
c = 1

if a <= b and a <= c:
    print(f"The smallest number is: {a}")
elif b <= a and b <= c:
    print(f"The smallest number is: {b}")
else:
    print(f"The smallest number is: {c}")
