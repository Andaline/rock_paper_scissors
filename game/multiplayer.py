from game.gui import MultiplayerGUI
import tkinter as tk
from game.multiplayer_gui import MultiplayerGUI

def start_multiplayer(theme="default"):
    MultiplayerGUI(theme=theme).run()

def local_multiplayer_round(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (
        (player1_choice == "rock" and player2_choice == "scissors") or
        (player1_choice == "paper" and player2_choice == "rock") or
        (player1_choice == "scissors" and player2_choice == "paper")
    ):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

    
def back_to_menu(self):
    self.root.destroy()
    import menu
    menu.MainMenu(tk.Tk()).run()


def start_multiplayer(theme="default"):
    print(f"Starting multiplayer with theme: {theme}")
    gui = MultiplayerGUI(theme=theme)
    gui.run()
