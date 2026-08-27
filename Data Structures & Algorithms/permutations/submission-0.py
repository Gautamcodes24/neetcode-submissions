class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(hm,arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for i in range(len(nums)):
                if not hm[i]:
                    hm[i] = True
                    arr.append(nums[i])
                    dfs(hm,arr)
                    hm[i] = False
                    arr.pop()
        dfs([False]*len(nums),[])
        return res
        
        