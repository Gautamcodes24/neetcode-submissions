class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Brute force approach 
        Time Complexity : O(n^2)
        Space complexity : O(n)
        '''
        product = []
        for indx1 in range(len(nums)):
            single_pro = 1
            for indx2 in range(len(nums)):
                single_pro *= nums[indx2] if indx1 != indx2 else 1
            product.append(single_pro)
        return product
             
