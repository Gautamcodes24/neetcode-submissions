class Solution:
    def minOperations(self, logs: List[str]) -> int:
        _dir = []
        for log in logs:
            if log == "../":
                if _dir:
                    _dir.pop()
                else:
                    continue
            elif log == "./":
                continue
            else:
                _dir.append(log)
        return len(_dir) if _dir else 0