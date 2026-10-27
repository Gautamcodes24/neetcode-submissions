class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []
        for x , y in points:
            dis = x * x + y * y
            heapq.heappush(pq,(-dis,x,y))
            while len(pq) > k:
                heapq.heappop(pq)
        return [p[1:] for p in pq]
        