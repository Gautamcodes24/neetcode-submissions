class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []   

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.stack_out.pop()
        

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]        

    def empty(self) -> bool:
        return max(len(self.stack_in) , len(self.stack_out)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()