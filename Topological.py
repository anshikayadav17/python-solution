from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

indegree = {i: 0 for i in graph}

for node in graph:
    for nxt in graph[node]:
        indegree[nxt] += 1

queue = deque(
    [node for node in indegree if indegree[node] == 0]
)

order = []

while queue:
    node = queue.popleft()
    order.append(node)

    for nxt in graph[node]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            queue.append(nxt)

print(order)
