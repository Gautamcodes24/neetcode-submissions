class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = set(nums)
        lng = 0
        for indx ,num in enumerate(nums):
            # is it a good start
            if num - 1 not in hm:
                l = 1
                curr = num
                while curr + 1 in hm:
                    l += 1
                    curr += 1
                lng = max(lng , l)
        return lng