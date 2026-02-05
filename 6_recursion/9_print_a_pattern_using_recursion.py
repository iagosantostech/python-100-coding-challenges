"""
Description:

- Write a Python program that prints the pattern of asterisks shown below for a given value of n.

- The program must include a recursive function.

- n represents the number of rows in the resulting pattern and the number of asterisks printed on the first row.
"""


def print_pattern(n):
    if n == 0:
        return
    else:
        print("*" * n)
        return print_pattern(n - 1)


print_pattern(6)
