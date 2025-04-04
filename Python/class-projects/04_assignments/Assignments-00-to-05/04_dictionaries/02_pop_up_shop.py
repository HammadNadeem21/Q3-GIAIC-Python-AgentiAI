# Problem Statement
# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.


def main():
    fruits = {'apple': 150, 'banana': 100, 'orange': 150, 'kiwi': 250, 'watermelon': 120, 'mango': 200}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (amount_bought * price)
    
    print("Your total is $" + str(total_cost))



if __name__ == '__main__':
    main()