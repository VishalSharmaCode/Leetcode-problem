from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store complete word at end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        # Build Trie
        for word in words:
            node = root
            for char in word:
                node = node.children.setdefault(char, TrieNode())
            node.word = word
        
        m, n = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            
            # If word found
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicates
            
            board[r][c] = "#"  # mark visited
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            
            board[r][c] = char  # restore
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return result