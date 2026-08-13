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
    def __get_min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp =  self.__get_min_value(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right,temp.data)
        return root
    
tree = BST()
arr = [10,20,17,26,67]
for i in arr:
    tree.root = tree.insert(tree.root,10)
    
tree.delete_node(tree.root, 20)


        