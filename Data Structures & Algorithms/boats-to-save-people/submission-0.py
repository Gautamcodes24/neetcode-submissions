class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1,2,4,5] 
        # -- > [1,5] , [2,4]

        # [1,2,2,3,3]
        # - []
        people.sort()
        l = 0
        r = len(people) - 1
        ans = 0
        print(people)
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1 
            ans += 1
        return ans