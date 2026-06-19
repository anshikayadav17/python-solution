import heapq

queue = []

heapq.heappush(queue, (2, "Medium"))
heapq.heappush(queue, (1, "High"))
heapq.heappush(queue, (3, "Low"))

while queue:
    print(heapq.heappop(queue))
