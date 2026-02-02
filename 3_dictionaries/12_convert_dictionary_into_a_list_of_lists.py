"""
Description:

- Write a Python program that takes the content of a dictionary and converts it into a list of lists.

- Each nested list should contain a key as the first element and its corresponding value as the second element.

- Print the final list of lists.
"""

product_info = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

list_of_items = []

for key in product_info:
    list_of_items.append([key, product_info[key]])

print(list_of_items)
