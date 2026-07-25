class Solution:
    def reverse_node(self,node):
        pre = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        return pre
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast , slow = head , head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        curr = head
        pre = self.reverse_node(slow)
        while curr and pre:
            val1 = curr.val if curr else None
            val2 = pre.val if pre else None
            if val1 != val2:
                return False
            curr = curr.next if curr else None
            pre = pre.next if pre else None
        return True

        