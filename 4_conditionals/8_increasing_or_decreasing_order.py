"""
Description:

- Write a Python program that determines if three numbers (a, b, and c) are in increasing order,
decreasing order, or none.

- If a > b > c, print "Decreasing Order".

- If a < b < c, print "Increasing Order".

- Else, print "None".
"""

a = 1
b = 2
c = 3

if a > b > c:
    print("Increasing Order")
elif a < b < c:
    print("Decreasing Order")
else:
    print("None")
