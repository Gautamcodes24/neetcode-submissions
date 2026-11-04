class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS , COLS = len(grid) , len(grid[0])
        visit = set()
        q = deque()
        def addVisit(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = dist
                addVisit(r,c+1)
                addVisit(r+1,c)
                addVisit(r,c-1)
                addVisit(r-1,c)
            dist += 1
        