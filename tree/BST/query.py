class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        elif key < root.val:
            root.left = self.insert(root.left,key)
        return root
    def find_min(self, root):
        if root is None:
            return None
        while root.left:
            root = root.left
        return root.val
    
    def find_max(self, root):
        if root is None:
            return None
        while root.right:
            root = root.right
        return root.val
    
    def is_valid(self, root, min_val = float('-inf'), max_val = float('inf')):
        if root is None:
            return True
        if not(min_val < root.val<max_val):
            return False
        return (self.is_valid(root.left, min_val, root.val) and self.is_valid(root.right, root.val,max_val))
    
tree = BST()
arr = [5,3,7,2,7,6,5,89,3]
for i in arr:
    tree.root = tree.insert(tree.root, i)

x = tree.is_valid(tree.root)
print(x)