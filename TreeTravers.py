class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(nodes):
    """
    Build a binary tree from a list of nodes assuming sequential left-right child assignment.
    """
    if not nodes:
        return None
    
    # Create tree nodes
    tree_nodes = [TreeNode(value) for value in nodes]
    root = tree_nodes[0]
    
    # Assign children based on sequential left-right assignment
    for i in range(len(tree_nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(tree_nodes):
            tree_nodes[i].left = tree_nodes[left_index]
        if right_index < len(tree_nodes):
            tree_nodes[i].right = tree_nodes[right_index]
    
    return root

def pre_order(node, result):
    if node:
        result.append(node.value)
        pre_order(node.left, result)
        pre_order(node.right, result)

def in_order(node, result):
    if node:
        in_order(node.left, result)
        result.append(node.value)
        in_order(node.right, result)

def post_order(node, result):
    if node:
        post_order(node.left, result)
        post_order(node.right, result)
        result.append(node.value)

# Input
input_data = "ABCDEF/1234567"
nodes = list(input_data.split("/")[0])  # Extract node list

# Build the tree
root = build_tree(nodes)

# Traverse the tree
pre_order_result = []
in_order_result = []
post_order_result = []

pre_order(root, pre_order_result)
in_order(root, in_order_result)
post_order(root, post_order_result)

# Display the results
print("Tree Traversal Results:")
print(f"Pre-Order Traversal: {' -> '.join(pre_order_result)}")
print(f"In-Order Traversal: {' -> '.join(in_order_result)}")
print(f"Post-Order Traversal: {' -> '.join(post_order_result)}")
