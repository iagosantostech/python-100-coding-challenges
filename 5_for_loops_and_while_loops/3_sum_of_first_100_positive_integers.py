"""
Description:

- Write a Python program that calculates and prints the sum of the first 100 non-negative integers (from 1 to 100).

- Use a loop to find this sum.
"""

from functools import reduce

# Solution 1

math_sum = 0

for num in range(1, 101):
    math_sum += num

print(math_sum)

# Solution 2

print(reduce(lambda x, y: x + y, list(range(1, 101))))
