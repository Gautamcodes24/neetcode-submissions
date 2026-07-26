class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(f'Mid is {mid}')
            if nums[mid] == target:
                # print(f'target found {mid}')
                return mid
            elif nums[mid] > target:
                # print(f'moving r to mid r:{r} = {mid - 1}')  
                r = mid - 1
            else:
                # print(f'moving l to mid l:{l} = {mid}')  
                l = mid + 1
        return -1