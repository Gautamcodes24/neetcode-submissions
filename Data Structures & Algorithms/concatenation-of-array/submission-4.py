class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums
        nums.extend(nums)
        return nums
        