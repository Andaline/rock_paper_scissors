import tkinter as tk
from tkinter import ttk
import random
from game.core import determine_winner, choices
from game.config import THEMES, DEFAULT_THEME

def launch_gui():
    round_limit = 3
    player_score = 0
    computer_score = 0
    global root, result_label, result_text, button_frame, round_selector, theme_var

    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.geometry("420x400")
    root.resizable(False, False)

    theme_var = tk.StringVar(value=DEFAULT_THEME)

    style = ttk.Style()
    style.theme_use('clam')

    def apply_theme(theme_name):
        theme = THEMES[theme_name]
        root.config(bg=theme["bg"])
        style.configure("TCombobox",
            fieldbackground=theme["bg"],
            background=theme["bg"],
            foreground=theme["fg"]
        )
        for widget in root.winfo_children():
            try:
                widget.config(bg=theme["bg"], fg=theme["fg"])
            except:
                pass

    def on_enter(e):
        e.widget['background'] = THEMES[theme_var.get()]["highlight"]

    def on_leave(e):
        e.widget['background'] = THEMES[theme_var.get()]["bg"]

    def flash_label():
        colors = ["red", "blue", "green", "black"]
        for i, color in enumerate(colors):
            root.after(i * 100, lambda c=color: result_label.config(fg=c))

    def update_scores(result):
        nonlocal player_score, computer_score
        if "Player wins" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        if player_score >= round_limit:
            result_text.set(f"Player wins the match! Final Score: {player_score} - {computer_score}")
            disable_buttons()
        elif computer_score >= round_limit:
            result_text.set(f"Computer wins the match! Final Score: {player_score} - {computer_score}")
            disable_buttons()

    def play_round(player_choice):
        computer_choice = random.choice(choices)
        result = determine_winner(player_choice, computer_choice)
        update_scores(result)
        result_text.set(
            f"Player chose {player_choice}\nComputer chose {computer_choice}\n{result}\n\nScores:\nPlayer: {player_score} | Computer: {computer_score}"
        )
        flash_label()

    def disable_buttons():
        for widget in button_frame.winfo_children():
            widget.config(state="disabled")

    def reset_game():
        nonlocal player_score, computer_score
        player_score = 0
        computer_score = 0
        result_text.set("Scores reset! Make your choice to start again.")
        for widget in button_frame.winfo_children():
            widget.config(state="normal")
        result_label.config(fg="black")

    def set_round_limit():
        nonlocal round_limit
        try:
            val = int(round_selector.get())
            round_limit = max(1, val)
        except ValueError:
            round_limit = 3

    theme_menu = ttk.Combobox(root, textvariable=theme_var, values=list(THEMES.keys()), state="readonly")
    theme_menu.pack(pady=5)
    theme_menu.bind("<<ComboboxSelected>>", lambda e: apply_theme(theme_var.get()))

    result_text = tk.StringVar()
    result_text.set("Make your choice to start playing!")
    result_label = tk.Label(root, textvariable=result_text, wraplength=380, justify="center")
    result_label.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    for choice in choices:
        btn = tk.Button(
            button_frame,
            text=choice.capitalize(),
            width=10,
            command=lambda c=choice: play_round(c),
            bg=THEMES[DEFAULT_THEME]["bg"],
            fg=THEMES[DEFAULT_THEME]["fg"],
            activebackground=THEMES[DEFAULT_THEME]["highlight"],
            activeforeground=THEMES[DEFAULT_THEME]["fg"]
        )
        btn.pack(side="left", padx=10)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    reset_button = tk.Button(root, text="Reset Game", command=reset_game,
                             bg=THEMES[DEFAULT_THEME]["bg"], fg=THEMES[DEFAULT_THEME]["fg"],
                             activebackground=THEMES[DEFAULT_THEME]["highlight"])
    reset_button.pack(pady=10)
    reset_button.bind("<Enter>", on_enter)
    reset_button.bind("<Leave>", on_leave)

    round_selector_label = tk.Label(root, text="Best of how many rounds?")
    round_selector_label.pack()
    round_selector = tk.Spinbox(root, from_=1, to=15, width=5, command=set_round_limit)
    round_selector.pack(pady=5)
    round_selector.delete(0, "end")
    round_selector.insert(0, "3")

    apply_theme(DEFAULT_THEME)
    root.mainloop()