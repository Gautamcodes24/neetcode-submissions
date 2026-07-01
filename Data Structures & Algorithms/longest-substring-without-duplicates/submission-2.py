class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        start = 0
        max_count = 0
        for indx in range(len(s)):
            ch = s[indx]
            while ch in hs:
                hs.remove(s[start])
                start += 1
            hs.add(ch)
            max_count = max(max_count , indx - start + 1)
        return max_count




