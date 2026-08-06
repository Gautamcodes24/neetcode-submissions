class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquare(num):
            square = 0
            while num > 0:
                digit = num % 10
                square += digit ** 2
                num //= 10
            return square
        slow = n
        fast = n
        while True:
            slow = sumOfSquare(slow)
            fast = sumOfSquare(sumOfSquare(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False

