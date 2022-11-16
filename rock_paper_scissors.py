import random


def play():
    user = ""
    while user != "e":
        user = input("'r' for rock, 'p' for paper, 's' for scissors, 'e' for exit: ")
        computer = random.choice(["r", "p", "s"])
        print(f"{user} vs {computer}")
        if user == computer:
            print("Draw! play again!")
        # r>s, s>p, p>r
        if is_win(user, computer):
            print("You won! Play again!")
        if is_win(computer, user):
            print("Computer won! Play again!")
        if user == "e":
            print("OK, let's play later...")


def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


play()
