class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

current = head

while current:
    print(current.value)
    current = current.next
