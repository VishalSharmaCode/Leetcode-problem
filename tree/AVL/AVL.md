# Comprehensive Guide to AVL Trees

## 1. Introduction

An **AVL Tree** (named after inventors **A**lderson-**V**elsky and **L**andis) is a **self-balancing Binary Search Tree (BST)**. It enforces a strict balance condition to ensure that the height of the tree remains logarithmic, avoiding the worst-case $\mathcal{O}(n)$ time complexity of standard BSTs.

### Balance Factor Property
For every node $N$ in an AVL tree, the **Balance Factor (BF)** must be strictly within the set $\{-1, 0, 1\}$:

$$\text{BalanceFactor}(N) = \text{height}(\text{Left Subtree}) - \text{height}(\text{Right Subtree})$$

* **$	ext{BF} = 0$:** Left and right subtrees have equal height.
* **$	ext{BF} = 1$:** Left subtree is taller by 1.
* **$	ext{BF} = -1$:** Right subtree is taller by 1.
* **$|\text{BF}| > 1$:** The tree is **unbalanced** and requires structural rebalancing via **rotations**.

```
       (30) [BF = 0]
      /    \
  (20)      (40) [BF = -1]
 [BF = 0]     \
              (50) [BF = 0]
```

---

## 2. Operations & Time Complexity

Unlike a standard BST, an AVL tree guarantees $\mathcal{O}(\log n)$ worst-case time complexity across all major dynamic set operations due to automatic rebalancing.

| Operation | Average Complexity | Worst-Case Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(h)$ |
| **Insertion** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(h)$ |
| **Deletion** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(h)$ |
| **Traversal** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ |

---

## 3. Tree Rotations

Rotations are constant-time $\mathcal{O}(1)$ local transformations used to restore the balance factor without violating the Binary Search Tree ordering property.

### 3.1 Left Rotation (RR Case)
Used when a node is **right-heavy** ($	ext{BF} < -1$) and the right child is also right-heavy or balanced ($	ext{BF} \le 0$).

```
    A                     B
     \                  / \
      B     ======>     A   C
       \
        C
```

### 3.2 Right Rotation (LL Case)
Used when a node is **left-heavy** ($	ext{BF} > 1$) and the left child is also left-heavy or balanced ($	ext{BF} \ge 0$).

```
        C                 B
       /                 / \
      B     ======>     A   C
     /
    A
```

### 3.3 Left-Right Rotation (LR Case)
Used when a node is left-heavy ($	ext{BF} > 1$), but its left child is right-heavy ($	ext{BF} < 0$).
1. Perform a **Left Rotation** on the left child.
2. Perform a **Right Rotation** on the node itself.

```
      C               C               B
     /               /               / \
    A   ======>     B   ======>     A   C
     \             /
      B           A
```

### 3.4 Right-Left Rotation (RL Case)
Used when a node is right-heavy ($	ext{BF} < -1$), but its right child is left-heavy ($	ext{BF} > 0$).
1. Perform a **Right Rotation** on the right child.
2. Perform a **Left Rotation** on the node itself.

```
    A               A                 B
     \               \               / \
      C   ======>     B   ======>     A   C
     /                 \
    B                   C
```

---

## 4. Python Implementation

```python
class AVLNode:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node: AVLNode) -> int:
        return node.height if node else 0

    def get_balance(self, node: AVLNode) -> int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, z: AVLNode) -> AVLNode:
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z: AVLNode) -> AVLNode:
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root: AVLNode, key: int) -> AVLNode:
        # 1. Perform standard BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed

        # 2. Update height of ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get balance factor
        balance = self.get_balance(root)

        # 4. If node becomes unbalanced, handle 4 cases:

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root: AVLNode) -> AVLNode:
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def delete(self, root: AVLNode, key: int) -> AVLNode:
        # 1. Standard BST deletion
        if not root:
            return root

        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get balance factor
        balance = self.get_balance(root)

        # 4. Handle unbalancing cases:

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root: AVLNode) -> list[int]:
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.val)
            result.extend(self.inorder(root.right))
        return result


# Example Usage
if __name__ == "__main__":
    tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        root = tree.insert(root, key)

    print("In-order traversal of constructed AVL tree:", tree.inorder(root))
    print("Root node value:", root.val)  # Should be 30 due to rebalancing

    root = tree.delete(root, 30)
    print("In-order traversal after deleting 30:", tree.inorder(root))
    print("New Root node value:", root.val)
```

---

## 5. Comparison: AVL Tree vs. Red-Black Tree

| Feature | AVL Tree | Red-Black Tree |
| :--- | :--- | :--- |
| **Strictness of Balance** | Very strict (height difference $\le 1$). | Flexible (longest path $\le 2 \times$ shortest path). |
| **Lookup Speed** | Faster (shorter height due to strict balance). | Slightly slower (potentially taller height). |
| **Insertion / Deletion** | Slower (requires more rotations to rebalance). | Faster (fewer rotations on average). |
| **Use Cases** | Read-heavy workloads (e.g., databases, lookup tables). | Write-heavy or frequent modification workloads. |