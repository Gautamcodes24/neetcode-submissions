from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        current = Counter() 
        l = 0          
        min_len = float('inf')
        result = ""
        for r in range(len(s)):
            current[s[r]] += 1
            while l <= r and not (freq - current):
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    result = s[l:r+1]    
                current[s[l]] -= 1
                if current[s[l]] == 0:
                    del current[s[l]]  # Clean up keys with 0 count
                l += 1
        return result