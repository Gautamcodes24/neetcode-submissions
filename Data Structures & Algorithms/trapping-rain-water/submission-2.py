class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        lmax = height[l]
        rmax = height[r]
        water = 0 
        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax , height[l])
                water += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax,height[r])
                water += rmax - height[r]
        return water