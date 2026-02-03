"""
Description:

- Write a Python program that prints if a number num is either "Positive", "Negative", or "Zero".
"""

number = float(input("Type a number: "))

if number == 0:
    print("The number typed is zero.")
elif number > 0:
    print("The number typed is positive.")
else:
    print("The number typed is negative.")
