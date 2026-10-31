class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        minheap = []
        currPass = 0
        for t in trips:
            pas , st , en = t
            while minheap and minheap[0][0] <= st:
                currPass -= heapq.heappop(minheap)[1]
            currPass += pas
            if currPass > capacity:
                return False
            heapq.heappush(minheap,[en,pas])
        return True
