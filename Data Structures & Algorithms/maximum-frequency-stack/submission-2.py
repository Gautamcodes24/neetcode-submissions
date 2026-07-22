class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.hm = {}
        self.mxCnt = 0
        

    def push(self, val: int) -> None:
        self.hm[val] = self.hm.get(val,0) + 1
        valCnt = self.hm[val]
        if valCnt > self.mxCnt:
            self.stacks[valCnt] = []
            self.mxCnt = valCnt
        self.stacks[valCnt].append(val)
    def pop(self) -> int:
        res = self.stacks[self.mxCnt].pop()
        self.hm[res] -= 1
        if not self.stacks[self.mxCnt]:
            self.mxCnt -= 1
        return res
