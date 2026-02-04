"""
Description:

- Write a Python program that prints all the letters in the alphabet using a loop (one letter per line).

- The program should print the letters in uppercase.
"""

import string

# Solution 1
for letter in string.ascii_uppercase:
    print(letter)

# Solution 2
for i in range(65, 91):
    print(chr(i))
