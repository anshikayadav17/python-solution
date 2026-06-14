class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)

ds = DSU(5)

ds.union(0, 1)
ds.union(1, 2)

print(ds.find(2))
