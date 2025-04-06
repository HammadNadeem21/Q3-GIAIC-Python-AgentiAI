def main():
    print("Welcome to the Mad Libs Game!")

    name = input("Enter your name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    food = input("Enter a type of food: ")

    story = f"""
    One day, {name} went to {place} and saw a {adjective} {animal}.
    Without thinking, {name} decided to {verb} with it.
    Afterwards, they both sat down and enjoyed some delicious {food} together.
    It was a day to remember!
    """

    print(story)


if __name__ == '__main__':
    main()