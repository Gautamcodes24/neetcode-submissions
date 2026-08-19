class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        if n==0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        def calpow(x,n):
            nonlocal ans
            if n == 0:
                return
            if n % 2 == 1:
                ans *= x
            return calpow((x * x),n//2)
        calpow(x,n)
        return ans 