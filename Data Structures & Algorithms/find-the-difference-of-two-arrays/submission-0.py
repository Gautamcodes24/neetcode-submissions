class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1)
        num2 = set(nums2)
        return [list(num1 - num2),list(num2 - num1)]