from collections import deque

queue = deque(["1"])

for _ in range(10):
    value = queue.popleft()

    print(value)

    queue.append(value + "0")
    queue.append(value + "1")
