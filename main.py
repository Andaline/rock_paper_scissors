import tkinter as tk
from game.config import DEFAULT_THEME
from menu import MainMenu
from game import core, multiplayer
import json

def get_theme_from_profile():
    try:
        with open("profile/default.json", "r") as f:
            data = json.load(f)
        return data.get("theme", DEFAULT_THEME)
    except Exception as e:
        print(f"Error loading theme: {e}")
        return DEFAULT_THEME

def launch_game(mode):
    theme = get_theme_from_profile()
    if mode == "single":
        core.start_game(theme=theme)
    elif mode == "multi":
        multiplayer.start_multiplayer(theme=theme)

if __name__ == "__main__":
    theme = get_theme_from_profile()
    root = tk.Tk()
    menu = MainMenu(root, theme=theme)  # ✅ finally passing the actual theme here!
    menu.run()
