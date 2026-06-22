class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # seen = {}
        # for indx , num in enumerate(nums):
        #     if num in seen and abs(seen[num] - indx) <= k:
        #         return True
        #     seen[num] = indx
        # return False
        if len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+1+k]: # [2,3,1]
                return True
        return False