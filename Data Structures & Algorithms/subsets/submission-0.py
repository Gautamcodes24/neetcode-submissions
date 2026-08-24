class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            sub_set = [curr + [num] for curr in subsets]
            subsets.extend(sub_set)
        return subsets
        