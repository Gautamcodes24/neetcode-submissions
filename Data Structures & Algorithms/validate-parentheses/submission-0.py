class Solution:
    def isValid(self, s: str) -> bool:
        # --------------------------Using extra khopdi(mind)--------------------
        open_br = {
            '(':')',
            '{':'}',
            '[':']'
            }
        stack = []
        for c in s:
            if c in open_br:
                stack.append(open_br[c])
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False
        return len(stack) == 0