import random


def main():
    print("Welcome to your password generator")
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%^&0123456789'

    number = int(input("Amount of password to generate: "))
    length = int(input("Your password length: "))

    print("\nhere are your passwords:")

    for i in range(number):
        password = ''
        for _ in range(length):
            password += random.choice(chars)
        print(password)


if __name__ == '__main__':
    main()