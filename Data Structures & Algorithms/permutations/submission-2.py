class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(indx,arr):
            if indx >= len(nums):
                res.append(arr.copy())
                return
            for i in range(indx , len(nums)):
                arr[indx] , arr[i] = arr[i] , arr[indx]
                dfs(indx+1 , arr)
                arr[indx] , arr[i] = arr[i] , arr[indx]
        dfs(0,nums)
        return res


        