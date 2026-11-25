from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        def find(x: int) -> int:
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[parent[x]])  # path compression
            return parent[x]
        def union(u: int, v: int) -> bool:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False  # already connected -> cycle!
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []