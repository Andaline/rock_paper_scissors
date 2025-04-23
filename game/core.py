import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
win_sound = pygame.mixer.Sound("game/assets/win.wav")
lose_sound = pygame.mixer.Sound("game/assets/lose.wav")
tie_sound = pygame.mixer.Sound("game/assets/tie.wav")

choices = ["rock", "paper", "scissors"]

def start_game(theme="default"):
    print(f"Starting game with theme: {theme}")
    # Initialize game with theme (e.g., background colors, button styles)
    # Existing game logic...


def determine_winner(player, computer):
    if player == computer:
        tie_sound.play()
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        win_sound.play()
        return "Player wins!"
    else:
        lose_sound.play()
        return "Computer wins!"
