class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        # Step 1: Calculate prefix products (left to right)
        # res[i] will contain the product of all elements to the left of nums[i]
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        # Step 2: Calculate postfix/suffix products (right to left)
        # Multiply the stored prefix product by the postfix product on the fly
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
