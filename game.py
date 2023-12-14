import random

print("Choose - Rock, Paper, or Scissor")
user_play = input("Enter your move - ").lower() 
computer_play = ""
random_number = random.randint(1, 3)

if random_number == 1:
    computer_play = "rock"
elif random_number == 2:
    computer_play = "paper"
elif random_number == 3:
    computer_play = "scissors"


valid_inputs = ["rock", "paper", "scissors"]

if user_play in valid_inputs:
    print("Computer played -", computer_play)
    if user_play == computer_play:
        print("It's a tie")
    elif user_play == "rock" and computer_play == "paper":
        print("Computer Wins")
    elif user_play == "paper" and computer_play == "scissors":
        print("Computer Wins")
    elif user_play == "scissors" and computer_play == "rock":
        print("Computer Wins")
    else:
        print("You win")
else:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")
