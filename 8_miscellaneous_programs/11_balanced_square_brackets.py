"""
Description:

- Write a Python program that determines if a string with square brackets is balanced
(if it has opening and closing square brackets in the correct order).

- You can write this implementation as a function.

- Return the value True if the string is balanced and False if it is not balanced.

- You may assume that the string only contains square brackets [ and ].
"""


def balanced_brackets(string):
    count = 0
    for bracket in string:
        if bracket == "[":
            count += 1

        elif bracket == "]":
            count -= 1

        if count < 0:
            break

    return count == 0


print(balanced_brackets("[]"))  # True
print(balanced_brackets("[]]]"))  # False
print(balanced_brackets("[[[[[[[]]]]]]]"))  # True
