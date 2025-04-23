# server.py
import socket
import threading

HOST = '0.0.0.0'
PORT = 5555

def handle_client(conn, addr, player_id, player_choices):
    print(f"Player {player_id} connected from {addr}")
    conn.sendall(f"Welcome Player {player_id}!\n".encode())
    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if data:
                player_choices[player_id] = data
                print(f"Player {player_id} chose: {data}")
            if all(player_choices):
                result = evaluate_round(player_choices)
                for i, sock in enumerate(player_sockets):
                    sock.sendall(result.encode())
                player_choices[0], player_choices[1] = None, None
        except:
            print(f"Player {player_id} disconnected.")
            break
    conn.close()

def evaluate_round(choices):
    a, b = choices[0], choices[1]
    if a == b:
        return "It's a tie!"
    elif (a == "rock" and b == "scissors") or (a == "scissors" and b == "paper") or (a == "paper" and b == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Set up server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
print(f"Server listening on {HOST}:{PORT}...")

player_choices = [None, None]
player_sockets = []

for player_id in range(2):
    conn, addr = server.accept()
    player_sockets.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr, player_id, player_choices))
    thread.start()
