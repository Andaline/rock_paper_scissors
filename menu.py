import tkinter as tk
import subprocess
import sys

def launch_game():
    import game.gui
    game.gui.launch_gui()

def launch_multiplayer():
    subprocess.Popen([sys.executable, "network/client.py"])

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Rock Paper Scissors - Main Menu")
root.geometry("360x300")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title.pack(pady=20)

play_btn = tk.Button(root, text="🕹 Start Game", width=25, height=2, command=launch_game)
play_btn.pack(pady=5)

multi_btn = tk.Button(root, text="🌐 Play Online (Multiplayer)", width=25, height=2, command=launch_multiplayer)
multi_btn.pack(pady=5)

exit_btn = tk.Button(root, text="❌ Quit", width=25, height=2, command=exit_app)
exit_btn.pack(pady=20)

root.mainloop()
