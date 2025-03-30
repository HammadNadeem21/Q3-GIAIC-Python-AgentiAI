# Problem Statement

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

max_length = 3

def shorten(lst):

    while len(lst) > max_length:
        removed_items = lst.pop()
        print(f"Removed {removed_items}")


def get_user_list():
    lst = []

    while True:

        value = input("Enter a value: ")

        if value == "":
            break

        lst.append(value)

    return(lst)

lst = get_user_list()
shorten(lst)
print(f"Final List: {lst}")