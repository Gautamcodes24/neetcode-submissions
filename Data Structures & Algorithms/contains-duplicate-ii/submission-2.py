class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for indx , num in enumerate(nums):
            if num in seen and abs(seen[num] - indx) <= k:
                return True
            seen[num] = indx
        return False