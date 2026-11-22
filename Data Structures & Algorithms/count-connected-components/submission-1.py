class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for nod in range(n):
            if not visit[nod]:
                visit[nod] = True
                dfs(nod)
                res += 1
        return res