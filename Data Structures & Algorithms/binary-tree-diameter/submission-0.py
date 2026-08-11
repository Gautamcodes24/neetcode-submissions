# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        def getSubTreeHeight(root):
            if not root:
                return 0
            left = getSubTreeHeight(root.left)
            right = getSubTreeHeight(root.right)
            nonlocal max_height
            max_height = max(max_height , left + right)
            return max(left , right) + 1
        getSubTreeHeight(root)
        return max_height