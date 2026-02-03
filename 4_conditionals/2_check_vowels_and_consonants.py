"""
Description:

- Write a Python program that prints a descriptive message indicating if each character in a string is a vowel or a
consonant. For example: "<char> is a <consonant | vowel>"

- If the character is a special character, number, or symbol, print "<char> is not a letter".

- If the string is empty, print "Empty String".
"""

text = input("Type something: ")

vowels = ["a", "e", "i", "o", "u"]

for char in text.lower():
    if char.isalpha():
        if char in vowels:
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    else:
        print(f"{char if char != ' ' else 'space'} is not a letter.")
