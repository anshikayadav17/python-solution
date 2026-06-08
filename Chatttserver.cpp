import socket

server = socket.socket()
server.bind(("localhost", 9999))
server.listen()

print("Waiting for connection...")

client, addr = server.accept()
print("Connected:", addr)

while True:
    msg = client.recv(1024).decode()
    print("Client:", msg)
