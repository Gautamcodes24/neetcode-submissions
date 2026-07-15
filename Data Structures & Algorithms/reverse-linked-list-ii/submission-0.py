class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        curr = pre.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next 
            next_node.next = pre.next
            pre.next = next_node
        return dummy.next
