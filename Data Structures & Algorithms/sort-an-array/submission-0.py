class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # ------------working bruteforce approach------------
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    nums[j],nums[i] = nums[i],nums[j]
        return nums