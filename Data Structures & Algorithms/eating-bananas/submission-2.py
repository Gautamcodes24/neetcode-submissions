class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isFeasible(speed):
            return sum(math.ceil(p / speed) for p in piles) <= h
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isFeasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo