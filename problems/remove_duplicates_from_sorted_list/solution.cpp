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
    ListNode* deleteDuplicates(ListNode* head) {
        if( head == nullptr || head->next == nullptr )
        {
            return head;
        }
        
        ListNode* list = head;
        
        while( list->next != nullptr )
        {
            if( list->val == list->next->val )
            {
                list->next = list->next->next;
            }
            else
            {
                list = list->next;
            }
        }
        return head;
    }
};
