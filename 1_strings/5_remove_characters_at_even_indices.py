"""
Description:

- Write a Python program that prints the string s without the characters located at even indices.

- If the string is empty or only has one character, print it without any changes.
"""

text = input("Type something: ")

# Solution 1
if len(text) <= 1:
    print(text)
else:
    new_text = ""
    for index, letter in enumerate(text):
        if index % 2 != 0:
            new_text += letter
    print(new_text)

# Solution 2
print(text if len(text) <= 1 else text[1::2])

# Solution 3
new_text = ""
for index in range(len(text)):
    if index % 2 != 0:
        new_text += text[index]
print(new_text)

# Solution 4
new_text = ""
for index in range(1, len(text), 2):
    new_text += text[index]
print(new_text)
