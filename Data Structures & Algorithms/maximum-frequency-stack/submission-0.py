from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.hm = defaultdict(int)
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.hm[val] += 1
        

    def pop(self) -> int:
        mx = max(self.hm.values())
        i = len(self.stack) - 1
        while self.hm[self.stack[i]] != mx:
            i -= 1
        self.hm[self.stack[i]] -= 1
        return self.stack.pop(i)

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()