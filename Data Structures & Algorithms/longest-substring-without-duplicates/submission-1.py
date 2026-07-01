class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lookup = set()
        # count = 0
        # start = 0
        # for indx , ch in enumerate(s):
        #     if ch in lookup:
        #         lookup.discard(ch)
        #         start += 1
        #     lookup.add(ch)
        #     count = max(indx - start , count)
        # return count+1
        l = r = 0
        max_len = 0
        while r < len(s):
            while s[r] in s[l:r] and r != 0:
                l += 1
            r += 1
            max_len = max(r - l,max_len)
        return max_len




# pwwkew
# cnt = 2
# hm = {p,w}
# strt = 1
# step 1 : p False
# step 2: w False
# step 3: w True 
# step 4: k False



