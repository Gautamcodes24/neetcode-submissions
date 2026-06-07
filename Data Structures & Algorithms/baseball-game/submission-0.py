class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record_log = []
        for op in operations:
            if op == "+":
                # No need for len() check if constraints guarantee 2 elements
                record_log.append(record_log[-1] + record_log[-2])
            elif op == "D":
                record_log.append(2 * record_log[-1])
            elif op == "C":
                record_log.pop()
            else:
                # If it's not a command, it's a number (positive or negative)
                record_log.append(int(op))
        return sum(record_log)