"""
Description:

- Write a Python program that prints Floyd's Triangle with n number of rows.

- The value of n should be entered by the user. You may assume that it is a positive integer.

- Floyd's Triangle is made with consecutive numbers that fill the rows of the triangle (as shown below).
"""

number = int(input("Please type a positive integer number: "))

# Solution 1
k = 1

for i in range(1, number + 1):
    n = int((i * (i + 1)) / 2)

    for j in range(k, n + 1):
        print(j, end=" ")

    k = n + 1
    print("")

# Solution 2

k = 1
for i in range(1, number + 1):
    for j in range(0, i):
        print(k, end=" ")
        k += 1
    print("")
