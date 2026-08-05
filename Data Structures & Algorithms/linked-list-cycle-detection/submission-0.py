# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev , current = head , head
        while current and current.next:
            prev = prev.next
            current = current.next.next
            if prev == current:
                return True
        return False

        