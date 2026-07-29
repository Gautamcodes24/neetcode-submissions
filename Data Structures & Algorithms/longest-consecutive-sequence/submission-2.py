class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        long = 0
        for num in nums:
            # is it a good start
            if num - 1 not in hm:
                length = 0
                n = num
                while n in nums:
                    length += 1
                    n += 1
                long = max(long , length)
        return long
