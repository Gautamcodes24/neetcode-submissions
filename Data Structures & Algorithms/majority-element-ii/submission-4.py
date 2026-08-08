from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [ele for ele , fre in freq.items() if fre > len(nums) // 3 ]