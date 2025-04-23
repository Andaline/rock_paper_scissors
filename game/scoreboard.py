import tkinter as tk
import random
from game.core import determine_winner, choices, win_sound, lose_sound, tie_sound
from game.config import VOLUME, THEME
from game.scoreboard import load_scores, save_scores, reset_scores
from game.profiles import list_profiles, load_profile, save_profile, delete_profile
from game.multiplayer import local_multiplayer_round

player_score = 0
computer_score = 0
round_limit = 3
current_profile = "default"
is_multiplayer = False

# Set initial volumes
win_sound.set_volume(VOLUME)
lose_sound.set_volume(VOLUME)
tie_sound.set_volume(VOLUME)

def update_scores(result):
    global player_score, computer_score
    if "Player 1 wins" in result or "Player wins" in result:
        player_score += 1
    elif "Player 2 wins" in result or "Computer wins" in result:
        computer_score += 1

    save_scores(player_score, computer_score, profile=current_profile)

    if player_score >= round_limit:
        result_text.set(f"{current_profile} wins the match! Final Score: {player_score} - {computer_score}")
        disable_buttons()
    elif computer_score >= round_limit:
        result_text.set(f"Opponent wins the match! Final Score: {player_score} - {computer_score}")
        disable_buttons()

def flash_label():
    colors = [THEME["highlight"], THEME["fg"]]
    for i, color in enumerate(colors * 2):
        root.after(i * 150, lambda c=color: result_label.config(fg=c))

def play_round(player_choice):
    if is_multiplayer:
        player2_choice = multiplayer_choice.get()
        result = local_multiplayer_round(player_choice, player2_choice)
    else:
        computer_choice = random.choice(choices)
        result = determine_winner(player_choice, computer_choice)
    update_scores(result)
    result_text.set(
        f"{result}\n\nScores:\n{current_profile}: {player_score} | Opponent: {computer_score}"
    )
    flash_label()

def disable_buttons():
    for widget in button_frame.winfo_children():
        widget.config(state="disabled")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_text.set("Scores reset! Make your choice to start again.")
    for widget in button_frame.winfo_children():
        widget.config(state="normal")
    result_label.config(fg=THEME["fg"])
    reset_scores(profile=current_profile)

def set_round_limit():
    global round_limit
    try:
        val = int(round_selector.get())
        round_limit = max(1, val)
    except ValueError:
        round_limit = 3

def open_profile_manager():
    def refresh():
        for w in listbox.get(0, tk.END):
            listbox.delete(0)
        for name in list_profiles():
            listbox.insert(tk.END, name)

    def delete_selected():
        selected = listbox.curselection()
        if selected:
            delete_profile(listbox.get(selected))
            refresh()

    def set_active():
        nonlocal profile_window
        selected = listbox.curselection()
        if selected:
            global current_profile, player_score, computer_score
            current_profile = listbox.get(selected)
            data = load_scores(current_profile)
            player_score = data.get("player", 0)
            computer_score = data.get("computer", 0)
            profile_window.destroy()
            launch_gui()

    def create_profile():
        name = entry.get().strip()
        if name:
            save_profile(name, {"player": 0, "computer": 0, "highscore": 0, "streak": 0})
            refresh()

    profile_window = tk.Tk()
    profile_window.title("Profile Manager")

    listbox = tk.Listbox(profile_window)
    listbox.pack(padx=10, pady=5)

    for name in list_profiles():
        listbox.insert(tk.END, name)

    tk.Button(profile_window, text="Set Active", command=set_active).pack(fill="x")
    tk.Button(profile_window, text="Delete", command=delete_selected).pack(fill="x")

    entry = tk.Entry(profile_window)
    entry.pack(pady=5)
    tk.Button(profile_window, text="Create New", command=create_profile).pack(fill="x")

    profile_window.mainloop()

def show_leaderboard():
    leaderboard = tk.Tk()
    leaderboard.title("Leaderboard")
    leaderboard.geometry("300x300")

    tk.Label(leaderboard, text="High Scores (by wins)").pack()

    sorted_profiles = sorted(
        [(name, load_scores(name)) for name in list_profiles()],
        key=lambda item: item[1].get("highscore", 0),
        reverse=True
    )

    for name, stats in sorted_profiles:
        tk.Label(leaderboard, text=f"{name}: {stats.get('highscore', 0)} wins, Streak: {stats.get('streak', 0)}").pack()

def choose_profile():
    def start():
        global current_profile, player_score, computer_score
        current_profile = profile_entry.get()
        data = load_scores(current_profile)
        player_score = data.get("player", 0)
        computer_score = data.get("computer", 0)
        profile_window.destroy()
        launch_gui()

    profile_window = tk.Tk()
    profile_window.title("Select Profile")
    tk.Label(profile_window, text="Enter your profile name:").pack(pady=10)

    profile_entry = tk.Entry(profile_window)
    profile_entry.pack(pady=5)

    profile_list = list_profiles()
    tk.Label(profile_window, text=f"Available: {', '.join(profile_list)}").pack(pady=5)

    tk.Button(profile_window, text="Start Game", command=start).pack(pady=10)
    tk.Button(profile_window, text="Profile Manager", command=lambda: [profile_window.destroy(), open_profile_manager()]).pack()
    profile_window.mainloop()

def toggle_multiplayer():
    global is_multiplayer
    is_multiplayer = not is_multiplayer
    multiplayer_frame.pack_forget() if not is_multiplayer else multiplayer_frame.pack(pady=5)
    toggle_button.config(text="Switch to Single Player" if is_multiplayer else "Switch to Multiplayer")

def launch_gui():
    global root, result_label, result_text, button_frame, round_selector, multiplayer_choice, multiplayer_frame, toggle_button

    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.geometry("420x520")
    root.resizable(False, False)
    root.configure(bg=THEME["bg"])

    result_text = tk.StringVar()
    result_text.set("Make your choice to start playing!")

    result_label = tk.Label(root, textvariable=result_text, wraplength=380, justify="center", bg=THEME["bg"], fg=THEME["fg"])
    result_label.pack(pady=20)

    button_frame = tk.Frame(root, bg=THEME["bg"])
    button_frame.pack()

    for choice in choices:
        btn = tk.Button(
            button_frame,
            text=choice.capitalize(),
            width=10,
            command=lambda c=choice: play_round(c)
        )
        btn.pack(side="left", padx=10)

    multiplayer_frame = tk.Frame(root, bg=THEME["bg"])
    tk.Label(multiplayer_frame, text="Player 2 choice:", bg=THEME["bg"], fg=THEME["fg"]).pack()
    multiplayer_choice = tk.StringVar(value="rock")
    tk.OptionMenu(multiplayer_frame, multiplayer_choice, *choices).pack()

    toggle_button = tk.Button(root, text="Switch to Multiplayer", command=toggle_multiplayer)
    toggle_button.pack(pady=5)

    reset_button = tk.Button(root, text="Reset Game", command=reset_game)
    reset_button.pack(pady=10)

    round_selector_label = tk.Label(root, text="Best of how many rounds?", bg=THEME["bg"], fg=THEME["fg"])
    round_selector_label.pack()

    round_selector = tk.Spinbox(root, from_=1, to=15, width=5, command=set_round_limit)
    round_selector.pack(pady=5)
    round_selector.delete(0, "end")
    round_selector.insert(0, "3")

    leaderboard_button = tk.Button(root, text="View Leaderboard", command=show_leaderboard)
    leaderboard_button.pack(pady=5)

    root.mainloop()

# Entry point for GUI
if __name__ == "__main__":
    choose_profile()