"""
Description:

- Write a Python program that simulates an interactive calculator with the basic arithmetic
operations in Python (addition, subtraction, multiplication, division, integer division, and modulo).

- The program must interact with the user by asking for the values and the type of operation that will be performed.

- The output should include the values, the operation, and the result (as shown below).

- The type of operation will be denoted by an integer.

    - 1 for addition
    - 2 for subtraction
    - 3 for multiplication
    - 4 for division
    - 5 for integer division
    - 6 for modulo

- The program should present an initial message to the user describing the types of operations
and the integer that has to be entered to select each one of them.

- If the values entered by the user are invalid for the operation selected, a descriptive message
should be displayed. For example, for a division operation the denominator cannot be 0.

- If the user enters an invalid integer to select the operation, print

- "Please choose a valid operation"
"""

num1 = input("Please type a number: ")
num2 = input("Please type another number: ")
operation = input(
    """Please choose an operation:

1 for addition
2 for subtraction
3 for multiplication
4 for division
5 for integer division
6 for modulo

"""
)

if not num1.isdecimal or not num2.isdecimal():
    print("\nPlease enter only numbers to do the operation.")
else:
    if int(operation) == 1:
        print(f"\nThe return of the sum is: {float(num1) + float(num2)}")
    elif int(operation) == 2:
        print(f"\nThe return of the subtraction is: {float(num1) - float(num2)}")
    elif int(operation) == 3:
        print(f"\nThe return of the multiplication is: {float(num1) * float(num2)}")
    elif int(operation) == 4:
        print(f"\nThe return of the division is: {float(num1) / float(num2)}")
    elif int(operation) == 5:
        print(f"\nThe return of the integer division is: {float(num1) // float(num2)}")
    elif int(operation) == 6:
        print(f"\nThe return of the modulo is: {float(num1) % float(num2)}")
    else:
        print("\nChoose a valid operation!")
