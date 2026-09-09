class Solution:
    def dfs(self,node,visit,adj):
        visit[node] = True
        for i in range(len(adj[node])):
            if adj[node][i] == 1 and not visit[i]:
                self.dfs(i,visit,adj)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        V = len(isConnected)
        visit = [False] * V
        for i in range(V):
            if not visit[i]:
                count += 1
                self.dfs(i,visit,isConnected)
        return count