class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # part 1 -- Init 
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        island = 0
        ROWS , COLS = len(grid) , len(grid[0])
        # dfs 
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            # visit all four direction
            for dr , dc in direction:
                dfs(r+dr , c+dc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r,c)
        return island

        