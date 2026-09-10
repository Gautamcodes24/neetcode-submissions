class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS , COLS = len(image) , len(image[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        orig = image[sr][sc]
        if orig == color:
            return image
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or image[r][c] != orig:
                return
            image[r][c] = color
            for rdir , cdir in direction:
                dfs(r+rdir,c+cdir)
        dfs(sr,sc)
        return image
