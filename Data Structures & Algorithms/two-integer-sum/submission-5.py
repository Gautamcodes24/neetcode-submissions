from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two distinct indices where nums[i] + nums[j] = target.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices or empty list if no solution exists
        """
        if not nums or len(nums) < 2:
            return []
        
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        
        return []