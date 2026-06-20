class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        k = len(nums) - 1
        while left <= right:
            l_square = nums[left] * nums[left]
            r_square = nums[right] * nums[right]
            if l_square > r_square:
                ans[k] = l_square
                left += 1
            else:
                ans[k] = r_square
                right -= 1
            k -= 1
        return ans