"""
Description:

- Write a Python program that prints the character at index i in the string s.

- If the index is out of range, the program should print "i out of range"

- If the string is empty, the program should print "Empty String"

"""

s = input("Type something: ")
index = int(input("Type an index: "))

if not s:
    print("Empty String")
elif index < len(s):
    print(f"The character in the index {index} is {s[index]}")
else:
    print("Index out of range")
