class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for cor , pre in prerequisites:
            preMap[cor].append(pre)
        visitSet = set()
        def dfs(cors):
            if cors in visitSet:
                return False
            if preMap[cors] == []:
                return True
            visitSet.add(cors)
            for pre in preMap[cors]:
                if not dfs(pre):
                    return False
            preMap[cors] = []
            visitSet.remove(cors)
            return True
        for cors in range(numCourses):
            if not dfs(cors):
                return False
        return True