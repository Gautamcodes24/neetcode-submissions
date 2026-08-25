class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(i , arr):
            if i > n:
                if len(arr) == k:
                    ans.append(arr.copy())
                return
            arr.append(i)
            dfs(i+1 , arr)
            arr.pop()
            dfs(i+1 , arr)
        dfs(1,[])
        return ans


        