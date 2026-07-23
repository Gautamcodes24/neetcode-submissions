class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for indx , t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = indx - popped
            stack.append(indx)
        return res
