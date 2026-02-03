"""
Description:

- Write a Python program that simulates the "Rock, Paper, Scissors" game.

- The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").

- The player should play against the computer, which will select a random option.

- The computer's selection will be compared against the player's selection to determine who wins.

- A descriptive message should be displayed indicating if the player won, lost, or if the game ended in a tie.
"""

from random import randint

player = input("What do you want to play? (Rock, Paper or Scissors): ").lower()

random_choice = randint(0, 2)

options = ["rock", "paper", "scissors"]

computer = options[random_choice]

if player == computer:
    print("It's a tie! Try again.")
elif player == "rock":
    if computer == "paper":
        print("You lose! Your opponent chose 'Paper'")
    else:
        print("You win! Your opponent chose 'Scissors'")
elif player == "paper":
    if computer == "scissors":
        print("You lose! Your opponent chose 'Scissors'")
    else:
        print("You win! Your opponent chose 'Rock'")
elif player == "scissors":
    if computer == "rock":
        print("You lose! Your opponent chose 'Rock'")
    else:
        print("You win! Your opponent chose 'Paper'")
else:
    print("Please enter a valid option.")
