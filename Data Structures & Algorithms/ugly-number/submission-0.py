class Solution:
    def isUgly(self, n: int) -> bool:
        # step 1 
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5
        print(n)
        return n == 1
        
        