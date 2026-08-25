class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(indx , arr , total):
            if total == target:
                res.append(arr.copy())
                return
            if total > target or indx == len(nums):
                return
            arr.append(nums[indx])
            dfs(indx , arr , total + nums[indx])
            arr.pop()
            dfs(indx + 1, arr , total)
        dfs(0,[],0)
        return res
