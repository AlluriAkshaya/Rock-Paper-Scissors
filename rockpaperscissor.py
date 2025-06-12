import random

# Game options
choices = ["rock", "paper", "scissors"]

# Function to check winner
def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Game loop
while True:
    print("\n--- Rock, Paper, Scissors ---")
    user_input = input("Choose rock, paper, or scissors (or 'exit' to stop): ").lower()

    if user_input == "exit":
        print("Thanks for playing!")
        break

    if user_input not in choices:
        print("Invalid input. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    print(check_winner(user_input, computer_choice))
