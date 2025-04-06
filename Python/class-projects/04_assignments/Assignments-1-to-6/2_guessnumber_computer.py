import random

def main():
    secret_number = random.randint(1, 10)
    print("I have selected a number between 1 and 10. Try to guess it!")

    while True:
        guess_number = int(input("\nEnter your guess: "))

        if guess_number < secret_number:
            print("Too low! Try again")
        elif guess_number > secret_number:
            print("Too high! Try again")
        else:
            print(f"Congrats, The number was {secret_number}")
            break


if __name__ == '__main__':
    main()
