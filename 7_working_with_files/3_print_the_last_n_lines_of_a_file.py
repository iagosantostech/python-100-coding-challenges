"""
Description:
- Write a Python program that prints the last n lines of a text file in order.

- The value of n should be provided by the user.

- You may assume that n is a valid positive integer.
"""

number = int(input("Type the number of the last lines: "))

with open("text_file.txt") as file:
    content = file.readlines()
    num_lines = len(content)

    if number > num_lines:
        for i in range(num_lines):
            print(content[i].strip("\n"))
    else:
        for i in range(-number, 0, 1):
            print(content[i].strip("\n"))
