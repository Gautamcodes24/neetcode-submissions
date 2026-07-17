class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0
            if left and right:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return n <= 0
            