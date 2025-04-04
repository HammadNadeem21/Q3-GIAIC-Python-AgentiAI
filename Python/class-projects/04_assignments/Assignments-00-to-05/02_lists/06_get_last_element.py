# Problem Statement

# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_first_element(lst):
    print(lst[-1])

user_list_size = int(input("List size? "))

lst = []

for i in range(user_list_size):
    elements = input(f"Enter {i + 1} Elements: ")
    lst.append(elements)

get_first_element(lst)