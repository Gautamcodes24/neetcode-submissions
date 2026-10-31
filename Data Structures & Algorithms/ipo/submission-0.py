class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [(c,p) for c , p in zip(capital,profits)]
        heapq.heapify(minHeap)
        maxHeap = []
        for i in range(k):
            while minHeap and w >= minHeap[0][0]:
                heapq.heappush(maxHeap,-heapq.heappop(minHeap)[1])

            if not maxHeap:
                break
            w += -heapq.heappop(maxHeap)
        return w