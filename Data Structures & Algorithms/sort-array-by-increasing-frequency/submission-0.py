from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        # Sahi Order: Pehle sorting check karo, fir us number ko uski frequency jitni baar repeat karo
        # return [num for num, f in sorted(freq.items(), key=lambda x: x[1]) for _ in range(f)]
        return sorted(nums, key=lambda x: (freq[x], -x))