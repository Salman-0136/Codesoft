import random

user_wins = 0
computer_wins = 0

print("Welcome to Rock Paper Scissors Game!")

def game():
    global user_wins
    global computer_wins
    
    randomNumber = random.randint(0, 2)
    options = ["rock", "paper", "scissors"]
    
    print("Choose Rock, Paper, Scissors or Quit:")
    print("Press 'rock' to choose Rock")
    print("Press 'paper' to choose Paper")
    print("Press 'scissors' to choose Scissors")
    user_choice = input("Enter your choice: ").lower()
    
    if user_choice not in options:
        print("\nInvalid choice. Please try again.\n")
        return game()

    computer_choice = options[randomNumber]
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

while True:
    game()
    print("You won", user_wins, "times.")
    print("Computer won", computer_wins, "times.")
    print("\n")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y":
        game()
    elif play_again.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        break
