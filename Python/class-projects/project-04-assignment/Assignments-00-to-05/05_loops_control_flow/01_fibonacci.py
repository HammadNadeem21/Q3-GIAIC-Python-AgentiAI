# Problem Statement
# Write a program to print terms in the Fibonacci sequence up to a maximum value.

max_value = 10000

def fibonacci():

    a, b = 0, 1

    while a < max_value:

        print(a)
        a, b = b, b + a


if __name__ == '__main__':
    fibonacci()