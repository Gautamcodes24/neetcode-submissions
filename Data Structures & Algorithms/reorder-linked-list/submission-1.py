# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # second is the head of the second half
        second = slow.next
        # Break the link to split into two separate lists
        slow.next = None
        
        # Step 2: Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Step 3: Merge the two halves alternately
        first, second = head, prev
        while second:
            # Save the next nodes for continuation
            next_first, next_second = first.next, second.next
            
            # Connect first half node to second half node
            first.next = second
            # Connect second half node to next first half node
            second.next = next_first
            
            # Move the pointers forward
            first = next_first
            second = next_second