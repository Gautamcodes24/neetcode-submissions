class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l = 0
        best = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0) + 1
            while hm[s[r]] > 1:
                hm[s[l]] -= 1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l += 1
            best = max(best , r - l + 1)
        return best
