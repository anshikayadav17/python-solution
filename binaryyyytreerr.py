class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)

inorder(root)
