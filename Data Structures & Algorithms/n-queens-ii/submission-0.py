class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [["."] * n for _ in range(n)]
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return 
            for c in range(n):
                if self.isSafe(r,c,board):
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."
        backtrack(0)
        return res
    def isSafe(self,r,c,board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        row , col = r - 1 , c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        row , col = r - 1 , c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        return True