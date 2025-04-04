# Problem Statement
# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

blue = "\033[94m" 
reset = "\033[0m" 
AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():

    print("Please type the following affirmation: " + AFFIRMATION)

    while True:
        user_input = input(f"Please type the following affirmation:\n{AFFIRMATION}\n{blue}User Input: {reset}")

        if user_input == AFFIRMATION:
            print("That's right! :")
            break
        else:
            print("That was not the affirmation.")


if __name__ == '__main__':
    main()
            