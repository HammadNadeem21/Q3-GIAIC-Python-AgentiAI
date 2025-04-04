# Problem Statement
# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting.

bold_italics = "\033[1;3m"
reset = "\033[0m"

def greet(name):
    return "Greeting " + name


def main():
    user_name = input(f"{bold_italics}What's your name? {reset}")
    print(greet(user_name))


if __name__ == '__main__':
    main()