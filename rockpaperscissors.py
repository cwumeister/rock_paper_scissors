import random

def main():
    user = show_hand()
    comp = comp_hand()

    print("Rock, paper, scissors, shoot!")
    print("User hand: " + user)
    print("Computer hand: " + comp)

    if user == comp:
        print("We both drew the same thing, it's a tie!")
    elif user == "ROCK":
        if comp == "PAPER":
            print("Paper beats Rock, I win!")
        else:
            print("Rock beats Scissors, you win!")
    elif user == "PAPER":
        if comp == "ROCK":
            print("Paper beats Rock, you win!")
        else:
            print("Scissors beats Paper, I win!")
    else:
        if comp == "PAPER":
            print("Scissors beats Paper, you win!")
        elif comp == "ROCK":
            print("Rock beats Scissors, I win!")
            
#prompts user for input
def show_hand():
    possible = {"ROCK", "PAPER", "SCISSORS"}

    #if user does not choose one of the three, repeats
    while True:
        hand = str(input("Rock, Paper, or Scissors?: "))
        hand = hand.upper().strip()
        if hand in possible:
            break
        else:
            print("That is not one of the plays! Try again!")
    return hand

#assigns computer a random value
def comp_hand():
    words = ("ROCK", "PAPER", "SCISSORS")
    word = random.choice(words)
    return word

main()