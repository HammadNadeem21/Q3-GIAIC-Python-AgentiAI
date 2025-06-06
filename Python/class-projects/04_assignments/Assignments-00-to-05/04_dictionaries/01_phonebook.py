# # Problem Statement
# # In this program we show an example of using dictionaries to keep track of information in a phonebook.



def read_phone_numbers():

    phonebook = {}                  

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):

    for name in phonebook:
        print(str(name) + " : " + str(phonebook[name]))


def search_numbers(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    search_numbers(phonebook)


if __name__ == '__main__':
    main()