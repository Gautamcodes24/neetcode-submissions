class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for indx , num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num],indx]
            seen[num] = indx
        return []
