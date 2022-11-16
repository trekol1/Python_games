import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    # getting user input
    while (len(word_letters) > 0) and (lives > 0):

        # used letters and current lives
        print("you have used these letters", " ".join(used_letters))
        print(f"You have {lives} lives")

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("You have already used this charachter. Please try another one")
        else:
            print("Invalid character. Please use a letter")

    # get here if len(word_letters) == 0 or lives == 0
    if len(word_letters) == 0:
        print(f"Mazal Tov! The word is {word}")
    if lives == 0:
        print(f"Sorry, you loose. The word is {word}")


hangman()
