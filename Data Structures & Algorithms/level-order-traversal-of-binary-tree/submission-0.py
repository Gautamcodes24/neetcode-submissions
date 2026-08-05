# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                pop = q.popleft()
                if pop:
                    level.append(pop.val)
                    q.append(pop.left)
                    q.append(pop.right)
            if level:
                res.append(level)
        return res

