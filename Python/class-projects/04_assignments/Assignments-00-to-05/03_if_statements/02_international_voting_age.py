# Problem Statement

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# User age
age = int(input("How old are you?: "))

# Peturksbouipo Voting
if age >= 16:
    print("You can vote in Peturksbouipo where the voting age is 16.")
else:
    print("You cannot vote in Peturksbouipo where the voting age is 16.")

# Stanlau Voting
if age >= 25:
    print("You can vote in Stanlau where the voting age is 25.")
else:
    print("You cannot vote in Stanlau where the voting age is 25.")

# Mayengua Voting
if age >= 48:
    print("You can vote in Mayengua where the voting age is 48.")
else:
    print("You cannot vote in Mayengua where the voting age is 48.")
