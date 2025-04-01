# Problem Statement
# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

bold_italics = "\033[1;3m"
reset = "\033[0m"


ADULT_AGE : int = 18

def is_adult(age:int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input(f"{bold_italics}How old is this person?: {reset}"))
    print(is_adult(age))


if __name__ == '__main__':
    main()