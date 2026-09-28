class Solution:
    def maxDepth(self, s: str) -> int:
        max_dep = 0
        curr_dep = 0
        for c in s:
            if c == '(':
                curr_dep += 1
            elif c == ')':
                curr_dep -= 1
            max_dep = max(max_dep , curr_dep)
        return max_dep