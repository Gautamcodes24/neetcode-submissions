from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while q or maxHeap:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                rem = 1 + heapq.heappop(maxHeap)
                if rem:
                    q.append((rem,time+n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
        