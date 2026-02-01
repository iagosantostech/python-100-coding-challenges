"""
Description:
- Write a Python program that calculates the distance between two 3D points.

- The points are represented by two lists with three elements. The first element is the x-coordinate.
The second element is the y-coordinate. The third element is the z-coordinate.
"""

import math

list_a = [3, 4, 5]
list_b = [1, 3, 5]

AB = (
    ((list_b[0] - list_a[0]) ** 2)
    + ((list_b[1] - list_a[1]) ** 2)
    + ((list_b[2] - list_a[2]) ** 2)
)

print(math.sqrt(AB))
