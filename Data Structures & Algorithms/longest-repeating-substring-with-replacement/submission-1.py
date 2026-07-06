'''
s = "AAABABB", k = 1
l = 0
max_len = 0
{A:3,B:1}
(r - l + 1) - max < k : 
4 - 3 < 1:
    max_len = max(max_len , r-l+1)
while (r - l + 1) - max > k:


'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_con = 0
        max_val = 0
        hm = {}
        l = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0) + 1
            max_val = max(hm.values())
            # if (r - l + 1) - max_val <= k:
            #     max_con = max(max_con , (r - l + 1))
            while (r - l + 1) - max_val > k:
                hm[s[l]] = hm.get(s[l],0) - 1
                l += 1
            max_con = max(max_con , (r - l + 1))
        return max_con


        
