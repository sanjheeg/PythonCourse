"""
Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter
"""

def lit_to_met(lit):
    cubic = lit / 1000.0
    return cubic


def strong_pass(password):
    count = 0
    if len(password) >= 8:
        count += 1
    for letter in password:
        if letter.isdigit():
            count += 1
            break
    for letter in password:
        if letter.isupper():
            count += 1
            break

    if count >= 3:
        print("STRONG PASSWORD")
    else:
        print("WEAK PASSWORD")


strong_pass("S00")