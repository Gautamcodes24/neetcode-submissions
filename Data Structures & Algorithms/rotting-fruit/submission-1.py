from collections import deque
class Solution:
    def __init__(self):
        self.directions = [[0,1],[1,0],[-1,0],[0,-1]]
    def is_valid(self,i,j,n,m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time = 0
        count = 0
        total = 0
        q = deque()
        n , m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    q.append((i,j))
                    count += 1
        # bfs
        while q:
            q_len = len(q)
            for _ in range(q_len):
                row , col = q.popleft()
                for nr,nc in self.directions:
                    nRow = row + nr
                    nCol = col + nc
                    if self.is_valid(nRow,nCol,n,m) and grid[nRow][nCol] == 1:
                        grid[nRow][nCol] = 2
                        q.append((nRow,nCol))
                        count += 1
            if q:
                time += 1
        if total == count:
            return time
        return -1