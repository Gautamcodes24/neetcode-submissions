class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l = 0 
        r = length - 1
        while l < r:
            mid = l + (r-l) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid 
        peak = l
        l = 0 
        r = peak
        while l <= r:
            mid = l + (r-l) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1
        l = peak + 1
        r = length - 1
        while l <= r:
            mid = l + (r-l) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif target < val:
                l = mid + 1
            else:
                r = mid - 1
         
        return -1