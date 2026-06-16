class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        
class GeneralTree:
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    def insert_direct(self, parent_node, child_node):
        new_node = Node(child_node)
        parent_node.children.append(new_node)
        return new_node