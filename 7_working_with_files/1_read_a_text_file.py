"""
Description:

- Write a Python program that reads a text file and saves its content line by line to a list called file_content.

- The list should contain strings that represent each line of the text file.

- The program should print the resulting list.
"""

# Solution 1
with open("text_file.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Solution 2

file_content = []

with open("text_file.txt", "r") as file:
    for line in file:
        file_content.append(line)
print(file_content)
