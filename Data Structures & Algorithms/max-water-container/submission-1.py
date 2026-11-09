class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_sum = 0
        while left < right:
            area = min(heights[left],heights[right]) * (right - left)
            max_sum = max(max_sum,area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_sum

        