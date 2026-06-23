class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if not self.front:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if not self.front:
            return None

        value = self.front.value
        self.front = self.front.next

        return value

q = Queue()

q.enqueue(10)
q.enqueue(20)

print(q.dequeue())
