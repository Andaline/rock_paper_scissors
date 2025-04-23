import socket
import threading

HOST = '0.0.0.0'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
print("Server started on port 5555. Waiting for players...")

clients = []
moves = {}

def determine_winner(p1, p2):
    if p1 == p2:
        return "It's a tie!"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def handle_client(conn, player_id):
    conn.sendall(f"You are Player {player_id + 1}".encode())
    while True:
        try:
            move = conn.recv(1024).decode()
            if not move:
                break
            moves[player_id] = move
            if len(moves) == 2:
                result = determine_winner(moves[0], moves[1])
                for c in clients:
                    c.sendall(f"Player 1 chose {moves[0]}, Player 2 chose {moves[1]}\n{result}".encode())
                moves.clear()
        except:
            break
    conn.close()

while len(clients) < 2:
    conn, addr = server.accept()
    print(f"Player {len(clients) + 1} connected from {addr}")
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, len(clients) - 1)).start()

# After both players connect:
if len(clients) == 2:
    for c in clients:
        c.sendall("Both players connected. You can now play!".encode())
clients.append(conn)

