class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Count the total number of nodes
        total_length = 0
        current = head
        while current is not None:
            total_length += 1
            current = current.next
            
        # Step 2: Find the target index for the middle node
        # For length 5: 5 // 2 = 2 (0-indexed: index 2 is the 3rd node)
        # For length 6: 6 // 2 = 3 (0-indexed: index 3 is the 4th node)
        middle_index = total_length // 2
        
        # Step 3: Move a pointer to that middle index
        p = head
        for _ in range(middle_index):
            p = p.next
            
        return p
        