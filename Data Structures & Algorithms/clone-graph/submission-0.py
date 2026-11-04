"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashset = {}
        def clone(node):
            if node in hashset:
                return hashset[node]
            copy = Node(node.val)
            hashset[node] = copy
            for neighbor in node.neighbors:
                hashset[node].neighbors.append(clone(neighbor))
            return copy
        return clone(node) if node else None