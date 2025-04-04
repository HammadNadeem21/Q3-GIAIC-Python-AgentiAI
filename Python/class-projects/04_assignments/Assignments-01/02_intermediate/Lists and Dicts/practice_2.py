def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."
    
def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."
    
def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."




def index_game():
    while True:
        lst = ["Hammad", 20, True, ("Apple", "Banana"), 66.78]

        print("\nCurrent List: ", lst)
        print("Chose one option")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

    
        choice = int(input("\nSelect an option (1 to 4): "))

        if choice == 1:
            index = int(input("Enter the index to access: "))
            print("Result: ", access_element(lst, index))
        elif choice == 2:
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print("Result: ", modify_element(lst, index, new_value))
        elif choice == 3:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Result: ",slice_list(lst, start, end))
        elif choice == 4:
            break



if __name__ == '__main__':
    index_game()