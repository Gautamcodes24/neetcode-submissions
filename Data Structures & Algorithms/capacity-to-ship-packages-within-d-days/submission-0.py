class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isFeasible(cap):
            day = 1
            ship_cap = 0
            for w in weights:
                if ship_cap + w > cap:
                    day += 1
                    ship_cap = 0
                ship_cap += w
            return day <= days
        lower = max(weights)
        upper = sum(weights)
        while lower < upper:
            mid = lower + (upper - lower) // 2
            if isFeasible(mid):
                upper = mid
            else:
                lower = mid + 1
        return lower