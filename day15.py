import random
from parsers import parse


def rand_num():
    upper = int(input("upper bound: "))
    lower = int(input("lower bound: "))
    print(random.randint(lower, upper))

def parse_debug():
    # Ask the user to enter a lower and an upper bound divided by a comma
    user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")

    # Parse the user string by calling the parse function
    parsed = parse(user_input)

    # Pick a random int between the two numbers
    rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

    print(rand)


#rand_num()
parse_debug()