import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)

            nickname = nicknames[index]
            nicknames.remove(nickname)

            broadcast(f"{nickname} left the chat!".encode())

            client.close()
            break

def receive():
    while True:
        client, address = server.accept()

        print("Connected:", str(address))

        client.send("NICK".encode())

        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print("Nickname:", nickname)

        broadcast(f"{nickname} joined!".encode())

        client.send("Connected to server!".encode())

        thread = threading.Thread(
            target=handle,
            args=(client,)
        )

        thread.start()

print("Server Running...")
receive()
