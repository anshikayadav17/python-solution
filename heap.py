import heapq

arr = [9, 4, 7, 1, 3, 6]

heapq.heapify(arr)

sorted_arr = []

while arr:
    sorted_arr.append(heapq.heappop(arr))

print(sorted_arr)
