class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        ans = []
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left + 1, right + 1]
            elif sums > target:
                right -= 1
            else:
                left += 1
        return ans 