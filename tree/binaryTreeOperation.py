from collections import deque
class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    # Insertion
    def insert(self, data):
        new_node = Node(data)
        
        if not self.root:
            self.root = new_node
            return 
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)
    
    # Delete
    def _delete_deepest(self, deepest_node):
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current == deepest_node:
                self.root = None
                return
            if current.right:
                if current.right ==deepest_node:
                    current.right = None
                    return
                else:
                    queue.append(current.right)
            if current.left == deepest_node:
                current.left = None
                return
            else:
                queue.append(current.left)
    def delete_value(self, key):
        if not self.root:
            print('Tree is empty')
            return
        if not self.root.left and not self.root.right:
            if self.root.data ==key:
                self.root = None
                return True
            return False
        target = None
        current = None
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.data == key:
                target = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        if target:
            deepest_val = current.data
            self._delete_deepest(current)
            target.data = deepest_val
            return True
        print(f"Value '{key}' not found ")
        return False
    # Clone 
    def clone(self):
        cloned_tree = BinaryTree()
        cloned_tree.root = self._clone_recursive(self.root)
        return cloned_tree
    def _clone_recursive(self, current_node):
        if current_node is None:
            return None
        new_node = Node(current_node.data)
        new_node.left = self._clone_recursive(current_node.left)
        new_node.right = self._clone_recursive(current_node.right)
        return new_node
    
    # Delete Entire tree
    def clean_tree(self):
        self.clear_recursive(self.root)
        self.root = None
        
    def clear_recursive(self, current_node):
        if current_node is None:
            return 
        self.clean_recursive(current_node.left)
        self.clean_recursive(current_node.right)
        current_node.left = None
        current_node.right = None
        
    
# Display
def display_inorder(node):
    if node:
        display_inorder(node.left)
        print(node.data, end=" ")
        display_inorder(node.right)
            
tree = BinaryTree()
for val in [10, 20, 30, 40, 50]:
    tree.insert(val)

print("Original Tree (Inorder):")
display_inorder(tree.root)  # Output: 40 20 50 10 30 
print("\n" + "-"*30)

tree.delete_value(10)
print("After delete Tree (Inorder):")
display_inorder(tree.root)  # Output: 40 20 50 10 30 
print("\n" + "-"*30)


