class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for cor , pre in prerequisites:
            preMap[cor].append(pre)
        cycle , visit = set() , set()
        out = []
        def dfs(cor):
            if cor in cycle:
                return False
            if cor in visit:
                return True
            cycle.add(cor)
            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            cycle.remove(cor)
            visit.add(cor)
            out.append(cor)
            return True
        for cor in range(numCourses):
            if not dfs(cor):
                return []
        return out