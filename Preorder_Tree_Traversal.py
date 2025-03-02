# Preorder Tree Traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

if __name__ == "__main__":
    root = None
    values = list(map(int, input("Enter values to insert into the tree (space-separated): ").split()))
    
    for value in values:
        root = insert(root, value)
    
    print("Preorder Traversal of the tree:")
    preorder_traversal(root)
