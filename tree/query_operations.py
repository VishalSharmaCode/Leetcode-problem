class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

# find the size of tree
def treeSize(node):
    if node is None:
        return 0
    return 1+treeSize(node.left)+treeSize(node.right)

# Maximum depth of tree
def treeHeight(node):
    if node is None:
        return 0
    return  1+max(treeHeight(node.left), treeHeight(node.right))

# Count leaf
def leafCount(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return leafCount(node.left) + leafCount(node.right)

# Search for a target value
def search_value(node, target):
    if node is None:
        return False 
    if node.data == target:
        return True
    return search_value(node.left, target) or search_value(node.right, target)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(11)
root.left.left = Node(9)
root.left.left.left = Node(5)

print('Size of tree:',treeSize(root)) # 6
print('Depth Of tree:', treeHeight(root)) # 4
print('Leaf node of tree:', leafCount(root)) # 3
print('Search value:', search_value(root, 10)) # False
print('Search value:', search_value(root, 11)) # True 