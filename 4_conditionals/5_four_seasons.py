"""
Description:

- Write a Python program that prints the corresponding season based on the value of the variable season_num.

- The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.

- If the value of season_num is neither one of these values, print "Please enter a valid number".
"""

season_number = int(input("Type a number (1-4): "))

if season_number == 1:
    print("Spring")
elif season_number == 2:
    print("Summer")
elif season_number == 3:
    print("Fall")
elif season_number == 4:
    print("Winter")
else:
    print("Please enter a valid number!")
