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
    bool isPalindrome(ListNode* head)
    {
        if( head == NULL || head->next == NULL ) return true;
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        for( ; fast->next != NULL && fast->next->next != NULL; fast = fast->next->next, slow = slow->next ){}
        
        cout << slow->val;
        ListNode* reversedPartHead = reversePalindrome(slow->next);
        
        for( ListNode* cur = head; reversedPartHead != NULL; reversedPartHead = reversedPartHead->next, cur = cur->next)
        {
            if( cur->val != reversedPartHead->val )
            {
                return false;
            }
        }
        
        return true;
        
    }
    ListNode* reversePalindrome(ListNode * head)
    {
        ListNode* prev = NULL;
        ListNode* next = NULL;
        
        while( head != NULL )
        {
            next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        /*
        // BURADA SIKINTI VAR !!!
        for( ; head != NULL; head = head->next) // Next kullanmadan yapınca bir sıkıntı var???
        {
            head->next = prev;
            prev = head;
        }
        */
        return prev;
    }
};
