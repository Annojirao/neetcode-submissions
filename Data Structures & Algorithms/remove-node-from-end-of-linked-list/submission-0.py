# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pointer_two = head
        prev = ListNode(0, head)
        pointer_one = prev
        while n:
            pointer_two = pointer_two.next
            n = n-1
        while pointer_two:
            pointer_two = pointer_two.next
            pointer_one = pointer_one.next
        pointer_one.next = pointer_one.next.next
        return prev.next