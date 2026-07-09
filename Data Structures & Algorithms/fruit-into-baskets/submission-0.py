class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = {}
        l = 0
        max_f = 0
        for r in range(len(fruits)):
            hm[fruits[r]] = hm.get(fruits[r],0) + 1

            # window check
            while l < r and len(hm.keys()) > 2:
                # invalid window
                hm[fruits[l]] -= 1
                if hm[fruits[l]] == 0:
                    del hm[fruits[l]]
                l += 1
            # print(f'Current window {hm}')
            # calculate max window
            max_f = max(max_f, r-l+1)
                
        return max_f  