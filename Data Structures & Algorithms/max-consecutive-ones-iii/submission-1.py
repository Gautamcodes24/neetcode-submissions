class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        one_len = 0
        l = 0
        for r in range(len(nums)):
            num = nums[r]
            if num == 1:
                one_len += 1
            while (r - l + 1) - one_len > k:
                if nums[l] == 1:
                    one_len -= 1
                l += 1
            max_len = max(max_len , r - l + 1)
        return max_len
        