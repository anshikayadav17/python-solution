import socket
import threading

nickname = input("Choose username: ")

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(("127.0.0.1", 5555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "NICK":
                client.send(nickname.encode())
            else:
                print(message)

        except:
            print("Disconnected")
            client.close()
            break

def write():
    while True:
        msg = input("")
        message = f"{nickname}: {msg}"

        client.send(message.encode())

receive_thread = threading.Thread(
    target=receive
)

receive_thread.start()

write_thread = threading.Thread(
    target=write
)

write_thread.start()
