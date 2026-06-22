class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        freq = len(nums) // 3
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0) + 1
        for key , val in seen.items():
            if val > freq:
                ans.append(key) 
        return ans
        