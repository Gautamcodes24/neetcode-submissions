# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            level = []
            len_q = len(q)
            for _ in range(len_q):
                pop = q.popleft()
                if pop:
                    level.append(pop.val)
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            if len(res) % 2:
                level.reverse()
            res.append(level)
        return res
                
