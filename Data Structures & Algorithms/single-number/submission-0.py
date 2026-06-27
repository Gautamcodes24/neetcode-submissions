class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            print(f'Doing xor for {ans} ^ {num} = {ans ^ num}')
            ans = ans ^ num
        return ans