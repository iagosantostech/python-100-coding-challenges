"""
Description:

- Write a Python program that generates and prints all the possible permutations of a list.

- A permutation is a possible arrangement of the elements of the list. For example, [2, 1, 3]
is a permutation of [1, 2, 3].

- Print each permutation as a list on a separate line. You can print them as lists or tuples.

- Include the list itself as a permutation.
"""

import itertools

elements = [1, 2, 3]

for permutation in itertools.permutations(elements):
    print(list(permutation))
