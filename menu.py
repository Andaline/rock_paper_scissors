import tkinter as tk
from tkinter import messagebox
import game.core as core
import game.multiplayer as multiplayer  # Fixed import
from game.config import THEMES

class MainMenu:
    def __init__(self, root, theme='default'):
        self.root = root
        self.root.title("Rock Paper Scissors - Main Menu")
        self.root.geometry("400x400")

        self.current_theme = theme

        # Create widgets first
        self.title = tk.Label(self.root, text="Rock Paper Scissors", font=("Arial", 20))
        self.title.pack(pady=20)

        self.single_btn = tk.Button(self.root, text="Single Player", font=("Arial", 14), command=self.start_singleplayer)
        self.single_btn.pack(pady=10)

        self.multi_btn = tk.Button(self.root, text="Multiplayer", font=("Arial", 14), command=self.start_multiplayer)
        self.multi_btn.pack(pady=10)

        self.theme_btn = tk.Button(self.root, text="Change Theme", font=("Arial", 14), command=self.change_theme)
        self.theme_btn.pack(pady=10)

        # Now it's safe to apply the theme
        self.apply_theme(self.current_theme)

        self.root.bind("<Button-1>", self.mouse_click)

    def run(self):
        self.root.mainloop()


    def start_singleplayer(self):
        self.root.destroy()
        from game.gui import launch_gui
        launch_gui()  # ✅ Correct entry point


    def start_multiplayer(self):
        self.root.destroy()
        multiplayer.start_multiplayer(theme=self.current_theme)

    def change_theme(self):
        theme_keys = list(THEMES.keys())
        current_index = theme_keys.index(self.current_theme)
        self.current_theme = theme_keys[(current_index + 1) % len(theme_keys)]
        self.apply_theme(self.current_theme)

    def apply_theme(self, theme_name):
        theme = THEMES[theme_name]
        self.root.config(bg=theme['bg'])
        for widget in [self.title, self.single_btn, self.multi_btn, self.theme_btn]:
            widget.config(bg=theme['bg'], fg=theme['fg'])
            self.single_btn.config(bg=theme['bg'], fg=theme['fg'])
            self.multi_btn.config(bg=theme['bg'], fg=theme['fg'])
            self.theme_btn.config(bg=theme['bg'], fg=theme['fg'])

    def mouse_click(self, event):
        print(f"Mouse clicked at: {event.x}, {event.y}")
        # Tkinter already handles button clicks, this is just a debug log

if __name__ == "__main__":
    from game.config import DEFAULT_THEME  # import this for consistency
    root = tk.Tk()
    app = MainMenu(root, theme=DEFAULT_THEME)  # or hardcode "Dark" here
    root.mainloop()
