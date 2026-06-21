class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0

    return 1 + max(
        height(node.left),
        height(node.right)
    )

root = Node(10)
root.left = Node(5)
root.right = Node(20)

print(height(root))
