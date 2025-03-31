# Problem Statement

# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

def leap_year():
    user_year = int(input("Enter a year: "))

    if(user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        print("That's a leap year")
    else:
        print("That's not a leap year.")


if __name__ == "__main__":
    leap_year()