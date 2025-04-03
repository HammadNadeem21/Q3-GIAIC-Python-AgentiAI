import random


def main():

    your_score = 0
    print("Welcome to the High-Low Game!")
    
    round = int(input("How many rounds would you like to play? "))

    for num_round in range(1, round + 1):

        print("\nRound ", num_round)
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)

        print("Your number is ", your_num)

        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        if computer_num == your_num:
            print("Computer is Win")

        if guess == "higher" and your_num > computer_num or guess == "lower" and your_num < computer_num:
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
            print("Your Score Now: ", your_score)
            print("Wow! You played perfectly!")

            if your_score > 1:
                print("Good job, you played really well!")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
            print("Your Score Now: ", your_score)
            print("Better luck next time!")

    print("\nYour Final Score is: ", your_score )
    print("Thanks for playing!")


    

if __name__ == '__main__':
    main()