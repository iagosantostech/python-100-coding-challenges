"""
Description:

- Write a Python program that creates and prints a frequency dictionary of the words found in a text file.

- The keys of the dictionary should be the words in the file.

- The values should be their frequencies.

- You may assume that each line of the file only contains one word.
"""

file_path = "text_file_2.txt"

freq_dict = {}

with open(file_path) as file:
    for word in file:
        word = word.strip("\n")
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1

print(freq_dict)
