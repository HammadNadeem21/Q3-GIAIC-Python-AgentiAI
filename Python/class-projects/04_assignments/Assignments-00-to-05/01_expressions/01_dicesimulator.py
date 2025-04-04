# Problem Statement:

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.


import random

dice_sides = 6

def rool_dice():
    dice1 = random.randint(1, dice_sides)
    dice2 = random.randint(1, dice_sides)
    total = dice1 + dice2

    print(f"Dice rolls: {dice1}, {dice2} (Total: {total})")


def main():
    dice1 = 10

    print(f"die1 in main(): {dice1}")

    rool_dice()
    rool_dice()
    rool_dice()

    print(f"die1 in main(): {dice1}")

if __name__ == '__main__':
    main()