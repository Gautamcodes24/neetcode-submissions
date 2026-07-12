class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ln = len(prices)
        profit = 0
        for indx , num in enumerate(prices):
            nm = [num]
            r = indx + 1
            while r < ln and nm[-1] < prices[indx + 1]:
                nm.append(prices[r])
                r += 1
            if len(nm) > 1:
                profit += nm[-1] - nm[0]
        return profit