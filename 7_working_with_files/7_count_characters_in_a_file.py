"""
Description:

- Write a Python program that counts the number of characters in a file.

- Count all the characters in the file, including commas and quotes.

- Do not count spaces and remove \n (new line) characters.
"""

file_path = "text_file_3.txt"

character_count = 0

with open(file_path) as file:
    for line in file:
        character_count += len(line.replace(" ", "").strip("\n"))

print(character_count)
