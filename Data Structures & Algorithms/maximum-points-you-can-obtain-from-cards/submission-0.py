class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_pts = sum(cardPoints)
        n = len(cardPoints)
        l = 0
        pre = []
        sumOfCurrentWindow = 0
        for r in range(n):
            if r - l + 1 > n - k:
                pre.append(sumOfCurrentWindow)
                sumOfCurrentWindow -= cardPoints[l]
                l += 1
            sumOfCurrentWindow += cardPoints[r]
        pre.append(sumOfCurrentWindow)
        return total_pts - min(pre)