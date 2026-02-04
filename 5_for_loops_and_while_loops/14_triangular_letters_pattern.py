"""
Description:

- Write a Python program that prints a triangular pattern made with letters (as shown below).

- The first row should have one letter A (in uppercase). The second row should have two letters B.
The third row should have three letters C and so on.

- The number of rows is determined by the value of n, which is entered by the user.

- The letters must be separated by a space.
"""

import string

number = int(input("Please type a positive integer number between 1 and 26: "))

# Solution 1
for i in range(1, number + 1):
    print(" ".join(string.ascii_uppercase[i - 1] * i))

# Solution 2
for i in range(1, number + 1):
    for j in range(0, i):
        print(string.ascii_uppercase[i - 1], end=" ")
    print("")

# Solution 3
for i in range(number):
    print(chr(65 + i) * (i + 1))
