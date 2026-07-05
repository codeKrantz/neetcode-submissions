# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        #while not null
        while fast and fast.next:
            slow = slow.next #will reach the middle of the list
            fast = fast.next.next #will reach the end of the list
        
        second = slow.next
        prev = slow.next = None
        while second:
            #pointers and swapping
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #reordering the list
        first, second =  head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        