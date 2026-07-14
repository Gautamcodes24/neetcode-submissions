class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            correct_indx = nums[i] - 1
            if nums[i] != nums[correct_indx]:
                nums[i] , nums[correct_indx] = nums[correct_indx] , nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
        return -1
