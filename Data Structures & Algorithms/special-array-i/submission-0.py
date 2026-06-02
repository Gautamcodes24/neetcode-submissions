class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        
        for indx in range(0 , len(nums)-1):
            if nums[indx] % 2 == nums[indx + 1] % 2:
                return False
                
        return True
        