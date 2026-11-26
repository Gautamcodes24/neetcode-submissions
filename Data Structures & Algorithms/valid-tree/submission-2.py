class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 < len(edges):
            return False
        adj = [[] for _ in range(n)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def dfs(node , pre):
            if node in visit:
                return False
            visit.add(node)
            for j in adj[node]:
                if j == pre:
                    continue
                if not dfs(j,node):
                    return False
            return True
        return dfs(0,-1) and n == len(visit)