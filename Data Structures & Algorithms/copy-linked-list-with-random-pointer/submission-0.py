"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        hm = {None:None}
        curr = head
        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next
        # step 2: Create a new linked list and conn next to next node form hm and same for random
        curr = head
        while curr:
            copy = hm[curr]
            copy.next = hm[curr.next]
            copy.random = hm[curr.random]
            curr = curr.next
        return hm[head]
