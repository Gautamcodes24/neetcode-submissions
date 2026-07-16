# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_node(n1,n2):
            dummy = ListNode()
            curr = dummy
            while n1 and n2:
                if n1.val < n2.val:
                    curr.next = n1
                    n1 = n1.next
                else:
                    curr.next = n2
                    n2 = n2.next
                curr = curr.next
            curr.next = n1 if n1 else n2
            return dummy.next
        # 2. Edge case: Empty input
        if not lists:
            return None
        
        # 3. The "One by One" Loop
        # We start by assuming the first list is our "result so far"
        merged_result = lists[0]
        
        # We loop through the rest of the lists, starting from index 1
        for i in range(1, len(lists)):
            
            # Merge our running total with the next list in line
            merged_result = merge_node(merged_result, lists[i])
            
        # 4. Return the massive, fully merged list!
        return merged_result
        
        
        