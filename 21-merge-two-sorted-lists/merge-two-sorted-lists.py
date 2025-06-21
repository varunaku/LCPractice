# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        # return head, iterate dummy

        # While both ptrs are not pointing at null (still going thru list)
        while list1 and list2: 
        # if one of the lists finishes, the other is already sorted, so we can stop
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next 
            else: 
                dummy.next = list2 # set the next
                list2 = list2.next
            dummy = dummy.next # actually go to the next (iterate)
         
        # determine which is list is left
        # then list1 or list2 ptr should point at the rest of the list
        # so just set dummy.next as equal to list1 or list2
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        
        return head.next