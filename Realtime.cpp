from collections import Counter

with open("log.txt") as file:
    words = file.read().split()

top = Counter(words).most_common(10)

for word, count in top:
    print(word, count)
