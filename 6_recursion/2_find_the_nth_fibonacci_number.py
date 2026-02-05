"""
Description:
- Write a Python program that calculates and prints the nth Fibonacci number.

- The value of n represents the position of the element in the sequence.

- The initial value of n should be 0.

- You may assume that the value of n is a non-negative integer.
"""

number = 9

a = 0
b = 1
c = 0

for i in range(0, number + 1):
    if i == 0 or i == 1:
        print(i, end=" ")
    else:
        c = a + b
        a = b
        b = c
        print(c, end=" ")
print()


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))
