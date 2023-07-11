"""Define a function that has two parameters, year_of_birth and current_year . The current_year
parameter should be a default parameter with the current year as a default value.
The function should calculate and return the age of the user given the year of birth and the current year."""

def give_age(year_of_birth, current_year = 2023):
    return current_year - year_of_birth


birth = int(input("what year were you born in: "))
age = give_age(birth)

if age > 120:
    birth = int(input("stop lying! re-enter birth year"))
    age = give_age(birth)

print(age)

"""
Write a program that gets a list of names from the user and returns the 
number of names given. You are encouraged to use a function.
"""

def num_names():
    names_str = input("enter names separated by commas:")
    all_names = names_str.split(",")
    print(len(all_names))

num_names()

