from queue import Queue
from threading import Thread
import time

q = Queue()

def producer():
    for i in range(5):
        q.put(i)
        print("Produced", i)

def consumer():
    while True:
        item = q.get()
        print("Consumed", item)
        q.task_done()

Thread(target=producer).start()
Thread(target=consumer, daemon=True).start()

time.sleep(2)
