class StockSpanner:

    def __init__(self):
        self.arr = []
        
    # Brute force
    def next(self, price: int) -> int:
        self.arr.append(price)
        start = len(self.arr) - 2
        while start >= 0 and self.arr[start] <= price:
            start -= 1
        return len(self.arr) - start - 1

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# [[100], [80], [60], [70], [60], [75],85]