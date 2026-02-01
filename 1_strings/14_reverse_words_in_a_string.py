"""
Description:

- Write a Python program that reverses the individual words in the string s and changes their capitalization.
Uppercase letters should be printed in lowercase and vice versa.

- Assume that the string only contains letters and spaces are used to separate words.
"""

text = input("Type something: ")

text_splitted_by_space = text.split(" ")
text_reversed = ""

for word in text_splitted_by_space:
    text_reversed += word[::-1].swapcase()
    text_reversed += " "

print(text_reversed.rstrip())
