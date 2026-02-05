"""
Description:

- Write a Python program that converts a decimal number to binary using recursion.

- The function must return the binary representation as a string.

- The program must print the value returned.
"""


def convert_from_decimal_to_binary(n):
    if n == 0:
        return "0"
    else:
        return convert_from_decimal_to_binary(n // 2) + str(n % 2)


print(convert_from_decimal_to_binary(567))
