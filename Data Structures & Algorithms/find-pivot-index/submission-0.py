class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        for i , num in enumerate(nums):
            if lsum == total - lsum - num:
                return i
            lsum += num
        return -1