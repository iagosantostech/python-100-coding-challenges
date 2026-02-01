"""
Description:

- Write a Python program that prints the string s without the character at index n.

- If the index n is out of range, print the string s intact.

- If the string s is empty, print the string s intact.
"""

text = input("Type something: ")
index_to_remove = int(input("Which index do you want to remove from the string: "))

# Solution 1
if not text or index_to_remove > len(text):
    print(text)
else:
    new_text = ""
    for index, letter in enumerate(text):
        if index != index_to_remove:
            new_text += letter

    print(new_text)

# Solution 2
if (len(text) == 0) or (index_to_remove >= len(text)):
    print(text)
else:
    new_text = ""
    for i in range(len(text)):
        if i != index_to_remove:
            new_text += text[i]
    print(new_text)
