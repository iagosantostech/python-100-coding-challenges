"""
Description:

- Write a Python program that checks if the string s starts with the sequence of characters denoted by the
variable prefix.

- If it does, print True. Else, print False.

- This test should be case sensitive. For example, "A" should not be equivalent to "a".

- If the length of the prefix is greater than the length of the string, print False.
"""

text = input("Type something: ")
prefix = input("Type the prefix to check if the string starts with: ")

# Solution 1
text_starts_with_prefix = text.startswith(prefix)
print(
    "String typed starts with prefix."
    if text_starts_with_prefix
    else "String typed doesn't start with the prefix."
)

# Solution 2
text_starts_with_prefix = True
for index in range(len(prefix)):
    if text[index] != prefix[index]:
        text_starts_with_prefix = False
        break

print(
    "String typed starts with prefix."
    if text_starts_with_prefix
    else "String typed doesn't start with the prefix."
)


# Solution 3
print(
    "String typed starts with prefix."
    if text[: len(prefix)] == prefix
    else "String typed doesn't start with the prefix."
)
