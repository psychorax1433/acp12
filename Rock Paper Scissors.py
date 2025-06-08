import tkinter as tk
import random

# Game logic
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie! 😐"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win! 🎉"
    else:
        result = "Computer Wins! 😢"

    # Update display
    user_choice_var.set(f"You chose: {user_choice}")
    comp_choice_var.set(f"Computer chose: {comp_choice}")
    result_var.set(result)

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Variables
user_choice_var = tk.StringVar()
comp_choice_var = tk.StringVar()
result_var = tk.StringVar()

# Labels
tk.Label(root, text="Choose Rock, Paper or Scissors:", font=("Arial", 14)).pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=12, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=12, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=12, command=lambda: play("Scissors")).pack(pady=5)

# Output Labels
tk.Label(root, textvariable=user_choice_var, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=comp_choice_var, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=result_var, font=("Arial", 14, "bold")).pack(pady=10)

root.mainloop()
