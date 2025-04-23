# client.py
import socket
import threading

HOST = '127.0.0.1'  # Use the server's IP if remote
PORT = 5555

def listen_for_result():
    while True:
        try:
            result = client.recv(1024).decode()
            if result:
                print("\nResult: ", result)
        except:
            print("Connection lost.")
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(client.recv(1024).decode())  # Welcome message

threading.Thread(target=listen_for_result, daemon=True).start()

while True:
    move = input("Enter your move (rock/paper/scissors): ").strip().lower()
    if move not in ["rock", "paper", "scissors"]:
        print("Invalid move. Try again.")
        continue
    client.sendall(move.encode())