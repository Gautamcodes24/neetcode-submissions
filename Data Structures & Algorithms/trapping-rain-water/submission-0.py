class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = height[0]
        rmax = height[-1]
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax , height[l])
                water = lmax - height[l]
                ans += water if water >= 0 else 0
            else:
                r -= 1
                rmax = max(rmax , height[r])
                water = rmax - height[r]
                ans += water if water >= 0 else 0
        return ans

