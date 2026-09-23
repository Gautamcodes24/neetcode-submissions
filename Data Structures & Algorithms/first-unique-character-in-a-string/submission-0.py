from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for indx, c in enumerate(s):
            if freq.get(c) == 1:
                return indx
        return -1
        