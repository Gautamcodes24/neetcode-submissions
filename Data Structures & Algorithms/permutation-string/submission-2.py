from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original_hm = Counter(s1)
        hm = {}
        l = 0
        len_p = len(s1)
        for r in range(len(s2)):
            hm[s2[r]] = hm.get(s2[r],0) + 1

            while r - l + 1 == len_p:
                if original_hm == hm:
                    return True
                hm[s2[l]] = hm.get(s2[l],0) - 1
                if hm.get(s2[l],0) == 0:
                    del hm[s2[l]]
                l += 1
        return False
