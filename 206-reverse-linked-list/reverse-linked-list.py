# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2-> 3 -> None
        # store 1, point 0 in opposite direction
        # store 2, point 1 at 2
        # on and on 
        prev = None # current head pointer
        curr = head

        while curr:
            nexty = curr.next # store val
            curr.next = prev # point in opposite direction
            # set next previous as current
            prev = curr
            curr = nexty

        return prev