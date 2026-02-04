"""
Description:

- Write a Python program that prints the digits of a number in reverse order on the same line.

- If the number only has one digit, print this digit.
"""

# Solution 1
number = input("Please type a number: ")

print(number[::-1])


# Solution 2
reversed_num = 0

while number > 0:
    remainder = number % 10
    reversed_num = (reversed_num * 10) + remainder
    number = number // 10

print(reversed_num)
