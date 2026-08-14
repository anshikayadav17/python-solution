sentence = input("Enter sentence: ")

words = sentence.split()

print("Words:", len(words))

frequency = {}

for word in words:
    frequency[word] = frequency.get(word,0)+1

print(frequency)
