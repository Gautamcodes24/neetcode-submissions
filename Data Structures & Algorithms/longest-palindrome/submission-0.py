from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        length = 0
        has_odd = False
        for val in hm.values():
            if val & 1 == 0:
                length += val
            else:
                length += val - 1
                has_odd = True
        return length + 1 if has_odd else length
        