# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # 'fast' moves 2 steps while 'slow' moves 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # When 'fast' reaches the end, 'slow' is exactly at the middle
        return slow