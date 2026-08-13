# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        ans = []
        while q:
            right_side = 0
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    right_side=node.val
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                ans.append(right_side)
        return ans

        