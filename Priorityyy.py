from queue import PriorityQueue

pq = PriorityQueue()

pq.put((3, "Low"))
pq.put((1, "High"))
pq.put((2, "Medium"))

while not pq.empty():
    print(pq.get())
