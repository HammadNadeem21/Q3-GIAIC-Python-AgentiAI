import random

# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css', 'typescript']


def hangman():
    print("Welcome to Hangman Game!")

    word = random.choice(word_list)
    word_lenth = len(word)
    guess_word = ['_'] * word_lenth
    attempt_left = 6
    guess_letter = []

    while attempt_left > 0:
        print("\nWord to guess:"," ".join(guess_word))
        print(f"Guessed letters: {', '.join(guess_letter)}")
        print(f"Attempts left: {attempt_left}")

        guess = input("Guess a letter: ").lower()

        if guess in guess_letter:
            print("You already guessed that letter. Try a different one.")
            continue
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only a single letter.")
            continue

        guess_letter.append(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")

            for i in range(word_lenth):
                if word[i] == guess:
                    guess_word[i] = guess

        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempt_left -= 1 


        if ''.join(guess_word) == word:
            print(f"\nCongratulations! You've guessed the word: {word}")
            break

    if attempt_left == 0:
        print(f"\nGame Over! The word was: {word}")


if __name__ == '__main__':
    hangman()

        
