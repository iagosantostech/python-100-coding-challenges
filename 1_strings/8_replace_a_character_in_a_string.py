"""
Description:

- Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

- curr_char and new_char are variables that contain strings with a single character.

- You may assume that new_char will not be an empty string.

- The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

- If no match is found, print the initial string.
"""

text = input("Type something: ")
current_char = input("Which character do you want to replace: ")
new_char = input("Which is the new character do you want to put in the string: ")

# Solution 1
new_text = ""
for letter in text:
    if letter != current_char:
        new_text += letter
    else:
        new_text += new_char

print(new_text)

# Solution 2
print(text.replace(current_char, new_char))
