class DoubleLL:
    def __init__(self,val , pre=None,next=None) -> None:
        self.value = val
        self.prev = pre
        self.next = next     
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = DoubleLL(homepage)
    def visit(self, url: str) -> None:
        self.curr.next = DoubleLL(url , self.curr)
        self.curr = self.curr.next
    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.value
    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.value
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)