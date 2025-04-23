import socket
import threading

def listen_for_result(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            if data:
                print("\n>>", data)
        except:
            print("Disconnected from server.")
            break

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected to server.")

threading.Thread(target=listen_for_result, args=(client,), daemon=True).start()

while True:
    move = input("Your move (rock/paper/scissors): ").strip().lower()
    if move not in ["rock", "paper", "scissors"]:
        print("Invalid move.")
        continue
    client.sendall(move.encode())
