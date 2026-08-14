class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left , q.left) and isSameTree(p.right , q.right)

        # Base cases for the main function
        if not subRoot: return True
        if not root: return False

        # If the current trees match, we're done
        if isSameTree(root, subRoot):
            return True

        # Otherwise, recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)