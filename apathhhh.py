import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2)],
    "C": [("D", 1)],
    "D": []
}

def astar(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            return cost

        if node in visited:
            continue

        visited.add(node)

        for nxt, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, nxt))

print(astar("A", "D"))
