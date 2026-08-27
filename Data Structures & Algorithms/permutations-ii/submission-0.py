class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(pick , arr):
            if len(arr) == len(nums):
                if arr not in res:
                    res.append(arr.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    arr.append(nums[i])
                    pick[i] = True
                    dfs(pick , arr)
                    arr.pop()
                    pick[i] = False
        dfs([False] * len(nums) , [])
        return res