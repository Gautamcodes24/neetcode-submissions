class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for ch in num1:
            getchar = ord(ch) - ord('0')
            n1 = n1 * 10 + getchar
        for ch in num2:
            getchar = ord(ch) - ord('0')
            n2 = n2 * 10 + getchar
        return str(n1 * n2)