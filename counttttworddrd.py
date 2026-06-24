sentence = "Python is powerful and Python is easy"

words = sentence.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
