class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            area = 1
            visited.add((r,c))
            for nr , nc in direction:
                newr = r + nr
                newc = c + nc
                if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and (newr, newc) not in visited and grid[newr][newc] == 1:
                    area += dfs(newr,newc)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not (i,j) in visited and grid[i][j] == 1:
                    max_area = max(max_area , dfs(i,j))
        return max_area                            