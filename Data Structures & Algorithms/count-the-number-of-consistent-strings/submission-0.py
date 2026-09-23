class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0

        for w in words:
            flag = 1
            for c in w:
                if c not in allowed:
                    flag = 0
                    break
            res += flag

        return res