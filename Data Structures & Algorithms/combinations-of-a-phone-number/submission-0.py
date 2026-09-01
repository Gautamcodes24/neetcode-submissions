class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def backtrack(i,currS):
            if len(currS) == len(digits):
                res.append(currS)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1 ,currS+c)
        if digits:
            backtrack(0,"")
        return res
