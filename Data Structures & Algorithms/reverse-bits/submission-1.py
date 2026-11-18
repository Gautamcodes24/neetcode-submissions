class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f"{n:032b}"
        return int(binary[::-1],2) 