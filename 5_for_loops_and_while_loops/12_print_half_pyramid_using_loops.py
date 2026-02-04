"""
Description:

- Write a Python program that prints a pyramid pattern made with asterisks.

- The number of rows should be determined by the value of the variable n. This value will be entered by the user.

- You may assume that the value of n is a positive integer.
"""

number = int(input("Type a positive integer number: "))


k = (2 * number) - 2

for i in range(0, number):

    for j in range(0, k):
        print("", end=" ")

    k = k - 2

    for j in range(0, i + 1):
        print("*", end=" ")

    print("")
