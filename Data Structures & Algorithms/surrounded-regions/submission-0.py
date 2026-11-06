class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS , COLS = len(board) , len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def capture(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for _r , _c in directions:
                capture(r + _r , c + _c)
        
        for row in range(ROWS):
            if board[row][0] == "O":
                capture(row,0)
            if board[row][COLS-1] == "O":
                capture(row,COLS-1)
        for col in range(COLS):
            if board[0][col] == "O":
                capture(0,col)
            if board[ROWS-1][col] == "O":
                capture(ROWS-1,col)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
                