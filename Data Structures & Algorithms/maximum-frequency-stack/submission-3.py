class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.hm = {}
    def push(self, val: int) -> None:
        self.hm[val] = self.hm.get(val,0) + 1
        valCnt = self.hm[val]
        if valCnt not in self.stacks:
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)
    def pop(self) -> int:
        mx_count = max(self.stacks.keys())
        res = self.stacks[mx_count].pop()
        self.hm[res] -= 1
        if not self.stacks[mx_count]:
            del self.stacks[mx_count]
        return res