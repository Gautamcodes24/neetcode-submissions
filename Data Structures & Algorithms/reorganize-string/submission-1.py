from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = [(-1*count,char) for char , count in Counter(s).items()]
        heapq.heapify(maxHeap)
        res = ""
        while maxHeap:
            count , char = heapq.heappop(maxHeap)
            if len(res)>0 and res[-1] == char:
                if not maxHeap:
                    return ""
                count2 , char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap,(count2,char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap,(count,char))
        return res
                