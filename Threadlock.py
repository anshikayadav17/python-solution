from threading import Lock

lock = Lock()

with lock:
    print("Critical Section")
