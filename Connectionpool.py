from queue import Queue

pool = Queue(maxsize=3)

for i in range(3):
    pool.put(f"Connection-{i}")

conn = pool.get()

print(conn)

pool.put(conn)
