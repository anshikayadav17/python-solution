activities = [
    (1,2),
    (3,4),
    (0,6),
    (5,7),
    (8,9)
]

activities.sort(key=lambda x: x[1])

last = 0

for start, end in activities:
    if start >= last:
        print(start, end)
        last = end
