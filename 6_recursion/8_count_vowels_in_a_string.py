"""
Description:

- Write a Python program that counts the number of vowels in a string recursively.

- If the string is empty or only contains one consonant, print 0.

- The program should be case-insensitive. Therefore, vowels in uppercase should also be counted.
"""

vowels = ["a", "e", "i", "o", "u"]


def count_vowels(word):
    word = word.lower()
    if len(word) == 0:
        return 0
    elif word[0] in vowels:
        return 1 + count_vowels(word[1:])
    else:
        return count_vowels(word[1:])


result = count_vowels("Python")
print(result)
