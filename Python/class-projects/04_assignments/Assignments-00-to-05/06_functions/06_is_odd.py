def is_odd(value:int):
    reminder = value % 2
    return reminder == 1

def main():
    for i in range(11):
        if is_odd(i):
            print(i, "Odd", end=" ")
        else:
            print(i, "Even", end=" ")

if __name__ == '__main__':
    main()
