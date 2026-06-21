class HashTable:

    def __init__(self):
        self.table = [[] for _ in range(10)]

    def insert(self, key, value):
        index = hash(key) % 10
        self.table[index].append((key, value))

    def search(self, key):
        index = hash(key) % 10

        for k, v in self.table[index]:
            if k == key:
                return v

ht = HashTable()

ht.insert("python", 100)

print(ht.search("python"))
