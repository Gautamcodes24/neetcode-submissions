class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(indx , running):
            if indx == len(nums):
                return running
            return backtrack(indx+1 , running ^ nums[indx]) + backtrack(indx + 1, running)
        return backtrack(0,0)