from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_count = Counter(ransomNote) 
        mag_count = Counter(magazine)
        # rans_count = sorted(rans, key = lambda x : x[1] , reverse=True)
        for key , val in rans_count.items():
            if mag_count[key] >= val:
                continue
            else:
                return False
        return True