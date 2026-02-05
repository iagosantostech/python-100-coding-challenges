"""
Description:

- Write a Python program that calculates and prints the value of the factorial
of the number num using recursion.

- The factorial of a number x is denoted by x! and it is equal to x * (x-1) * (x-2) * ... * 1,
the product of all positive integers less than or equal to the number.

- The value of 0! is equal to 1 by mathematical convention.
"""


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


result = fatorial(1)
print(result)
