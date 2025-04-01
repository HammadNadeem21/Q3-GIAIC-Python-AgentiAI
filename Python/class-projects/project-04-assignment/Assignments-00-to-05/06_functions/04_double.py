# Problem Statement
# Fill out the double(num) function to return the result of multiplying num by 2.

def double(num):
    return num * 2


def main():
    num = int(input("Enter a number: "))
    double_number = double(num)
    print(f"Double that is {double_number}")


if __name__ == '__main__':
    main()