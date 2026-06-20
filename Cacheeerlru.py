class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            oldest = next(iter(self.cache))
            del self.cache[oldest]

    def get(self, key):
        if key not in self.cache:
            return None

        value = self.cache.pop(key)
        self.cache[key] = value

        return value

l = LRU(2)

l.put(1, 100)
l.put(2, 200)

print(l.get(1))
