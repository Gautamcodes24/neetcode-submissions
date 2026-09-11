from collections import deque
class Solution:
    def bfs(self, visit, grid, q):
        rows, cols = len(grid), len(grid[0])
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            ele = q.popleft()
            for dr, dc in direction:
                newRow = ele[0] + dr
                newCol = ele[1] + dc
                if (
                    newCol < 0
                    or newRow < 0
                    or newRow >= rows
                    or newCol >= cols
                    or grid[newRow][newCol] == 0
                    or visit[newRow][newCol]
                ):
                    continue
                visit[newRow][newCol] = True
                q.append((newRow,newCol))

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]
        q = deque()
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and grid[i][j] == 1:
                    visit[i][j] = True
                    q.append((i, j))
        self.bfs(visit, grid, q)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visit[i][j]:
                    count += 1
        return count
