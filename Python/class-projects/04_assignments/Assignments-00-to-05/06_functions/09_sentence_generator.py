# Problem Statement
# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"

# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"

# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.

blue = "\033[94m" 
reset = "\033[0m" 

def make_sentence(word:str, part_of_speach:int):
    if part_of_speach == 0:
        #  Noun
         print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speach == 1:
        #  Verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speach == 2:
        # Adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")
    

def main():
    word :  str = input(f"{blue}Please type a noun, verb, or adjective: {reset}")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input(f"{blue}Type 0 for noun, 1 for verb, 2 for adjective: {reset}"))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()