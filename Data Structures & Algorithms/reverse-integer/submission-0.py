class Solution:
    def reverse(self, x: int) -> int:
        sign = '-' if x < 0 else '+'
        x = list(str(abs(x)))
        left = 0
        right = len(x) - 1
        while left < right:
            if left < right:
                x[left] , x[right] = x[right] , x[left]
                left += 1
                right -= 1
        final = -int("".join(x)) if sign == '-' else int("".join(x))
        return final if -2 ** 31 <= final <= 2 ** 31 - 1 else 0
        