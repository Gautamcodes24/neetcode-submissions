class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for ele in nums:
            if ele in seen:
                return True
            else:
                seen[ele] = 1
        return False