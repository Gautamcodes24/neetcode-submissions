class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            fisrt = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if fisrt < second:
                heapq.heappush(stones,fisrt-second)
        stones.append(0)
        return abs(stones[0])