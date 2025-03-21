# Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

inches_in_feet = 12

def feet_to_inches():
    feet = float(input("Enter number of feet: "))
    inches:float = feet * inches_in_feet

    print(f"{feet} feet = {inches} inches")

if __name__ == '__main__':
    feet_to_inches()