class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(indx , arr=[]):
            if indx >= len(nums):
                res.append(arr.copy())
                return 
            arr.append(nums[indx])
            dfs(indx+1 , arr)
            arr.pop()
            dfs(indx+1 , arr)
        dfs(0,[])
        return res

        