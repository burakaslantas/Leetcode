/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* cur = head;
        
        for( ; cur != NULL; cur = cur->next) // traverse linkedlist
        {
            if( cur->val != NULL ) 
            {
                cur->val = NULL; // mark current node as "visited" by changing their value to NULL.
            }
            else if( cur->val == NULL ) // if current node is already "visited", there must be a circle.
            {
                return true;
            }
        }
        
        return false; // if for loop terminated successfully there must be a node next value which is equal to "NULL", so there is no circle in this case.
    }
};
