class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # step 1 : l , r = 0 whlile sum >= target r++ , max if l == 0 else min 
        # step 2: while sum - l sum < target , l++ min 
        psum = 0
        count = float('inf')
        l = 0
        for r in range(len(nums)):
            psum += nums[r]

            while psum >= target:
                count = min(count , (r - l )+ 1)
                psum -= nums[l]
                l += 1
        # print(count)
        return count if count != float('inf') else 0

        