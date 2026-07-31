class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(threashold):
            curr_sum = 0
            part = 1
            for val in nums:
                if curr_sum + val > threashold:
                    part += 1
                    curr_sum = 0
                curr_sum += val
                if part > k:
                    return False
            return True
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = low + (high - low ) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        return low