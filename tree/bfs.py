from collections import deque
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
    
def bfs_level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

def bfs_grouped_by_level(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level_node = []
        for _ in range(level_size):
            current = queue.popleft()
            current_level_node.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(current_level_node)
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)

print("BFS traversal:", bfs_level_order(root))
# Output[1,2,3,4,5,6]

print("BFS Group traversal:", bfs_grouped_by_level(root))
# Output[[1], [2, 3], [4, 5, 6]]