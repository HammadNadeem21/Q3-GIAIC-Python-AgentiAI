import random

# Problem Statement

# Simulate rolling two dice, and prints results of each roll as well as the total.

dice_side = 6

def rool_dice():

    die1:int = random.randint(1, dice_side)
    die2:int = random.randint(1, dice_side)
    total:int = die1 + die2

    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    rool_dice()