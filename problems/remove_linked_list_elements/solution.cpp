/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        //There is three case for the position of the node which is valued "val"
        //It could be;
        //  1. at the head of the list
        //  2. at the middle of the list
        //  3. at the end of the list
        // In above, we can solve second and third cases with the same approach but we need another approach for the first case.
        // For eliminate this dilemma (two different approaches), we add a "dummy" node. When we add a "dummy" node, we get rid of the first case. Now we can solve this question with one approach. Great!
        
        ListNode* dummy = new ListNode(-1, head);
        head = dummy;
        
        ListNode* prev = head;
        ListNode* cur = head->next;
        ListNode* next;
        
        for( ; cur != NULL; cur = cur->next )
        {
            next = cur->next;
            
            if( cur->val == val )
            {
                prev->next = cur->next;
                cur->next = NULL;
                delete cur;
                cur = prev;
            }
            
            prev = cur;
        }
        
        return head->next;
        
    }
};
