# 🪨 Rock Paper Scissors — Python GUI Game

A fully-featured Rock Paper Scissors game built with Python. Includes sound, animation, multiplayer, persistent profiles, and customizable themes.

---

## ✨ Features

- 🎮 **Tkinter GUI** with hover animations and theme selector
- 🔊 **Sound effects** using `pygame`
- 👤 **Profile system** with persistent scores
- 🏆 **Leaderboard** (high scores + streaks)
- 🔁 **Best-of-N mode** (set number of rounds to win)
- 🧑‍🤝‍🧑 **Multiplayer Modes**:
  - Local 2-player mode
  - Real-time online multiplayer (via sockets)
- 🎨 **Themes**: Light, Dark, Retro — all dynamic
- ⚙️ Easy to extend and configure

---

## 🗂 Project Structure

```plaintext

rock_paper_scissors/
├── game/
│   ├── gui.py              # Main GUI with themes, multiplayer
│   ├── core.py             # Game logic + pygame sound
│   ├── config.py           # Theme settings, volume
│   ├── scoreboard.py       # Profile scores + leaderboard
│   ├── profiles.py         # Profile CRUD
│   ├── multiplayer.py      # Local multiplayer logic
│   └── assets/             # Sound and icon files
├── network/
│   ├── server.py           # Socket server for online play
│   └── client.py           # Socket client
├── profiles/               # Profile score JSONs
├── tests/                  # Unit tests
├── main.py                 # Entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 🖥️ Prerequisites

Install required libraries:

```bash
pip install -r requirements.txt
```

### ▶️ Run the Game

```bash
python main.py
```

---

## 🌐 Online Multiplayer

Start the server:

```bash
python network/server.py
```

On each client:

```bash
python network/client.py
```

---

## 📦 Packaging (.exe or .app)

Use `pyinstaller` to bundle the game:

```bash
pyinstaller --onefile --windowed --icon=game/assets/icon.ico main.py
```

The output will be in the `dist/` folder.

---

## 🧪 Testing

```bash
python -m unittest discover tests
```

---

## 📬 Credits & License

- Built with `tkinter`, `pygame`, and Python 3.
- MIT License — free for use and modification.

---
