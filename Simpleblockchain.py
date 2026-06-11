import hashlib

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = str(self.data) + self.prev_hash
        return hashlib.sha256(text.encode()).hexdigest()

genesis = Block("Genesis", "0")
block2 = Block("Transaction A", genesis.hash)

print(genesis.hash)
print(block2.hash)
