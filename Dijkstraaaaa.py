import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}

pq = [(0, 'A')]
dist = {'A': 0}

while pq:
    cost, node = heapq.heappop(pq)

    for nxt, weight in graph[node]:
        new_cost = cost + weight

        if nxt not in dist or new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(pq, (new_cost, nxt))

print(dist)
