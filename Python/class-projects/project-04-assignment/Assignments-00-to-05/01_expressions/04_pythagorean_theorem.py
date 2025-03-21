import math

# Problem Statement

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

bold_italics = "\033[1;3m"
reset = "\033[0m"

def pythagorean_theorem():

    AB:float = float(input(f"{bold_italics}Enter the length of AB: {reset}"))
    AC:float = float(input(f"{bold_italics}Enter the length of AC: {reset}"))

    print("BC ** 2 = AB ** 2 + AC ** 2")

    BC:float = math.sqrt(AB ** 2 + AC ** 2)

    print(f"The length of BC (the hypotenuse) is: {BC}")

pythagorean_theorem()

