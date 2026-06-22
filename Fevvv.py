class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, index, value):
        while index <= self.n:
            self.bit[index] += value
            index += index & -index

    def query(self, index):
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

tree = FenwickTree(5)

tree.update(1, 5)
tree.update(2, 3)
tree.update(5, 7)

print(tree.query(5))
