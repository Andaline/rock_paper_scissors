import tkinter as tk
import socket
import threading

class MultiplayerGUI:
    def __init__(self, theme="default"):
        self.theme = theme
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.move_sent = False

        self.root = tk.Tk()
        self.root.title("Multiplayer - Rock Paper Scissors")
        self.root.geometry("420x380")

        self.status = tk.StringVar()
        self.status.set("Connecting to server...")

        self.build_ui()
        threading.Thread(target=self.connect_to_server, daemon=True).start()

    def build_ui(self):
        tk.Label(self.root, text="Multiplayer Mode", font=("Helvetica", 18)).pack(pady=10)
        tk.Label(self.root, textvariable=self.status, wraplength=400, justify="center").pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        for move in ["rock", "paper", "scissors"]:
            btn = tk.Button(self.button_frame, text=move.capitalize(), width=10,
                            command=lambda m=move: self.send_move(m), state="disabled")
            btn.pack(side="left", padx=10)

        self.play_again_btn = tk.Button(self.root, text="Play Again", command=self.reset_game, state="disabled")
        self.play_again_btn.pack(pady=5)

        self.back_btn = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu)
        self.back_btn.pack(pady=5)

    def connect_to_server(self):
        try:
            self.client.connect(('127.0.0.1', 5555))
            msg = self.client.recv(1024).decode()
            self.status.set(f"{msg}\nWaiting for another player to join...")
            ready = self.client.recv(1024).decode()
            if "both players" in ready.lower():
                self.status.set("Both players connected!\nMake your move:")
                self.set_buttons_state("normal")

            self.connected = True
            threading.Thread(target=self.listen_for_result, daemon=True).start()
        except Exception as e:
            self.status.set(f"Connection failed: {e}")

    def send_move(self, move):
        if self.connected and not self.move_sent:
            try:
                self.client.sendall(move.encode())
                self.status.set(f"You chose {move.capitalize()}\nWaiting for opponent...")
                self.move_sent = True
                self.set_buttons_state("disabled")
            except:
                self.status.set("Failed to send move. Disconnected.")

    def listen_for_result(self):
        while True:
            try:
                result = self.client.recv(1024).decode()
                if result:
                    self.status.set(f"🟢 {result}")
                    self.play_again_btn.config(state="normal")
            except:
                self.status.set("Connection lost.")
                break

    def set_buttons_state(self, state):
        for child in self.button_frame.winfo_children():
            child.config(state=state)

    def reset_game(self):
        self.status.set("Make your choice:")
        self.move_sent = False
        self.set_buttons_state("normal")
        self.play_again_btn.config(state="disabled")

    def back_to_menu(self):
        try:
            self.client.close()
        except:
            pass
        self.root.destroy()
        import menu
        menu.MainMenu(tk.Tk()).run()

    def run(self):
        self.root.mainloop()