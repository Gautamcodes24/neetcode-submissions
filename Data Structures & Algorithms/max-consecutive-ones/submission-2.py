class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        maxc = 0
        for i in nums:
            if i == 1:
                temp += 1
                maxc = max(maxc, temp)
            else:
                temp = 0
        return maxc
