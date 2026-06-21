class BloomFilter:
    def __init__(self, size):
        self.bits = [0] * size
        self.size = size

    def add(self, item):
        index = hash(item) % self.size
        self.bits[index] = 1

    def contains(self, item):
        return self.bits[hash(item) % self.size] == 1

bf = BloomFilter(100)

bf.add("python")

print(bf.contains("python"))
print(bf.contains("java"))
