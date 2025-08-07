import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")
        
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
        
    if (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "scissors" and computer_choice == "paper") or \
    (user_choice == "paper" and computer_choice == "rock"):
        return "You Win!"   
    else:
        return "You Lose!"
    
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

# To start the game
if __name__ == "__main__":
    play_game() 