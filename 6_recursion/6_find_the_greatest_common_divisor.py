"""
Description:
- Write a Python program that finds and prints the Greatest Common Divisor (GCD) of
the numbers a and b (the largest number that divides them both).
"""

import math


# Solution 1
def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)


print(find_gcd(48, 60))


# Solution 2


a = 4
b = 2

math.gcd(a, b)
