"""
Description:

- Write a Python program that creates and print a dictionary that maps each element in a
list to its corresponding frequency (how many times it occurs in the list).

- The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".
"""

# list_text = ["a", "a", "b", "c", "a", "b"]
list_numbers = [1, 2, 3, 4, 3, 2, 1, 2]

letters_dict = {}

for letter in list_numbers:
    if letters_dict.get(letter):
        letters_dict[letter] += 1
    else:
        letters_dict[letter] = 1

print(letters_dict)
