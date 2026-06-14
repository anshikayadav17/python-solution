from threading import Lock, Thread

lock = Lock()

counter = 0

def increment():
    global counter

    for _ in range(100000):
        with lock:
            counter += 1

threads = [
    Thread(target=increment)
    for _ in range(4)
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(counter)
