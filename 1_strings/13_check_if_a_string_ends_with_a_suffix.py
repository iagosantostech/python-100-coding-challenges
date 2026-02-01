"""
Description:

- Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the
variable suffix.

- If it does, print True. Else, print False.

- This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

- If the length of the suffix is greater than the length of the string, print False.
"""

text = input("Type something: ")
suffix = input("Type the suffix to check if the string ends with: ")

# Solution 1
text_ends_with_suffix = text.endswith(suffix)
print(
    "String typed ends with suffix."
    if text_ends_with_suffix
    else "String typed doesn't end with the suffix."
)

# Solution 2
text_ends_with_suffix = True
for index in range(-len(suffix), 0):
    if text[index] != suffix[index]:
        text_ends_with_suffix = False
        break

print(
    "String typed ends with suffix."
    if text_ends_with_suffix
    else "String typed doesn't end with the suffix."
)


# Solution 3
print(
    "String typed ends with suffix."
    if text[-len(suffix) :] == suffix
    else "String typed doesn't end with the suffix."
)
