import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer's choice: {computer_choice}\n{result}")

    update_score(result)

def update_score(result):
    global user_score, computer_score
    if 'win' in result:
        user_score += 1
    elif 'lose' in result:
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

def on_button_click(choice):
    play_game(choice)

def on_play_again():
    result_label.config(text="")
    user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# User input entry
user_entry = tk.Entry(root, width=20)
user_entry.grid(row=0, column=0, padx=10, pady=10)

# Buttons for rock, paper, and scissors
rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click("rock"))
rock_button.grid(row=1, column=0, padx=5, pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("paper"))
paper_button.grid(row=1, column=1, padx=5, pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("scissors"))
scissors_button.grid(row=1, column=2, padx=5, pady=5)

# Result display label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Score display label
score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Arial", 12))
score_label.grid(row=3, column=0, columnspan=3, pady=10)

# Play again button
play_again_button = tk.Button(root, text="Play Again", command=on_play_again)
play_again_button.grid(row=4, column=0, columnspan=3, pady=10)

# Initialize scores
user_score = 0
computer_score = 0

# Run the GUI
root.mainloop()
