# Problem Statement
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit.

blue = "\033[94m" 
reset = "\033[0m" 


def print_one_degit(num):
    print("The ones digit is", num % 10)


def main():
    num = int(input(f"{blue}Enter a number: {reset}"))
    print_one_degit(num)

if __name__ == '__main__':
    main()