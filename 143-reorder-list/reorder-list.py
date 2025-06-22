# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # fast and slow ptr to determine start of second list ( end of first list.next)
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow ptr is now the end of the 2nd list, and should point to null
        list2 = slow.next
        slow.next = None
        
        # now we have 2 lists, one at head, one at list2

        # reverse the 2nd list
        prev = None
        while list2:
            #store next
            tmp = list2.next
            #point next at prev
            list2.next = prev

            # update prev
            prev = list2
            #iterate
            list2 = tmp
        
        # prev stores the head of the 2nd list
        
        # merge lists
        #[2,4,6] head
        # [10,8] prev
        f, s = head,prev
        while s:
            h_next = f.next
            p_next = s.next

            f.next = s
            s.next = h_next

            f = h_next
            s = p_next
        