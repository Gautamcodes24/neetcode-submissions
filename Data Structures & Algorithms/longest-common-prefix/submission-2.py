class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs,key = len)
        ans = ""
        for i,ch in enumerate(strs[0]):
            if all(ch == w[i] for w in strs if len(w) >= i):
                ans += ch
            else:
                return ans
        return ans