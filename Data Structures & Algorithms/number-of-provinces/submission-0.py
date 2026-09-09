class Solution:
    def dfs(self,node,adj,visit):
        visit[node] = True
        for n in adj[node]:
            if not visit[n]:
                self.dfs(n,adj,visit)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        count = 0
        visit = [False] * V
        adj_array = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_array[i].append(j)
        for node in range(V):
            if not visit[node]:
                count += 1
                self.dfs(node,adj_array,visit)
        return count


        