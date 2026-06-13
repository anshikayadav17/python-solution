from collections import deque

graph = {
    1:[2,3],
    2:[4],
    3:[5],
    4:[],
    5:[]
}

queue = deque([1])
visited = {1}

while queue:
    node = queue.popleft()

    print(node)

    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)
