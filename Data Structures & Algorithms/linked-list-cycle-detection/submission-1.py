# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        visit = set()
        current = head
        while current.next:
            if current in visit:
                return True
            
            visit.add(current)
            current = current.next
        return False
        