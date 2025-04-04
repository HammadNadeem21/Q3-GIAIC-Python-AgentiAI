# Problem Statement
#  fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)


messages = []

user_message = input("Enter a message to copy: ")

print("list before: ", messages)

add_three_copies(messages, user_message)

print("list after: ", messages)