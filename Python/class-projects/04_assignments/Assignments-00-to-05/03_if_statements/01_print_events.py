# Problem Statement

# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

def even_num():
    for even in range(20):
        print(even * 2)


if __name__ == "__main__":
    even_num()