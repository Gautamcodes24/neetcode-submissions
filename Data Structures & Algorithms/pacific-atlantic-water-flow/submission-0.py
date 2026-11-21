class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS , COLS = len(heights) , len(heights[0])
        alt , pac = set(),set()
        def dfs(r,c,visit,preHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < preHeight):
                return
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,alt,heights[r][COLS-1])
          
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,alt,heights[ROWS-1][c])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in alt and (r,c) in pac:
                    res.append((r,c))
        return res
        