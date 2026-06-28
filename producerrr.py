from threading import Semaphore,Thread

sem=Semaphore(0)

def producer():

    print("Produced")

    sem.release()

def consumer():

    sem.acquire()

    print("Consumed")

Thread(target=consumer).start()

Thread(target=producer).start()
