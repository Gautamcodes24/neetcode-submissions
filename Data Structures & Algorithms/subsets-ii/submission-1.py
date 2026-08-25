class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, arr):
            if i == len(nums):
                res.append(arr.copy())
                return

            # All subsets that INCLUDE nums[i]
            arr.append(nums[i])
            dfs(i + 1, arr)
            arr.pop()

            # All subsets that EXCLUDE nums[i]
            # Skip consecutive identical elements to avoid duplicate branches
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1, arr)

        dfs(0, [])
        return res