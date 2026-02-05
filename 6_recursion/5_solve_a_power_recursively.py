"""
Description:

- Write a Python program that find the value of a raised to the power b recursively.

- The operation is a ** b in Python, where a is the base and b is the exponent but for this challenge,
you should not use the built-in ** operator directly. You should solve the power recursively.

- If the value of b is 0, the result is automatically 1 because every number raised to the power 0 is 1.
"""


def calculate_power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * calculate_power(a, b - 1)


a = 5
b = 2
result = calculate_power(a, b)
print(result)
