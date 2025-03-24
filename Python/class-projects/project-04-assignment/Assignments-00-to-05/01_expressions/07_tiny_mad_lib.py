# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

bold_italics = "\033[1;3m"
reset = "\033[0m"


sentence = "Code in Place is fun. I learned to program and used Python to make my"

def mad_libs():
    adjective:str = input(f"{bold_italics}Please type an adjective and press enter. {reset}")
    noun:str = input(f"{bold_italics}Please type a noun and press enter. {reset}")
    verb:str = input(f"{bold_italics}Please type a verb and press enter. {reset}")

    print(f"{bold_italics}The {adjective} {noun} loves to {verb} every day.{reset}")

if __name__ == '__main__':
    mad_libs()