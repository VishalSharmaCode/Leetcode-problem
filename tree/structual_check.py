from collections import deque
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
    
# Check if full binary tree(is_full)
def is_full_binary(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left is not None and node.right is not None:
        return is_full_binary(node.left) and is_full_binary(node.right)
    return False

# Check perfect Binary tree
def perfect_tree(node):
    def _find_leftmost_depth(node):
        depth = 0
        while node:
            depth +=1
            node = node.left
        return depth
    def _is_perfect_recursive(node, target_depth, current_level=1):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return current_level == target_depth
        if node.left is None or node.right is None:
            return False
        return (_is_perfect_recursive(node.left,target_depth, current_level+1) and _is_perfect_recursive(node.right, target_depth, current_level+1))
    def is_perfect_binary(root):
        target_depth = _find_leftmost_depth(root)
        return _is_perfect_recursive(root, target_depth)
    return is_perfect_binary(node)
# Blanced Binary tree
def blanaced_tree(node):
    def _check_height_balance(node):
        if node is None:
            return 0
        left_height =_check_height_balance(node.left)
        if left_height == -1:
            return -1
        right_height = _check_height_balance(node.right)
        if right_height == -1:
            return -1
        if abs(left_height-right_height)> 1:
            return -1
        return 1+max(left_height, right_height)
    def is_blanced_binary_tree(root):
        return _check_height_balance(node) != -1
    return is_blanced_binary_tree(node)

# Complete Binary tree
def is_complete_binary_tree(root):
    if not root:
        return True
    queue = deque([root])
    seen_null_flag = False
    while queue:
        current = queue.popleft()
        if current is None:
            seen_null_flag = True
        else:
            if seen_null_flag:
                return False
            queue.append(current.left)
            queue.append(current.right)
    return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left =Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
print('Full binnary tree:', is_full_binary(root)) # False
print('Perfect binary tree:',perfect_tree(root)) # False
print('Blanced tree:', blanaced_tree(root)) # False
print('Complete binary tree:', is_complete_binary_tree(root)) # False