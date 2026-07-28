class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(leftKiright):
            l = 0
            r = len(nums) - 1
            bound = -1
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    bound = mid
                    if leftKiright:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return bound
        return [find(True),find(False)]
        