class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, cols, diagonals, antiDiagonals, board):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if (col in cols or
                    (row - col) in diagonals or
                    (row + col) in antiDiagonals):
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                diagonals.add(row - col)
                antiDiagonals.add(row + col)

                backtrack(row + 1, cols, diagonals, antiDiagonals, board)

                # Backtrack
                board[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row - col)
                antiDiagonals.remove(row + col)
        
        res = []
        board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return res
