class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(curr))
                return
            for j in range(i,len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    curr.append(word)
                    backtrack(j+1)
                    curr.pop()
        res = []
        curr = []
        backtrack(0)
        return res