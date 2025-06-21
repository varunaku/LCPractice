# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        headfast = head
        cycle = False

        while headfast and headfast.next:
            
            head = head.next

            headfast = headfast.next.next

            if head == headfast:
                cycle = True
                break
        
        return cycle