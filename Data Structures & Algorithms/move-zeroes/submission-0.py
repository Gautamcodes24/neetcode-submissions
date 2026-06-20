class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for indx in range(len(nums)):
            if nums[indx] != 0:
                nums[i] , nums[j] = nums[indx] , nums[i]
                i += 1
                j += 1
            else:
                j+=1
        return nums


        