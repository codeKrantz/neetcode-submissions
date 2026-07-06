# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        current = head
        while current:
            N += 1
            current = current.next
        
        #found after first iteration
        removeIndex = N - n
        if removeIndex == 0:
            return head.next

        current = head
        for i in range(N - 1):
            if (i+1) == removeIndex:
                #using pointers to skip removed element
                current.next = current.next.next
                break
            current = current.next
        
        return head
        