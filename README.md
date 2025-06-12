# Rock-Paper-Scissors Game 🎮

This is a simple **Rock-Paper-Scissors** game built using Python. It runs in the terminal and allows you to play against the computer.

## 🧠 How It Works

- You choose either **rock**, **paper**, or **scissors**.
- The computer randomly picks one of the three options.
- The game determines the winner based on the following rules:
  - Rock beats Scissors
  - Paper beats Rock
  - Scissors beats Paper
- If both selections are the same, it's a tie.
- The game continues until you type `exit`.

## 📜 Rules Table

| Player Choice | Computer Choice | Result         |
|---------------|------------------|----------------|
| Rock          | Scissors         | You win!       |
| Paper         | Rock             | You win!       |
| Scissors      | Paper            | You win!       |
| Same          | Same             | It's a tie!    |
| Invalid       | -                | Invalid input  |

## 💻 Code

```python
import random

# Game options
choices = ["rock", "paper", "scissors"]

# Function to check winner
def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or          (user == "paper" and computer == "rock") or          (user == "scissors" and computer == "paper"):
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
```

## ▶️ How to Run

1. Save the code in a file named `rock_paper_scissors.py`.
2. Run the file using Python:

```bash
python rock_paper_scissors.py
```

## ✅ Requirements

- Python 3.x
- No external libraries needed

## 🏁 Exit the Game

To quit the game, type:

```
exit
```
