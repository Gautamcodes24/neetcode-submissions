class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans  = []
        for i in range(len(temperatures)):
            count = 0
            append = False
            for j in range(i,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    append = True
                    break
                else:
                    count += 1

            ans.append(count if append else 0)
        return ans