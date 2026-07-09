class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse = 0
        original = x
        while x > 0:
            reminder = x % 10
            x = x // 10
            print(f'rem is {reminder}')
            print(f'x is {x}')
            reverse = (reverse * 10) + reminder
            print(f'Now rev is {reverse}')
        return reverse == original
