import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low!")
        if guess > random_number:
            print("Too high!")
    print(f"Mazal tov! The numer is {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        feedback = input(f"Is {guess} your number? pass 'h', 'l' or 'c'").lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"Kol aKavod, computer! The numer is {guess}")


computer_guess(100)
