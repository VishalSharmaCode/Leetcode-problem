class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# The Recursive Blueprint
   
# 1. Preorder: root > left > right
def dfs_preorder(node):
    if node is None:
        return 
    print(node.data, end = " ")
    
    dfs_preorder(node.left)
    
    dfs_preorder(node.right)
    
# 2. Inorder: left > root > right
def dfs_inorder(node):
    if node is None:
        return 
    dfs_inorder(node.left)
    print(node.data, end=" ")
    dfs_inorder(node.right)

# 3. Postorder: Left > Right > Root
def dfs_postorder(node):
    if node is None:
        return 
    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.data, end = " ")
    
    
def dfs_preorder_iterartive(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.data)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result
    
    
tree = Node(10)
tree.left = Node(20)
tree.right = Node(30)
tree.left.left = Node(40)
tree.right.left = Node(9)

print('Recursive Blueprint')
print()
print('------Inorder-------')
dfs_inorder(tree)  
print() 

print('-------Postorder--------')
dfs_postorder(tree)
print()

print('--------Preorder---------')
dfs_preorder(tree)
print()
print()

print('Iterative Blueprint')
dfs = dfs_preorder_iterartive(tree)
print(dfs)