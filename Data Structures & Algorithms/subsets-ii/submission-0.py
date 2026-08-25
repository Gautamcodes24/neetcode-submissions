class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(i , arr):
            if i == len(nums):
                res.add(tuple(arr.copy()))
                return
            arr.append(nums[i])
            dfs(i+1 , arr)
            arr.pop()
            dfs(i+1 , arr)
        nums.sort()
        dfs(0,[])
        return [arr for arr in res]

        