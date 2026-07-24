class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #will store char and sub sequ count
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            if stack and stack[-1][1] == k:
                stack.pop()
        return "".join(ch * count for ch , count in stack)