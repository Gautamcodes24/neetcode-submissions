class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        if len(s) <= 1 or s == s[::-1]:
            return s
        best = ''
        for i in range(str_len):

            # first check odd length center 
            l = r = i
            while l >= 0 and r < str_len and s[l] == s[r]:
                # found first valid palindrome
                if r - l + 1 > len(best):
                    best = s[l:r+1]
                l -= 1
                r += 1
            # Now check even length center 
            l , r = i , i + 1
            while l >= 0 and r < str_len and s[l] == s[r]:
                # found first valid palindrome
                if r - l + 1 > len(best):
                    best = s[l:r+1]
                l -= 1
                r += 1
        return best

