class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        l = 0
        for r in range(k-1,len(nums)):
            win_size = r - l + 1
            if win_size > k:
                l += 1
            ans.append(max(nums[l:r+1]))
        return ans