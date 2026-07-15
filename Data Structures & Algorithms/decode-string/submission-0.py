class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for indx in range(len(s)):
            if s[indx] != ']':
                stack.append(s[indx])
            else:
                sub = ""
                while stack and stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                stack.append(sub * int(num))
            print(stack)
        return ''.join(stack)
        
        