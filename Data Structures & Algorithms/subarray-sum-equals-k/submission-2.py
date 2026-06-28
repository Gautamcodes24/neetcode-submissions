class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count = 0
        currentSum = 0
        for num in nums:
            currentSum += num
            need = currentSum - k
            if need in seen:
                count += seen[need]
            seen[currentSum] = seen.get(currentSum,0)+1
        return count 

        