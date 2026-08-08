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
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root
    
    def search_parent(self, root, target):
        if root is None:
            return None
        if root.data == target:
            return None
        if target < root.data:
            if root.left is not None and root.left.data == target:
                return root
            return self.search_parent(root.left, target)
        else:
            if root.right is not None and root.right.data == target:
                return root
            return self.search_parent(root.right, target)
        

tree = BST()
arr = [10,11,12,1,9,4,2,88]
for i in arr:
    tree.root = tree.insert(tree.root, i)
print(tree.search_parent(tree.root,4).data)