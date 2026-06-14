class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

s = Stack()

s.push(10)
s.push(20)

print(s.pop())
