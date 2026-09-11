class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node initialized with height 1

class AVLTree:
    # Get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get the Balance Factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # 1. Right Rotation (Fixes LL Case)
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Rotate
        y.right = z
        z.left = T3

        # Update Heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # 2. Left Rotation (Fixes RR Case)
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Rotate
        y.left = z
        z.right = T2

        # Update Heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Core Insertion Function
    def insert(self, root, key):
        # Step 1: Standard BST Insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are ignored

        # Step 2: Update height of ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Check Balance Factor
        balance = self.get_balance(root)

        # Step 4: Rebalance if needed

        # Case A: Left-Left (LL)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Case B: Right-Right (RR)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Case C: Left-Right (LR)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case D: Right-Left (RL)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def delete(self, root, key):
        # 1. Standard BST Deletion
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with 1 or 0 children
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with 2 children: get inorder successor
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            # Delete the inorder successor
            root.right = self.delete(root.right, temp.key)

        # If the tree had only one node, return
        if root is None:
            return root

        # 2. Update height of current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get Balance Factor
        balance = self.get_balance(root)

        # 4. Handle Rebalancing Cases

        # Left Left (LL) Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right (LR) Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right (RR) Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left (RL) Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Visualization helper: Preorder Traversal
    def preorder(self, root):
        if root:
            print(f"{root.key}(h:{root.height})", end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


# --- Test Execution ---
tree = AVLTree()
root = None
sequence = [10, 20, 30, 40, 50, 25]

for num in sequence:
    root = tree.insert(root, num)

print("Preorder Traversal of constructed AVL Tree (Root -> Left -> Right):")
tree.preorder(root)
# Output: 30(h:3) 20(h:2) 10(h:1) 25(h:1) 40(h:2) 50(h:1)

tree.delete(root, 30)
print(' ')
print("After delete: ")
tree.preorder(root)