import random

def main():

    while True:
        user = input("\nChoose Rock (r), Paper (p), or Scissors (s) or Quite (q): ").lower()

        computer = random.choice(["r", "p", "s"])

        if user == computer:
            print("Computer: ", computer)

            print("It's a draw!")
        elif (user == "r" and computer == "s") or (user == "s" and computer    == "p") or (user == "p" and computer == "r"):
            print("Computer: ", computer)
            print("You win!")
        elif user == "q":
            break
        else:
            print("Computer: ", computer)
            print("Computer wins!")



if __name__ == "__main__":
    main()