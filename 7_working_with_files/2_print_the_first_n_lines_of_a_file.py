"""
Description:

- Write a Python program that reads a text file and prints the first n lines of the file.

- The value of n should be entered by the user.

- If the value of n is greater than the total number of lines in the file, print

- "Please enter a value for n. The file has <num_lines> lines".
"""

number = int(input("How many lines of the file do you want to read: "))

with open("text_file.txt") as file:
    content = file.readlines()
    num_lines = len(content)

    if number > num_lines:
        print(f"Please enter a valid value. The file has {num_lines} lines.")
    else:
        for i in range(0, number):
            print(content[i].strip("\n"))
