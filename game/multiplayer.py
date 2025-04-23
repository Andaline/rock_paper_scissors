# multiplayer.py

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

# For online multiplayer: future socket implementation