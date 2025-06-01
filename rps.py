import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")
window.config(bg="lightblue")

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

# UI Elements
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20), bg="lightblue")
title_label.pack(pady=20)

btn_frame = tk.Frame(window, bg="lightblue")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, height=2, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, height=2, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, height=2, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(window, text="", font=("Arial", 14), justify="center")
result_label.pack(pady=30)

window.mainloop()
