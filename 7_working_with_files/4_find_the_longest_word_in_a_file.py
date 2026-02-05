"""
Description:

- Write a Python program that finds and prints the longest word in a text file.

- For this challenge, you may assume that the file only contains one word per line.
"""

longest_word = ""

with open("text_file_2.txt") as file:
    # content = file.read().replace("\n", "")
    # words = content.split(" ")
    content = file.readlines()

    for word in content:  # words
        if len(word) > len(longest_word):
            longest_word = word

    print(f"The longest word in the file is: {longest_word}")
