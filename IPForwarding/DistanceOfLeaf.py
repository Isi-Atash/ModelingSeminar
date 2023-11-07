def preorder(node, distance):
    if node is None:
        return 0
    if node.isLeaf() and distance == 9:
        return 1
    count = 0
    for child in node.children:
        count += preOrder(child, distance + 1)
    return count

# Usage:
root = ... # Initialize the tree
leaf_count = preorder(root, 0) # Start with distance 0 from the root
print(f"Number of leaves at distance 9: {leaf_count}")
