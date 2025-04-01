# Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message.

blue = "\033[94m" 
reset = "\033[0m" 


def print_multiple(message:str, repeat:int):
    for i in range(repeat):
        print(message)


def main():
    message = input(f"{blue}Please type a message: {reset}")
    repeat_num = int(input(f"{blue}Enter a number of times to repeat your message: {reset}"))
    print_multiple(message, repeat_num)


if __name__ == '__main__':
    main()