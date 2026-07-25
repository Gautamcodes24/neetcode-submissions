# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # step 1 find the middle node
        slow , fast = head , head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # step 2 Reverse the 2nd half
        pre = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        second = pre
        max_val = 0
        curr = head
        while second:
            max_val = max(max_val , curr.val + second.val)
            curr = curr.next
            second = second.next
        return max_val
