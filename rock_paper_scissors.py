import random
choices = ["ROCK","PAPER","SCISSORS"]
while True:
    user_choice = input("ENTER YOUR CHOICE ROCK,PAPER,SCISSORS :")
    computer_choice = random.choice(choices)
    print("YOU CHOOSE:",user_choice)
    print("computer_choice:",computer_choice)

    if user_choice == computer_choice:
       print("IT'S A TIE")
    elif user_choice == "ROCK" and computer_choice == "SCISSORS":
       print("YOU WIN!")
    elif user_choice == "PAPER" and computer_choice == "ROCK":
       print("YOU WIN!")
    elif user_choice == "SCISSORS" and computer_choice == "PAPER":
       print("YOU WIN!")
    elif user_choice in choices:
       print("COMPUTER WINS!")
    else:
       print("INVALID CHOICE!")

    play_again = input("DO YOU WANT TO PLAY AGAIN?")

    if play_again != "YES":
      print("THANKS FOR PLAYING")
      break
