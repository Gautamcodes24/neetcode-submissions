class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i , arr , runningSum):
            if runningSum == target:
                res.append(arr.copy())
                return
            if runningSum > target or i == len(candidates):
                return
            arr.append(candidates[i])
            dfs(i+1,arr,runningSum+candidates[i])
            arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,arr,runningSum)
        dfs(0,[],0)
        return res

        