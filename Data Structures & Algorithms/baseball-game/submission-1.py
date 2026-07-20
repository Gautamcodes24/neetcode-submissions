class Solution:
    def calPoints(self, operations: List[str]) -> int:
        preSum = 0
        stack = []
        for op in operations:
            if op == "+":
                if stack:
                    pre_sum = stack[-1] + stack[-2]
                    stack.append(pre_sum)
                    preSum += pre_sum
                else:
                    return ""
            elif op == "C":
                if stack:
                    popped = stack.pop()
                    preSum = preSum - popped
            elif op == "D":
                if stack:
                    d = stack[-1] * 2
                    preSum += d
                    stack.append(d)
            else:
                stack.append(int(op))
                preSum += int(op)
        return preSum
                
        