import random


def computer_guess():
    low = 1
    high = 10
    feedback = ""

    print("Think of a number between 1 and 100 and I'll try to guess it!")


    while feedback != "c":
        guess = random.randint(low, high)

        feedback = input(f"Is {guess} too High (H), too Low (L), or Correct (C)? ").lower()

        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1

        
    print(f"Yay! I guessed your number: {guess} 😎")


if __name__ == '__main__':
    computer_guess()
