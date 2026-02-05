"""
Description:

- Write a Python program that calculates and prints the sum of the digits of a positive integer num.

- The program must find the sum recursively.

- If the integer has only one digit, print the integer as the total sum.
"""

num = 111

# Solution 1
str_num = str(num)


def sum_of_digits(s):
    if len(s) == 0:
        return 0
    else:
        return int(s[0]) + sum_of_digits(s[1:])


result = sum_of_digits(str_num)
print(result)


# Solution 2
def sum_of_digits2(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits2(num // 10)
