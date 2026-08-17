class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        count = 0
        preSum = 0
        for num in nums:
            preSum += num
            need = preSum - k
            if need in hm:
                count += hm[need]
            hm[preSum] = hm.get(preSum,0) + 1
        return count

        