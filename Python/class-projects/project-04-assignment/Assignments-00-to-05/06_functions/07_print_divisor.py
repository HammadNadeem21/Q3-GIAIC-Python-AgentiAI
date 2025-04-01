# Problem Statement
# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors

def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)



if __name__ == '__main__':
    main()