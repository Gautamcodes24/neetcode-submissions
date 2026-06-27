class Solution:
    def romanToInt(self, s: str) -> int:
        rmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(1,len(s)):
            if rmap[s[i-1]] < rmap[s[i]]:
                result -= rmap[s[i-1]]
                print(result)
            else:
                result += rmap[s[i-1]]

        return result + rmap[s[-1]]