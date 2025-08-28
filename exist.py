class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, idx):
            if idx == len(word):   # Word fully matched
                return True
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[idx]):  # Out of bounds or mismatch
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 directions
            found = (backtrack(r + 1, c, idx + 1) or
                     backtrack(r - 1, c, idx + 1) or
                     backtrack(r, c + 1, idx + 1) or
                     backtrack(r, c - 1, idx + 1))

            # Restore cell after exploration
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False