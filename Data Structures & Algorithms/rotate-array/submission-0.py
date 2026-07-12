class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n #only k mod n rotate needed
        def reverse(l : int , r : int) -> None:
            '''Inplace Reverse in nums'''
            while l < r:
                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
                r -= 1
        # step 1: Reverse entire array
        reverse(0 , n-1)
        
        # step 2: Reverse k ele
        reverse(0 , k - 1)

        # step 3: Reverse now n - k ele 
        reverse(k , n-1)