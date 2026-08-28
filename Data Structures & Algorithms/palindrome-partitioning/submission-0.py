class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for ch in range(i,len(s)):
                if self.isPali(s,i,ch):
                    part.append(s[i:ch+1])
                    dfs(ch+1)
                    part.pop()
        dfs(0)
        return res
    def isPali(self,s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True