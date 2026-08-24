class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n *= -1
        ans = 1.0
        def cal_pow(x,n):
            nonlocal ans
            if n == 0:
                return
            if n % 2 == 1:
                ans *= x
            return cal_pow(x*x,n//2)      
        cal_pow(x,n)
        return ans  