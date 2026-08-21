# Comprehensive Guide to Binary Search Trees (BST)

## 1. Introduction

A **Binary Search Tree (BST)** is a node-based binary tree data structure that possesses the **Binary Search Property**:

* The **left subtree** of a node contains only nodes with keys **less than** the node's key.
* The **right subtree** of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.
* Duplicate keys are generally not allowed (or handled explicitly using frequency counters or right-subtree placement).

```
        (8)
       /   \
     (3)   (10)
     / \      \
   (1) (6)    (14)
       / \    /
     (4) (7)(13)
```

---

## 2. Fundamental Operations & Complexity

| Operation | Average Time Complexity | Worst Case Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | $\mathcal{O}(\log n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ |
| **Insertion** | $\mathcal{O}(\log n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ |
| **Deletion** | $\mathcal{O}(\log n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ |
| **Traversal** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ |

> **Note:** The worst-case complexity occurs when the BST becomes unbalanced (skewed tree), effectively degrading into a linked list. $h$ represents the height of the tree.

---

## 3. Core Algorithms

### 3.1 Search Operation
To search for a target value $k$:
1. Start at the root node.
2. If the node is `null` or matches $k$, return the node.
3. If $k < \text{node.val}$, recurse/iterate to the **left child**.
4. If $k > \text{node.val}$, recurse/iterate to the **right child**.

### 3.2 Insertion Operation
To insert a new value $k$:
1. Traverse the tree starting from the root to find the appropriate leaf position according to BST properties.
2. Insert a new node as a child of the leaf node.

### 3.3 Deletion Operation
Deleting a node $x$ involves three main scenarios:
1. **Node $x$ is a leaf (no children):** Simply remove $x$.
2. **Node $x$ has one child:** Replace $x$ with its child.
3. **Node $x$ has two children:**
   - Find $x$'s **Inorder Successor** (smallest key in the right subtree) or **Inorder Predecessor** (largest key in the left subtree).
   - Copy the value of the successor/predecessor to $x$.
   - Recursively delete the successor/predecessor node.

---

## 4. Tree Traversal Techniques

1. **In-Order (Left, Root, Right):** Visits nodes in non-decreasing sorted order.
2. **Pre-Order (Root, Left, Right):** Useful for creating a copy or clone of the tree.
3. **Post-Order (Left, Right, Root):** Useful for deleting the tree from bottom to top.
4. **Level-Order (Breadth-First):** Visits nodes level by level from left to right.

---

## 5. Python Implementation

```python
class TreeNode:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key: int) -> None:
        def _insert(node: TreeNode, key: int) -> TreeNode:
            if not node:
                return TreeNode(key)
            if key < node.val:
                node.left = _insert(node.left, key)
            elif key > node.val:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def search(self, key: int) -> bool:
        curr = self.root
        while curr:
            if curr.val == key:
                return True
            elif key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def delete(self, key: int) -> None:
        def _min_value_node(node: TreeNode) -> TreeNode:
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node: TreeNode, key: int) -> TreeNode:
            if not node:
                return node

            if key < node.val:
                node.left = _delete(node.left, key)
            elif key > node.val:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                temp = _min_value_node(node.right)
                node.val = temp.val
                node.right = _delete(node.right, temp.val)

            return node

        self.root = _delete(self.root, key)

    def inorder_traversal(self) -> list[int]:
        result = []
        def _inorder(node: TreeNode):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        _inorder(self.root)
        return result


if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    
    for el in elements:
        bst.insert(el)

    print("In-order Traversal (Sorted):", bst.inorder_traversal())
    print("Search 6:", bst.search(6))
    print("Search 15:", bst.search(15))

    bst.delete(3)
    print("In-order Traversal after deleting 3:", bst.inorder_traversal())
```

---

## 6. Self-Balancing Binary Search Trees

When data is inserted in sorted or nearly sorted order, standard BSTs degrade to $\mathcal{O}(n)$ time complexity. To guarantee $\mathcal{O}(\log n)$ operations, self-balancing BST variants maintain balanced tree height:

* **AVL Trees:** Strictly balanced trees where height difference between left and right subtrees (balance factor) is at most 1.
* **Red-Black Trees:** Flexibly balanced trees using node coloring (red/black) and specific structural rules; widely used in standard libraries (e.g., C++ `std::map`, Java `TreeMap`).
* **Splay Trees:** Dynamically adjusts to bring frequently accessed elements closer to the root.