# Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


def get_first_element(lst):
    print(lst[0])

user_list_size = int(input("List size? "))

lst = []

for i in range(user_list_size):
    elements = input(f"Enter {i + 1} Elements: ")
    lst.append(elements)

get_first_element(lst)