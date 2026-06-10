import socket

server = socket.socket()
server.bind(("localhost", 9999))
server.listen()

print("Waiting...")

client, addr = server.accept()

print("Connected:", addr)

client.send(
    b"Welcome Client"
)
