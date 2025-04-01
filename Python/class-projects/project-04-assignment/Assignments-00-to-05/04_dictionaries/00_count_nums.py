# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def count_numbers():

    frequency = {}

    while True:

        num = input("Enter a number: ")

        if num == "":
            break

        num = int(num)

        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        
    for number, count in frequency.items():
            print(f"{number} appears {count} times")

    
if __name__ == '__main__':
    count_numbers()