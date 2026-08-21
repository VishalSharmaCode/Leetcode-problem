from collections import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(node):
            if node is None:
                return [None]
            return [
                node.val,
                *preorder(node.left),
                *preorder(node.right)
            ]
        return preorder(p) == preorder(q)