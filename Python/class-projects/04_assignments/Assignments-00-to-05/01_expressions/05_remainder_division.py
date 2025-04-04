# Problem Statement

# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

bold_italics = "\033[1;3m"
reset = "\033[0m"

def remainder_division():

    divided = int(input(f"{bold_italics}Please enter an integer to be divided: {reset}"))
    divide_by = int(input(f"{bold_italics}Please enter an integer to divide by: {reset}"))

    division = divided // divide_by
    remainder = divided % divide_by

    print(f"The result of this division is {division} with a remainder of {remainder}")


if __name__ == '__main__':
    remainder_division()