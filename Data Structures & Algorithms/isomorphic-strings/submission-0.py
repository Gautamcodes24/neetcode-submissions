class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        hm = {}
        for s_ch , t_ch in zip(s,t):
            if s_ch in hm:
                if hm[s_ch] != t_ch:
                    return False
            else:
                hm[s_ch] = t_ch
        return True
        