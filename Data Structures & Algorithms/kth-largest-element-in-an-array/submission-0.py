import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = []
        for i in range(k):
            heapq.heappush(pq,nums[i])
        
        for i in range(k,len(nums)):
            if pq[0] < nums[i]:
                heapq.heappop(pq)
                heapq.heappush(pq, nums[i])
        return pq[0]