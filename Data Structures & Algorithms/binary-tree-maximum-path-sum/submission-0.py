# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = [root.val]
        def getLRmax(root):
            if not root:
                return 0
            leftMax = getLRmax(root.left)
            rightMax = getLRmax(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            max_sum[0] = max(max_sum[0] , root.val + leftMax + rightMax)
            return root.val + max(leftMax , rightMax)
        getLRmax(root)
        return max_sum[0]
 
        