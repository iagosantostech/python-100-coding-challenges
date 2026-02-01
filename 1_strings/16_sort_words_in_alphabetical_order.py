"""
Description:

- Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order,
and print the resulting string.

- You may assume that the string only contains letters and spaces to separate the words.

- Spaces should be preserved in the final string.
"""

text = input("Type something: ")

list_of_words = text.lower().split(" ")

new_text = ""
for word in list_of_words:
    new_text += "".join(sorted(word))
    new_text += " "

print(new_text.rstrip())
