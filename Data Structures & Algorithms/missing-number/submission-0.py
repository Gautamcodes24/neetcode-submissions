class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sol 1
        return ((len(nums) * (len(nums) + 1 )) // 2) - sum(nums)
        