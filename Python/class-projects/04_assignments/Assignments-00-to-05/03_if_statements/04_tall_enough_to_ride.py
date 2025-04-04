# Problem Statement

# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.


bold_italics = "\033[1;3m"
reset = "\033[0m"


min_height = 30

def main():

    while True:
        height = input(f"{bold_italics}How tall are you?: {reset}")

        if height == "":
            print("Exiting...")
            break


        height = int(height)

        if height >= min_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride")

if __name__ == "__main__":
    main()