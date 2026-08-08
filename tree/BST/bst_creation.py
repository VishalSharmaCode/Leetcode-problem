class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    def _insert_recursive (self, current, key):
        if key < current.data:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.data:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)
    def second_way_insertion(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.second_way_insertion(root.left, key)
        elif key > root.data:
            root.right = self.second_way_insertion(root.right,key)
        return root
    
    def search(self, root, target):
        if root is None or root.data ==target:
            return root
        if target < root.data:
            return self.search(root.left, target)
        return self.search(root.right, target)
    
tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(11)
tree.insert(15)
tree.insert(13)

print(tree.search(tree.root, 11))
                