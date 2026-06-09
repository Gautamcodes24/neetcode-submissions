class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        max_sum = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_sum = max(max_sum , area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_sum