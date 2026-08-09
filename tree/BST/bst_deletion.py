class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left,key)
        elif key > root.data:
            root.right = self.insert(root.right,key)
        return root
    
    def delete(self, root, target):
        if root is None:
            return None
        if root.data == target:
            root = None
        