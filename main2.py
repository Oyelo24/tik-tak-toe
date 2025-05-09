import customtkinter as ctk
from tkinter import messagebox
from random import randint

# Initialize appearance
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")

# GLOBAL VARIABLES
ActivePlayer = 1
p1 = []
p2 = []
Count = 0
ScoreX = 0
ScoreO = 0

# Functions
def ButtonClick(id):
    global ActivePlayer
    global Count

    button = buttons[id - 1]
    if button.cget("text") == "":
        if ActivePlayer == 1:
            button.configure(text='X', text_color="blue")
            p1.append(id)
            ActivePlayer = 2
            root.title("Tic Tac Toe :Player 2")
        elif ActivePlayer == 2:
            button.configure(text='O', text_color="red")
            p2.append(id)
            ActivePlayer = 1
            root.title("Tic Tac Toe :Player 1")
        Count += 1
        CheckWinner()

def CheckWinner():
    global ScoreX, ScoreO

    winner = -1
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)              # diagonals
    ]

    for combo in winning_combinations:
        if all(pos in p1 for pos in combo):
            winner = 1
        if all(pos in p2 for pos in combo):
            winner = 2

    if winner == 1:
        ScoreX += 1
        messagebox.showinfo("Tic Tac Toe", "Player 1 Wins!")
        Restart()
    elif winner == 2:
        ScoreO += 1
        messagebox.showinfo("Tic Tac Toe", "Player 2 Wins!")
        Restart()
    elif Count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        Restart()

def Restart():
    global p1, p2, Count, ActivePlayer
    p1 = []
    p2 = []
    Count = 0
    ActivePlayer = 1
    root.title("Tic Tac Toe :Player 1")
    for btn in buttons:
        btn.configure(text="")
    UpdateScore()

def UpdateScore():
    label2.configure(text=f'SCORE-->PLAYER1: {ScoreX}\n-->PLAYER2: {ScoreO}')

def AutoPlay():
    global ActivePlayer

    empty_cells = [i for i in range(1, 10) if i not in p1 and i not in p2]
    if empty_cells:
        cell = randint(0, len(empty_cells) - 1)
        ButtonClick(empty_cells[cell])

# Main Window
root = ctk.CTk()
root.title("Tic Tac Toe :Player 1")
root.geometry("600x800")
root.resizable(False, False)

# Labels
label1 = ctk.CTkLabel(root, text='Tic Tac Toe', font=("Times", 20, "bold"), text_color='black', height=50, width=120, fg_color='cyan', corner_radius=6)
label1.grid(row=0, column=1, padx=5, pady=5, sticky='nsnew')

label2 = ctk.CTkLabel(root, text=f'SCORE-->PLAYER1: {ScoreX}\n-->PLAYER2: {ScoreO}', font=("Times", 15, "bold"), text_color='black', height=50, width=120, fg_color='cyan', corner_radius=6)
label2.grid(row=4, column=0, padx=5, pady=5, sticky='nsnew')

label3 = ctk.CTkLabel(root, text='PLAYER 1', font=("Times", 15, "bold"), text_color='black', height=50, width=120, fg_color='cyan', corner_radius=6)
label3.grid(row=0, column=0, padx=15, pady=5, sticky='nsnew')

label4 = ctk.CTkLabel(root, text='PLAYER 2', font=("Times", 15, "bold"), text_color='black', height=50, width=120, fg_color='cyan', corner_radius=6)
label4.grid(row=0, column=2, padx=15, pady=5, sticky='nsnew')

# Buttons (game board)
buttons = []
for i in range(9):
    btn = ctk.CTkButton(root, text='', font=("Times", 35, "bold"), fg_color='white', text_color='black', width=160, height=160, command=lambda i=i: ButtonClick(i+1))
    btn.grid(row=1 + i // 3, column=i % 3, padx=15, pady=5, sticky='news')
    buttons.append(btn)

# Control Buttons
restart_btn = ctk.CTkButton(root, text='RESTART', font=("Times", 20, "bold"), fg_color='green', text_color='white', corner_radius=6, command=Restart)
restart_btn.grid(row=4, column=1, padx=5, pady=5, sticky='nsnew')

auto_btn = ctk.CTkButton(root, text='Auto Play', font=("Times", 20, "bold"), fg_color='blue', text_color='white', corner_radius=6, command=AutoPlay)
auto_btn.grid(row=4, column=2, padx=5, pady=5, sticky='nsnew')

root.mainloop()
