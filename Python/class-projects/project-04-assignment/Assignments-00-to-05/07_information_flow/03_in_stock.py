# Problem Statement
# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory.


bold_italics = "\033[1;3m"
reset = "\033[0m"


def num_in_stock(fruit):

    if fruit == "apple":
        return 15
    elif fruit == "banana":
        return 36
    elif fruit == "orange":
        return 24
    elif fruit == "pear":
        return 200
    else:
        return 0
    
def main():
    fruit = input(f"{bold_italics}Enter a fruit: {reset}")
    stock = num_in_stock(fruit)
        
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)


if __name__ == '__main__':
    main()