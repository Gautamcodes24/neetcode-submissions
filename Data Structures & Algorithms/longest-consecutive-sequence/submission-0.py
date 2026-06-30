class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)
        max_cons = 0
        for num in setNum:
            # is it a good start ? n - 1 hai kya
            if num - 1 not in setNum:
                length = 1
                current = num
                while current + 1 in setNum:
                    length += 1
                    current += 1
                max_cons = max(max_cons, length)
        return max_cons
