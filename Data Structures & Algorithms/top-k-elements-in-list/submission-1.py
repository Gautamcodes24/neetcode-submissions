from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        items = list(count.items())
        items.sort(key = lambda x : x[1], reverse=True)
        ans = [item[0] for item in items[:k]]
        # ans = []
        # for key , value in count.items():
        #     if value >= k:
        #         ans.append(key)
        return ans