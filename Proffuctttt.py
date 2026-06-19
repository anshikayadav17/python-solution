from queue import Queue
from threading import Thread

queue = Queue()

def producer():
    for i in range(10):
        queue.put(i)

def consumer():
    while True:
        item = queue.get()
        print(item)
        queue.task_done()

Thread(target=consumer, daemon=True).start()
producer()

queue.join()
