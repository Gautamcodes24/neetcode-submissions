class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                hm[stack.pop()] = num
            stack.append(num)
        while stack:
            hm[stack.pop()] = -1
        return [hm[num] for num in nums1]