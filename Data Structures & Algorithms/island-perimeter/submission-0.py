from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        rows , cols = len(grid) , len(grid[0])
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(r,c):
            peri = 0
            q = deque()
            q.append((r,c))
            visit.add((r, c))
            while q:
                curr_r, curr_c = q.popleft()
                for dr , dc in direction:
                    nr = curr_r + dr
                    nc = curr_c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        peri += 1
                    elif (nr , nc) not in visit:
                        visit.add((nr , nc))
                        q.append((nr , nc))
            return peri
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i,j)
        return 0