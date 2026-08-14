from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        # Queue stores tuples of (node, max_val_along_its_path)
        q = deque([(root, root.val)])
        good_nodes = 0
        
        while q:
            node, curr_max = q.popleft()
            
            # If the node's value is >= the max seen on its path, it's a good node
            if node.val >= curr_max:
                good_nodes += 1
                
            # The new max for the children will be the max of the current path max and the node's value
            path_max = max(curr_max, node.val)
            
            # Add children to the queue with the updated path_max
            if node.left:
                q.append((node.left, path_max))
            if node.right:
                q.append((node.right, path_max))
                
        return good_nodes