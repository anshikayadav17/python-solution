from queue import Queue
from threading import Thread

q = Queue()

def producer():
    for i in range(5):
        q.put(i)

def consumer():
    while True:
        item = q.get()
        print(item)
        q.task_done()

Thread(target=consumer, daemon=True).start()
producer()

q.join()
