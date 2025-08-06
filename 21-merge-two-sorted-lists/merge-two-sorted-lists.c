/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    //while list1 and list 2 both still exist
    //when the loop breaks, only one of them will be left
    // add that ptr to that to the list

    struct ListNode* head = malloc(sizeof(struct ListNode)); 
    // This will stay in place

    head->val = 0;
    head->next = NULL;

    struct ListNode* list = head;

    while(list1 && list2) {
        // if list1.val >= list2.val, 
        // list.next = list2
        // list2 = list2.next

        // else list.next = list1
        // list1 = list1.next
        if (list1->val >= list2->val){
            list->next = list2;
            list2 = list2->next;
        } else {
            list->next = list1;
            list1 = list1->next;
        }

        list = list->next;
    }

    // what if one of the arrays still has nodes left?
    if (list1){
        list->next = list1;
    } 
    if (list2){
        list->next = list2;
    }

    return head->next; // list is currently the node before the beginning.
}