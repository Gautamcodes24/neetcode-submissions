class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = 0
        sell = 1
        while sell < len(prices):
            p = prices[sell] - prices[minp]
            maxp = max(maxp , p)
            if prices[sell] < prices[minp]:
                minp = sell
            sell += 1
        return maxp
        