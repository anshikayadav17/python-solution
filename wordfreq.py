from collections import Counter
import heapq

words = [
    "python",
    "java",
    "python",
    "c",
    "python",
    "java"
]

counter = Counter(words)

print(
    heapq.nlargest(
        2,
        counter.items(),
        key=lambda x: x[1]
    )
)
