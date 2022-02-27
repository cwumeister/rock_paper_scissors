import random

def main():
    user = show_hand()
    comp = comp_hand()

    print("Rock, paper, scissors, shoot!")
    print("User hand: " + user)
    print("Computer hand: " + comp)

    if user == "ROCK":
        if comp == "PAPER":
            print("Paper beats Rock, I win!")
        elif comp == "SCISSORS":
            print("Rock beats Scissors, you win!")
        else:
            print("We both drew the same thing, it's a tie!")
    elif user == "PAPER":
        if comp == "ROCK":
            print("Paper beats Rock, you win!")
        elif comp == "SCISSORS":
            print("Scissors beats Paper, I win!")
        else:
            print("We both drew the same thing, it's a tie!")
    else:
        if comp == "PAPER":
            print("Scissors beats Paper, you win!")
        elif comp == "ROCK":
            print("Rock beats Scissors, I win!")
        else:
            print("We both drew the same thing, it's a tie!")


def show_hand():
    possible = {"ROCK", "PAPER", "SCISSORS"}

    while True:
        hand = str(input("Rock, Paper, or Scissors?: "))
        hand = hand.upper().strip()
        if hand in possible:
            break
        else:
            print("That is not one of the plays! Try again!")
    return hand

def comp_hand():
    words = ("ROCK", "PAPER", "SCISSORS")
    word = random.choice(words)
    return word

main()