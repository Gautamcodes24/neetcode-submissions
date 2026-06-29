from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        hm_sorted = sorted(hm.items() , key=lambda x:x[1],reverse=True)
        print(hm_sorted)
        return [item[0] for item in hm_sorted[:k]]
        # return []
        