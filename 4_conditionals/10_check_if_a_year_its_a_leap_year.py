"""
Description:

- Write a Python program that prints if a given year was (or will) be a leap year.
"""

year = 1836

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")
