
"""
Build a percentage calculator that gets from the user the "total value" and the "value" and returns the percentage. The 
program should also print a message if the user doesn't enter a number for the "total value or for the "value"
"""


def percentage():
    try:
        total_val = float(input("enter the total value: "))
        portion = float(input("enter value: "))
        percentage = portion/ total_val
        print(percentage)
    except ValueError:
        print("you need to enter a value. run the program again.")
    except ZeroDivisionError:
        print("your total value cannot be zero")



percentage()
