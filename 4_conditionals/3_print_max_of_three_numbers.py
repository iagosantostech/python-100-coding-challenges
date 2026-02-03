"""
Description:

- Write a Python program that prints the maximum of three integers (a, b, c).
"""

a = 43
b = 56
c = 7

if a >= b and a >= c:
    print(f"The biggest number is: {a}")
elif b >= a and b >= c:
    print(f"The biggest number is: {b}")
else:
    print(f"The biggest number is: {c}")
