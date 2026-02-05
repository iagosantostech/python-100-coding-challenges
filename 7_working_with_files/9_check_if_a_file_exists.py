"""
Description:

- Write a Python program that checks if a file exists in the specified path or not.

- If it exists, print "The file <file_name> exists"

- If it doesn't, print "The file <file_name> doesn't exist"

- The file name could also be an absolute path to the file.
"""

import os.path

my_file = "famous_quotes.txt"

if os.path.isfile(my_file):
    print(f"The file {my_file} exists")
else:
    print(f"The file {my_file} doesn't exist")
