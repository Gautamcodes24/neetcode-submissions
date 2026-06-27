class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits and digits[-1] != 9:
            digits[-1] += 1 
            return digits
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        # digits.insert(0,1) #O(n)
        # digits = [0, 0, 0]
        # digits = [1] + digits #O(n)
        digits.append(1)

        return digits[::-1]